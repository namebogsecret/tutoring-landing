# -*- coding: utf-8 -*-
"""Контракт-тест страницы /compare-exam-programs/ (answer_pages._compare_page).
Запуск:  python3 build.py && python3 -m pytest tests/test_compare_programs.py
"""
import html as htmllib
import json
import os
import re
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from test_pillar_pages import FORBIDDEN, FORBIDDEN_VISIBLE, visible_text  # noqa: E402
from test_answer_pages import EXTRA_FORBIDDEN, strip_razbor              # noqa: E402

BASE = "https://tutor.podlevskikh.com"
URL = "/compare-exam-programs/"
PILLARS = ["/ege-physics/", "/ib-physics-tutor/", "/ap-physics-tutor/", "/igcse-physics-0625/"]


def read(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as f:
        return f.read()


class TestCompare(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = read("compare-exam-programs/index.html")

    def jsonld(self):
        return [json.loads(x) for x in re.findall(r'<script type="application/ld\+json">\s*(.*?)\s*</script>', self.html, re.S)]

    def test_page_exists_and_basics(self):
        h = self.html
        self.assertIn('<link rel="canonical" href="%s%s"' % (BASE, URL), h)
        m = re.search(r'<meta name="description" content="([^"]*)"', h)
        self.assertTrue(m and len(m.group(1)) < 160, m and len(m.group(1)))
        self.assertIn("<main", h)
        self.assertEqual(len(re.findall(r"<h1[ >]", h)), 1)
        self.assertIn("Сравнение программ подготовки по физике: ЕГЭ, IB, AP, IGCSE", h)
        self.assertIn('class="lead', h)  # Answer-First абзац сразу под h1

    def test_table_has_four_programmes(self):
        tables = re.findall(r"<table.*?</table>", self.html, re.S)
        self.assertEqual(len(tables), 1)
        head = re.search(r"<thead>.*?</thead>", tables[0], re.S).group(0)
        self.assertEqual(len(re.findall(r"<th[ >]", head)), 5)  # «Параметр» + 4 программы
        for name in ("ЕГЭ", "IB", "AP", "IGCSE"):
            self.assertIn(name, head)
        for tr in re.findall(r"<tr>.*?</tr>", re.search(r"<tbody>.*?</tbody>", tables[0], re.S).group(0), re.S):
            self.assertEqual(len(re.findall(r"<t[hd][ >]", tr)), 5)

    def test_faq_jsonld_matches_visible(self):
        blocks = self.jsonld()
        faq = [b for b in blocks if b.get("@type") == "FAQPage"]
        self.assertEqual(len(faq), 1)
        qs = faq[0]["mainEntity"]
        self.assertGreaterEqual(len(qs), 4)
        vis = htmllib.unescape(re.sub(r"<[^>]+>", " ", self.html))
        vis = re.sub(r"\s+", " ", vis)
        for q in qs:
            self.assertEqual(q["@type"], "Question")
            self.assertEqual(q["acceptedAnswer"]["@type"], "Answer")
            self.assertIn(q["name"], vis)
            self.assertIn(q["acceptedAnswer"]["text"], vis)
        self.assertIn('class="faq-item"', self.html.replace(" open", ""))

    def test_in_sitemap_and_llms(self):
        self.assertIn("<loc>%s%s</loc>" % (BASE, URL), read("sitemap.xml"))
        self.assertIn(BASE + URL, read("llms.txt"))

    def test_links_out(self):
        for p in PILLARS + ["/exam-prep-online/", "/answers/"]:
            self.assertIn('href="%s"' % p, self.html, p)
        self.assertIn("data-cta=", self.html)
        self.assertIn("Записаться на разбор", self.html)

    def test_linked_from_hub_and_pillars(self):
        for src in ["answers/index.html"] + [p.strip("/") + "/index.html" for p in PILLARS]:
            self.assertIn('href="%s"' % URL, read(src), src)

    def test_no_stop_words(self):
        txt = visible_text(strip_razbor(self.html)) if callable(visible_text) else self.html
        raw = strip_razbor(self.html)
        for pat in FORBIDDEN + EXTRA_FORBIDDEN:
            # data-cta= разрешён по ТЗ (как на страницах проекта), остальное — запрещено
            if pat == r"data-cta=":
                continue
            self.assertIsNone(re.search(pat, raw, re.I), pat)
        for pat in FORBIDDEN_VISIBLE:
            self.assertIsNone(re.search(pat, txt, re.I), pat)

    def test_no_ap_physics_1_2(self):
        txt = re.sub(r"<[^>]+>", " ", self.html)
        self.assertNotRegex(txt, r"AP Physics [12]\b")


if __name__ == "__main__":
    unittest.main()
