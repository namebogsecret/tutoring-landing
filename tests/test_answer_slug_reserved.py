"""Префикс slug «top-» зарезервирован: site.js шлёт cta-to-tutor-answers-<slug>, а кнопка вверху страницы —
answers-top-<slug> (build.py). cta-report воронки считает всё answers-top-* верхней кнопкой, поэтому страница
со slug «top-…» увела бы свою обычную кнопку в чужую таблицу."""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import answer_pages as AP  # noqa: E402


class TestSlugTopReserved(unittest.TestCase):
    def test_no_answer_slug_starts_with_top(self):
        pages = AP.ANSWERS + AP.ANSWERS_EN + AP.ANSWERS_MATH + AP.ANSWERS_PHYS
        self.assertTrue(pages)
        slugs = [a["slug"] for a in pages] + [p.name for p in AP_DIR.iterdir() if p.is_dir()]
        self.assertEqual([s for s in slugs if s.startswith("top-")], [])


AP_DIR = __import__("pathlib").Path(__file__).resolve().parent.parent / "answers"

if __name__ == "__main__":
    unittest.main()
