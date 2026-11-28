# -*- coding: utf-8 -*-
"""AI-SEO контракт отдаваемых страниц: сущность Person/Service, FAQ, answer-first,
запрещённые упоминания, sitemap, robots.txt, llms.txt, факты из ФАКТ-ЛИСТа.
Запуск: python3 tests/test_ai_seo.py  или  python3 -m pytest -q tests/test_ai_seo.py
Страницы /answers/ — страницы замеров: проверяются только на школу/Кипр и sitemap,
их нарушения не валят тест (печатаются как XFAIL)."""
import glob, html, json, os, re, subprocess, sys, urllib.robotparser
import xml.etree.ElementTree as ET
from html.parser import HTMLParser

H = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://tutor.podlevskikh.com"
PID = BASE + "/#vladimir"
SUBJECT = ["exam-prep-online", "ap-physics-tutor", "ib-physics-tutor", "igcse-physics-0625",
           "ege-physics", "olympiad-physics", "physics-tutor-online", "russian-tutor-abroad"]
PAGES = [""] + SUBJECT
BANNED = re.compile(r"nyberg|нюберг|найберг|cyprus|кипр|limassol|лимассол", re.I)
# ФАКТ-ЛИСТ, «Нельзя» / «Можно»
BAD_FACTS = re.compile(
    r"4[.,]88|\b(?:127|214)\s*(?:отзыв|review)|\+\s?30\s?[–-]\s?60|95\s?%\+?\s*(?:довольн|satisf)|"
    r"20\+\s*(?:приз[её]р|winners|years|лет)|yerevan|ереван|\bPodlevskih\b|Подлевск(?:ий|ого)\b|"
    r"23\s+(?:years\s+(?:of\s+)?classroom|года?\s+(?:школьного|в классе))", re.I)
AI_BOTS = ("GPTBot", "ClaudeBot", "PerplexityBot")


def rd(p):
    with open(os.path.join(H, p), encoding="utf-8") as f:
        return f.read()


def page_file(slug):
    return slug + "/index.html" if slug else "index.html"


def blocks(doc):
    return re.findall(r'<script\b[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', doc, re.S | re.I)


def walk(o, key=""):
    if isinstance(o, dict):
        yield key, o
        for k, v in o.items():
            yield from walk(v, k)
    elif isinstance(o, list):
        for v in o:
            yield from walk(v, key)


def nodes(slug):
    out = []
    for b in blocks(rd(page_file(slug))):
        try:
            out.extend(walk(json.loads(b)))
        except ValueError:
            pass  # ловится test_jsonld_parses
    return out


def is_type(d, t):
    v = d.get("@type")
    return t in (v if isinstance(v, list) else [v])


def about_vladimir(d):
    names = json.dumps([d.get("name"), d.get("alternateName")], ensure_ascii=False)
    return bool(re.search(r"vladimir|владимир|podlevsk|подлевск", names, re.I))


class Visible(HTMLParser):
    SKIP = {"script", "style", "head", "template", "noscript"}
    INLINE = {"a", "b", "i", "em", "strong", "span", "sup", "sub", "code", "u", "small", "mark", "abbr", "nobr"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.skip, self.out = 0, []

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self.skip += 1
        elif tag not in self.INLINE:
            self.out.append(" ")

    def handle_endtag(self, tag):
        if tag in self.SKIP:
            self.skip = max(0, self.skip - 1)
        elif tag not in self.INLINE:
            self.out.append(" ")

    def handle_data(self, data):
        if not self.skip:
            self.out.append(data)


def norm(s):
    return " ".join(html.unescape(s).split())


def visible(doc):
    p = Visible()
    p.feed(doc)
    p.close()
    return norm("".join(p.out))


def served():
    """Те же файлы, что deploy.sh кладёт в gh-pages (плюс llms.txt), только текстовые."""
    files = subprocess.run(["git", "ls-files", "-z"], cwd=H, capture_output=True, check=True).stdout.decode().split("\0")
    return [f for f in files if f and not re.match(r"(tests|src)/|deploy\.sh$|\.gitignore$", f)
            and not f.endswith((".py", ".md")) and f.endswith((".html", ".txt", ".xml", ".js", ".json", ".css", ".svg", ".webmanifest"))
            and os.path.isfile(os.path.join(H, f))]


def noindex(doc):
    return any(re.search(r'name=["\']robots["\']', m, re.I) and "noindex" in m.lower()
               for m in re.findall(r"<meta\b[^>]*>", doc, re.I))


def url_file(u):
    path = re.split(r"[?#]", u[len(BASE):])[0].lstrip("/")
    if not path or path.endswith("/"):
        return path + "index.html"
    return path if os.path.isfile(os.path.join(H, path)) else path + "/index.html"


def report(errs):
    assert not errs, "\n" + "\n".join(errs)


def test_jsonld_parses():
    errs = []
    for s in PAGES:
        bs = blocks(rd(page_file(s)))
        if not bs:
            errs.append(f"/{s}: нет JSON-LD")
        for i, b in enumerate(bs):
            try:
                json.loads(b)
            except ValueError as e:
                errs.append(f"/{s}: блок {i} не парсится: {e}")
    report(errs)


def test_person_present_and_identified():
    errs = []
    for s in PAGES:
        ns = nodes(s)
        if not any(is_type(d, "Person") and d.get("@id") == PID for _, d in ns):
            errs.append(f"/{s}: нет Person с @id {PID}")
        for key, d in ns:
            person_like = is_type(d, "Person") or (key in ("author", "provider", "creator", "instructor") and "@type" not in d)
            if person_like and about_vladimir(d) and d.get("@id") != PID:
                errs.append(f"/{s}: узел Vladimir в «{key or 'корне'}» с @id={d.get('@id')!r}")
    report(errs)


def test_service_with_provider_ref():
    errs = []
    for s in PAGES:
        services = [d for _, d in nodes(s) if is_type(d, "Service")]
        if not services:
            types = sorted({str(d.get("@type")) for k, d in nodes(s) if not k and d.get("@type")})
            errs.append(f"/{s}: нет узла Service (верхнеуровневые типы: {', '.join(types)})")
        for d in services:
            p = d.get("provider")
            if not (isinstance(p, dict) and p.get("@id") == PID):
                errs.append(f"/{s}: Service «{d.get('name')}» provider={p!r}, ожидается ссылка на {PID}")
    report(errs)


def test_same_as_consistent():
    errs, seen = [], {}
    for s in PAGES:
        sets = [d["sameAs"] for _, d in nodes(s) if (is_type(d, "Person") or d.get("@id") == PID) and "sameAs" in d]
        if not sets:
            errs.append(f"/{s}: у Person нет sameAs")
        for v in sets:
            v = frozenset(v if isinstance(v, list) else [v])
            seen.setdefault(v, set()).add("/" + s)
    if len(seen) > 1:
        errs.append("разные наборы sameAs: " + "; ".join(f"{sorted(p)} -> {sorted(v)}" for v, p in seen.items()))
    report(errs)


def test_faq_verbatim_visible():
    errs = []
    for s in PAGES:
        text = visible(rd(page_file(s)))
        faqs = [d for _, d in nodes(s) if is_type(d, "FAQPage")]
        if not faqs or not all(f.get("mainEntity") for f in faqs):
            errs.append(f"/{s}: нет FAQPage или она пустая")
        for f in faqs:
            for q in f.get("mainEntity") or []:
                pairs = (("вопрос", q.get("name", "")), ("ответ", (q.get("acceptedAnswer") or {}).get("text", "")))
                for kind, raw in pairs:
                    t = visible("<body>" + raw + "</body>")
                    if not t or t not in text:
                        errs.append(f"/{s}: FAQ {kind} нет дословно в видимом тексте: «{t[:160]}»")
    report(errs)


def test_answer_first():
    errs = []
    subj = re.compile(r"физик|математик|репетитор|олимпиад|ЕГЭ|physics|math|tutor|IGCSE|IB\b|AP\b|SAT\b|A-Level", re.I)
    for s in PAGES:
        doc = rd(page_file(s))
        after = doc.split("</h1>", 1)
        if len(after) != 2:
            errs.append(f"/{s}: нет H1")
            continue
        m = re.search(r"<p\b[^>]*>(.*?)</p>", after[1], re.S)
        t = visible("<body>" + m.group(1) + "</body>") if m else ""
        if len(t) < 80 or not subj.search(t):
            errs.append(f"/{s}: первый абзац после H1 ({len(t)} зн., предмет {'есть' if subj.search(t) else 'не назван'}): «{t[:200]}»")
    report(errs)


def _banned_hits(files):
    errs = []
    for f in files:
        with open(os.path.join(H, f), encoding="utf-8", errors="replace") as fh:
            raw = fh.read()
        hits = {m.group(0) for m in BANNED.finditer(raw + "\n" + html.unescape(raw))}
        if hits:
            errs.append(f"{f}: {sorted(hits)}")
    return errs


def test_no_school_no_cyprus():
    files = served()
    assert "llms.txt" in files and "index.html" in files
    report(_banned_hits([f for f in files if not f.startswith("answers/")]))


def test_no_school_no_cyprus_answers_xfail():
    errs = _banned_hits([f for f in served() if f.startswith("answers/")])
    if errs:
        _xfail("/answers/ (замеры, не правятся): " + "; ".join(errs))


def _xfail(msg):
    if "pytest" in sys.modules:
        import pytest
        pytest.xfail(msg)
    print("XFAIL: " + msg)


def sitemap_locs():
    ns = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
    return [e.text.strip() for e in ET.fromstring(rd("sitemap.xml").encode()).iter(ns + "loc")]


def _sitemap_errors():
    locs, errs = sitemap_locs(), []
    assert locs, "sitemap пуст"
    for u in locs:
        if not u.startswith(BASE + "/"):
            errs.append((u, f"sitemap: чужой loc {u}"))
            continue
        f = url_file(u)
        if not os.path.isfile(os.path.join(H, f)):
            errs.append((f, f"sitemap: нет файла для {u}"))
        elif f.endswith(".html") and noindex(rd(f)):
            errs.append((f, f"sitemap: {u} помечен noindex"))
    for f in served():
        if os.path.basename(f) == "index.html" and not noindex(rd(f)):
            u = BASE + "/" + f[:-len("index.html")]
            if u not in locs:
                errs.append((f, f"sitemap: indexable {f} отсутствует"))
    return errs


def test_sitemap():
    report([m for f, m in _sitemap_errors() if not f.startswith("answers/")])


def test_sitemap_answers_xfail():
    errs = [m for f, m in _sitemap_errors() if f.startswith("answers/")]
    if errs:
        _xfail("; ".join(errs))


def test_robots():
    txt = rd("robots.txt")
    rp = urllib.robotparser.RobotFileParser()
    rp.parse(txt.splitlines())
    errs = [f"robots.txt: {b} запрещён на {u}" for b in AI_BOTS for u in sitemap_locs() if not rp.can_fetch(b, u)]
    if not re.search(r"(?mi)^Sitemap:\s*%s/sitemap\.xml\s*$" % re.escape(BASE), txt):
        errs.append("robots.txt: нет Sitemap:")
    report(errs)


def test_llms_links_and_coverage():
    links = [u.rstrip(".,;:") for u in re.findall(re.escape(BASE) + r"(?:/[^\s)\]>\"']*)?", rd("llms.txt"))]
    assert links
    errs = [f"llms.txt: ссылка без файла {u}" for u in links if not os.path.isfile(os.path.join(H, url_file(u)))]
    listed = {url_file(u) for u in links}
    errs += [f"llms.txt: не перечислена /{s}/" for s in SUBJECT if page_file(s) not in listed]
    report(errs)


def test_facts_match_fact_sheet():
    errs = []
    texts = {"llms.txt": rd("llms.txt")}
    for s in PAGES:
        doc = rd(page_file(s))
        ld = []
        for b in blocks(doc):
            try:
                ld.append(json.dumps(json.loads(b), ensure_ascii=False))
            except ValueError:
                pass
        texts[f"/{s} JSON-LD"] = "\n".join(ld)
        texts[f"/{s} видимый текст"] = visible(doc)
    for name, t in texts.items():
        t = re.sub(r"https?://[^\s\"')]+", " ", t)  # URL профилей содержат старую транслитерацию
        for m in BAD_FACTS.finditer(t):
            errs.append(f"{name}: против ФАКТ-ЛИСТа «{m.group(0)}»: …{t[max(0, m.start() - 70):m.end() + 50]}…")
    report(errs)


if __name__ == "__main__":
    failed = 0
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
                print("ok   " + name)
            except AssertionError as e:
                failed += 1
                print(f"FAIL {name}: {e}")
    print(f"красных: {failed}" if failed else "OK: все проверки зелёные")
    sys.exit(1 if failed else 0)
