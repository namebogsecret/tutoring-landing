# -*- coding: utf-8 -*-
"""Тесты страниц-ответов /answers/ (answer_pages.py) и сборщика.
Запуск:  python3 build.py && python3 tests/test_answer_pages.py
"""
import html as htmllib
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
ALL = AP.ANSWERS + AP.ANSWERS_EN + AP.ANSWERS_MATH + AP.ANSWERS_PHYS
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
        self.assertEqual(len(set(URLS.values())), 33)  # 11 + 6 EN-пар + 6 математических + 4 AP/IB Physics + 1 план ЕГЭ физика + 2 «как выбрать» + 1 A-level/IB + 1 план ЕГЭ математика + 1 IGCSE физика/математика

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
            # 19.11 страница правилась повторно (TestMissFix1119) — дата 13.11 или 19.11
            self.assertRegex(s, r'<time datetime="2026-11-(13|19)">', slug)
            self.assertRegex(s, r'"dateModified": "2026-11-(13|19)"', slug)
            self.assertIn('"@type": "FAQPage"', s, slug)
            self.assertIn("<lastmod>2026-11-13</lastmod>", open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8").read())
            # таблица стоит до FAQ и после lead
            self.assertLess(s.index('class="lead'), s.index("<table"), slug)


REPROBE_SLUGS = ["repetitor-fizika-ege-online", "repetitor-fizika-ege-msu", "podgotovka-ege-fizika-za-rubezhom",
                 "repetitor-ap-physics-na-russkom", "vladimir-podlevskikh-physics-tutor",
                 "igcse-physics-0625-tutor-russian-speaking", "ap-physics-1-tutor-online",
                 "ege-physics-tutor-online", "ege-physics-tutor-msu", "ege-physics-preparation-abroad-online",
                 "ap-physics-tutor-russian-speaking"]


class TestReprobeTables(Base):
    """16.11 (замер 15.11, 0/12): таблица на первом экране + дата + FAQPage на страницах #1–#3, #6–#9 и EN-парах."""
    def test_table_date_faq(self):
        for slug in REPROBE_SLUGS:
            s = self.src["/answers/%s/" % slug]
            self.assertIn('<table class="spec-table">', s, slug)
            self.assertRegex(s, r'<time datetime="2026-11-(16|19)">', slug)
            self.assertRegex(s, r'"dateModified": "2026-11-(16|19)"', slug)
            self.assertIn('"@type": "FAQPage"', s, slug)
            self.assertLess(s.index('class="lead'), s.index("<table"), slug)
            # таблица до «Кто преподаёт» и до разделов-пояснений
            self.assertLess(s.index("<table"), s.index('id="who"'), slug)


class TestMissFix1119(Base):
    """19.11: по одной нацеленной правке на провал замера 15.11 (#1–#11; #12 запрещён). Метрика: из_ИИ_на_репетитора."""
    def page(self, slug):
        return self.src["/answers/%s/" % slug]

    def test_lead_repeats_query_1(self):
        s = self.page("repetitor-fizika-ege-online")
        self.assertRegex(s, r'class="lead reveal">Репетитор по физике ЕГЭ онлайн')

    def test_question_h2_with_short_answer_3(self):
        s = self.page("podgotovka-ege-fizika-za-rubezhom")
        m = re.search(r"<h2>Как готовиться к ЕГЭ по физике, живя за границей\?</h2>\s*<p>(.*?)</p>", s, re.S)
        self.assertTrue(m)
        self.assertLessEqual(len(re.sub(r"<[^>]+>", "", m.group(1)).split()), 50)

    def test_six_topics_4(self):
        s = self.page("repetitor-igcse-fizika-0625-na-russkom")
        self.assertIn("Шесть тем IGCSE Physics 0625", s)
        self.assertIn("Космическая физика", s)

    def test_format_block_5(self):
        self.assertIn("IB Physics SL/HL на русском: как проходят занятия", self.page("repetitor-ib-physics-russkoyazychnyj"))

    def test_scope_in_lead_6(self):
        s = self.page("repetitor-ap-physics-na-russkom")
        self.assertRegex(s, r'class="lead reveal">[^<]*Physics C: Mechanics')

    def test_profilepage_7(self):
        s = self.page("vladimir-podlevskikh-physics-tutor")
        self.assertIn('"@type": "ProfilePage"', s)
        self.assertIn("https://tutor.podlevskikh.com/#vladimir", s)

    def test_h1_verbatim_8(self):
        self.assertIn(">IGCSE Physics 0625 tutor, Russian-speaking</h1>", self.page("igcse-physics-0625-tutor-russian-speaking"))

    def test_checklists_9_10(self):
        s9 = self.page("ap-physics-1-tutor-online")
        self.assertIn("five checks", s9)
        self.assertEqual(len(re.findall(r"<tr><td>", s9)), 5)
        s10 = self.page("ib-physics-hl-tutor-online")
        self.assertIn("How to choose an IB Physics HL tutor: five checks", s10)

    def test_table_first_11(self):
        s = self.page("russian-ege-physics-tutor-english-speaking")
        self.assertLess(s.index("<table"), s.index('id="facts"'))

    def test_tutor_link_utm_via_razbor(self):
        # ссылка на страницу репетитора с UTM: блок «разбор» (utm_medium=razbor, campaign=tutor-answers-<slug>);
        # tutor→tutor UTM не ставим (tutor_links.py: «ссылка tutor→tutor не сквозная»)
        for slug in ("repetitor-fizika-ege-online", "ap-physics-1-tutor-online"):
            self.assertIn("utm_campaign=tutor-answers-" + slug, self.page(slug))

    def test_faq_counts_and_forbidden(self):
        for slug in ("repetitor-fizika-ege-msu", "ap-physics-1-tutor-online", "igcse-physics-0625-tutor-russian-speaking"):
            s = self.page(slug)
            self.assertIn('"@type": "FAQPage"', s)
            self.assertNotRegex(s, r"(?i)Кипр|Лимассол|Cyprus|Limassol")


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
        for a in AP.ANSWERS_EN + [m for m in AP.ANSWERS_MATH + AP.ANSWERS_PHYS if m["lang"] == "en"]:
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
        for a in AP.ANSWERS_EN + AP.ANSWERS_MATH + AP.ANSWERS_PHYS:
            self.assertIn(BASE + URLS[a["slug"]], llms)

    def test_tutor_page_metric_hook_on_en(self):
        for a in AP.ANSWERS_EN + [m for m in AP.ANSWERS_MATH + AP.ANSWERS_PHYS if m["lang"] == "en"]:
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
        import shutil
        out = os.path.join(ROOT, "answers", "_t")
        try:
            build.build_page(p)
            self.assertIn("FAQPage", open(os.path.join(out, "index.html"), encoding="utf-8").read())
        finally:
            shutil.rmtree(out, ignore_errors=True)


MATH_RU = [a for a in AP.ANSWERS_MATH if a["lang"] == "ru"]
MATH_EN = [a for a in AP.ANSWERS_MATH if a["lang"] == "en"]
OFFICIAL = {   # twin n → (подстрока официального URL, ...) — страницы программ, на которые обязана ссылаться пара
    201: ("https://www.ibo.org/programmes/diploma-programme/curriculum/mathematics/",),
    202: ("https://apcentral.collegeboard.org/courses/ap-calculus-bc",),
    203: ("https://www.cambridgeinternational.org/programmes-and-qualifications/cambridge-igcse-mathematics-0580/",),
}
MATH_QUERIES = ["репетитор IB Math AA онлайн русскоязычный", "репетитор AP Calculus онлайн на русском",
                "репетитор IGCSE математика 0580 на русском", "best IB Math AA HL tutor online",
                "best AP Calculus BC tutor online", "IGCSE Maths 0580 tutor Russian-speaking"]


class TestMathPages(Base):
    """Шесть математических страниц-ответов (15.11): покрытие запросов, пары, официальные ссылки, FAQ, дата."""

    def test_six_queries_covered(self):
        self.assertEqual(len(MATH_RU), 3)
        self.assertEqual(len(MATH_EN), 3)
        self.assertEqual(sorted(AP.QUERIES_MATH.values()), sorted(MATH_QUERIES))
        for a in AP.ANSWERS_MATH:
            self.assertIn(AP.QUERIES_MATH[a["n"]], self.src[URLS[a["slug"]]], a["slug"])   # запрос в eyebrow

    def test_pairs_and_hreflang(self):
        for en in MATH_EN:
            ru = next(r for r in MATH_RU if r["n"] == en["twin"])
            for u in (URLS[en["slug"]], URLS[ru["slug"]]):
                h = dict(re.findall(r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)"', self.src[u]))
                self.assertEqual(h["en"], BASE + URLS[en["slug"]], u)
                self.assertEqual(h["ru"], BASE + URLS[ru["slug"]], u)
                self.assertEqual(h["x-default"], BASE + URLS[en["slug"]], u)

    def test_official_program_links(self):
        for en in MATH_EN:
            ru = next(r for r in MATH_RU if r["n"] == en["twin"])
            for a in (en, ru):
                s = self.src[URLS[a["slug"]]]
                for url in OFFICIAL[en["twin"]]:
                    m = re.search(r'<a href="%s"[^>]*>' % re.escape(url), s)
                    self.assertIsNotNone(m, "%s: нет ссылки %s" % (a["slug"], url))
                    self.assertIn('rel="noopener"', m.group(0))

    def test_date_and_dateModified(self):
        sm = open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8").read()
        for a in AP.ANSWERS_MATH:
            s = self.src[URLS[a["slug"]]]
            self.assertRegex(s, r'<time datetime="2026-11-15">', a["slug"])
            self.assertIn('"dateModified": "2026-11-15"', s, a["slug"])
            self.assertRegex(visible_text(s), r"(Обновлено: 15 ноября 2026|Updated: 15 November 2026)", a["slug"])
            blk = re.search(r"<url>\s*<loc>%s%s</loc>\s*<lastmod>([^<]*)</lastmod>" % (re.escape(BASE), re.escape(URLS[a["slug"]])), sm)
            self.assertIsNotNone(blk, a["slug"])
            self.assertEqual(blk.group(1), "2026-11-15")

    def test_faq_jsonld_valid_json(self):
        import json
        for a in AP.ANSWERS_MATH:
            s = self.src[URLS[a["slug"]]]
            raws = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
            parsed = [json.loads(r) for r in raws]          # каждый блок — валидный JSON
            faq = [p for p in parsed if p.get("@type") == "FAQPage"]
            self.assertEqual(len(faq), 1, a["slug"])
            self.assertGreaterEqual(len(faq[0]["mainEntity"]), 3, a["slug"])
            self.assertGreaterEqual(len(a["faq"]), 3)

    def test_razbor_and_tutor_cta(self):
        for a in AP.ANSWERS_MATH:
            s = self.src[URLS[a["slug"]]]
            self.assertEqual(len(RAZBOR_RE.findall(s)), 1, a["slug"])
            self.assertIn('data-cta="tutor-page" href="/exam-prep-online/"', s)

    def test_hubs_link_math_pages(self):
        for a in MATH_RU:
            self.assertIn('href="%s"' % URLS[a["slug"]], self.src[HUB])
        for a in MATH_EN:
            self.assertIn('href="%s"' % URLS[a["slug"]], self.src[HUB_EN])

    def test_math_who_facts_only_known(self):
        for a in AP.ANSWERS_MATH:
            t = visible_text(self.src[URLS[a["slug"]]])
            self.assertIn("5165", t)
            self.assertIn("200/200", t)
            for pat in (r"Лимасс", r"Limassol", r"Кипр", r"Cyprus"):
                self.assertIsNone(re.search(pat, t, re.I), (a["slug"], pat))

    def test_unverified_exam_numbers_absent_on_ib(self):
        # ibo.org отдаёт 403 автоматическим запросам: часы/веса/длительность работ IB на страницах не приводятся
        for a in (m for m in AP.ANSWERS_MATH if m["n"] in (201, 301)):
            t = visible_text(self.src[URLS[a["slug"]]])
            self.assertIsNone(re.search(r"\b(150|240)\b", t), a["slug"])
            self.assertIsNone(re.search(r"\b(Paper [12]|Paper 3)\b.*\d+ (min|мин)", t), a["slug"])

    def test_ib_update_caveat_and_ab_exam_link(self):
        upd = "https://www.ibo.org/university-admission/latest-curriculum-updates/dp-mathematics-analysis-and-approaches-updates/"
        for n in (201, 301):
            a = next(m for m in AP.ANSWERS_MATH if m["n"] == n)
            s = self.src[URLS[a["slug"]]]
            self.assertIn('<a href="%s" target="_blank" rel="noopener">' % upd, s, n)
            t = visible_text(s)
            self.assertRegex(t, r"обновлённую программу математики DP|updated DP mathematics programme")
            self.assertIsNone(re.search(r"\b20(2[7-9]|3\d)\b", t), n)   # дат перехода нет
        for n in (202, 302):
            a = next(m for m in AP.ANSWERS_MATH if m["n"] == n)
            self.assertIn('href="https://apcentral.collegeboard.org/courses/ap-calculus-ab/exam"', self.src[URLS[a["slug"]]], n)

    def test_ap_format_matches_verified_facts(self):
        for n in (202, 302):
            a = next(m for m in AP.ANSWERS_MATH if m["n"] == n)
            s = self.src[URLS[a["slug"]]]
            self.assertIn('<table class="spec-table">', s)
            t = visible_text(s)
            for token in ("42", "100", "90", "29", "62", "13", "38"):
                self.assertRegex(t, r"\b%s\b" % token, (n, token))

    def test_igcse_math_facts(self):
        for n in (203, 303):
            a = next(m for m in AP.ANSWERS_MATH if m["n"] == n)
            s = self.src[URLS[a["slug"]]]
            t = visible_text(s)
            self.assertIn("0580", t)
            self.assertRegex(t, r"80")
            self.assertRegex(t, r"100")
            self.assertIn("A*–E", t)


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
                             "&utm_medium=razbor&utm_campaign=" + slug + ("" if a["lang"] == "ru" else "&utm_content=intl"))
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

    def test_en_country_utm_in_component(self):
        mine = open(os.path.join(ROOT, "assets", "start-block.js"), encoding="utf-8").read()
        self.assertIn('"&utm_content=" + country', mine)
        self.assertIn('"razbor-country-"', mine)
        self.assertNotIn("cta-book-razbor-country", mine)   # событие среза не должно попадать под счётчик «записей»

    def test_site_js_skips_block_links(self):
        js = open(os.path.join(ROOT, "assets", "site.js"), encoding="utf-8").read()
        self.assertIn('if(a.hasAttribute("data-sb-cta")) return;', js)   # без дубля cta-calendly в «Записях»


PHYS_QUERIES = ["Подготовка к IGCSE по физике и математике онлайн: программа Edexcel и Cambridge, план по месяцам, типичные ошибки, первое занятие", "Подготовка к A-level и IB по физике онлайн: программа, план по месяцам, разбор типичных ошибок", "Подготовка к ЕГЭ по физике 2027: план по месяцам", "AP Physics 1, 2 и C: чем отличаются и какой сдавать", "IB Physics HL или SL: чем отличаются и как готовиться",
                "AP Physics 1 vs 2 vs C: which exam to take", "IB Physics HL vs SL: differences and how to prepare",
                "How to choose an AP Physics 1 tutor online: 5 criteria", "How to choose an IB Physics HL tutor online: 5 criteria",
                "Подготовка к ЕГЭ по математике (профиль) 2027: план по месяцам, типичные ошибки, как заниматься онлайн"]


class TestPhysPages(Base):
    """Четыре страницы AP Physics 1/2/C и IB Physics HL/SL (15.11): запросы, пары, FAQPage, блок разбора с UTM, факты."""
    PH = [a for a in AP.ANSWERS_PHYS if a["n"] not in (405, 406)]    # 405 (математика, 18.11) — в TestEgeMathPlanPage

    def u(self, n):
        return self.src[URLS[next(a["slug"] for a in self.PH if a["n"] == n)]]

    def test_four_queries_and_pairs(self):
        self.assertEqual(len(self.PH), 8)
        self.assertEqual(sorted(AP.QUERIES_PHYS.values()), sorted(PHYS_QUERIES))
        for a in self.PH:
            self.assertIn(AP.QUERIES_PHYS[a["n"]], self.src[URLS[a["slug"]]], a["slug"])
        for en, ru in ((501, 401), (502, 402)):
            en_u, ru_u = URLS[next(a["slug"] for a in self.PH if a["n"] == en)], URLS[next(a["slug"] for a in self.PH if a["n"] == ru)]
            for u in (en_u, ru_u):
                h = dict(re.findall(r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)"', self.src[u]))
                self.assertEqual((h["en"], h["ru"], h["x-default"]), (BASE + en_u, BASE + ru_u, BASE + en_u), u)

    def test_faqpage_jsonld_matches_visible_and_has_5(self):
        for a in self.PH:
            s = self.src[URLS[a["slug"]]]
            faq = [b for b in jsonld_blocks(s) if b.get("@type") == "FAQPage"]
            self.assertEqual(len(faq), 1, a["slug"])
            qs = [e["name"] for e in faq[0]["mainEntity"]]
            self.assertEqual(qs, [q for q, _ in a["faq"]])
            self.assertGreaterEqual(len(qs), 5)
            vis = visible_text(s)
            for q, ans in a["faq"]:
                self.assertIn(q, vis)

    def test_razbor_block_utm_per_page(self):
        for a in self.PH:
            b = RAZBOR_RE.search(self.src[URLS[a["slug"]]]).group(0)
            self.assertIn("utm_campaign=tutor-answers-" + a["slug"], b)
            self.assertIn("utm_medium=razbor", b)
            self.assertIn("utm_source=tutor.podlevskikh.com", b)

    def test_date_table_and_hubs(self):
        for a in (x for x in self.PH if x["n"] != 404):   # 404 — страница A-level/IB (18.11), своя дата и тесты
            s = self.src[URLS[a["slug"]]]
            self.assertIn('<table class="spec-table">', s)
            self.assertIn('<time datetime="2026-11-15">', s)
            self.assertIn('"dateModified": "2026-11-15"', s)
            hub = self.src[HUB if a["lang"] == "ru" else HUB_EN]
            self.assertIn('href="%s"' % URLS[a["slug"]], hub)

    def test_ap_facts_verified(self):
        for n in (401, 501):
            t = visible_text(self.u(n))
            for must in ("42", "85", "95"):
                self.assertIn(must, t)
            for bad in (r"\b(?:AP )?Physics 1 (?:requires|prerequisite)", r"college credit", r"кредит", r"проходной"):
                self.assertIsNone(re.search(bad, t, re.I), (n, bad))
        for n in (401, 501):
            self.assertIn("apcentral.collegeboard.org/courses/ap-physics-1", self.u(n))
            self.assertIn("apcentral.collegeboard.org/courses/ap-physics-2", self.u(n))

    def test_ib_facts_match_guide(self):
        for n in (402, 502):
            s = self.u(n)
            t = visible_text(s)
            for must in ("240", "150", "4 ч 30 мин" if n == 402 else "4 h 30 min", "38", "19", "24"):
                self.assertIn(must, t, (n, must))
            self.assertNotRegex(t, r"(?i)границ\w* оценок|grade boundar|band")

    def test_no_unsourced_claims_and_table_cells(self):
        for a in self.PH:
            t = visible_text(self.src[URLS[a["slug"]]])
            self.assertNotRegex(t, r"(?i)чаще рассматрива|usual consideration")
            if "Bluebook" in t:   # гибридный формат подтверждён только для Physics 1 и 2
                self.assertRegex(t, r"Physics 1 (и|and) 2 (экзамен|exams)")
        ib = {r[0]: r[1:] for r in AP._IB_PHYS_TABLE_RU["rows"]}
        self.assertEqual(ib["D. Fields"], ["19 ч", "38 ч"])
        self.assertEqual(ib["A. Space, time and motion"], ["27 ч", "42 ч"])
        self.assertEqual(ib["Часы всего (из них контент)"], ["150 (110)", "240 (180)"])
        ap = {r[0]: r[1:] for r in AP._AP_PHYS_TABLE_RU["rows"]}
        self.assertEqual(ap["Калькулятор"], ["разрешён"] * 4)
        self.assertTrue(all("42 вопроса" in c and "85 мин" in c for c in ap["Раздел I"]))
        self.assertTrue(all("4 вопроса" in c and "95 мин" in c for c in ap["Раздел II"]))


class TestEgeMathPlanPage(Base):
    """Страница «Подготовка к ЕГЭ по математике (профиль) 2027: план по месяцам, ошибки, онлайн» (18.11):
    данные exam-topics + спецификация ФИПИ 2027, FAQPage, UTM-блок «следующий шаг», llms.txt, разметка."""
    SLUG = "podgotovka-ege-matematika-profil-2027-plan"

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.s = cls.src[URLS[cls.SLUG]]
        cls.entry = next(a for a in AP.ANSWERS_PHYS if a["slug"] == cls.SLUG)

    def test_faqpage_jsonld_matches_visible_faq(self):
        faq = next(b for b in jsonld_blocks(self.s) if b.get("@type") == "FAQPage")
        self.assertEqual(len(faq["mainEntity"]), len(self.entry["faq"]))
        self.assertGreaterEqual(len(faq["mainEntity"]), 5)
        for q, (qq, aa) in zip(faq["mainEntity"], self.entry["faq"]):
            self.assertEqual((q["@type"], q["name"], q["acceptedAnswer"]["@type"], q["acceptedAnswer"]["text"]),
                             ("Question", qq, "Answer", aa))
            self.assertIn(qq, self.s)

    def test_jsonld_types_and_webpage_fields(self):
        blocks = jsonld_blocks(self.s)
        self.assertTrue({"FAQPage", "WebPage", "Course"} <= {b.get("@type") for b in blocks})
        wp = next(b for b in blocks if b.get("@type") == "WebPage")
        self.assertEqual(wp["url"], BASE + "/answers/%s/" % self.SLUG)
        self.assertEqual((wp["inLanguage"], wp["dateModified"]), ("ru", "2026-11-18"))
        self.assertIn("<h1", self.s)
        self.assertEqual(len(re.findall(r"<h1[ >]", self.s)), 1)

    def test_next_step_utm_block_and_tutor_link(self):
        slug = AP.razbor_slug(self.entry)
        self.assertEqual(slug, "tutor-answers-" + self.SLUG)
        self.assertIn('data-slug="%s"' % slug, self.s)                 # из_ИИ_на_репетитора / показ-клик в funnel-metrics
        for part in ("utm_source=tutor.podlevskikh.com", "utm_medium=razbor", "utm_campaign=%s" % slug):
            self.assertIn(part, self.s)
        # клики_к_репетитору: ссылка на /exam-prep-online/ (site.js считает как tutor-page)
        self.assertIn('href="/exam-prep-online/"', self.s)
        self.assertIn('href="/ege-physics/"', self.s)

    def test_in_hub_sitemap_llms(self):
        self.assertIn("/answers/%s/" % self.SLUG, self.src[HUB])
        sm = open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8").read()
        self.assertIn("%s/answers/%s/" % (BASE, self.SLUG), sm)
        llms = open(os.path.join(ROOT, "llms.txt"), encoding="utf-8").read()
        self.assertIn("%s/answers/%s/" % (BASE, self.SLUG), llms)

    def test_facts_from_fipi_spec_2027(self):
        text = visible_text(self.s)
        for must in ("19 заданий", "32 первичных балла", "12 заданий", "7 заданий", "62,5%", "235 минут", "3 ч 55 мин",
                     "13, 15 и 16 — по 2", "14 и 17 — по 3", "18 и 19 — по 4", "7 заданий и 7 баллов",
                     "10 заданий и 17 баллов", "2 задания (18 и 19) и 8 баллов"):
            self.assertIn(must, text)
        # баллы сходятся: 12*1 + 3*2 + 2*3 + 2*4 = 32, уровни 7+10+2 = 19, 7+17+8 = 32
        self.assertEqual(12 + 3 * 2 + 2 * 3 + 2 * 4, 32)
        self.assertEqual((7 + 10 + 2, 7 + 17 + 8), (19, 32))
        for bad in (r"(июн|июл)\w*[^.]{0,20}2027", r"2027[^.]{0,20}(июн|июл)", r"\d{1,2}[./]\d{1,2}[./]2027",
                    r"100 баллов", r"100-балл", r"тестов(ых|ый) балл", r"\d{1,2}\s+(мая|июня|июля)\s+2027",
                    r"калькулятор"):
            self.assertNotRegex(text, bad)

    def test_sections_cover_exam_topics(self):
        path = os.path.expanduser("~/exam-topics/site/data/ege-math.json")
        if not os.path.exists(path):
            self.skipTest("exam-topics недоступен")
        import json
        data = json.load(open(path, encoding="utf-8"))
        cells = " ".join(r[2] for r in AP._EGE_MATH_TABLE_RU["rows"]).lower().replace("ё", "е")
        key = {"calc-num": "числа и вычисления", "equineq": "уравнения и неравенства", "functions": "функции и анализ",
               "planimetry": "планиметрия", "stereometry": "стереометрия", "vectors": "координаты и векторы",
               "probstat": "вероятность и статистика", "applied": "прикладные и текстовые задачи",
               "numtheory": "числа и их свойства"}
        ids = {t["id"] for t in data["topics"]}
        self.assertEqual(ids, set(key), "новый раздел в exam-topics — добавьте в план")
        for k, phrase in key.items():
            self.assertIn(phrase, cells, k)
        months = [r[0] for r in AP._EGE_MATH_TABLE_RU["rows"]]
        self.assertEqual(months, ["Ноябрь", "Декабрь", "Январь", "Февраль", "Март", "Апрель", "Май"])
        for n in range(13, 20):                      # задания части 2 привязаны к месяцам
            self.assertRegex(cells, r"задани[ея] %d\b" % n)

    def test_mistakes_and_online_sections(self):
        text = visible_text(self.s)
        for must in ("Типичные ошибки", "Как заниматься онлайн", "наблюдения из практики преподавания, а не статистика",
                     "балл не обещаю"):
            self.assertIn(must, text)


class TestChooseTutorPages(Base):
    """Две страницы-чеклиста «как выбрать репетитора» (15.11, провальные запросы замера #9 AP Physics 1, #10 IB Physics HL)."""
    SLUGS = ("how-to-choose-ap-physics-1-tutor", "how-to-choose-ib-physics-hl-tutor")

    def entries(self):
        return [next(a for a in AP.ANSWERS_PHYS if a["slug"] == s) for s in self.SLUGS]

    def test_registered_sitemap_llms_hub(self):
        sm = open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8").read()
        llms = open(os.path.join(ROOT, "llms.txt"), encoding="utf-8").read()
        for slug in self.SLUGS:
            u = "/answers/%s/" % slug
            self.assertIn("<loc>%s%s</loc>" % (BASE, u), sm)
            self.assertIn(BASE + u, llms)
            self.assertIn('href="%s"' % u, self.src[HUB_EN])
            self.assertNotIn('href="%s"' % u, self.src[HUB])

    def test_faqpage_jsonld_at_least_3(self):
        for a in self.entries():
            s = self.src[URLS[a["slug"]]]
            faq = [b for b in jsonld_blocks(s) if b.get("@type") == "FAQPage"]
            self.assertEqual(len(faq), 1, a["slug"])
            self.assertGreaterEqual(len(faq[0]["mainEntity"]), 3)
            self.assertEqual([e["name"] for e in faq[0]["mainEntity"]], [q for q, _ in a["faq"]])

    def test_answer_first_lead_up_to_50_words(self):
        for a in self.entries():
            m = re.search(r'<p class="lead[^"]*">(.*?)</p>', self.src[URLS[a["slug"]]], re.S)
            self.assertLessEqual(len(visible_text(m.group(1)).split()), 50, a["slug"])

    def test_five_criteria_in_list_and_table(self):
        for a in self.entries():
            s = self.src[URLS[a["slug"]]]
            ol = re.search(r"<ol>(.*?)</ol>", s, re.S).group(1)
            self.assertGreaterEqual(len(re.findall(r"<li>", ol)), 5, a["slug"])
            self.assertEqual(a["table"]["head"], ["Criterion", "What to check", "Red flag"])
            self.assertGreaterEqual(len(a["table"]["rows"]), 5)
            self.assertTrue(all(len(r) == 3 and all(r) for r in a["table"]["rows"]))
            self.assertIn('<table class="spec-table">', s)

    def test_stop_words_and_razbor_block(self):
        for a in self.entries():
            s = self.src[URLS[a["slug"]]]
            for pat in FORBIDDEN + EXTRA_FORBIDDEN:
                self.assertIsNone(re.search(pat, strip_razbor(s).replace('data-cta="tutor-page"', ""), re.I), (a["slug"], pat))
            b = RAZBOR_RE.search(s).group(0)
            self.assertIn("utm_campaign=tutor-answers-" + a["slug"], b)
            self.assertIn('data-cta="tutor-page" href="/exam-prep-online/"', s)

    def test_facts_from_verified_sheet_only(self):
        ap = visible_text(self.src[URLS[self.SLUGS[0]]])
        for must in ("42", "85", "95", "8 units", "algebra-based"):
            self.assertIn(must, ap)
        ib = visible_text(self.src[URLS[self.SLUGS[1]]])
        for must in ("240", "150", "60 marks", "90 marks", "4 h 30 min", "24 marks"):
            self.assertIn(must, ib)
        for t in (ap, ib):
            self.assertNotRegex(t, r"(?i)college credit|grade boundar|\bband|score of [1-7]")


class TestALevelIbPage(Base):
    """Страница «Подготовка к A-level и IB по физике онлайн» (автопилот 18.11): данные exam-topics, FAQPage, блок «следующий шаг» с UTM,
    запись в llms.txt, метрики (data-cta и razbor-slug), валидность разметки."""
    SLUG = "podgotovka-a-level-ib-fizika-onlajn"
    DATA = os.path.expanduser("~/exam-topics/site/data/")

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.s = cls.src[URLS[cls.SLUG]]
        cls.entry = next(a for a in AP.ANSWERS_PHYS if a["slug"] == cls.SLUG)

    def _json(self, name):
        import json
        path = self.DATA + name
        if not os.path.exists(path):
            self.skipTest("exam-topics недоступен")
        return json.load(open(path, encoding="utf-8"))

    def test_faqpage_jsonld_valid_and_matches_visible_faq(self):
        blocks = jsonld_blocks(self.s)   # json.loads внутри: невалидный JSON-LD уронит тест
        faq = [b for b in blocks if b.get("@type") == "FAQPage"]
        self.assertEqual(len(faq), 1)
        self.assertEqual(faq[0]["@context"], "https://schema.org")
        self.assertEqual(len(faq[0]["mainEntity"]), len(self.entry["faq"]))
        self.assertGreaterEqual(len(faq[0]["mainEntity"]), 5)
        for q, (qq, aa) in zip(faq[0]["mainEntity"], self.entry["faq"]):
            self.assertEqual(q["@type"], "Question")
            self.assertEqual(q["name"], qq)
            self.assertEqual(q["acceptedAnswer"]["@type"], "Answer")
            self.assertEqual(q["acceptedAnswer"]["text"], aa)
            self.assertIn(htmllib.escape(qq, quote=False), self.s.replace("&#x27;", "'"))   # вопрос виден на странице
        types = [b.get("@type") for b in blocks]
        for t in ("Course", "WebPage"):
            self.assertIn(t, types)
        wp = next(b for b in blocks if b.get("@type") == "WebPage")
        self.assertEqual(wp["url"], BASE + URLS[self.SLUG])
        self.assertEqual(wp["inLanguage"], "ru")
        self.assertEqual(wp["dateModified"], "2026-11-18")

    def test_a_level_plan_covers_every_exam_topics_topic_once(self):
        d = self._json("alevel-physics.json")
        for t in d["topics"]:
            name = t["name"]["en"]
            # «Mechanics» входит в «Further Mechanics»: считаем вхождения как самостоятельной темы через разделитель «; »/начало ячейки
            parts = [p.strip() for cell in (r[1] for r in AP._ALEVEL_IB_PLAN_TABLE_RU["rows"]) for p in cell.split(";")]
            hits = [p for p in parts if p == name or p.startswith(name + " (")]
            self.assertEqual(len(hits), 1, "тема A-level %r встречается в плане %d раз" % (name, len(hits)))
        self.assertEqual(len(d["topics"]), 13)

    def test_ib_plan_covers_every_subtopic_once(self):
        d = self._json("ib-physics.json")
        col = " ; ".join(r[2] for r in AP._ALEVEL_IB_PLAN_TABLE_RU["rows"])
        for th in d["topics"]:
            for c in th["children"]:
                name = c["name"]["en"]          # «A.1 Kinematics» или «A.4 Rigid body mechanics (HL)»
                code = name.split(" ", 1)[0]
                self.assertEqual(len(re.findall(r"(?<![\w.])" + re.escape(code) + r"(?![\w])", col)), 1, "IB %s: не ровно один раз в плане" % code)
                self.assertIn(name, col, name)
        self.assertEqual(len(d["topics"]), 5)

    def test_format_numbers_match_exam_topics(self):
        al, hl, sl = (self._json(n) for n in ("alevel-physics.json", "ib-physics.json", "ib-physics-sl.json"))
        self.assertEqual([t["maxPrimary"] for t in al["tasks"]], [90, 90, 120])
        self.assertEqual(al["maxPrimary"], 300)
        self.assertEqual(sl["tasks"][0]["maxPrimary"], 25)
        self.assertEqual(hl["tasks"][0]["maxPrimary"], 40)
        self.assertEqual(sl["tasks"][3]["maxPrimary"], 24)
        text = visible_text(self.s)
        for must in ("Paper 1 (90 баллов)", "Paper 2 (90)", "Paper 3 (120)", "300 баллов", "25 вопросов (1A)", "40 вопросов (1A)",
                     "240 часов", "150 часов", "24 балла", "13 тем", "9PH0", "Physics data booklet"):
            self.assertIn(must, text)

    def test_plan_table_rendered_on_page(self):
        """Таблица плана реально выведена в HTML страницы (а не только лежит в словаре)."""
        self.assertIn('<table class="spec-table">', self.s)
        self.assertIn(AP._ALEVEL_IB_PLAN_TABLE_RU["title"], self.s)
        self.assertEqual(self.s.count('<table class="spec-table">'), 2)    # план + формат экзамена
        for r in AP._ALEVEL_IB_PLAN_TABLE_RU["rows"]:
            self.assertIn("<td>%s</td>" % r[0], self.s)
        self.assertIn("черновик internal assessment", self.s)               # IA-черновик не в последнем месяце

    def test_months_are_in_order_and_abstract(self):
        self.assertEqual([r[0] for r in AP._ALEVEL_IB_PLAN_TABLE_RU["rows"]], ["Месяц %d" % i for i in range(1, 9)])
        self.assertTrue(all(len(r) == 3 and all(r) for r in AP._ALEVEL_IB_PLAN_TABLE_RU["rows"]))
        main = self.s[self.s.index('<main id="main">'):self.s.index("</main>")]   # без футера («Обновлено: ноябрь 2026»)
        text = visible_text(main).replace("Обновлено: 18 ноября 2026", "")
        for bad in (r"(май|мая|июн\w*|июл\w*|нояб\w*)\s+20\d\d", r"\d{1,2}[./]\d{1,2}[./]20\d\d", r"\bA\*\s*=\s*\d+", r"границ\w+ оценок\s*:"):
            self.assertNotRegex(text, bad)

    def test_next_step_block_utm_and_metrics_hooks(self):
        slug = AP.razbor_slug(self.entry)
        self.assertEqual(slug, "tutor-answers-" + self.SLUG)
        b = RAZBOR_RE.search(self.s).group(0)
        for part in ("utm_source=tutor.podlevskikh.com", "utm_medium=razbor", "utm_campaign=" + slug, 'data-slug="%s"' % slug):
            self.assertIn(part, b)
        self.assertEqual(len(RAZBOR_RE.findall(self.s)), 1)
        self.assertIn('data-cta="tutor-page" href="/exam-prep-online/"', self.s)     # tutor-страница: событие cta-tutor-page
        self.assertIn('href="/answers/ib-physics-hl-ili-sl-chto-vybrat/"', self.s)   # перелинковка на соседний ответ
        self.assertIn('/assets/start-block.js', self.s)

    def test_stop_words_and_location_online(self):
        s = strip_razbor(self.s).replace('data-cta="tutor-page"', "")
        for pat in FORBIDDEN + EXTRA_FORBIDDEN:
            self.assertIsNone(re.search(pat, s, re.I), pat)
        self.assertRegex(visible_text(self.s), r"онлайн")
        self.assertNotRegex(visible_text(self.s), r"(?i)lond|лондон|москв|ереван")   # место не называем: только онлайн

    def test_in_hub_sitemap_llms(self):
        u = "/answers/%s/" % self.SLUG
        self.assertIn(u, self.src[HUB])
        self.assertIn(BASE + u, open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8").read())
        llms = open(os.path.join(ROOT, "llms.txt"), encoding="utf-8").read()
        line = next(l for l in llms.splitlines() if BASE + u in l)
        self.assertIn("A-level", line)
        self.assertIn("IB", line)
        self.assertIn("## Short answers to common queries", llms.split(line)[0])


class TestReprobe1118(Base):
    """Правки по замеру ИИ 18.11 (набор newpages): title с фразой запроса, FAQ под запросы, FAQPage = видимый FAQ, без стоп-слов."""
    CASES = {
        "podgotovka-a-level-ib-fizika-onlajn": ("Подготовка к A-level и IB по физике онлайн", ["по месяцам", "русскоязычный репетитор по A-level"]),
        "podgotovka-ege-matematika-profil-2027-plan": ("Подготовка к ЕГЭ по математике профиль 2027", ["по месяцам", "Как выбрать репетитора"]),
    }

    def test_title_starts_with_query_phrase_and_faq_added(self):
        import re
        for slug, (phrase, faq_marks) in self.CASES.items():
            s = self.src[URLS[slug]]
            title = re.search(r"<title>(.*?)</title>", s).group(1)
            self.assertTrue(title.startswith(phrase), title)
            qs = [q for q, _ in next(a for a in AP.ANSWERS_PHYS if a["slug"] == slug)["faq"]]
            for m in faq_marks:
                self.assertTrue(any(m.lower() in q.lower() for q in qs), (slug, m))

    def test_jsonld_faqpage_matches_visible_and_short_answers(self):
        import json, re
        for slug in self.CASES:
            s = self.src[URLS[slug]]
            blocks = [json.loads(b) for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)]
            faq = next(b for b in blocks if b.get("@type") == "FAQPage")
            entry = next(a for a in AP.ANSWERS_PHYS if a["slug"] == slug)
            self.assertEqual(len(faq["mainEntity"]), len(entry["faq"]))
            for item, (q, a) in zip(faq["mainEntity"], entry["faq"]):
                self.assertEqual(item["name"], q)
                self.assertLessEqual(len(item["acceptedAnswer"]["text"].split()), 60, q)
            for pat in EXTRA_FORBIDDEN:
                self.assertIsNone(re.search(pat, s, re.I), (slug, pat))


class TestIgcsePage(Base):
    """Страница «Подготовка к IGCSE по физике и математике онлайн» (автопилот 19.11): данные exam-topics и ФАКТЫ-ЭКЗАМЕНЫ,
    FAQPage + Course, блок «следующий шаг» с UTM (из_ИИ_на_репетитора, клики_к_репетитору), llms.txt, sitemap, хаб, стоп-слова."""
    SLUG = "podgotovka-igcse-fizika-matematika-onlajn"
    DATA = os.path.expanduser("~/exam-topics/site/data/")

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.s = cls.src[URLS[cls.SLUG]]
        cls.entry = next(a for a in AP.ANSWERS_PHYS if a["slug"] == cls.SLUG)

    def _json(self, name):
        import json
        path = self.DATA + name
        if not os.path.exists(path):
            self.skipTest("exam-topics недоступен")
        return json.load(open(path, encoding="utf-8"))

    def test_faqpage_course_webpage_valid(self):
        blocks = jsonld_blocks(self.s)
        faq = [b for b in blocks if b.get("@type") == "FAQPage"]
        self.assertEqual(len(faq), 1)
        self.assertEqual(len(faq[0]["mainEntity"]), len(self.entry["faq"]))
        self.assertGreaterEqual(len(faq[0]["mainEntity"]), 5)
        for q, (qq, aa) in zip(faq[0]["mainEntity"], self.entry["faq"]):
            self.assertEqual((q["@type"], q["name"], q["acceptedAnswer"]["@type"], q["acceptedAnswer"]["text"]), ("Question", qq, "Answer", aa))
            self.assertIn(htmllib.escape(qq, quote=False), self.s.replace("&#x27;", "'"))
        self.assertTrue({"Course", "WebPage"} <= {b.get("@type") for b in blocks})
        wp = next(b for b in blocks if b.get("@type") == "WebPage")
        self.assertEqual((wp["url"], wp["inLanguage"], wp["dateModified"]), (BASE + URLS[self.SLUG], "ru", "2026-11-19"))
        self.assertEqual(len(re.findall(r"<h1[ >]", self.s)), 1)

    def test_plan_covers_every_topic_once(self):
        rows = AP._IGCSE_PLAN_TABLE_RU["rows"]
        self.assertEqual([r[0] for r in rows], ["Месяц %d" % i for i in range(1, 7)])
        phys = [p.strip() for r in rows for p in r[1].split(";") if r[1] != "Повторение всех тем"]
        math = [p.strip() for r in rows for p in r[2].split(";") if r[2] != "Повторение всех тем"]
        dp, dm = self._json("igcse-physics.json"), self._json("igcse-math.json")
        self.assertEqual(sorted(phys), sorted(t["name"]["en"] for t in dp["topics"]))
        self.assertEqual(sorted(math), sorted(t["name"]["en"] for t in dm["topics"]))
        self.assertEqual((len(dp["topics"]), len(dm["topics"])), (6, 9))

    def test_format_numbers_match_facts(self):
        text = visible_text(self.s)
        for must in ("0625", "0580", "Paper 1", "Paper 4", "Paper 5", "Paper 6", "20% оценки", "30%", "50%", "A*–G", "A*–E",
                     "130", "6 тем", "9 тем", "без калькулятора", "4PH1", "4MA1", "Edexcel", "Cambridge", "онлайн"):
            self.assertIn(must, text)
        dm = self._json("igcse-math.json")
        self.assertEqual([t["maxPrimary"] for t in dm["tasks"]], [70, 130])

    def test_no_dates_or_grade_scales(self):
        main = self.s[self.s.index('<main id="main">'):self.s.index("</main>")]
        text = visible_text(main).replace("Обновлено: 19 ноября 2026", "")
        for bad in (r"(май|мая|июн\w*|июл\w*|нояб\w*)\s+20\d\d", r"\d{1,2}[./]\d{1,2}[./]20\d\d", r"границ\w+ оценок\s*:", r"проходн"):
            self.assertNotRegex(text, bad)

    def test_next_step_block_utm_and_metrics_hooks(self):
        slug = AP.razbor_slug(self.entry)
        self.assertEqual(slug, "tutor-answers-" + self.SLUG)
        b = RAZBOR_RE.search(self.s).group(0)
        for part in ("utm_source=tutor.podlevskikh.com", "utm_medium=razbor", "utm_campaign=" + slug, 'data-slug="%s"' % slug):
            self.assertIn(part, b)
        self.assertEqual(len(RAZBOR_RE.findall(self.s)), 1)
        self.assertIn('data-cta="tutor-page" href="/exam-prep-online/"', self.s)
        self.assertIn('/assets/start-block.js', self.s)
        self.assertIn('href="/answers/repetitor-igcse-fizika-0625-na-russkom/"', self.s)

    def test_stop_words_and_location_online(self):
        s = strip_razbor(self.s).replace('data-cta="tutor-page"', "")
        for pat in FORBIDDEN + EXTRA_FORBIDDEN:
            self.assertIsNone(re.search(pat, s, re.I), pat)
        self.assertNotRegex(visible_text(self.s), r"(?i)lond|лондон|москв|ереван")

    def test_in_hub_sitemap_llms(self):
        u = "/answers/%s/" % self.SLUG
        self.assertIn(u, self.src[HUB])
        self.assertIn(BASE + u, open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8").read())
        llms = open(os.path.join(ROOT, "llms.txt"), encoding="utf-8").read()
        line = next(l for l in llms.splitlines() if BASE + u in l)
        self.assertIn("IGCSE", line)
        self.assertIn("## Short answers to common queries", llms.split(line)[0])


if __name__ == "__main__":
    unittest.main()
