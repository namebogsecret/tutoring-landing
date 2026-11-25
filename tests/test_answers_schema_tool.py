# -*- coding: utf-8 -*-
"""Тесты tools/validate_answers_schema.py: реальное дерево — 0, синтетические дубли/ошибки — 1.
Запуск:  python3 -m pytest -q tests/test_answers_schema_tool.py
"""
import json
import os
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOL = os.path.join(ROOT, "tools", "validate_answers_schema.py")

COURSE = {"@context": "https://schema.org", "@type": "Course", "@id": "https://x/#c", "name": "C"}
FAQ = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
    {"@type": "Question", "name": "q", "acceptedAnswer": {"@type": "Answer", "text": "a"}}]}
FAQ_HTML = '<section id="faq"><div class="faq-list"><details class="faq-item"></details></div></section>'


def page(blocks, body=FAQ_HTML):
    ld = "".join('<script type="application/ld+json">%s</script>\n' % (b if isinstance(b, str) else json.dumps(b))
                 for b in blocks)
    return "<html><head>%s</head><body>%s</body></html>" % (ld, body)


def run(root, *extra):
    return subprocess.run([sys.executable, TOOL, "--root", root] + list(extra),
                          capture_output=True, text=True)


class TestValidateAnswersSchema(unittest.TestCase):
    def tree(self, html):
        d = tempfile.TemporaryDirectory()
        self.addCleanup(d.cleanup)
        os.makedirs(os.path.join(d.name, "answers", "x"))
        with open(os.path.join(d.name, "answers", "x", "index.html"), "w", encoding="utf-8") as f:
            f.write(html)
        return d.name

    def fails(self, html, needle):
        r = run(self.tree(html))
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn(needle, r.stdout)

    def test_real_tree_clean(self):
        r = run(ROOT)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("OK", r.stdout)

    def test_real_tree_json(self):
        r = run(ROOT, "--json")
        self.assertEqual(r.returncode, 0, r.stdout)
        d = json.loads(r.stdout)
        self.assertTrue(d["ok"])
        self.assertGreaterEqual(d["pages"], 36)

    def test_synthetic_ok(self):
        r = run(self.tree(page([COURSE, FAQ])))
        self.assertEqual(r.returncode, 0, r.stdout)

    def test_duplicate_faqpage(self):
        self.fails(page([COURSE, FAQ, dict(FAQ, name="other")]), "FAQPage")

    def test_duplicate_identical_block(self):
        self.fails(page([COURSE, COURSE, FAQ]), "дубль")

    def test_duplicate_id(self):
        other = {"@context": "https://schema.org", "@type": "WebPage", "@id": COURSE["@id"]}
        self.fails(page([COURSE, other, FAQ]), "@id")

    def test_duplicate_type_in_graph(self):
        g = {"@context": "https://schema.org", "@graph": [COURSE, dict(COURSE, **{"@id": "https://x/#c2"})]}
        self.fails(page([g, FAQ]), "@type Course")

    def test_broken_json(self):
        self.fails(page([COURSE, FAQ, '{"@type": "WebPage",}']), "невалидный JSON")

    def test_no_context(self):
        self.fails(page([{"@type": "Course"}, FAQ]), "@context")

    def test_faq_visible_without_faqpage(self):
        self.fails(page([COURSE]), "FAQPage нет")

    def test_faqpage_without_visible_faq(self):
        self.fails(page([COURSE, FAQ], body="<p>нет</p>"), "видимого FAQ")

    def test_no_course_or_service(self):
        self.fails(page([FAQ]), "Course или Service")

    def test_type_as_list_ok(self):
        c = dict(COURSE, **{"@type": ["Course", "Thing"]})
        self.assertEqual(run(self.tree(page([c, FAQ]))).returncode, 0)

    def test_type_as_list_dup(self):
        c = dict(COURSE, **{"@type": ["Course", "Thing"]})
        d = dict(COURSE, **{"@id": "https://x/#d", "@type": ["Thing"]})
        self.fails(page([c, d, FAQ]), "@type Thing")

    def test_top_level_array_block_ok(self):
        self.assertEqual(run(self.tree(page([[COURSE, FAQ]]))).returncode, 0)

    def test_top_level_array_no_context(self):
        self.fails(page([[{"@type": "Course"}, FAQ]]), "@context")

    def test_empty_array_block(self):
        self.fails(page([COURSE, FAQ, "[]"]), "@context")

    def test_script_variants_with_broken_json(self):
        for tag in ('<script nonce="abc" type="application/ld+json">',
                    '<script id="x" type="application/ld+json">',
                    "<script type='application/ld+json'>",
                    '<SCRIPT TYPE="APPLICATION/LD+JSON">'):
            html = page([COURSE, FAQ]).replace("</head>", tag + "{broken,}</script></head>")
            self.fails(html, "невалидный JSON")

    def test_unrecognized_ld_script(self):
        html = page([COURSE, FAQ]).replace("</head>", "<script type=application/ld+json defer src=x></script></head>")
        self.fails(html, "невалидный JSON")  # без кавычек, с лишними атрибутами
        # упоминание вне script-тега ловится счётчиком
        html = page([COURSE, FAQ]).replace("</head>", "<link data-x=application/ld+json></head>")
        self.fails(html, "упоминаний")

    def test_nested_duplicate_faqpage(self):
        f = dict(FAQ, mainEntity=[dict(FAQ["mainEntity"][0], **{"@type": "FAQPage"})])
        self.fails(page([COURSE, f]), "повтор FAQPage")

    def test_nested_faqpage_counts_as_faq(self):
        g = {"@context": "https://schema.org", "@type": "WebPage", "mainEntity": FAQ}
        self.assertEqual(run(self.tree(page([COURSE, g]))).returncode, 0)

    def test_question_answer_not_duplicates(self):
        f = dict(FAQ, mainEntity=FAQ["mainEntity"] * 2)
        self.assertEqual(run(self.tree(page([COURSE, f]))).returncode, 0)

    def test_faq_marker_in_comment(self):
        self.fails(page([COURSE, FAQ], body='<!-- <div id="faq" class="faq-list"> --><p>x</p>'), "видимого FAQ")

    def test_faq_marker_in_hidden_section(self):
        self.fails(page([COURSE, FAQ], body='<div hidden><div class="faq-list"></div></div>'), "видимого FAQ")

    def test_context_as_list_ok(self):
        c = dict(COURSE, **{"@context": ["https://schema.org", {"x": "https://x/"}]})
        self.assertEqual(run(self.tree(page([c, FAQ]))).returncode, 0)

    def test_context_as_object_ok(self):
        c = dict(COURSE, **{"@context": {"@vocab": "https://schema.org/"}})
        self.assertEqual(run(self.tree(page([c, FAQ]))).returncode, 0)

    def test_context_wrong_list(self):
        c = dict(COURSE, **{"@context": ["https://example.org"]})
        self.fails(page([c, FAQ]), "@context")

    def test_no_pages(self):
        d = tempfile.TemporaryDirectory()
        self.addCleanup(d.cleanup)
        self.assertEqual(run(d.name).returncode, 1)


if __name__ == "__main__":
    unittest.main()
