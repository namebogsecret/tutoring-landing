# -*- coding: utf-8 -*-
"""Блок «Разобрать задачу из ИИ» (#ai-task-paste, assets/ai-task-paste.js) и форма #task-intake на /exam-prep-online/.
Запуск:  python3 build.py && python3 -m pytest -q tests/test_ai_task_paste.py
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

ALL = AP.ANSWERS + AP.ANSWERS_EN + AP.ANSWERS_MATH + AP.ANSWERS_PHYS
BLOCK_RE = re.compile(r'<div class="paste-block" id="ai-task-paste".*?</div>', re.S)
STOP = re.compile(r"школ|schools?\b|Кипр|Cyprus|Лимассол|Limassol|Записаться|Book a|Calendly|без обязательств", re.I)


def read(*parts):
    with open(os.path.join(ROOT, *parts), encoding="utf-8") as f:
        return f.read()


def page(slug):
    return read("answers", slug, "index.html")


class TestPasteBlock(unittest.TestCase):
    def test_every_answer_page_has_one_block(self):
        self.assertEqual(len(ALL), 44)
        for a in ALL:
            s = page(a["slug"])
            self.assertEqual(s.count('id="ai-task-paste"'), 1, a["slug"])
            self.assertEqual(s.count("/assets/ai-task-paste.js"), 1, a["slug"])
            title = "Разобрать задачу из ИИ" if a["lang"] == "ru" else "Work through a problem from an AI chat"
            self.assertIn("<h2>%s</h2>" % title, s)

    def test_hubs_have_no_block(self):
        for u in ("answers/index.html", "answers/en/index.html"):
            self.assertNotIn("ai-task-paste", read(u), u)

    def test_link_label_and_utm(self):
        for a in ALL:
            blk = BLOCK_RE.search(page(a["slug"])).group(0)
            links = re.findall(r"<a [^>]*>", blk)
            self.assertEqual(len(links), 1, a["slug"])
            self.assertIn('data-tutor-src="paste-%s"' % a["slug"], links[0])
            href = re.search(r'href="([^"]+)"', links[0]).group(1)
            self.assertTrue(href.startswith("/exam-prep-online/?"), href)
            self.assertIn("utm_medium=ai-task-paste", href)
            self.assertIn("utm_campaign=paste-%s#razbor-zapros" % a["slug"], href)

    def test_textarea_maxlength_and_hidden_without_js(self):
        for a in ALL:
            blk = BLOCK_RE.search(page(a["slug"])).group(0)
            self.assertEqual(blk.count("<textarea"), 1, a["slug"])
            self.assertIn('maxlength="2000"', blk)
            self.assertRegex(page(a["slug"]), r'<div class="paste-block" id="ai-task-paste"[^>]* hidden>')
        self.assertIn(".paste-block[hidden]", read("assets", "content.css"))

    def test_no_stop_words_in_block(self):
        for a in ALL:
            blk = BLOCK_RE.search(page(a["slug"])).group(0)
            self.assertIsNone(STOP.search(blk), (a["slug"], STOP.search(blk)))

    def test_site_js_sends_paste_event(self):
        js = read("assets", "site.js")
        self.assertIn("/^(diag|paste)-/", js)
        self.assertIn('name="to-tutor-"+a.getAttribute("data-tutor-src")', js)
        self.assertLess(js.index("/^(diag|paste)-/"), js.index('name="to-tutor-answers-"'))

    def test_intake_form_on_exam_prep(self):
        s = read("exam-prep-online", "index.html")
        self.assertEqual(s.count('id="task-intake"'), 1)
        self.assertEqual(s.count("/assets/ai-task-paste.js"), 1)
        form = re.search(r'<form class="task-intake" id="task-intake".*?</form>', s, re.S).group(0)
        self.assertIn('maxlength="2000"', form)
        self.assertIn('data-mail="vladimir@podlevskikh.com"', form)
        self.assertRegex(form, r'<form [^>]*\bhidden\b')            # без JS форма скрыта
        self.assertNotIn("mailto:", form)                              # статического письма без тела нет
        self.assertIn(".task-intake[hidden]", read("assets", "content.css"))
        self.assertIn('id="task-copy"', form)
        self.assertIsNone(STOP.search(form))

    def test_js_keeps_text_out_of_url_and_analytics(self):
        js = read("assets", "ai-task-paste.js")
        self.assertIn("localStorage", js)
        self.assertIn("sessionStorage", js)
        self.assertIn('"tutorTask"', js)
        for bad in ("location.search +=", "location.search=", "location.href", "location.hash", "history.",
                    "innerHTML", "outerHTML", "insertAdjacentHTML", "fetch(", "XMLHttpRequest", "sendBeacon", "Image(",
                    "encodeURIComponent(text", "document.cookie", "goatcounter"):
            self.assertNotIn(bad, js)


try:
    from playwright.sync_api import sync_playwright
except Exception:           # pragma: no cover
    sync_playwright = None


@unittest.skipIf(sync_playwright is None, "playwright не установлен")
class TestPasteClickScenario(unittest.TestCase):
    TEXT = "Найдите ускорение: m=2 кг, F=6 Н; ответ ИИ 4 м/с² — проверьте <b>SECRETTASK</b> & 'кавычки'"

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

    def _open(self, slug):
        pg = self.browser.new_page()
        reqs = []
        pg.on("request", lambda r: reqs.append((r.url, r.post_data or "")))
        pg.route("**/stats.podlevskikh.com/**", lambda route: route.fulfill(status=200, body=""))
        pg.goto("http://127.0.0.1:%d/answers/%s/" % (self.port, slug))
        pg.wait_for_load_state("networkidle")
        return pg, reqs

    def test_click_stores_text_and_form_picks_it_up(self):
        slug = "ib-physics-hl-tutor-online"
        pg, reqs = self._open(slug)
        self.assertTrue(pg.locator("#ai-task-paste").is_visible())
        pg.locator("#ai-task-paste textarea").fill(self.TEXT)
        with pg.expect_navigation():
            pg.locator('a[data-tutor-src="paste-%s"]' % slug).click()
        pg.wait_for_load_state("networkidle")
        url = pg.url
        self.assertIn("/exam-prep-online/", url)
        self.assertIn("utm_medium=ai-task-paste", url)
        self.assertIn("utm_campaign=paste-" + slug, url)
        self.assertTrue(url.endswith("#razbor-zapros"), url)
        self.assertNotIn("SECRET", url)
        self.assertNotIn("SECRET", pg.evaluate("decodeURIComponent(location.href)"))
        self.assertEqual(pg.locator("#task-intake textarea").input_value(), self.TEXT)
        self.assertIsNone(pg.evaluate("localStorage.getItem('tutorTask')"))
        self.assertTrue(pg.locator("#task-intake textarea").evaluate("e => document.activeElement === e"))
        href = pg.locator("#task-mail").get_attribute("href")
        self.assertTrue(href.startswith("mailto:vladimir@podlevskikh.com?subject="), href)
        self.assertIn("SECRETTASK", __import__("urllib.parse").parse.unquote(href))
        self.assertIn(slug, __import__("urllib.parse").parse.unquote(href))
        self.assertEqual(pg.locator("#task-intake b").count(), 0)         # текст не интерпретируется как HTML
        beacons = [u for u, _ in reqs if "stats.podlevskikh.com/count?" in u]
        self.assertTrue(any(u.split("?p=")[1].split("&")[0].endswith("cta-to-tutor-paste-" + slug)
                            or "cta-to-tutor-paste-" + slug in __import__("urllib.parse").parse.unquote(u) for u in beacons), beacons)
        for u, body in reqs:
            self.assertNotIn("SECRET", __import__("urllib.parse").parse.unquote(u))
            self.assertNotIn("SECRET", body)
        pg.close()

    def test_empty_field_does_not_block_navigation_or_store(self):
        slug = "repetitor-fizika-ege-online"
        pg, _ = self._open(slug)
        with pg.expect_navigation():
            pg.locator('a[data-tutor-src="paste-%s"]' % slug).click()
        pg.wait_for_load_state("networkidle")
        self.assertIn("/exam-prep-online/", pg.url)
        self.assertEqual(pg.locator("#task-intake textarea").input_value(), "")
        self.assertIsNone(pg.evaluate("localStorage.getItem('tutorTask')"))
        pg.close()

    def test_mailto_follows_typing_and_without_js_block_hidden(self):
        pg = self.browser.new_page()
        pg.goto("http://127.0.0.1:%d/exam-prep-online/" % self.port)
        pg.locator("#task-intake textarea").fill("x=1")
        self.assertIn("body=x%3D1", pg.locator("#task-mail").get_attribute("href"))
        pg.close()
        ctx = self.browser.new_context(java_script_enabled=False)
        pg = ctx.new_page()
        pg.goto("http://127.0.0.1:%d/answers/repetitor-fizika-ege-online/" % self.port)
        self.assertFalse(pg.locator("#ai-task-paste").is_visible())
        ctx.close()


    def _intake(self, init=None, text=None):
        ctx = self.browser.new_context()
        if init:
            ctx.add_init_script(init)
        pg = ctx.new_page()
        pg.goto("http://127.0.0.1:%d/exam-prep-online/" % self.port)
        return ctx, pg

    def test_ttl_expired_record_ignored_and_removed(self):
        old = int((__import__("time").time() - 31 * 60) * 1000)
        init = "if (!localStorage.getItem('seeded')) { localStorage.setItem('seeded','1'); localStorage.setItem('tutorTask', JSON.stringify({text:'OLDTEXT',slug:'x',ts:%d})); }" % old
        ctx, pg = self._intake(init)
        self.assertEqual(pg.locator("#task-intake textarea").input_value(), "")
        self.assertIsNone(pg.evaluate("localStorage.getItem('tutorTask')"))
        ctx.close()
        fresh = int((__import__("time").time() - 5 * 60) * 1000)
        init = "if (!localStorage.getItem('seeded')) { localStorage.setItem('seeded','1'); localStorage.setItem('tutorTask', JSON.stringify({text:'FRESHTEXT',slug:'x',ts:%d})); }" % fresh
        ctx, pg = self._intake(init)
        self.assertEqual(pg.locator("#task-intake textarea").input_value(), "FRESHTEXT")
        self.assertIsNone(pg.evaluate("localStorage.getItem('tutorTask')"))
        ctx.close()

    def test_empty_click_erases_saved_text(self):
        slug = "repetitor-fizika-ege-online"
        pg, _ = self._open(slug)
        pg.evaluate("localStorage.setItem('tutorTask', JSON.stringify({text:'STALE',slug:'x',ts:Date.now()}))")
        with pg.expect_navigation():
            pg.locator('a[data-tutor-src="paste-%s"]' % slug).click()
        pg.wait_for_load_state("networkidle")
        self.assertEqual(pg.locator("#task-intake textarea").input_value(), "")
        pg.close()

    def test_auxclick_middle_button_and_ctrl_click_save(self):
        slug = "ib-physics-hl-tutor-online"
        ctx = self.browser.new_context()
        ctx.route("**/exam-prep-online/**", lambda route: route.abort())      # вкладки-приёмники не должны забрать запись
        pg = ctx.new_page()
        pg.goto("http://127.0.0.1:%d/answers/%s/" % (self.port, slug))
        pg.wait_for_load_state("networkidle")
        pg.evaluate("['click','auxclick'].forEach(t => document.querySelector('a[data-tutor-src]').addEventListener(t, e => e.preventDefault()))")
        pg.locator("#ai-task-paste textarea").fill("MIDDLE")
        pg.locator('a[data-tutor-src="paste-%s"]' % slug).click(button="middle")
        pg.wait_for_function("localStorage.getItem('tutorTask') !== null", timeout=3000)
        self.assertEqual(__import__("json").loads(pg.evaluate("localStorage.getItem('tutorTask')"))["text"], "MIDDLE")
        pg.evaluate("localStorage.clear()")
        pg.locator("#ai-task-paste textarea").fill("CTRL")
        pg.locator('a[data-tutor-src="paste-%s"]' % slug).click(modifiers=["Control"])
        pg.wait_for_function("localStorage.getItem('tutorTask') !== null", timeout=3000)
        self.assertEqual(__import__("json").loads(pg.evaluate("localStorage.getItem('tutorTask')"))["text"], "CTRL")
        ctx.close()
        pg, _ = self._open(slug)
        pg.locator("#ai-task-paste textarea").fill("ENTER")
        pg.locator('a[data-tutor-src="paste-%s"]' % slug).focus()
        with pg.expect_navigation():
            pg.keyboard.press("Enter")
        pg.wait_for_load_state("networkidle")
        self.assertEqual(pg.locator("#task-intake textarea").input_value(), "ENTER")      # Enter по ссылке = click
        pg.close()

    def test_long_cyrillic_text_mailto_limited(self):
        long = "Решите задачу про ускорение. " * 80
        long = long[:2000]
        pg = self.browser.new_page()
        pg.goto("http://127.0.0.1:%d/exam-prep-online/" % self.port)
        pg.locator("#task-intake textarea").fill(long)
        href = pg.locator("#task-mail").get_attribute("href")
        self.assertLessEqual(len(href), 2100, len(href))
        body = __import__("urllib.parse").parse.unquote(href.split("&body=")[1])
        self.assertIn("текст обрезан", body)
        self.assertTrue(body.startswith("Решите задачу"))
        self.assertTrue(pg.locator("#task-long").is_visible())
        self.assertIn("Скопировать", pg.locator("#task-long").text_content())
        pg.locator("#task-intake textarea").fill("коротко")
        self.assertFalse(pg.locator("#task-long").is_visible())
        self.assertNotIn("%D0%BE%D0%B1%D1%80%D0%B5%D0%B7", pg.locator("#task-mail").get_attribute("href"))
        pg.close()

    def test_form_hidden_in_html_visible_after_js(self):
        ctx = self.browser.new_context(java_script_enabled=False)
        pg = ctx.new_page()
        pg.goto("http://127.0.0.1:%d/exam-prep-online/" % self.port)
        self.assertFalse(pg.locator("#task-intake").is_visible())
        ctx.close()
        pg = self.browser.new_page()
        pg.goto("http://127.0.0.1:%d/exam-prep-online/" % self.port)
        self.assertTrue(pg.locator("#task-intake").is_visible())
        pg.close()

    def test_storage_unavailable_does_not_break(self):
        init = ("Object.defineProperty(window,'localStorage',{get(){throw new Error('denied')}});"
                "Object.defineProperty(window,'sessionStorage',{get(){throw new Error('denied')}});")
        ctx = self.browser.new_context()
        ctx.add_init_script(init)
        pg = ctx.new_page()
        errors = []
        pg.on("pageerror", lambda e: errors.append(str(e)))
        slug = "ib-physics-hl-tutor-online"
        pg.goto("http://127.0.0.1:%d/answers/%s/" % (self.port, slug))
        self.assertTrue(pg.locator("#ai-task-paste").is_visible())
        pg.locator("#ai-task-paste textarea").fill("TEXT")
        with pg.expect_navigation():
            pg.locator('a[data-tutor-src="paste-%s"]' % slug).click()
        pg.wait_for_load_state("networkidle")
        self.assertIn("/exam-prep-online/", pg.url)
        self.assertTrue(pg.locator("#task-intake").is_visible())
        self.assertEqual(pg.locator("#task-intake textarea").input_value(), "")
        self.assertEqual(errors, [])
        ctx.close()

if __name__ == "__main__":
    unittest.main()
