#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Entity-контракт сайта: единый Person @id, sameAs только из профилей самого человека,
собственные проекты — в subjectOf, сеть без снятых сайтов, нет устаревших фактов.
Запуск: python3 tests/test_entity.py (после python3 build.py)."""
import glob, json, os, re, unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PID = "https://tutor.podlevskikh.com/#vladimir"
SAMEAS = {
    "https://linkedin.com/in/vladimir-podlevskikh",
    "https://preply.in/VLADIMIR6EN2958527510",
    "https://t.me/VladimirPodlevskikh",
    "https://profi.ru/profile/PodlevskihVN/",
    "https://www.lessonface.com/node/133512",
    "https://www.superprof.com/mathematics-msu-superprof-super-tutor-for-gcse-igcse-level-sat.html",
}
REMOVED_SITES = ("events.podlevskikh.com", "ideas.podlevskikh.com", "auto.podlevskikh.com", "aiact.podlevskikh.com")
STALE = re.compile(r"Yerevan|Ереван|Nyberg|GMT\+4|Лимассол|Limassol|Cyprus|Кипр|I Can|4\.88|\+7 ?\(|"
                   r"ВКонтакте|vk\.com|Armenia|Армени|23\+|aggregateRating|reviewCount")
# неподтверждённые результаты/отзывы/рейтинг (ФАКТ-ЛИСТ: «Нельзя»): ловим на ВСЕХ отдаваемых страницах
# \blaureate: ловим «laureate» как слово-заявку, но не «International Baccalaureate» (официальное имя программы на /ib-physics-tutor/).
UNVERIFIED = re.compile(r"призёр|призер|medalist|\blaureate|Mikhail N|Valeriia|Sonya S|Anetta|Nadya M|1620|2060|"
                        r"double-digit|десятки баллов|рекомендательн|reference letters|from a Level C|с уровня C|82 ?(→|to|до) ?96|"
                        r"Бауман|Bauman|Oracle|Amazon|C→A|★★|\+30–60|95%\+", re.I)


def pages():
    out = ["index.html"] + [os.path.relpath(p, ROOT) for p in glob.glob(os.path.join(ROOT, "*/index.html"))
                           if not p.startswith(os.path.join(ROOT, "hub"))] + \
          [os.path.relpath(p, ROOT) for p in glob.glob(os.path.join(ROOT, "blog/*/index.html"))]
    return sorted(set(out))


def blocks(html):
    return [json.loads(x) for x in re.findall(r'<script type="application/ld\+json">\s*(.*?)\s*</script>', html, re.S)]


def walk(o):
    if isinstance(o, dict):
        yield o
        for v in o.values():
            yield from walk(v)
    elif isinstance(o, list):
        for v in o:
            yield from walk(v)


class T(unittest.TestCase):
    def test_person(self):
        for p in pages():
            html = open(os.path.join(ROOT, p), encoding="utf-8").read()
            persons = [n for b in blocks(html) for n in walk(b) if n.get("@type") == "Person"]
            self.assertTrue(persons, p)
            for n in persons:
                self.assertEqual(n.get("@id"), PID, p)
                self.assertEqual(set(n.get("sameAs", [])), SAMEAS, p)
                self.assertNotIn("aggregateRating", n, p)
                sub = n.get("subjectOf", [])
                self.assertTrue(sub, p)
                for w in sub:
                    self.assertEqual(w["@type"], "WebSite")
                    self.assertEqual(w["creator"], {"@id": PID})
                    self.assertTrue(w["url"].startswith("https://") and "podlevskikh.com" in w["url"])
            # любые ссылки-на-человека по @id должны указывать на тот же узел
            for b in blocks(html):
                for n in walk(b):
                    if n.get("@type") in ("Person",) or "@id" not in n:
                        continue
                    if "podlevskikh.com/#" in n["@id"]:
                        self.assertEqual(n["@id"], PID, p)

    def test_network_and_stale(self):
        files = [f for f in glob.glob(os.path.join(ROOT, "**/*"), recursive=True)
                 if f.endswith((".html", ".txt", ".xml", ".js")) and "/src/" not in f and "/tests/" not in f
                 and "/.git/" not in f]
        for f in files:
            s = open(f, encoding="utf-8", errors="ignore").read()
            for d in REMOVED_SITES:
                self.assertNotIn(d, s, f)
            m = STALE.search(s)
            self.assertIsNone(m, "%s: %r" % (f, m.group(0) if m else ""))
            m = UNVERIFIED.search(s)
            self.assertIsNone(m, "%s: %r" % (f, m.group(0) if m else ""))


if __name__ == "__main__":
    unittest.main()
