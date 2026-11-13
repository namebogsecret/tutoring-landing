# -*- coding: utf-8 -*-
"""Тесты страниц-ответов /answers/ (answer_pages.py) и сборщика.
Запуск:  python3 build.py && python3 tests/test_answer_pages.py
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
import answer_pages as AP                      # noqa: E402
from test_pillar_pages import FORBIDDEN, FORBIDDEN_VISIBLE, visible_text, jsonld_blocks  # noqa: E402

BASE = "https://tutor.podlevskikh.com"
ALL = AP.ANSWERS + AP.ANSWERS_EN
URLS = {a["slug"]: "/answers/%s/" % a["slug"] for a in ALL}
HUB = "/answers/"
HUB_EN = "/answers/en/"

# Дополнительно к FORBIDDEN из pillar-тестов: решение Vladimir 06.11 (школа, Кипр, Лимассол).
EXTRA_FORBIDDEN = [r"школ", r"\bschools?\b", r"Кипр", r"Cyprus", r"Лимас", r"Limassol", r"работодател", r"employer",
                   r"бесплатн", r"\bfree\b(?!-response)", r"гаранти", r"guarantee"]


def read(url):
    with open(os.path.join(ROOT, url.strip("/"), "index.html"), encoding="utf-8") as f:
        return f.read()


# Единый блок «записаться на разбор» (задача автопилота 13.11): ЕДИНСТВЕННОЕ разрешённое место записи на
# страницах-ответах. Запрет «Записаться/Book/Calendly» действует на всю остальную страницу — блок вырезается
# ровно по своей разметке, а сам проверяется отдельно (TestRazbor).
RAZBOR_RE = re.compile(r'<div class="razbor" data-start-block data-variant="razbor"[^>]*>.*?</div>\s*'
                       r'<script src="/assets/start-block\.js" defer></script>', re.S)


def strip_razbor(s):
    return RAZBOR_RE.sub(" ", s, count=1)


class Base(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.src = {u: read(u) for u in list(URLS.values()) + [HUB, HUB_EN]}


class TestRegistry(unittest.TestCase):
    def test_one_page_per_failed_query(self):
        # 11 запросов замера 11.11 без «Кипр»-запроса (#12, запрещён решением 06.11)
        self.assertEqual(sorted(a["n"] for a in AP.ANSWERS), list(range(1, 12)))
        self.assertEqual(len(set(URLS.values())), 17)  # 11 + 6 EN-пар

    def test_queries_match_measurement_file(self):
        path = os.path.expanduser("~/воронка-репетитор/ЗАМЕРЫ-ИИ.md")
        if not os.path.exists(path):
            self.skipTest("ЗАМЕРЫ-ИИ.md недоступен")
        text = open(path, encoding="utf-8").read()
        for n, q in AP.QUERIES.items():
            self.assertIn("| %d | %s |" % (n, q), text, "запрос #%d не совпадает с замером" % n)

    def test_cyprus_query_not_covered(self):
        self.assertNotIn(12, AP.QUERIES)


class TestForbidden(Base):
    def test_no_forbidden_words(self):
        for u, s in self.src.items():
            s2 = strip_razbor(s).replace('data-cta="tutor-page"', "")
            for pat in FORBIDDEN + EXTRA_FORBIDDEN:
                m = re.search(pat, s2, re.I)
                self.assertIsNone(m, "%s: %r near %r" % (u, pat, s2[max(0, m.start() - 40):m.end() + 40] if m else ""))

    def test_no_marketplaces_in_visible(self):
        for u, s in self.src.items():
            vis = re.sub(r'(?s)<script type="application/ld\+json">.*?</script>', " ", s)
            for pat in FORBIDDEN_VISIBLE:
                self.assertIsNone(re.search(pat, vis, re.I), "%s: %r" % (u, pat))

    def test_forbidden_detector_works(self):
        # самопроверка теста: паттерны действительно ловят запрещённое
        for bad in ("школа", "в Лимассоле", "Кипр", "Cyprus"):
            self.assertTrue(any(re.search(p, bad, re.I) for p in FORBIDDEN + EXTRA_FORBIDDEN), bad)


UPGRADED = ["repetitor-igcse-fizika-0625-na-russkom", "repetitor-ib-physics-russkoyazychnyj",
            "ib-physics-hl-tutor-online", "russian-ege-physics-tutor-english-speaking"]


class TestUpgraded(Base):
    """Правки 13.11 из «одна правка на провал»: таблица, свежая дата, FAQPage, прямой ответ."""
    def test_table_date_faq(self):
        for slug in UPGRADED:
            s = self.src["/answers/%s/" % slug]
            self.assertIn('<table class="spec-table">', s, slug)
            self.assertRegex(s, r'<time datetime="2026-11-13">', slug)
            self.assertIn('"dateModified": "2026-11-13"', s, slug)
            self.assertIn('"@type": "FAQPage"', s, slug)
            self.assertIn("<lastmod>2026-11-13</lastmod>", open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8").read())
            # таблица стоит до FAQ и после lead
            self.assertLess(s.index('class="lead'), s.index("<table"), slug)


class TestFacts(Base):
    def test_numeric_claims_whitelisted(self):
        allowed_years, allowed_students = {"23"}, {"350"}
        for u, s in self.src.items():
            t = visible_text(s)
            for m in re.finditer(r"(?<!\d)(\d{1,3})\+?\s*(years|лет|года|учеников|students)", t):
                n, w = m.group(1), m.group(2)
                ok = (n in allowed_years) if w in ("years", "лет", "года") else (n in allowed_students)
                self.assertTrue(ok, "%s: непроверенная цифра %r" % (u, m.group(0)))
            for m in re.finditer(r"\d+/\d+", t):
                self.assertEqual(m.group(0), "200/200", "%s: %s" % (u, m.group(0)))

    def test_case_not_claimed_as_physics(self):
        for u, s in self.src.items():
            t = visible_text(s)
            if "Полина" in t:
                self.assertRegex(t, r"96 баллов на ЕГЭ и 100 на ДВИ")
                self.assertNotRegex(t, r"96[^.]{0,30}по физике")
            if "Polina" in t:
                self.assertRegex(t, r"96 on the EGE and 100 on the DVI")
                self.assertNotRegex(t, r"96[^.]{0,30}in physics")


class TestMeta(Base):
    def test_single_h1_title_desc_canonical(self):
        for slug, u in list(URLS.items()) + [("hub", HUB), ("hub-en", HUB_EN)]:
            s = self.src[u]
            self.assertEqual(len(re.findall(r"<h1\b", s)), 1, u)
            title = re.search(r"<title>(.*?)</title>", s, re.S).group(1)
            desc = re.search(r'<meta name="description" content="(.*?)"', s).group(1)
            self.assertTrue(0 < len(title) <= 65, "%s title %d" % (u, len(title)))
            self.assertTrue(0 < len(desc) <= 160, "%s desc %d" % (u, len(desc)))
            self.assertIn('<link rel="canonical" href="%s%s"' % (BASE, u), s)

    def test_html_lang(self):
        for a in ALL:
            self.assertIn('<html lang="%s"' % a["lang"], self.src[URLS[a["slug"]]])


class TestAnswerFirst(Base):
    def test_lead_is_direct_answer(self):
        for a in ALL:
            s = self.src[URLS[a["slug"]]]
            m = re.search(r'<p class="lead[^"]*">(.*?)</p>', s, re.S)
            self.assertIsNotNone(m, a["slug"])
            lead = visible_text(m.group(1))
            self.assertRegex(lead, r"Podlevskikh|Подлевских|MSU|МГУ|There is no objective", a["slug"])
            self.assertLessEqual(len(lead.split()), 70, "lead слишком длинный: " + a["slug"])
            # ответ идёт раньше любого h2 и раньше списка фактов
            self.assertLess(s.index('class="lead'), s.index("<h2"), a["slug"])

    def test_key_facts_block(self):
        for a in ALL:
            s = self.src[URLS[a["slug"]]]
            self.assertIn('<h2 id="facts">', s)
            self.assertGreaterEqual(len(a["facts"]), 4, a["slug"])


class TestEnglishAndHreflang(Base):
    def test_en_twins_cover_ru_pages_1_to_6(self):
        self.assertEqual(sorted(a["twin"] for a in AP.ANSWERS_EN), list(range(1, 7)))
        self.assertEqual(sorted(AP.QUERIES_EN), list(range(1, 7)))
        for a in AP.ANSWERS_EN:
            self.assertEqual(a["lang"], "en")
            self.assertEqual(len(a["faq"]), len(next(r for r in AP.ANSWERS if r["n"] == a["twin"])["faq"]))

    def test_no_cyrillic_in_visible_en_text(self):
        for a in AP.ANSWERS_EN:
            src = self.src[URLS[a["slug"]]]
            main = src[src.index('<section class="subhero'):src.index('id="tutor-page-block"')]  # без общего nav/футера
            vis = visible_text(main)
            # допустимы только «Владимир Подлевских»-подобных вставок нет: EN-страница без кириллицы в видимом тексте,
            # кроме пометки «(RU)»-ссылок и названий
            body = re.sub(r"\(RU\)", "", vis)
            self.assertIsNone(re.search(r"[а-яё]", body, re.I), a["slug"])

    def hreflangs(self, u):
        return dict(re.findall(r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)"', self.src[u]))

    def test_pairs_are_reciprocal(self):
        for a in AP.ANSWERS_EN:
            en_u = URLS[a["slug"]]
            ru_slug = next(r["slug"] for r in AP.ANSWERS if r["n"] == a["twin"])
            ru_u = URLS[ru_slug]
            for u in (en_u, ru_u):
                h = self.hreflangs(u)
                self.assertEqual(h["en"], BASE + en_u, u)
                self.assertEqual(h["ru"], BASE + ru_u, u)
                self.assertEqual(h["x-default"], BASE + en_u, u)

    def test_standalone_en_pages_self_and_default(self):
        for a in AP.ANSWERS:
            if a["lang"] == "en":
                h = self.hreflangs(URLS[a["slug"]])
                self.assertEqual(h, {"en": BASE + URLS[a["slug"]], "x-default": BASE + URLS[a["slug"]]})

    def test_hubs_reciprocal(self):
        for u in (HUB, HUB_EN):
            h = self.hreflangs(u)
            self.assertEqual((h["ru"], h["en"], h["x-default"]), (BASE + HUB, BASE + HUB_EN, BASE + HUB_EN))

    def test_sitemap_has_xhtml_alternates(self):
        sm = open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8").read()
        self.assertIn('xmlns:xhtml="http://www.w3.org/1999/xhtml"', sm)
        n_en = sm.count('hreflang="en" href="%s/answers/ege-physics-tutor-online/"' % BASE)
        self.assertEqual(n_en, 2)  # в блоках RU- и EN-страницы

    def test_llms_lists_en_pages(self):
        llms = open(os.path.join(ROOT, "llms.txt"), encoding="utf-8").read()
        for a in AP.ANSWERS_EN:
            self.assertIn(BASE + URLS[a["slug"]], llms)

    def test_tutor_page_metric_hook_on_en(self):
        for a in AP.ANSWERS_EN:
            self.assertIn('data-cta="tutor-page" href="/exam-prep-online/"', self.src[URLS[a["slug"]]])


class TestJsonLd(Base):
    def test_faqpage_matches_visible(self):
        for a in ALL:
            u = URLS[a["slug"]]
            s = self.src[u]
            blocks = jsonld_blocks(s)
            types = [b.get("@type") for b in blocks]
            for t in ("FAQPage", "BreadcrumbList"):
                self.assertIn(t, types, u)
            faq = blocks[types.index("FAQPage")]
            names = [q["name"] for q in faq["mainEntity"]]
            self.assertGreaterEqual(len(names), 3, u)
            vis = re.findall(r'<summary class="faq-q">(.*?)<span class="plus">', s, re.S)
            vis = [re.sub(r"\s+", " ", htmllib.unescape(v)).strip() for v in vis]
            self.assertEqual(vis, names, u)
            answers = re.findall(r'<div class="faq-a">(.*?)</div>', s, re.S)
            for q, ans in zip(faq["mainEntity"], answers):
                self.assertEqual(q["acceptedAnswer"]["text"], visible_text(ans), u)

    def test_no_commerce_schema(self):
        for u, s in self.src.items():
            raw = "\n".join(re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S))
            for bad in ("aggregateRating", '"offers"', '"price"', "priceCurrency", "Review"):
                self.assertNotIn(bad, raw, u)

    def test_provider_is_person_entity(self):
        for a in ALL:
            blocks = jsonld_blocks(self.src[URLS[a["slug"]]])
            main = [b for b in blocks if b.get("@type") in ("Course", "Service")][0]
            self.assertEqual(main["provider"]["@id"], "https://tutor.podlevskikh.com/#vladimir")


class TestLinks(Base):
    def test_pillar_and_tutor_links(self):
        for a in ALL:
            s = self.src[URLS[a["slug"]]]
            hub = HUB if a["lang"] == "ru" else HUB_EN
            for h in ("/ege-physics/", "/ib-physics-tutor/", "/ap-physics-tutor/", "/igcse-physics-0625/",
                      "/exam-prep-online/", hub):
                self.assertIn('href="%s"' % h, s, "%s lacks %s" % (a["slug"], h))
            self.assertIn('data-cta="tutor-page" href="/exam-prep-online/"', s)

    def test_hub_lists_every_page(self):
        for a in ALL:
            hub = HUB if a["lang"] == "ru" else HUB_EN
            if a["lang"] == "ru" or a["n"] > 100 or a["lang"] == "en":
                self.assertIn('href="%s"' % URLS[a["slug"]], self.src[hub], a["slug"])

    def test_internal_links_resolve_and_in_sitemap(self):
        locs = set(re.findall(r"<loc>(.*?)</loc>", open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8").read()))
        for u, s in self.src.items():
            for href in re.findall(r'href="(/[^"/][^"]*)"', s):
                path = re.split(r"[#?]", href)[0]
                if os.path.splitext(path)[1]:
                    self.assertTrue(os.path.exists(os.path.join(ROOT, path.strip("/"))), "%s: %s" % (u, href))
                else:
                    self.assertTrue(os.path.exists(os.path.join(ROOT, path.strip("/"), "index.html")), "%s: %s" % (u, href))
                    self.assertIn(BASE + path, locs, "%s: %s not in sitemap" % (u, href))

    def test_external_links_noopener(self):
        for u, s in self.src.items():
            for tag in re.findall(r'<a [^>]*href="https?://[^"]*"[^>]*>', s):
                if "podlevskikh.com" in tag:
                    continue
                self.assertIn("noopener", tag, "%s: %s" % (u, tag))


class TestBuilder(unittest.TestCase):
    def test_sitemap_and_llms_contain_answers(self):
        sm = open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8").read()
        llms = open(os.path.join(ROOT, "llms.txt"), encoding="utf-8").read()
        for u in list(URLS.values()) + [HUB, HUB_EN]:
            self.assertIn("<loc>%s%s</loc>" % (BASE, u), sm)
        for u in URLS.values():
            self.assertIn(BASE + u, llms)
        self.assertIn("## Short answers to common queries", llms)

    def test_build_is_deterministic_and_clean(self):
        import subprocess
        before = {u: read(u) for u in URLS.values()}
        r = subprocess.run([sys.executable, os.path.join(ROOT, "build.py")], capture_output=True, text=True, cwd=ROOT)
        self.assertEqual(r.returncode, 0, r.stderr)
        for u, t in before.items():
            self.assertEqual(read(u), t, u)

    def test_build_page_accepts_body_html(self):
        import build
        p = {"url": "/answers/_t/", "lang": "ru", "body_html": "<h1>x</h1>{{FAQ}}", "title": "t", "desc": "d",
             "crumbs": [("a", "/"), ("b", None)], "faq": [("q?", "a.")], "no_cta": True}
        import tempfile, shutil
        out = os.path.join(ROOT, "answers", "_t")
        try:
            build.build_page(p)
            self.assertIn("FAQPage", open(os.path.join(out, "index.html"), encoding="utf-8").read())
        finally:
            shutil.rmtree(out, ignore_errors=True)


if __name__ == "__main__":
    unittest.main(verbosity=1)


class TestRazbor(Base):
    """Блок «записаться на разбор»: на каждой странице-ответе ровно один, UTM по странице-источнику."""

    def test_block_on_every_answer_page(self):
        for a in ALL:
            s = self.src[URLS[a["slug"]]]
            blocks = RAZBOR_RE.findall(s)
            self.assertEqual(len(blocks), 1, a["slug"])
            b = blocks[0]
            slug = AP.razbor_slug(a)
            self.assertIn('data-slug="%s"' % slug, b)
            self.assertIn('data-lang="%s"' % a["lang"], b)
            hrefs = re.findall(r'href="([^"]+)"', b)
            self.assertEqual(len(hrefs), 1, a["slug"])
            self.assertEqual(htmllib.unescape(hrefs[0]),
                             "https://calendly.com/vladimir-podlevskikh/30min?utm_source=tutor.podlevskikh.com"
                             "&utm_medium=razbor&utm_campaign=" + slug)
            self.assertIn("Записаться на разбор" if a["lang"] == "ru" else "Book a walkthrough", b)
            self.assertRegex(slug, r"^[a-z0-9-]+$")

    def test_slugs_unique(self):
        slugs = [AP.razbor_slug(a) for a in ALL]
        self.assertEqual(len(slugs), len(set(slugs)))

    def test_block_itself_clean(self):
        bad = [r"школ", r"\bschools?\b", r"Кипр", r"Cyprus", r"Лимас", r"Limassol", r"Nyberg", r"(?-i:\bI Can\b)",
               r"бесплатн", r"\bfree\b", r"гаранти", r"оплат", r"\$", r"Ереван", r"Yerevan"]
        for a in ALL:
            b = RAZBOR_RE.search(self.src[URLS[a["slug"]]]).group(0)
            for pat in bad:
                self.assertIsNone(re.search(pat, b, re.I), (a["slug"], pat))

    def test_no_razbor_on_hubs(self):
        for u in (HUB, HUB_EN):
            self.assertIsNone(RAZBOR_RE.search(self.src[u]), u)

    def test_component_shipped_and_same_as_source(self):
        mine = open(os.path.join(ROOT, "assets", "start-block.js"), encoding="utf-8").read()
        self.assertIn('variant === "razbor"', mine)
        self.assertIn('"cta-book-razbor-"', mine)
        self.assertIn('"razbor-shown-"', mine)
        self.assertIn('"https://calendly.com/vladimir-podlevskikh/30min"', mine)
        src = os.path.expanduser("~/воронка-репетитор/components/start-block/start-block.js")
        if os.path.exists(src) and 'variant === "razbor"' in open(src, encoding="utf-8").read():
            self.assertEqual(mine, open(src, encoding="utf-8").read(), "assets/start-block.js разошёлся с исходником")

    def test_site_js_skips_block_links(self):
        js = open(os.path.join(ROOT, "assets", "site.js"), encoding="utf-8").read()
        self.assertIn('if(a.hasAttribute("data-sb-cta")) return;', js)   # без дубля cta-calendly в «Записях»
