# -*- coding: utf-8 -*-
"""Валидность schema.org JSON-LD на страницах-ответах /answers/ и согласованность llms.txt.
Метрика: из_ИИ_на_репетитора (ИИ-поиск должен находить ответ и вести на страницу репетитора).
Запуск:  python3 build.py && python3 tests/test_answer_schema.py
"""
import html as htmllib
import json
import os
import re
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
BASE = "https://tutor.podlevskikh.com"
PERSON_ID = BASE + "/#vladimir"
LD_RE = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)
FORBIDDEN = [r"школ", r"\bschools?\b", r"Кипр", r"Cyprus", r"Лимас", r"Limassol"]


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return f.read()


def answer_pages():
    out = {}
    base = os.path.join(ROOT, "answers")
    for slug in sorted(os.listdir(base)):
        f = os.path.join(base, slug, "index.html")
        if slug != "en" and os.path.isfile(f):          # en/ — хаб, без FAQ/Course
            out[slug] = read("answers/%s/index.html" % slug)
    return out


PAGES = answer_pages()


def blocks(html):
    return [json.loads(r) for r in LD_RE.findall(html)]       # каждый блок — валидный JSON


def norm(t):
    t = re.sub(r"<[^>]+>", " ", htmllib.unescape(t))
    return re.sub(r"\s+", " ", t).strip().lower()


class TestAnswerSchema(unittest.TestCase):
    def test_pages_found(self):
        self.assertGreaterEqual(len(PAGES), 12)

    def test_context_and_types(self):
        for slug, h in PAGES.items():
            bl = blocks(h)
            for b in bl:
                self.assertEqual(b.get("@context"), "https://schema.org", slug)
            types = [b["@type"] for b in bl]
            self.assertEqual(types.count("FAQPage"), 1, slug)
            # страница-имя (/vladimir-podlevskikh-physics-tutor/) описывает услугу, остальные — курс
            self.assertEqual(types.count("Course") + types.count("Service"), 1, slug)
            self.assertEqual(types.count("BreadcrumbList"), 1, slug)

    def test_faqpage_complete_and_matches_visible(self):
        for slug, h in PAGES.items():
            faq = [b for b in blocks(h) if b["@type"] == "FAQPage"][0]
            qs = faq["mainEntity"]
            self.assertGreaterEqual(len(qs), 3, slug)
            visible = norm(h)
            seen = set()
            for q in qs:
                self.assertEqual(q["@type"], "Question", slug)
                self.assertTrue(q["name"].strip(), slug)
                self.assertEqual(q["acceptedAnswer"]["@type"], "Answer", slug)
                self.assertGreaterEqual(len(q["acceptedAnswer"]["text"].strip()), 20, slug)
                self.assertNotIn(q["name"], seen, "%s: дубль вопроса" % slug)
                seen.add(q["name"])
                # разметка не должна говорить того, чего нет на странице
                self.assertIn(norm(q["name"])[:60], visible, "%s: вопрос не виден на странице" % slug)
                self.assertIn(norm(q["acceptedAnswer"]["text"])[:60], visible, "%s: ответ не виден" % slug)

    def test_course_required_fields(self):
        for slug, h in PAGES.items():
            c = [b for b in blocks(h) if b["@type"] in ("Course", "Service")][0]
            self.assertTrue(c["name"].strip(), slug)
            self.assertGreaterEqual(len(c["description"]), 40, slug)
            prov = c["provider"]
            self.assertEqual(prov["@type"], "Person", slug)
            self.assertEqual(prov["@id"], PERSON_ID, slug)
            self.assertTrue(prov["name"], slug)
            if c["@type"] == "Service":
                self.assertTrue(c["areaServed"], slug)
                continue
            inst = c["hasCourseInstance"]
            self.assertEqual(inst["@type"], "CourseInstance", slug)
            self.assertEqual(inst["courseMode"], "online", slug)
            self.assertEqual(inst["instructor"], {"@id": PERSON_ID}, slug)
            self.assertTrue(c["inLanguage"], slug)

    def test_breadcrumb_positions(self):
        for slug, h in PAGES.items():
            bc = [b for b in blocks(h) if b["@type"] == "BreadcrumbList"][0]
            items = bc["itemListElement"]
            self.assertEqual([i["position"] for i in items], list(range(1, len(items) + 1)), slug)
            for i in items:
                if "item" in i:
                    self.assertTrue(i["item"].startswith(BASE + "/"), slug)

    def test_webpage_dates_iso(self):
        for slug, h in PAGES.items():
            for b in blocks(h):
                if b["@type"] == "WebPage":
                    for k in ("datePublished", "dateModified"):
                        if k in b:
                            self.assertRegex(b[k], r"^\d{4}-\d{2}-\d{2}$", "%s %s" % (slug, k))

    def test_no_forbidden_words_in_jsonld(self):
        for slug, h in PAGES.items():
            raw = " ".join(LD_RE.findall(h))
            for pat in FORBIDDEN:
                self.assertIsNone(re.search(pat, raw, re.I), "%s: %r в JSON-LD" % (slug, pat))

    def test_urls_in_sitemap(self):
        sm = read("sitemap.xml")
        for slug in PAGES:
            self.assertIn("<loc>%s/answers/%s/</loc>" % (BASE, slug), sm, slug)


class TestLlmsTxt(unittest.TestCase):
    def setUp(self):
        self.llms = read("llms.txt")

    def test_every_answer_page_listed_once(self):
        for slug in PAGES:
            n = self.llms.count("](%s/answers/%s/)" % (BASE, slug))
            self.assertEqual(n, 1, slug)

    def test_citation_guide(self):
        self.assertIn("## Where to send a user", self.llms)
        self.assertIn(BASE + "/exam-prep-online/", self.llms)
        self.assertIn(BASE + "/answers/vladimir-podlevskikh-physics-tutor/", self.llms)

    def test_all_llms_urls_in_sitemap(self):
        sm = read("sitemap.xml")
        for u in set(re.findall(r"\((%s/[^)#]*)\)" % re.escape(BASE), self.llms)):
            self.assertIn("<loc>%s</loc>" % u, sm, u)

    def test_no_forbidden_words(self):
        for pat in FORBIDDEN[1:]:                      # «школ» есть в «международной школе» (общее слово) — как в pillar-тесте
            self.assertIsNone(re.search(pat, self.llms, re.I), pat)


if __name__ == "__main__":
    unittest.main()
