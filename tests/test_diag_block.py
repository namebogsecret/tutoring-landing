# -*- coding: utf-8 -*-
"""Блок «Диагностика за 10 минут» на страницах-ответах (diag_sets.py, answer_pages._diag_block, assets/diag.js).
Запуск:  python3 build.py && python3 -m pytest -q tests/test_diag_block.py
Клик-сценарий в Chromium (playwright) выполняется, только если playwright установлен (~/.venv/playwright/bin/python -m pytest).
"""
import functools
import http.server
import os
import re
import socketserver
import sys
import threading
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import answer_pages as AP          # noqa: E402
import diag_sets as DS             # noqa: E402

ALL = AP.ANSWERS + AP.ANSWERS_EN + AP.ANSWERS_MATH + AP.ANSWERS_PHYS
CYR = re.compile(r"[А-Яа-яЁё]")
BLOCK_RE = re.compile(r'<div class="diag-block" id="diag-block".*?</ol>', re.S)
FULL_RE = re.compile(r'<div class="diag-block" id="diag-block".*?<script src="/assets/diag\.js" defer></script>', re.S)


def page(slug):
    with open(os.path.join(ROOT, "answers", slug, "index.html"), encoding="utf-8") as f:
        return f.read()


def expected_key(a):
    """Независимое от DIAG_SET_BY_SLUG ожидание: предмет/экзамен из slug и заголовка страницы."""
    s = a["slug"]
    for tok, key in (("ap-calculus-ab", "ap-calc-ab"), ("ap-statistics", "ap-statistics"),
                     ("oge-fizika", "oge-physics"), ("gcse-physics", "gcse-physics"),
                     ("a-level-further", "alevel-further"), ("step-maths", "step-maths"),
                     ("ap-precalculus", "ap-precalc"), ("a-level-maths", "alevel-maths")):   # страницы 24.11.2026
        if re.search(r"(^|-)%s" % tok, s):
            return key
    if "olimpiad" in s:
        return "olympiad-physics"
    if "ucas" in s:
        return "alevel-physics"
    if "vladimir-podlevskikh" in s:
        return "physics-general"
    if "a-level" in s:
        return "alevel-physics"
    is_math = any(t in s for t in ("matematik", "-math", "maths", "calculus")) and not any(t in s for t in ("physics", "fizika"))
    if is_math:
        for tok, key in (("ib", "ib-math"), ("ap", "ap-calc"), ("igcse", "igcse-math"), ("ege", "ege-math")):
            if re.search(r"(^|-)%s(-|$)" % tok, s):
                return key
    for tok, key in (("ege", "ege-physics"), ("igcse", "igcse-physics"), ("ib", "ib-physics"), ("ap", "ap-physics")):
        if re.search(r"(^|-)%s(-|$)" % tok, s):
            return key
    return None


class TestDiagBlock(unittest.TestCase):
    def test_every_answer_page_has_one_block(self):
        self.assertEqual(len(ALL), 44)
        for a in ALL:
            s = page(a["slug"])
            self.assertEqual(s.count('id="diag-block"'), 1, a["slug"])
            self.assertEqual(s.count('/assets/diag.js'), 1, a["slug"])
            self.assertIn("<h2>%s</h2>" % ("Диагностика за 10 минут" if a["lang"] == "ru" else "10-minute diagnostic"), s)

    def test_hubs_have_no_block(self):
        for u in ("answers/index.html", "answers/en/index.html"):
            with open(os.path.join(ROOT, u), encoding="utf-8") as f:
                self.assertNotIn("diag-block", f.read(), u)

    def test_exactly_five_questions_four_options_one_correct(self):
        for a in ALL:
            blk = BLOCK_RE.search(page(a["slug"])).group(0)
            qs = re.findall(r'<li class="diag-q" data-correct="(\d)">(.*?)</li>', blk, re.S)
            self.assertEqual(len(qs), 5, a["slug"])
            for i, (corr, body) in enumerate(qs):
                radios = re.findall(r'<input type="radio" name="diag-q%d" value="(\d)">' % i, body)
                self.assertEqual(radios, ["0", "1", "2", "3"], (a["slug"], i))
                self.assertIn(int(corr), range(4))
            self.assertEqual(blk.count('type="radio"'), 20, a["slug"])

    def test_sets_structure_one_correct_distinct_options(self):
        for key, langs in DS.SETS.items():
            for lang, qs in langs.items():
                self.assertEqual(len(qs), DS.N_QUESTIONS, (key, lang))
                self.assertEqual(len({q for q, _, _ in qs}), 5, (key, lang))
                for q, opts, c in qs:
                    self.assertEqual(len(opts), 4, (key, lang, q))
                    self.assertEqual(len(set(opts)), 4, (key, lang, q))
                    self.assertIsInstance(c, int)
                    self.assertTrue(0 <= c < 4, (key, lang, q))

    def test_set_matches_subject_of_page(self):
        for a in ALL:
            key = DS.DIAG_SET_BY_SLUG.get(a["slug"])
            self.assertIsNotNone(key, "страница без набора: " + a["slug"])
            self.assertEqual(key, expected_key(a), a["slug"])
            self.assertIn(a["lang"], DS.SETS[key], a["slug"])
            self.assertEqual(re.search(r'data-diag="([^"]+)"', page(a["slug"])).group(1), key)
        self.assertEqual(set(DS.DIAG_SET_BY_SLUG), {a["slug"] for a in ALL})

    def test_question_language_equals_page_language(self):
        for a in ALL:
            blk = BLOCK_RE.search(page(a["slug"])).group(0)
            text = re.sub(r"<[^>]+>", " ", blk)
            if a["lang"] == "ru":
                self.assertTrue(CYR.search(text), a["slug"])
            else:
                self.assertIsNone(CYR.search(text), (a["slug"], CYR.search(text)))

    def test_rendered_correct_index_matches_source(self):
        for a in ALL:
            key, qs = DS.diag_set(a["slug"], a["lang"])
            got = [int(x) for x in re.findall(r'<li class="diag-q" data-correct="(\d)"', page(a["slug"]))]
            self.assertEqual(got, [c for _, _, c in qs], a["slug"])

    def test_link_utm_and_event_label(self):
        for a in ALL:
            full = FULL_RE.search(page(a["slug"])).group(0)
            links = re.findall(r"<a [^>]*>", full)
            self.assertEqual(len(links), 1, a["slug"])
            self.assertIn('data-tutor-src="diag-%s"' % a["slug"], links[0])
            self.assertIn('href="/exam-prep-online/?utm_source=answers&amp;utm_medium=diag-block&amp;utm_campaign=diag-%s#razbor-zapros"' % a["slug"], links[0])
            self.assertEqual(AP.diag_block_href(a["slug"]).split("?")[0], AP.task_block_href(a["slug"]).split("?")[0])  # та же целевая страница

    def test_task_block_label_untouched(self):
        for a in ALL:
            s = page(a["slug"])
            if AP.has_task_block(a):
                self.assertIn('data-tutor-src="%s"' % a["slug"], s)
                self.assertEqual(s.count('data-tutor-src="%s"' % a["slug"]), 1)
            self.assertEqual(s.count('data-tutor-src="diag-%s"' % a["slug"]), 1)

    def test_no_external_requests_no_forms(self):
        for a in ALL:
            full = FULL_RE.search(page(a["slug"])).group(0)
            self.assertNotIn("<form", full)
            self.assertNotIn("http", full)
            self.assertIsNone(re.search(r'<input[^>]*type="(text|email|tel)"', full))
        js = open(os.path.join(ROOT, "assets", "diag.js"), encoding="utf-8").read()
        for bad in ("fetch(", "XMLHttpRequest", "sendBeacon", "http://", "https://", "localStorage", "cookie", "<script"):
            self.assertNotIn(bad, js)

    def test_degrades_without_js_block_hidden(self):
        for a in ALL:
            self.assertRegex(page(a["slug"]), r'<div class="diag-block" id="diag-block"[^>]* hidden>')
        css = open(os.path.join(ROOT, "assets", "content.css"), encoding="utf-8").read()
        self.assertIn(".diag-block[hidden]", css)

    def test_site_js_sends_diag_event(self):
        js = open(os.path.join(ROOT, "assets", "site.js"), encoding="utf-8").read()
        self.assertIn('name="to-tutor-"+a.getAttribute("data-tutor-src")', js)
        self.assertIn('/^(diag|paste)-/', js)
        self.assertIn('name="to-tutor-answers-"+a.getAttribute("data-tutor-src")', js)   # метка answers-<slug> не тронута
        self.assertLess(js.index('/^(diag|paste)-/'), js.index('name="to-tutor-answers-"'))
        self.assertLess(js.index('name="to-tutor-answers-"'), js.index('name="tutor-page"'))

    def test_ap_sets_stay_in_course_scope(self):
        """Ревью: AP Physics 1 без термодинамики/конденсаторов; AP Calculus AB без рядов (BC)."""
        out_of_scope = re.compile(r"изотерм|конденсатор|isotherm|capacitor|радиус сходимости|radius of convergence|ряд", re.I)
        for key in ("ap-physics", "ap-calc"):
            for lang in ("ru", "en"):
                for q, opts, _ in DS.SETS[key][lang]:
                    self.assertIsNone(out_of_scope.search(q + " " + " ".join(opts)), (key, lang, q))

    def test_result_shown_by_button_live_region_visible(self):
        """Результат по кнопке (disabled до 5 ответов); aria-live на изначально видимом контейнере."""
        for lang, label in (("ru", "Показать результат"), ("en", "Show result")):
            a = next(x for x in ALL if x["lang"] == lang and DS.diag_set(x["slug"], lang))
            full = FULL_RE.search(page(a["slug"])).group(0)
            self.assertRegex(full, r'<button type="button" class="btn btn-primary diag-show" disabled>%s</button>' % label)
            m = re.search(r'<div class="diag-result"([^>]*)>', full)
            self.assertIn('aria-live="polite"', m.group(1))
            self.assertNotIn("hidden", m.group(1))

    def test_results_texts_three_levels(self):
        for lang in ("ru", "en"):
            self.assertEqual(len(AP._DIAG_TEXT[lang]["levels"]), 3)


try:
    from playwright.sync_api import sync_playwright
except Exception:           # pragma: no cover
    sync_playwright = None


@unittest.skipIf(sync_playwright is None, "playwright не установлен")
class TestDiagClickScenario(unittest.TestCase):
    """Chromium: ответить на 5 вопросов → результат → клик по кнопке шлёт cta-to-tutor-diag-<slug>."""

    @classmethod
    def setUpClass(cls):
        handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=ROOT)
        handler.log_message = lambda *a, **k: None
        socketserver.TCPServer.allow_reuse_address = True
        cls.httpd = socketserver.TCPServer(("127.0.0.1", 0), handler)
        cls.port = cls.httpd.server_address[1]
        threading.Thread(target=cls.httpd.serve_forever, daemon=True).start()
        cls.pw = sync_playwright().start()
        cls.browser = cls.pw.chromium.launch()

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.pw.stop()
        cls.httpd.shutdown()

    def _run(self, slug, wrong):
        pg = self.browser.new_page()
        beacons, external = [], []
        def on_req(r):
            if "stats.podlevskikh.com/count?" in r.url:
                beacons.append(r.url)
            if not r.url.startswith("http://127.0.0.1"):
                external.append(r.url)
        pg.on("request", on_req)
        pg.route("**/stats.podlevskikh.com/**", lambda route: route.fulfill(status=200, body=""))
        pg.goto("http://127.0.0.1:%d/answers/%s/" % (self.port, slug))
        blk = pg.locator("#diag-block")
        pg.wait_for_load_state("networkidle")
        del external[:]                                   # шрифты и аналитика — штатные запросы страницы; считаем только после загрузки
        self.assertTrue(blk.is_visible())
        self.assertFalse(pg.locator(".diag-result").is_visible())
        self.assertTrue(pg.locator(".diag-show").is_disabled())
        qs = pg.locator(".diag-q")
        self.assertEqual(qs.count(), 5)
        for i in range(5):
            corr = int(qs.nth(i).get_attribute("data-correct"))
            pick = (corr + 1) % 4 if i < wrong else corr
            self.assertEqual(pg.locator(".diag-score").inner_text(), "")      # результата нет до кнопки
            qs.nth(i).locator("input").nth(pick).check()
        btn = pg.locator(".diag-show")
        self.assertTrue(btn.is_enabled())
        self.assertEqual(pg.locator(".diag-score").inner_text(), "")      # пятый ответ результат сам не показывает
        btn.click()
        self.assertTrue(pg.locator(".diag-result").is_visible())
        return pg, beacons, external

    def test_perfect_score_and_click_event(self):
        slug = "ib-physics-hl-tutor-online"
        pg, beacons, external = self._run(slug, wrong=0)
        self.assertIn("Correct: 5 out of 5", pg.locator(".diag-score").inner_text())
        self.assertEqual(pg.locator(".diag-level:visible").count(), 1)
        pg.evaluate("document.addEventListener('click',e=>{if(e.target.closest('a'))e.preventDefault()},false)")
        pg.locator('a[data-tutor-src="diag-%s"]' % slug).click()
        self.assertTrue(any("cta-to-tutor-diag-" + slug in b for b in beacons), beacons)
        self.assertFalse(any("cta-to-tutor-answers-" in b for b in beacons), beacons)
        self.assertEqual([u for u in external if "stats.podlevskikh.com" not in u], [])
        pg.close()

    def test_russian_page_low_score(self):
        pg, _, _ = self._run("repetitor-fizika-ege-online", wrong=5)
        self.assertIn("Верно: 0 из 5", pg.locator(".diag-score").inner_text())
        self.assertEqual(pg.locator(".diag-bad").count(), 5)
        self.assertIn("Основы пока нетвёрдые", pg.locator(".diag-level:visible").inner_text())
        pg.close()

    def test_middle_score(self):
        pg, _, _ = self._run("repetitor-ap-calculus-na-russkom", wrong=2)
        self.assertIn("Верно: 3 из 5", pg.locator(".diag-score").inner_text())
        self.assertIn("Основа есть", pg.locator(".diag-level:visible").inner_text())
        pg.close()

    def test_change_answer_before_show_is_counted(self):
        """Ответы можно менять до кнопки: последний выбор учитывается, кнопка активна только при всех 5 ответах."""
        pg = self.browser.new_page()
        pg.goto("http://127.0.0.1:%d/answers/repetitor-ap-calculus-na-russkom/" % self.port)
        qs = pg.locator(".diag-q")
        btn = pg.locator(".diag-show")
        for i in range(4):
            qs.nth(i).locator("input").nth(int(qs.nth(i).get_attribute("data-correct"))).check()
        self.assertTrue(btn.is_disabled())
        corr = int(qs.nth(4).get_attribute("data-correct"))
        qs.nth(4).locator("input").nth((corr + 1) % 4).check()      # промах (случайный выбор)
        self.assertTrue(btn.is_enabled())
        self.assertEqual(pg.locator(".diag-score").inner_text(), "")
        self.assertTrue(qs.nth(4).locator("input").first.is_enabled())   # ничего не заблокировано
        qs.nth(4).locator("input").nth(corr).check()                # исправил
        qs.nth(0).locator("input").nth((int(qs.nth(0).get_attribute("data-correct")) + 1) % 4).check()  # и испортил первый
        btn.click()
        self.assertIn("Верно: 4 из 5", pg.locator(".diag-score").inner_text())
        self.assertTrue(qs.nth(0).locator("input").first.is_disabled())  # после показа инпуты заблокированы
        self.assertEqual(pg.locator(".diag-bad").count(), 1)
        pg.close()

    def test_without_js_block_hidden(self):
        ctx = self.browser.new_context(java_script_enabled=False)
        pg = ctx.new_page()
        pg.goto("http://127.0.0.1:%d/answers/repetitor-fizika-ege-online/" % self.port)
        self.assertFalse(pg.locator("#diag-block").is_visible())
        ctx.close()


if __name__ == "__main__":
    unittest.main()
