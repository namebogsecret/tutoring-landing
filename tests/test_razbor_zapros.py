# -*- coding: utf-8 -*-
"""Секция «Разбор по вашему запросу» на /exam-prep-online/. Запуск ПОСЛЕ сборки: python3 build.py
python3 -m unittest discover -s tests -v"""
import html as htmllib
import os
import re
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import razbor_zapros as RZ  # noqa: E402

SLUGS = ["zapros-ege-fizika", "zapros-ib", "zapros-ap", "zapros-igcse", "zapros-vuz", "zapros-olimpiady"]
NAMES = ["ЕГЭ по физике", "IB Physics", "AP Physics", "IGCSE Physics", "Поступление в вуз", "Олимпиады по физике"]
BOOK = "https://calendly.com/vladimir-podlevskikh/30min"
FORBIDDEN = [r"школ", r"\bschools?\b", r"Кипр", r"Cyprus", r"Лимас", r"Limassol", r"Nyberg", r"(?-i:\bI Can\b)",
             r"без обязательств", r"гаранти", r"бесплатн", r"оплат", r"\$", r"Ереван", r"Yerevan", r"работодател"]


def read(p):
    with open(os.path.join(ROOT, p), encoding="utf-8") as f:
        return f.read()


def section(src):
    m = re.search(r'<section class="section" id="razbor-zapros">.*?\n</section>', src, re.S)
    assert m, "секция razbor-zapros не найдена"
    return m.group(0)


class TestRazborZapros(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.page = read("exam-prep-online/index.html")
        cls.sec = section(cls.page)
        cls.cards = re.findall(r'<article class="razbor-card".*?</article>', cls.sec, re.S)

    def test_section_and_heading(self):
        self.assertEqual(self.page.count('id="razbor-zapros"'), 1)
        self.assertIn("<h2>Разбор по вашему запросу</h2>", self.sec)
        self.assertIn('href="#razbor-zapros"', self.page)            # ссылка в оглавлении страницы

    def test_six_cards_with_slugs_in_order(self):
        self.assertEqual(len(self.cards), 6)
        self.assertEqual([re.search(r'id="([^"]+)"', c).group(1) for c in self.cards], SLUGS)
        for c, n in zip(self.cards, NAMES):
            self.assertIn(n, c)

    def test_four_weeks_each(self):
        for c, s in zip(self.cards, SLUGS):
            self.assertEqual(re.findall(r"<strong>(Неделя \d)\.", c), ["Неделя 1", "Неделя 2", "Неделя 3", "Неделя 4"], s)
            weeks = re.findall(r"<strong>Неделя \d\..*?</strong><ul>(.*?)</ul>", c, re.S)
            self.assertEqual(len(weeks), 4, s)
            for w in weeks:
                self.assertTrue(2 <= w.count("<li>") <= 4, (s, w.count("<li>")))
            self.assertIn("Диагностика", c)
            self.assertIn("Пробник и разбор ошибок", c)

    def test_static_no_js_needed(self):
        for c in self.cards:
            self.assertIn("<details", c)
            self.assertIn("План на 4 недели", c)
            self.assertEqual(len(re.findall(r'<a [^>]*href="http', c)), 1)   # статический запасной вариант записи
        self.assertEqual(self.sec.count('<script src="/assets/start-block.js" defer></script>'), 1)
        self.assertNotIn("<iframe", self.sec)

    def test_booking_block_utm_and_event_attrs(self):
        for c, s in zip(self.cards, SLUGS):
            b = re.search(r'<div class="razbor" data-start-block data-variant="razbor"[^>]*>.*?</div>', c, re.S)
            self.assertIsNotNone(b, s)
            b = b.group(0)
            self.assertIn('data-slug="%s"' % s, b)
            self.assertIn('data-lang="ru"', b)
            self.assertIn("&amp;utm_medium=razbor&amp;utm_campaign=%s" % s, b)       # &amp; в html
            hrefs = re.findall(r'href="([^"]+)"', b)
            self.assertEqual(len(hrefs), 1)
            self.assertEqual(htmllib.unescape(hrefs[0]),
                             BOOK + "?utm_source=tutor.podlevskikh.com&utm_medium=razbor&utm_campaign=" + s)
            self.assertIn("data-sb-cta", b)                                          # компонент считает cta-book-razbor-<slug>
            self.assertIn("Записаться на разбор", b)

    def test_booking_url_shared_with_answer_pages(self):
        import answer_pages as AP
        self.assertEqual(AP.RAZBOR_BOOK_URL, BOOK)
        self.assertIn(AP.razbor_block_html("zapros-ib", "ru", with_script=False), self.sec.replace(
            ' data-title="Разбор по этому запросу" data-lead="Принесите пробную работу или задачи, на которых застряли: разберём их и подстроим план под вас."', ""))

    def test_forbidden_words(self):
        text = self.sec
        for pat in FORBIDDEN:
            self.assertIsNone(re.search(pat, text, re.I), pat)
        low = " ".join(r["query"] + " ".join(x for _, it in r["weeks"] for x in it) for r in RZ.REQUESTS).lower()
        for w in ("баллов из", "гарантия результата"):
            self.assertNotIn(w, low)

    def test_no_invented_figures(self):
        # в тексте плана нет цифр-баллов/дат/номеров заданий: только «4 недели», «Неделя N»
        body = re.sub(r"<[^>]+>", " ", self.sec)
        body = re.sub(r"Неделя \d|4 недел\w+|\b0625\b|\b11 классе\b", " ", body)
        self.assertIsNone(re.search(r"\d", body), re.findall(r".{20}\d.{10}", body))

    def test_component_and_pages(self):
        js = read("assets/start-block.js")
        self.assertIn('"cta-book-razbor-"', js)
        self.assertIn('"razbor-shown-"', js)
        self.assertEqual(self.page.count("<h1"), 1)

    def test_llms_and_sitemap(self):
        llms = read("llms.txt")
        self.assertIn("/exam-prep-online/#razbor-zapros", llms)
        sm = read("sitemap.xml")
        m = re.search(r"<loc>https://tutor.podlevskikh.com/exam-prep-online/</loc>\s*<lastmod>([\d-]+)</lastmod>", sm)
        self.assertTrue(m and m.group(1) >= "2026-11-14")

    def test_source_has_placeholder_only(self):
        src = read("src/exam-prep-online.html")
        self.assertEqual(src.count("{{RAZBOR_ZAPROS}}"), 1)
        self.assertNotIn("razbor-card", src)


if __name__ == "__main__":
    unittest.main()
