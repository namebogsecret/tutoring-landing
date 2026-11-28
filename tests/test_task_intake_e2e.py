# -*- coding: utf-8 -*-
"""Путь «клик -> заявка» (#task-intake) на 360x800, локально: первый экран, EN, пустой ввод, запасной путь, событие.
Chromium-сценарии выполняются, только если установлен playwright (~/.venv/playwright/bin/python tests/test_task_intake_e2e.py)."""
import functools
import http.server
import os
import socketserver
import sys
import threading
import unittest
import urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
try:
    import task_intake_smoke as S
except Exception:           # pragma: no cover  (нет playwright)
    S = None

ADDR = "vladimir@podlevskikh.com"
TEXT = "SECRETTASK m=2"


@unittest.skipIf(S is None, "playwright не установлен")
class TestTaskIntake(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=ROOT)
        handler.log_message = lambda *a, **k: None
        socketserver.TCPServer.allow_reuse_address = True
        cls.httpd = socketserver.ThreadingTCPServer(("127.0.0.1", 0), handler)
        cls.base = "http://127.0.0.1:%d" % cls.httpd.server_address[1]
        threading.Thread(target=cls.httpd.serve_forever, daemon=True).start()
        for p in S.STATIC:                      # тесты в сеть не ходят
            S._cache["https://stats.podlevskikh.com" + p] = b""
        cls.pw = S.sync_playwright().start()
        cls.browser = cls.pw.chromium.launch()

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.pw.stop()
        cls.httpd.shutdown()
        cls.httpd.server_close()

    def open(self, path, init="", clip=True):
        self.hits = []
        ctx = S.context(self.browser, self.base, self.hits, init)
        if clip:
            ctx.grant_permissions(["clipboard-read", "clipboard-write"], origin=self.base)
        self.addCleanup(ctx.close)
        pg = ctx.new_page()
        pg.goto(self.base + path)
        S.settle(pg)
        return pg

    def assert_first_screen(self, pg, where):
        for sel in ("#task-intake textarea", "#task-mail", "#task-copy"):
            v = pg.evaluate(S.VIS, sel)
            self.assertTrue(v["ok"], (where, sel, v))

    def test_hash_arrivals_show_form_on_first_screen(self):
        for path in ("/exam-prep-online/#razbor-zapros", "/exam-prep-online/#task-intake",
                     "/exam-prep-online/?lang=en#task-intake"):
            self.assert_first_screen(self.open(path), path)

    def test_answer_page_links_show_form_on_first_screen(self):
        slug = "repetitor-igcse-matematika-0580-na-russkom"
        for sel in ('a[data-tutor-src="%s"]' % slug, 'a[data-tutor-src="top-%s"]' % slug):
            pg = self.open("/answers/%s/" % slug)
            with pg.expect_navigation():
                pg.locator(sel).click()
            S.settle(pg)
            self.assert_first_screen(pg, sel)

    def test_answer_page_links_without_scroll_anchoring(self):
        """Как на проде (и в Safari): без подстройки прокрутки форма оставалась ниже первого экрана."""
        slug = "repetitor-igcse-matematika-0580-na-russkom"
        css = ("document.addEventListener('DOMContentLoaded',()=>{const s=document.createElement('style');"
               "s.textContent='*{overflow-anchor:none!important}';document.head.appendChild(s)});")
        for sel in ('a[data-tutor-src="%s"]' % slug, 'a[data-tutor-src="top-%s"]' % slug):
            pg = self.open("/answers/%s/" % slug, css)
            with pg.expect_navigation():
                pg.locator(sel).click()
            S.settle(pg)
            self.assert_first_screen(pg, sel)

    def test_english_reader_gets_english_form(self):
        slug = "ib-physics-hl-tutor-online"
        for sel in ('a[data-tutor-src="%s"]' % slug, 'a[data-tutor-src="top-%s"]' % slug,
                    'a[data-tutor-src="paste-%s"]' % slug):
            pg = self.open("/answers/%s/" % slug)
            with pg.expect_navigation():
                pg.locator(sel).click()
            S.settle(pg)
            self.assertTrue(pg.url.endswith("#razbor-zapros"), pg.url)
            self.assertTrue(pg.inner_text("#task-intake").replace("→", "").isascii(), pg.inner_text("#task-intake"))
        pg.fill("#task-intake textarea", TEXT)
        pg.click("#task-mail")
        self.assertIn("did not open", pg.inner_text("#task-copied"))

    def test_russian_reader_keeps_russian_form(self):
        pg = self.open("/exam-prep-online/#task-intake")
        self.assertEqual(pg.inner_text("#task-intake h3"), "Ваша задача")
        self.assertIn(ADDR, pg.inner_text("#task-intake"))          # адрес виден до любых кликов

    def test_empty_input_is_explained_and_not_sent(self):
        pg = self.open("/exam-prep-online/#task-intake")
        pg.evaluate("navigator.clipboard.writeText('KEEP')")
        for sel in ("#task-mail", "#task-copy"):
            pg.evaluate("window.__ext=[]")
            pg.fill("#task-intake textarea", "  ")
            pg.click(sel)
            pg.wait_for_timeout(200)
            self.assertIn("Сначала вставьте", pg.inner_text("#task-copied"), sel)
            self.assertTrue(all(x["blocked"] for x in pg.evaluate("window.__ext")), sel)
        self.assertEqual(pg.evaluate("navigator.clipboard.readText()"), "KEEP")
        self.assertFalse([h for h in self.hits if "cta-book" in h], self.hits)

    def test_mail_and_copy_show_address_and_count_once(self):
        for first, second, name in (("#task-mail", "#task-copy", "mail"), ("#task-copy", "#task-mail", "copy")):
            pg = self.open("/exam-prep-online/#task-intake")
            pg.fill("#task-intake textarea", TEXT)
            pg.click(first)
            pg.wait_for_timeout(300)
            self.assertIn(ADDR, pg.inner_text("#task-copied"))
            pg.click(second)
            pg.click(first)
            pg.wait_for_timeout(300)
            book = [h for h in self.hits if "cta-book" in h]
            self.assertEqual(len(book), 1, self.hits)
            self.assertTrue(book[0].endswith("/cta-book-task-intake-" + name), book)
            self.assertFalse([h for h in self.hits if "SECRET" in urllib.parse.unquote(h)])
            href = urllib.parse.unquote(pg.get_attribute("#task-mail", "href"))
            self.assertIn(TEXT, href)

    def test_clipboard_denied_names_address_and_not_counted(self):
        pg = self.open("/exam-prep-online/#task-intake",
                       "navigator.clipboard.writeText=()=>Promise.reject(new Error('x'));")
        pg.fill("#task-intake textarea", TEXT)
        pg.click("#task-copy")
        pg.wait_for_timeout(300)
        self.assertIn(ADDR, pg.inner_text("#task-copied"))
        self.assertFalse([h for h in self.hits if "cta-book" in h], self.hits)


if __name__ == "__main__":
    unittest.main()
