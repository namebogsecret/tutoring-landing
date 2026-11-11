# -*- coding: utf-8 -*-
"""Contract tests for the two pillar pages (/ege-physics/, /igcse-physics-0625/).
Run AFTER building:  python3 build.py --only /ege-physics/ /igcse-physics-0625/
                     python3 -m unittest discover -s tests -v
"""
import html as htmllib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://tutor.podlevskikh.com"
PAGES = {"/ege-physics/": "ru", "/igcse-physics-0625/": "en"}
LASTMOD = "2026-11-08"

# Запретные слова/паттерны (регистронезависимо, кроме помеченных (?-i:)).
FORBIDDEN = [
    r"Nyberg", r"(?-i:\bI Can\b)", r"школ\w*[- ]работодател", r"в школе, где преподаю",
    r"Кипр", r"Cyprus", r"Лимасол", r"Limassol",
    r"Ереван", r"Yerevan", r"Armenia", r"Армени",
    r"\+7", r"(?-i:\bВК\b)", r"(?-i:\bVK\b)", r"Payoneer", r"оплат",
    r"\$", r"\bUSD\b", r"\bStandard\b", r"\bIntensive\b",
    r"4\.88", r"\b127\b", r"\b214\b", r"\+30", r"95%", r"20\+", r"100% результат",
    r"Записаться", r"\bBook\b", r"Free diagnostic", r"Бесплатная диагностика",
    r"#book", r"data-cta=", r"Calendly", r"mailto:", r"tel:",
    r"Лимассол", r"ВКонтакте", r"vk\.com", r"\bVK\b",
    r"отзыв", r"\breviews\b", r"\bratings?\b", r"aggregateRating",
    r"#results", r"#pricing", r"\b23\+",
]


# Маркетплейсы репетиторов: в видимом тексте и ссылках запрещены. В машинном Person.sameAs
# (JSON-LD, общий граф сущности сети из pages_registry.PERSON_SAMEAS) они пока есть — это
# отдельное решение, поэтому JSON-LD из этой проверки вырезается.
FORBIDDEN_VISIBLE = [r"preply", r"profi\.ru"]


def read(url):
    path = os.path.join(ROOT, url.strip("/"), "index.html")
    with open(path, encoding="utf-8") as f:
        return f.read()


def visible_text(src):
    src = re.sub(r"(?is)<(script|style|noscript)\b.*?</\1>", " ", src)
    src = re.sub(r"(?s)<!--.*?-->", " ", src)
    return re.sub(r"\s+", " ", htmllib.unescape(re.sub(r"<[^>]+>", " ", src))).strip()


def jsonld_blocks(src):
    out = []
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', src, re.S):
        out.append(json.loads(m.group(1)))
    return out


def sitemap():
    with open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8") as f:
        return f.read()


class Base(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.src = {u: read(u) for u in PAGES}
        cls.text = {u: visible_text(s) for u, s in cls.src.items()}


class TestForbidden(Base):
    def test_no_forbidden_patterns(self):
        for u, s in self.src.items():
            s = s.replace('data-cta="tutor-page"', "")  # событие ссылки на страницу репетитора, не CTA записи
            for pat in FORBIDDEN:
                m = re.search(pat, s, re.I)
                self.assertIsNone(m, "%s: forbidden %r found near %r" % (
                    u, pat, s[max(0, m.start() - 40):m.end() + 40] if m else ""))


    def test_no_marketplaces_outside_jsonld(self):
        for u, s in self.src.items():
            vis = re.sub(r'(?s)<script type="application/ld\+json">.*?</script>', " ", s)
            for pat in FORBIDDEN_VISIBLE:
                self.assertIsNone(re.search(pat, vis, re.I), "%s: %r" % (u, pat))


class TestMeta(Base):
    def test_single_h1(self):
        for u, s in self.src.items():
            self.assertEqual(len(re.findall(r"<h1\b", s)), 1, u)

    def test_title_desc_canonical(self):
        for u, s in self.src.items():
            title = re.search(r"<title>(.*?)</title>", s, re.S).group(1).strip()
            desc = re.search(r'<meta name="description" content="(.*?)"', s).group(1).strip()
            canon = re.search(r'<link rel="canonical" href="(.*?)"', s).group(1)
            self.assertTrue(title, u)
            self.assertLessEqual(len(title), 65, u)
            self.assertTrue(desc, u)
            self.assertLessEqual(len(desc), 160, u)
            self.assertEqual(canon, BASE + u)
            for prop in ("og:title", "og:description", "og:url"):
                self.assertRegex(s, r'property="%s" content="[^"]+"' % prop)
            self.assertIn('<html lang="%s"' % PAGES[u], s)

    def test_body_length(self):
        for u, s in self.src.items():
            m = re.search(r'<div class="prose reveal">(.*?)</div>\s*<aside', s, re.S)
            self.assertIsNotNone(m, u)
            words = len(visible_text(m.group(1)).split())
            self.assertGreaterEqual(words, 900, "%s: %d words" % (u, words))


class TestJsonLd(Base):
    def test_blocks(self):
        for u, s in self.src.items():
            blocks = jsonld_blocks(s)
            types = [b.get("@type") for b in blocks]
            for t in ("Course", "FAQPage", "BreadcrumbList"):
                self.assertIn(t, types, "%s lacks %s" % (u, t))
            raw = "\n".join(re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S))
            for bad in ("aggregateRating", '"offers"', '"price"', "priceCurrency"):
                self.assertNotIn(bad, raw, u)
            course = blocks[types.index("Course")]
            self.assertEqual(course["provider"]["@type"], "Person")
            self.assertEqual(course["inLanguage"], [PAGES[u]])

    def test_faq_matches_visible(self):
        for u, s in self.src.items():
            faq = [b for b in jsonld_blocks(s) if b.get("@type") == "FAQPage"][0]
            names = [q["name"] for q in faq["mainEntity"]]
            self.assertGreaterEqual(len(names), 5, u)  # контракт: ≥5 (12.11 добавлены ответы под ИИ-запросы)
            vis = re.findall(r'<summary class="faq-q">(.*?)<span class="plus">', s, re.S)
            vis = [re.sub(r"\s+", " ", htmllib.unescape(v)).strip() for v in vis]
            self.assertEqual(vis, names, u)
            answers = re.findall(r'<div class="faq-a">(.*?)</div>', s, re.S)
            self.assertEqual(len(answers), len(names), u)
            for q, a in zip(faq["mainEntity"], answers):
                self.assertEqual(q["acceptedAnswer"]["text"], visible_text(a))


class TestLinks(Base):
    def test_internal_links_exist_and_in_sitemap(self):
        sm = sitemap()
        locs = set(re.findall(r"<loc>(.*?)</loc>", sm))
        for u, s in self.src.items():
            for href in re.findall(r'href="(/[^"]*)"', s):
                if href.startswith("//"):
                    continue
                path = re.split(r"[#?]", href)[0]
                rel = path.strip("/")
                if path.endswith("/") or not os.path.splitext(path)[1]:
                    target = os.path.join(ROOT, rel, "index.html")
                    self.assertIn(BASE + (path if path.endswith("/") else path + "/"), locs,
                                  "%s: %s not in sitemap" % (u, href))
                else:
                    target = os.path.join(ROOT, rel)
                self.assertTrue(os.path.exists(target), "%s: broken link %s" % (u, href))

    def test_cross_links(self):
        needed = {
            "/ege-physics/": ["/igcse-physics-0625/", "/physics-tutor-online/",
                              "/russian-tutor-abroad/", "/olympiad-physics/", "/blog/"],
            "/igcse-physics-0625/": ["/ege-physics/", "/physics-tutor-online/", "/russian-tutor-abroad/",
                                     "/olympiad-physics/", "/blog/", "/ib-physics-tutor/", "/ap-physics-tutor/"],
        }
        for u, hrefs in needed.items():
            for h in hrefs:
                self.assertIn('href="%s' % h, self.src[u], "%s lacks link %s" % (u, h))

    def test_external_links_noopener(self):
        for u, s in self.src.items():
            for tag in re.findall(r'<a [^>]*href="https?://[^"]*"[^>]*>', s):
                if "podlevskikh.com" in tag:
                    continue
                self.assertIn("noopener", tag, "%s: %s" % (u, tag))


class TestAnswerFirst(Base):
    def lead(self, u):
        m = re.search(r'<p class="lead[^"]*">(.*?)</p>', self.src[u], re.S)
        self.assertIsNotNone(m, u)
        return visible_text(m.group(1))

    def test_ege(self):
        lead = self.lead("/ege-physics/")
        self.assertRegex(lead, r"Podlevskikh|Подлевских")
        self.assertIn("ЕГЭ", lead)
        self.assertRegex(lead, r"физик|МГУ")

    def test_igcse(self):
        lead = self.lead("/igcse-physics-0625/")
        self.assertRegex(lead, r"Podlevskikh|Подлевских")
        self.assertIn("0625", lead)


class TestAnswerFirstExtra(Base):
    def lead_p(self, u):
        return visible_text(re.search(r'<p class="lead[^"]*">(.*?)</p>', self.src[u], re.S).group(1))

    def test_lead_has_format_ratio_language(self):
        lead = self.lead_p("/ege-physics/")
        self.assertRegex(lead, r"онлайн|online")
        self.assertRegex(lead, r"1:1|один на один")
        self.assertRegex(lead, r"русск|English|английск|RU/EN")
        lead = self.lead_p("/igcse-physics-0625/")
        self.assertRegex(lead, r"(?i)онлайн|online")
        self.assertRegex(lead, r"1:1|one[- ]to[- ]one")
        self.assertRegex(lead, r"русск|English|английск|Russian|RU/EN")


class TestCaseStudy(Base):
    def test_igcse_has_no_case(self):
        self.assertIsNone(re.search(r"Полина|Polina|\b96\b", self.src["/igcse-physics-0625/"]))

    def test_ege_96_only_in_approved_phrase(self):
        t = self.text["/ege-physics/"]
        phrase = "Полина М. — 96 ЕГЭ и 100 ДВИ, мехмат МГУ"
        self.assertIn(phrase, t)
        stripped = t.replace(phrase, " ")
        self.assertIsNone(re.search(r"\b96\b", stripped), "96 outside approved phrase")
        for m in re.finditer(r"\b96\b", t):
            self.assertNotRegex(t[m.end():m.end() + 40], r"(?i)физик")

    def test_task_counts_whitelist(self):
        t = self.text["/ege-physics/"]
        t = t.replace("20 заданий", " ")  # подтверждённая формулировка
        self.assertIsNone(re.search(r"\b(2[0-5]|27|28|29|30) заданий", t))


class TestChrome(Base):
    def test_footer_years_and_nav(self):
        for u, s in self.src.items():
            foot = re.search(r"<footer.*?</footer>", s, re.S).group(0)
            self.assertRegex(foot, r"23 года|23 years")
            self.assertNotRegex(foot, r"23\+")
            nav = re.search(r'<nav class="nav-links">.*?</nav>', s, re.S).group(0)
            self.assertNotRegex(nav, r"#results|#pricing|#book|Results|Packages")

    def test_footer_date_from_lastmod(self):
        for u, s in self.src.items():
            self.assertIn('<time datetime="%s">' % LASTMOD[:7], s)


class TestToc(Base):
    def test_toc_anchors_have_ids(self):
        for u, s in self.src.items():
            toc = re.search(r'<aside.*?</aside>', s, re.S)
            self.assertIsNotNone(toc, u)
            ids = set(re.findall(r'\bid="([^"]+)"', s))
            hrefs = re.findall(r'href="#([^"]+)"', toc.group(0))
            self.assertTrue(hrefs, u)
            for h in hrefs:
                self.assertIn(h, ids, "%s: TOC href #%s has no id" % (u, h))


class TestFreshness(unittest.TestCase):
    def test_committed_html_matches_build(self):
        tmp = tempfile.mkdtemp()
        try:
            dst = os.path.join(tmp, "tree")
            shutil.copytree(ROOT, dst, ignore=shutil.ignore_patterns(".git", "__pycache__"))
            r = subprocess.run([sys.executable, "build.py", "--only"] + list(PAGES), cwd=dst,
                               capture_output=True, text=True, timeout=120)
            if r.returncode != 0:
                self.skipTest("build failed in tmp copy: %s" % r.stderr[-200:])
            for u in PAGES:
                rel = os.path.join(u.strip("/"), "index.html")
                with open(os.path.join(ROOT, rel), encoding="utf-8") as a, \
                        open(os.path.join(dst, rel), encoding="utf-8") as b:
                    self.assertEqual(a.read(), b.read(), "%s stale: rebuild with --only" % u)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)


class TestFacts(Base):
    def test_ege(self):
        t = self.text["/ege-physics/"]
        for needle in ("26", "45", "2027"):
            self.assertIn(needle, t)
        self.assertTrue("235" in t or "3 часа 55 минут" in t)
        self.assertTrue("21–26" in t or "развёрнут" in t)
        self.assertIn("Полина М. — 96 ЕГЭ и 100 ДВИ, мехмат МГУ", t)
        self.assertIn("fi_11_2027", self.src["/ege-physics/"])

    def test_igcse(self):
        t = self.text["/igcse-physics-0625/"]
        for needle in ("0625", "30%", "50%", "20%", "Core", "Extended",
                       "Paper 1", "Paper 2", "Paper 3", "Paper 4", "Paper 5", "Paper 6",
                       "AO1", "AO2", "AO3", "A* to G", "C to G"):
            self.assertIn(needle, t)
        self.assertIn("697209-2026-2028-syllabus.pdf", self.src["/igcse-physics-0625/"])

    def test_online_location(self):
        self.assertIn("GMT+2/+3", self.text["/ege-physics/"])
        self.assertIn("GMT+2/+3", self.text["/igcse-physics-0625/"])


class TestSitemap(unittest.TestCase):
    def test_entries(self):
        sm = sitemap()
        for u in PAGES:
            m = re.search(r"<loc>%s</loc>\s*<lastmod>(.*?)</lastmod>" % re.escape(BASE + u), sm)
            self.assertIsNotNone(m, u)
            self.assertEqual(m.group(1), LASTMOD)


class TestNoCtaChrome(Base):
    def test_no_cta(self):
        for u, s in self.src.items():
            # единственный допустимый data-cta — событие ссылки на страницу репетитора
            # (блок tutor_block из ai-discovery), а не кнопка записи/связи
            self.assertNotIn("data-cta=", s.replace('data-cta="tutor-page"', ""))
            self.assertNotIn("#book", s)
            self.assertNotIn("nav-cta", s)
            self.assertNotIn("Проекты сети", s)
            self.assertNotIn("calendly", s.lower())


class TestNeighboursUntouched(unittest.TestCase):
    def test_diff(self):
        try:
            out = subprocess.run(["git", "diff", "--name-only", "origin/gh-pages"], cwd=ROOT,
                                 capture_output=True, text=True, timeout=30)
            if out.returncode != 0:
                self.skipTest("git/origin/gh-pages unavailable")
            files = [f for f in out.stdout.split("\n") if f]
            new = subprocess.run(["git", "ls-files", "--others", "--exclude-standard"], cwd=ROOT,
                                 capture_output=True, text=True, timeout=30).stdout.split("\n")
            files += [f for f in new if f]
        except (OSError, subprocess.SubprocessError):
            self.skipTest("git unavailable")
        # Релизная ветка унификации правит сущность на всём сайте: допустимы только
        # страницы из реестра (src/<имя>.html и <url>/index.html) плюс ручные index/hub/404.
        sys.path.insert(0, ROOT)
        from pages_registry import PAGES
        allowed_src = {p["body"] for p in PAGES}
        allowed_idx = {p["url"].strip("/") + "/index.html" for p in PAGES} | {"index.html", "hub/index.html"}
        for f in files:
            if f.startswith("src/") and f.endswith(".html"):
                self.assertIn(f, allowed_src, f)
            if f.endswith("/index.html") or f == "index.html":
                self.assertIn(f, allowed_idx, f)


if __name__ == "__main__":
    unittest.main()
