"""Мобильная скорость /answers/ и хаба (360×800): LCP не ждёт JS-fade и Google Fonts, CTA на первом экране.
Проверки статические (по собранному HTML); замер Lighthouse — в ГРАБЛИ.md."""
import glob, os, re, unittest

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def pages():
    fs = sorted(glob.glob(os.path.join(HERE, "answers", "**", "index.html"), recursive=True))
    return [(f, open(f, encoding="utf-8").read()) for f in fs]


class TestAnswersMobile(unittest.TestCase):
    def test_pages_found(self):
        self.assertGreaterEqual(len(pages()), 30)

    def test_no_render_blocking_fonts_or_site_js(self):
        for f, h in pages():
            self.assertIn('rel="preload" as="style"', h, f)
            self.assertNotRegex(h, r'<link href="https://fonts\.googleapis[^>]*rel="stylesheet" />\n<link rel="stylesheet" href="/assets/site\.css"', f)
            self.assertIn('<script src="/assets/site.js" defer></script>', h, f)

    def test_first_screen_not_hidden_by_reveal(self):
        for f, h in pages():
            self.assertIn(".reveal{opacity:1;transform:none;transition:none}", h, f)

    def test_top_cta_one_per_page_with_event_source(self):
        for f, h in pages():
            m = re.findall(r'<a class="btn btn-primary btn-sm top-cta" data-tutor-src="(top-[a-z0-9-]+)" href="/exam-prep-online/\?utm_source=answers&amp;utm_medium=top-cta&amp;utm_campaign=\1#razbor-zapros">', h)
            self.assertEqual(len(m), 1, f)
            self.assertLess(h.index("top-cta\" data-tutor-src"), h.index("<main"), f)   # в шапке, до контента

    def test_event_wiring_kept(self):
        js = open(os.path.join(HERE, "assets", "site.js"), encoding="utf-8").read()
        self.assertIn('name="to-tutor-answers-"+a.getAttribute("data-tutor-src")', js)

    def test_other_pages_untouched(self):
        h = open(os.path.join(HERE, "exam-prep-online", "index.html"), encoding="utf-8").read()
        self.assertNotIn("top-cta", h)
        self.assertNotIn('rel="preload" as="style"', h)


if __name__ == "__main__":
    unittest.main()
