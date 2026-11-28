# -*- coding: utf-8 -*-
"""28.11 (замер ИИ 28.11, наборы A–F, J–L): по одной правке на провалы #407, #408, #410. Метрика: из_ИИ_на_репетитора.
Запуск: python3 build.py && python3 tests/test_miss_probe_al.py
"""
import html
import json
import os
import re
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FORBIDDEN = r"(?i)Кипр|Лимас+ол|Cyprus|Limassol|Ереван|Yerevan|Nyberg|I Can School"

# номер запроса -> (slug, дословное первое предложение lead)
LEADS = {
    407: ("ap-physics-calculus-onlajn-programma-grafik-mayskie-ekzameny",
          "AP Physics и AP Calculus онлайн программа подготовки к майским экзаменам."),
    408: ("olimpiadnaya-fizika-podgotovka-tehnicheskie-vuzy-onlajn",
          "Олимпиадная физика онлайн подготовка к поступлению в технические вузы программа по месяцам."),
    410: ("podgotovka-fizika-zarubezhnye-vuzy-ucas-oxford-cambridge-onlajn",
          "Физика для поступления в зарубежные вузы онлайн UCAS Oxford PAT Cambridge план подготовки."),
}
FIRST_FAQ = {
    407: "Когда начинать готовиться к майским экзаменам AP?",
    408: "Как олимпиадная подготовка связана с поступлением?",
}


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return f.read()


def page(n):
    return read("answers/%s/index.html" % LEADS[n][0])


def norm(t):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", t))).strip()


def lead(n):
    found = [norm(p) for p in re.findall(r"<p\b[^>]*>(.*?)</p>", page(n), re.S)]
    hits = [p for p in found if p.startswith(LEADS[n][1])]
    assert hits, "#%d: нет абзаца, начинающегося с запроса" % n
    return hits[0]


def faq(n):
    s = page(n)
    blocks = [json.loads(b) for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)]
    ld = [b for b in blocks if b.get("@type") == "FAQPage"]
    assert len(ld) == 1, n
    ld = [(norm(q["name"]), norm(q["acceptedAnswer"]["text"])) for q in ld[0]["mainEntity"]]
    vis = [(norm(q), norm(a)) for q, a in re.findall(
        r'<summary class="faq-q">(.*?)<span class="plus">.*?<div class="faq-a">(.*?)</div>', s, re.S)]
    return ld, vis


class TestMissProbeAL(unittest.TestCase):
    def test_lead_starts_with_query(self):
        for n in LEADS:
            first_p = re.search(r"</h1>.*?<p\b[^>]*>(.*?)</p>", page(n), re.S).group(1)
            self.assertTrue(norm(first_p).startswith(LEADS[n][1]), "#%d: %s" % (n, norm(first_p)))

    def test_lead_length_and_author(self):
        for n in LEADS:
            self.assertLessEqual(len(lead(n).split()), 50, n)
            self.assertRegex(lead(n), "МГУ|Подлевских")

    def test_first_faq_visible_equals_jsonld(self):
        for n, q in FIRST_FAQ.items():
            ld, vis = faq(n)
            self.assertEqual(ld, vis, n)
            self.assertEqual(ld[0][0], q, n)
            self.assertEqual([x for x, _ in ld].count(q), 1, n)

    def test_407_old_question_not_duplicated(self):
        ld, _ = faq(407)
        self.assertNotIn("Сколько месяцев нужно на подготовку к майским экзаменам?", [q for q, _ in ld])
        self.assertIn("семь месяцев, с ноября по май", ld[0][1])

    def test_408_answer_has_no_invented_numbers(self):
        self.assertNotRegex(faq(408)[0][0][1], r"\d")

    def test_410_esat_in_second_sentence(self):
        second = lead(410)[len(LEADS[410][1]):].strip().split(". ")[0]
        self.assertIn("PAT не используется", second)
        self.assertIn("ESAT", second)

    def test_forbidden_words(self):
        for n in LEADS:
            self.assertNotRegex(page(n), FORBIDDEN, n)

    def test_lastmod(self):
        sm = read("sitemap.xml")
        for slug, _ in LEADS.values():
            self.assertRegex(sm, r"<loc>https://tutor\.podlevskikh\.com/answers/%s/</loc>\s*<lastmod>2026-11-28<" % slug)


if __name__ == "__main__":
    unittest.main()
