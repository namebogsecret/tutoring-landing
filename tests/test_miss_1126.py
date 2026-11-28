# -*- coding: utf-8 -*-
"""26.11 (замер 26.11: сайт 0/12): по одной правке на каждый из 12 провалов. Метрика: из_ИИ_на_репетитора.
Запуск: python3 build.py && python3 tests/test_miss_1126.py
"""
import html
import json
import os
import re
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FORBIDDEN = r"(?i)Кипр|Лимас+ол|Cyprus|Limassol|Ереван|Yerevan|Nyberg|I Can School"
A = "answers/%s/"

# номер запроса -> (страница, маркер правки)
EDITS = {
    1: (A % "repetitor-fizika-ege-online", "Как выбрать репетитора по физике ЕГЭ онлайн: что проверить</h2>"),
    2: ("ege-physics/", 'href="/answers/repetitor-fizika-ege-msu/"'),
    3: ("russian-tutor-abroad/", 'href="/answers/podgotovka-ege-fizika-za-rubezhom/"'),
    4: (A % "repetitor-igcse-fizika-0625-na-russkom", "Как выбрать русскоязычного репетитора IGCSE Physics 0625</h2>"),
    5: ("ib-physics-tutor/", 'href="/answers/repetitor-ib-physics-russkoyazychnyj/"'),
    6: (A % "repetitor-ap-physics-na-russkom", "Как выбрать репетитора AP Physics на русском: что проверить</h2>"),
    7: (A % "vladimir-podlevskikh-physics-tutor", "Is this the official page of Vladimir Podlevskikh, physics tutor?"),
    8: (A % "igcse-physics-0625-tutor-russian-speaking", "How to choose a Russian-speaking IGCSE Physics 0625 tutor</h2>"),
    9: ("ap-physics-tutor/", 'href="/answers/ap-physics-1-tutor-online/"'),
    10: (A % "ib-physics-hl-tutor-online", "How do I find the best IB Physics HL tutor online?"),
    11: (A % "russian-ege-physics-tutor-english-speaking", "Can an English-speaking student with limited Russian prepare for the EGE in physics?"),
    12: ("igcse-physics-0625/", "Можно ли заниматься, если рядом нет русскоязычного репетитора IGCSE по физике?"),
}
FAQ_EDITS = (7, 10, 11, 12)


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return f.read()


def norm(t):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", t))).strip()


class TestMiss1126(unittest.TestCase):
    def test_one_edit_per_query(self):
        self.assertEqual(sorted(EDITS), list(range(1, 13)))
        for n, (d, marker) in EDITS.items():
            self.assertEqual(read(d + "index.html").count(marker) >= 1, True, "#%d %s" % (n, d))

    def test_link_targets_exist(self):
        for n in (2, 3, 5, 9):
            target = EDITS[n][1].split('"')[1].strip("/")
            self.assertTrue(os.path.isfile(os.path.join(ROOT, target, "index.html")), target)

    def test_forbidden_words(self):
        for d, _ in EDITS.values():
            self.assertNotRegex(read(d + "index.html"), FORBIDDEN, d)

    def test_faq_visible_equals_jsonld(self):
        for n in FAQ_EDITS:
            d, marker = EDITS[n]
            s = read(d + "index.html")
            blocks = [json.loads(b) for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)]
            faq = [b for b in blocks if b.get("@type") == "FAQPage"]
            self.assertEqual(len(faq), 1, d)
            ld = [(norm(q["name"]), norm(q["acceptedAnswer"]["text"])) for q in faq[0]["mainEntity"]]
            vis = [(norm(q), norm(a)) for q, a in re.findall(
                r'<summary class="faq-q">(.*?)<span class="plus">.*?<div class="faq-a">(.*?)</div>', s, re.S)]
            self.assertEqual(ld, vis, d)
            self.assertIn(marker, [q for q, _ in ld], d)

    def test_lastmod(self):
        sm = read("sitemap.xml")
        for d, _ in EDITS.values():
            self.assertRegex(sm, r"<loc>https://tutor\.podlevskikh\.com/%s</loc>\s*<lastmod>2026-11-2[68]<" % re.escape(d))   # 28.11: футер с математикой


if __name__ == "__main__":
    unittest.main()
