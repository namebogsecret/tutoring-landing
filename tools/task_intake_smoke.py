#!/usr/bin/env python3
"""Смоук пути «клик -> заявка» (#task-intake) на 360x800, ru и en. Повторять после выкатки:
    ~/.venv/playwright/bin/python tools/task_intake_smoke.py [BASE_URL]
Настоящих заявок и хитов не бывает: всё к статистике перехватывается и только записывается, чужие хосты обрываются,
переход по mailto:/calendly/t.me отменяется в странице. Статические скрипты stats.* (счётчик, виджет отзывов,
футер) скачиваются обычным GET один раз, чтобы плавающие элементы и вёрстка были как на проде. Код выхода 1 = есть обрыв.
"""
import sys
import urllib.parse
import urllib.request

from playwright.sync_api import sync_playwright

UA = ("Mozilla/5.0 (Linux; Android 14; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/126.0.0.0 Mobile Safari/537.36")
STATIC = ("/count.js", "/fb/static/feedback-widget.js", "/a/static/network-footer.js")
STUB = """
Object.defineProperty(Navigator.prototype,'webdriver',{get:()=>false});
window.__ext=[];
window.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a');
 if(a&&/^(mailto:|tg:|https:\\/\\/(t\\.me|calendly\\.com))/.test(a.href)){window.__ext.push({href:a.href,blocked:e.defaultPrevented});e.preventDefault();}},false);
"""
PAGES = {"ru": ["podgotovka-a-level-ib-fizika-onlajn", "repetitor-igcse-matematika-0580-na-russkom",
                "repetitor-ib-physics-russkoyazychnyj"],
         "en": ["ib-physics-hl-tutor-online", "best-ib-math-aa-hl-tutor-online", "igcse-physics-0625-tutor-russian"]}
TEXT = "SMOKETASK: m=2 kg, F=6 N, найдите ускорение"
VIS = """sel => { const e=document.querySelector(sel); if(!e) return {missing:true};
 const r=e.getBoundingClientRect(); const x=r.left+r.width/2, y=r.top+Math.min(r.height/2,40);
 const h=document.elementFromPoint(x,y);
 return {top:Math.round(r.top), bottom:Math.round(r.bottom),
   ok: r.width>0 && r.top>=0 && r.bottom<=innerHeight && !!h && (h===e||e.contains(h)),
   cover: h && h!==e && !e.contains(h) ? (h.tagName+'.'+h.className) : ''} }"""

_cache = {}


def _static(url):
    if url not in _cache:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=20) as r:
            _cache[url] = r.read()
    return _cache[url]


def context(browser, base, hits, init=""):
    """Контекст с перехватом всего внешнего. hits пополняется путями событий GoatCounter."""
    ctx = browser.new_context(viewport={"width": 360, "height": 800}, user_agent=UA, is_mobile=True, has_touch=True)
    host = urllib.parse.urlsplit(base).hostname

    def route(rt):
        u = urllib.parse.urlsplit(rt.request.url)
        if u.hostname == "stats.podlevskikh.com":
            if u.path in STATIC and rt.request.method == "GET":
                return rt.fulfill(status=200, content_type="application/javascript", body=_static(rt.request.url.split("?")[0]))
            p = urllib.parse.parse_qs(u.query).get("p")
            hits.append(p[0] if p else u.path)
            return rt.fulfill(status=200, body="", headers={"Access-Control-Allow-Origin": "*"})
        if u.hostname in (host, "fonts.googleapis.com", "fonts.gstatic.com"):
            return rt.continue_()
        return rt.abort()

    ctx.grant_permissions(["clipboard-read", "clipboard-write"], origin=base)
    ctx.route("**/*", route)
    ctx.add_init_script(STUB + init)
    return ctx


def settle(pg):
    pg.wait_for_load_state("load")
    pg.wait_for_timeout(1800)


def main(base):
    bad = []

    def row(step, ok, info=""):
        print("%-4s %s | %s" % ("ok" if ok else "FAIL", step, info))
        if not ok:
            bad.append(step)

    def form_rows(pg, step):
        for sel in ("#task-intake textarea", "#task-mail"):
            v = pg.evaluate(VIS, sel)
            row("%s first-screen %s" % (step, sel), v.get("ok", False), v)

    with sync_playwright() as p:
        b = p.chromium.launch()
        for lang, slugs in PAGES.items():
            for slug in slugs:
                hits = []
                ctx = context(b, base, hits)
                pg = ctx.new_page()
                pg.goto("%s/answers/%s/" % (base, slug))
                settle(pg)
                links = pg.eval_on_selector_all('a[href*="/exam-prep-online/"]', "a=>a.map(x=>x.getAttribute('data-tutor-src')||x.getAttribute('href'))")
                srcs = pg.eval_on_selector_all('a[data-tutor-src]', "a=>a.map(x=>x.getAttribute('data-tutor-src'))")
                top = pg.locator('a[href*="utm_medium=top-cta"]').count()
                print("-- %s %s: links=%d src=%s top-cta=%d hits_on_load=%s" % (lang, slug, len(links), srcs, top, hits))
                kinds = [('a[data-tutor-src="%s"]' % s, "paste" if s.startswith("paste-") else "task-block")
                         for s in srcs if not s.startswith(("diag-", "top-"))]
                if top:
                    kinds.append(('a[href*="utm_medium=top-cta"]', "top-cta"))
                for sel, kind in kinds:
                    pg.goto("%s/answers/%s/" % (base, slug))
                    settle(pg)
                    if kind == "paste":
                        pg.fill("#ai-task-paste textarea", TEXT)
                    del hits[:]
                    with pg.expect_navigation():
                        pg.locator(sel).first.click()
                    settle(pg)
                    step = "%s %s %s" % (lang, slug, kind)
                    row(step + " dest", "/exam-prep-online/" in pg.url, pg.url.replace(base, ""))
                    print("     hits:", hits)
                    form_rows(pg, step)
                    if lang == "en":
                        h = pg.locator("#task-intake h3").inner_text()
                        row(step + " form-in-english", h.isascii(), h)
                    if kind == "paste":
                        row(step + " text-carried", pg.input_value("#task-intake textarea") == TEXT)
                ctx.close()
            q = "?lang=en" if lang == "en" else ""
            for frag in ("#task-intake", "#razbor-zapros"):
                hits = []
                ctx = context(b, base, hits)
                pg = ctx.new_page()
                pg.goto(base + "/exam-prep-online/" + q + frag)
                settle(pg)
                form_rows(pg, "%s direct %s" % (lang, frag))
                print("     hits:", hits)
                ctx.close()
            # отправка
            hits = []
            ctx = context(b, base, hits)
            pg = ctx.new_page()
            pg.goto(base + "/exam-prep-online/" + q + "#task-intake")
            settle(pg)
            contact = pg.eval_on_selector_all("#task-intake input", "e=>e.length")
            print("     contact fields:", contact)
            row("%s address visible" % lang, "vladimir@podlevskikh.com" in pg.inner_text("#task-intake"))
            for sel in ("#task-mail", "#task-copy"):
                del hits[:]
                pg.evaluate("window.__ext=[]")
                pg.click(sel)
                pg.wait_for_timeout(300)
                ext = pg.evaluate("window.__ext")
                note = pg.inner_text("#task-copied")
                row("%s empty %s" % (lang, sel), bool(note) and note not in ("Скопировано", "Copied")
                    and all(x["blocked"] for x in ext) and not any("cta-book" in h for h in hits), "note=%r ext=%s hits=%s" % (note, ext, hits))
            pg.fill("#task-intake textarea", TEXT)
            del hits[:]
            pg.evaluate("window.__ext=[]")
            pg.click("#task-mail")
            pg.wait_for_timeout(400)
            ext = pg.evaluate("window.__ext")
            m = urllib.parse.unquote(ext[0]["href"]) if ext else ""
            row("%s mailto" % lang, m.startswith("mailto:vladimir@podlevskikh.com?subject=") and TEXT in m, m)
            body = pg.inner_text("#task-intake")
            row("%s mailto-fallback visible" % lang, ("не открыл" in body or "did not open" in body) and "vladimir@" in body, pg.inner_text("#task-copied"))
            pg.click("#task-copy")
            pg.wait_for_timeout(400)
            row("%s copy" % lang, pg.evaluate("navigator.clipboard.readText()") == TEXT, pg.inner_text("#task-copied"))
            book = [h for h in hits if "cta-book" in h]
            row("%s one cta-book per submission" % lang, len(book) == 1, hits)
            row("%s no text in hits" % lang, not any("SMOKETASK" in h for h in hits))
            pg.fill("#task-intake textarea", "Задача " * 285)
            row("%s long text hint" % lang, pg.locator("#task-long").is_visible(), pg.inner_text("#task-long"))
            ctx.close()
            for name, init in (("clipboard-denied", "navigator.clipboard.writeText=()=>Promise.reject(new Error('x'));"),
                               ("storage-denied", "for(const k of ['localStorage','sessionStorage'])Object.defineProperty(window,k,{get(){throw new Error('x')}});")):
                hits = []
                ctx = context(b, base, hits, init)
                pg = ctx.new_page()
                errs = []
                pg.on("pageerror", lambda e: errs.append("%s @ %s" % (e, (e.stack or "")[:300])))
                pg.goto(base + "/exam-prep-online/" + q + "#task-intake")
                settle(pg)
                pg.fill("#task-intake textarea", TEXT)
                pg.click("#task-copy")
                pg.wait_for_timeout(400)
                note = pg.inner_text("#task-copied")
                if name == "clipboard-denied":
                    row("%s %s" % (lang, name), "vladimir@" in note and not any("cta-book" in h for h in hits), note)
                else:
                    row("%s %s" % (lang, name), pg.locator("#task-intake").is_visible() and bool(note) and not any(x in e for e in errs for x in ("ai-task-paste", "/assets/site.js")),
                        "%s %s" % (note, errs))
                ctx.close()
        b.close()
    print("FAILED: %d" % len(bad))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main((sys.argv[1] if len(sys.argv) > 1 else "https://tutor.podlevskikh.com").rstrip("/")))
