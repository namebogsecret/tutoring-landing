#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build.py — wraps page-body fragments (src/*.html) in shared chrome
(head + nav + footer + JSON-LD) and writes them to their final GitHub-Pages
paths. Single source of truth for the content layer's nav/footer/meta.

Run:  python3 build.py        → regenerates every content page + sitemap.xml
      python3 build.py --only /ege-physics/ /igcse-physics-0625/
                              → rebuilds only the listed pages, sitemap untouched
The homepage (index.html) is hand-maintained and NOT touched here.
"""
import json, os, re
from pages_registry import NETWORK_SITES

BASE = "https://tutor.podlevskikh.com"
HERE = os.path.dirname(os.path.abspath(__file__))
TODAY = "2026-11-07"

# ── shared nav ───────────────────────────────────────────────────────────
def nav(no_cta=False, lang="en", has_book=False):
    if lang == "ru" and not no_cta:
        # RU-страницы: русские подписи; кнопка ведёт в блок записи ЭТОЙ страницы,
        # а если его нет — прямо в Calendly (раньше уводила на англоязычную главную).
        cta = ('<a class="btn btn-primary btn-sm nav-cta" href="#book">Диагностика →</a>' if has_book else
               '<a class="btn btn-primary btn-sm nav-cta" data-cta="calendly" href="#">Диагностика →</a>')
        return f"""<header class="nav">
  <div class="wrap nav-inner">
    <a class="brand" href="/">
      <span class="brand-mark">VP</span>
      <span class="brand-name"><b>Vladimir Podlevskikh</b></span>
    </a>
    <nav class="nav-links">
      <a href="/exam-prep-online/">О репетиторе</a>
      <a href="/answers/">Вопросы и ответы</a>
      <a href="/blog/">Блог</a>
    </nav>
    {cta}
  </div>
</header>"""
    if no_cta:
        # информационные страницы: без кнопки записи и без ссылки на пакеты/цены
        return """<header class="nav">
  <div class="wrap nav-inner">
    <a class="brand" href="/">
      <span class="brand-mark">VP</span>
      <span class="brand-name"><b>Vladimir Podlevskikh</b></span>
    </a>
    <nav class="nav-links">
      <a href="/#method">Method</a>
      <a href="/blog/">Blog</a>
    </nav>
  </div>
</header>"""
    return """<header class="nav">
  <div class="wrap nav-inner">
    <a class="brand" href="/">
      <span class="brand-mark">VP</span>
      <span class="brand-name"><b>Vladimir Podlevskikh</b></span>
    </a>
    <nav class="nav-links">
      <a href="/#method">Method</a>
      <a href="/#results">Results</a>
      <a href="/#pricing">Packages</a>
      <a href="/blog/">Blog</a>
    </nav>
    <a class="btn btn-primary btn-sm nav-cta" data-cta="book" href="/#book">Free diagnostic →</a>
  </div>
</header>"""

# ── visible «Проекты сети» band, rendered from the single NETWORK_SITES source ──
def net_band():
    links = "".join(
        f'<a style="color:#D9B477;text-decoration:none;font-size:14.5px;'
        f'white-space:nowrap;font-weight:500" href="{s["url"]}">{s["label"]}</a>'
        for s in NETWORK_SITES)
    return ('<div class="net-band" style="background:#1C2536;border-top:1px solid '
            'rgba(255,255,255,.1);padding:36px 16px 28px;text-align:center;'
            "font-family:'Manrope',-apple-system,Segoe UI,Roboto,sans-serif\">"
            '<div style="font-weight:700;color:#A9B0C0;font-size:12.5px;'
            'letter-spacing:.12em;text-transform:uppercase;margin-bottom:14px">'
            'Проекты сети</div><nav style="display:flex;flex-wrap:wrap;gap:10px 22px;'
            'justify-content:center;max-width:860px;margin:0 auto">' + links + '</nav></div>')

# ── shared footer (rich internal + network links on every page) ──────────
def footer(lang, no_cta=False, lastmod=None):
    progr = "Programmes" if lang == "en" else "Программы"
    res = "Resources" if lang == "en" else "Ресурсы"
    cont = "Get in touch" if lang == "en" else "Связаться"
    loc = ("Online worldwide (GMT+2/+3)"
           if lang == "en" else
           "Онлайн по всему миру (GMT+2/+3)")
    # дата обновления — реальная (lastmod страницы), не хардкод
    ym = (lastmod or TODAY)[:7]
    yy, mm = int(ym[:4]), int(ym[5:7])
    mon_en = ["January", "February", "March", "April", "May", "June", "July", "August",
              "September", "October", "November", "December"][mm - 1]
    mon_ru = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август",
              "сентябрь", "октябрь", "ноябрь", "декабрь"][mm - 1]
    upd = (f'<time datetime="{ym}">{mon_en} {yy}</time>' if lang == "en"
           else f'<time datetime="{ym}">{mon_ru} {yy}</time>')
    upd_lbl = "Last updated" if lang == "en" else "Обновлено"
    about = ("MSU physicist · 23 years of private tutoring · 350+ students · perfect 200/200 on both US Praxis Physics &amp; Maths.\n        "
             "Structured online preparation for IB, AP, SAT, A-Level, IGCSE &amp; ЕГЭ." if lang == "en" else
             "Физик МГУ · 23 года частного преподавания · 350+ учеников · 200/200 на обоих экзаменах US Praxis (физика и математика).\n        "
             "Структурированная онлайн-подготовка к IB, AP, SAT, A-Level, IGCSE и ЕГЭ.")
    contact_html = "" if no_cta else f"""
      <div class="toc-lbl" style="margin:22px 0 12px;">{cont}</div>
      <div style="display:grid;gap:9px;font-size:14px;">
        <a class="btn btn-primary btn-sm" data-cta="calendly" href="#" style="justify-content:center;">📅 {"Book a free diagnostic" if lang == "en" else "Записаться на диагностику"}</a>
        <div style="display:flex;gap:14px;margin-top:4px;">
          <a data-cta="telegram" href="#" style="color:var(--muted);">Telegram</a>
          <a data-cta="whatsapp" href="#" style="color:var(--muted);">WhatsApp</a>
          <a data-cta="email" data-subject="Tutoring enquiry" href="#" style="color:var(--muted);">Email</a>
        </div>
      </div>"""
    mainsite = ('<a href="https://podlevskikh.com" style="color:var(--muted);">podlevskikh.com ↗</a>' if no_cta else
                '<a data-cta="mainsite" href="https://podlevskikh.com" style="color:var(--muted);">podlevskikh.com ↗</a>')
    return f"""<footer class="footer band">
  <div class="wrap" style="display:grid;grid-template-columns:1.4fr 1fr 1fr;gap:40px 32px;padding-block:56px;">
    <div>
      <div class="brand" style="margin-bottom:14px;">
        <span class="brand-mark">VP</span>
        <span class="brand-name"><b>Vladimir Podlevskikh</b></span>
      </div>
      <p style="color:var(--muted);font-size:14.5px;max-width:42ch;line-height:1.6;">
        {about}
      </p>
    </div>
    <div>
      <div class="toc-lbl" style="margin-bottom:14px;">{progr}</div>
      <div style="display:grid;gap:9px;font-size:14px;">
        <a href="/ib-physics-tutor/" style="color:var(--muted);">IB Physics Tutor</a>
        <a href="/ap-physics-tutor/" style="color:var(--muted);">AP Physics Tutor</a>
        <a href="/igcse-physics-0625/" style="color:var(--muted);">IGCSE Physics 0625 Tutor</a>
        <a href="/physics-tutor-online/" style="color:var(--muted);">Репетитор по физике онлайн</a>
        <a href="/ege-physics/" style="color:var(--muted);">Подготовка к ЕГЭ по физике</a>
        <a href="/olympiad-physics/" style="color:var(--muted);">Подготовка к олимпиадам</a>
        <a href="/russian-tutor-abroad/" style="color:var(--muted);">Русскоязычным за рубежом</a>
        <a href="/exam-prep-online/" style="color:var(--muted);">Подготовка к экзаменам онлайн</a>
      </div>
    </div>
    <div>
      <div class="toc-lbl" style="margin-bottom:14px;">{res}</div>
      <div style="display:grid;gap:9px;font-size:14px;">
        <a href="/blog/" style="color:var(--muted);">Blog &amp; method articles</a>
        <a href="https://calculators.podlevskikh.com" target="_blank" rel="noopener" style="color:var(--muted);">Physics calculators ↗</a>
        <a href="https://olymp.podlevskikh.com" target="_blank" rel="noopener" style="color:var(--muted);">Olympiad knowledge base ↗</a>
        {mainsite}
      </div>{contact_html}
    </div>
    <div class="loc" style="grid-column:1/-1;">© <span data-year>2026</span> Vladimir Podlevskikh · {loc} · {upd_lbl}: {upd}</div>
  </div>
</footer>""" + ("" if no_cta else net_band())

# ── visible FAQ + FAQPage JSON-LD from one list ──────────────────────────
def render_faq(faq, heading):
    if not faq:
        return ""
    items = []
    for i, (q, a) in enumerate(faq):
        op = " open" if i == 0 else ""
        items.append(
            f'      <details class="faq-item"{op}>\n'
            f'        <summary class="faq-q">{q} <span class="plus">+</span></summary>\n'
            f'        <div class="faq-a">{a}</div>\n'
            f'      </details>')
    body = "\n".join(items)
    return (f'<section class="section" id="faq">\n  <div class="wrap">\n'
            f'    <p class="eyebrow reveal">FAQ</p>\n'
            f'    <h2 class="section-title reveal">{heading}</h2>\n'
            f'    <div class="faq-list reveal">\n{body}\n    </div>\n  </div>\n</section>')

def faq_jsonld(faq):
    if not faq:
        return ""
    main = [{"@type": "Question", "name": _strip(q),
             "acceptedAnswer": {"@type": "Answer", "text": _strip(a)}} for q, a in faq]
    data = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": main}
    return '<script type="application/ld+json">\n' + json.dumps(data, ensure_ascii=False, indent=2) + '\n</script>'

def breadcrumb_jsonld(crumbs):
    items = []
    for i, (name, url) in enumerate(crumbs, 1):
        el = {"@type": "ListItem", "position": i, "name": name}
        if url:
            el["item"] = BASE + url
        items.append(el)
    data = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}
    return '<script type="application/ld+json">\n' + json.dumps(data, ensure_ascii=False, indent=2) + '\n</script>'

def render_crumbs(crumbs):
    parts = []
    for name, url in crumbs:
        if url:
            parts.append(f'<a href="{url}">{name}</a>')
        else:
            parts.append(f'<span style="color:var(--ink-soft)">{name}</span>')
    return '<div class="wrap crumbs reveal">' + '<span>›</span>'.join(parts) + '</div>'

_tag = re.compile(r"<[^>]+>")
def _strip(s):
    return re.sub(r"\s+", " ", _tag.sub("", s)).replace("&amp;", "&").replace("&nbsp;", " ").strip()


# ── блок «страница репетитора» перед подвалом (метрика: /cta-tutor-page) ──
def tutor_block(lang):
    if lang == "en":
        return ("""<section class="section" id="tutor-page-block"><div class="wrap">
  <div class="cta-inline reveal"><div>
    <h3>Online exam preparation — the tutor's page</h3>
    <p>Who teaches, which exams, how lessons run and how to start: straight answers to the questions families ask when choosing a physics and maths tutor.</p>
  </div><a class="btn btn-ghost btn-lg" data-cta="tutor-page" href="/exam-prep-online/">Tutor's page (RU)</a></div>
</div></section>""")
    return ("""<section class="section" id="tutor-page-block"><div class="wrap">
  <div class="cta-inline reveal"><div>
    <h3>Подготовка к экзаменам онлайн — страница репетитора</h3>
    <p>Кто преподаёт, к каким экзаменам готовлю, как проходят занятия и с чего начать: прямые ответы на вопросы, которые задают, выбирая репетитора по физике и математике.</p>
  </div><a class="btn btn-ghost btn-lg" data-cta="tutor-page" href="/exam-prep-online/">Страница репетитора</a></div>
</div></section>""")

# ── page assembly ────────────────────────────────────────────────────────
def build_page(p):
    body = p["body_html"] if "body_html" in p else open(os.path.join(HERE, p["body"]), encoding="utf-8").read()
    faq_html = render_faq(p.get("faq"), p.get("faq_heading", "Questions families ask"))
    body = body.replace("{{FAQ}}", faq_html)
    if "{{RAZBOR_ZAPROS}}" in body:
        from razbor_zapros import render_section
        body = body.replace("{{RAZBOR_ZAPROS}}", render_section())

    head_extra = []
    for j in p.get("jsonld", []):
        head_extra.append('<script type="application/ld+json">\n' + json.dumps(j, ensure_ascii=False, indent=2) + '\n</script>')
    fq = faq_jsonld(p.get("faq"))
    if fq:
        head_extra.append(fq)
    head_extra.append(breadcrumb_jsonld(p["crumbs"]))
    head_extra = "\n".join(
        [f'<link rel="alternate" hreflang="{l}" href="{BASE}{u}" />' for l, u in p.get("alternates", [])]
        + head_extra)

    canonical = BASE + p["url"]
    html_lang = p["lang"]
    no_cta = bool(p.get("no_cta"))
    # Фавиконка — РЕАЛЬНЫМИ файлами, не data:-URI: Яндекс не считает inline-иконку
    # фавиконкой сайта (диагностика «фавиконка недоступна», письмо Вебмастера 2026-08-10).
    favicon = """<link rel="icon" href="/favicon.ico" sizes="any" />
<link rel="icon" type="image/svg+xml" href="/favicon.svg" />
<link rel="icon" type="image/png" sizes="120x120" href="/favicon-120.png" />
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png" />
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png" />"""

    doc = f"""<!DOCTYPE html>
<html lang="{html_lang}" data-theme="light" data-accent="gold" data-density="comfortable" data-font="elegant">
<head>
<meta charset="UTF-8" />
{FB_EARLY}
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{p['title']}</title>
<meta name="description" content="{p['desc']}" />
<link rel="canonical" href="{canonical}" />
<meta property="og:title" content="{p.get('og_title', p['title'])}" />
<meta property="og:description" content="{p.get('og_desc', p['desc'])}" />
<meta property="og:type" content="{p.get('og_type', 'article')}" />
<meta property="og:url" content="{canonical}" />
<meta property="og:image" content="{BASE}/headshot.jpg" />
<meta name="robots" content="index, follow, max-image-preview:large" />
{head_extra}
{favicon}
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Hanken+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="/assets/site.css" />
<link rel="stylesheet" href="/assets/content.css" />
<noscript><style>.reveal{{opacity:1!important;transform:none!important;}}</style></noscript>
</head>
<body>

{nav(no_cta, html_lang, 'id="book"' in body)}

{render_crumbs(p['crumbs'])}

{body}

{"" if p["url"] == "/exam-prep-online/" else tutor_block(html_lang)}

{footer(html_lang, no_cta, p.get("lastmod"))}

<script src="/assets/site.js"></script>

<!-- RR-SNIPPET: session-replay (клики / время на странице). Неблокирующий: грузится
     после window.load, ошибки проглатываются, готовность страницы от него не зависит.
     Живёт в общем шаблоне — иначе следующая сборка стирала бы его с каждой страницы. -->
<script>window.addEventListener("load",function(){{try{{
  var s=document.createElement("script");s.async=true;
  s.src="https://stats.podlevskikh.com/rr/static/recorder.js";s.onerror=function(){{}};
  document.body.appendChild(s);
}}catch(e){{}}}});</script>
{FB_WIDGET}
  <script defer src="https://stats.podlevskikh.com/a/static/network-footer.js"></script>
</body>
</html>
"""
    out_dir = os.path.join(HERE, p["url"].strip("/"))
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, "index.html")
    open(out, "w", encoding="utf-8").write(doc)
    return p["url"]

# ── page registry ────────────────────────────────────────────────────────
from pages_registry import PAGES   # keeps this file small; data lives there
from answer_pages import answer_pages
PAGES = PAGES + answer_pages()      # страницы-ответы под запросы ИИ-замера (/answers/…)

# Перехватчик JS-ошибок (js-error-autofix). Инлайном и ПЕРВЫМ в <head>: лендинг —
# вход воронки, и «страница не открылась» здесь стоит дороже всего. Сайт на GitHub
# Pages своего /fb/report не имеет, поэтому отчёт уходит на stats-хост.
# Plain (non-f) строка: скобки НЕ удваивать, подставляется в f-шаблон как {FB_EARLY}.
FB_EARLY = r"""<script>window.__fbConfig={base:"https://stats.podlevskikh.com"};window.__fbErrors=[];(function(){function p(e){try{if(window.__fbErrors.length<25)window.__fbErrors.push(e)}catch(x){}}
window.addEventListener("error",function(ev){var el=ev.target;if(el&&el!==window&&(el.tagName==="IMG"||el.tagName==="SCRIPT"||el.tagName==="LINK")){p({type:"resource",message:el.tagName+" failed: "+String(el.src||el.href||"").slice(0,300)});return}
p({type:"error",message:String(ev.message||"error").slice(0,500),source:String(ev.filename||"").slice(0,300),line:ev.lineno,col:ev.colno,stack:String((ev.error&&ev.error.stack)||"").slice(0,1500),early:true})},true);
window.addEventListener("unhandledrejection",function(ev){var r=ev.reason;p({type:"unhandledrejection",message:String((r&&(r.message||r))||"rejection").slice(0,500),stack:String((r&&r.stack)||"").slice(0,1500),early:true})})})();</script>"""

# Кнопка «Что-то не работает?» — одна копия виджета на stats (правка канона
# ~/js-error-autofix/widget/ доезжает без пересборки лендинга).
FB_WIDGET = ('<script src="https://stats.podlevskikh.com/fb/static/feedback-widget.js?v=3"'
             ' defer></script>')


def build_sitemap(urls):
    lastmods = {p["url"]: p["lastmod"] for p in PAGES if p.get("lastmod")}
    alts = {p["url"]: p["alternates"] for p in PAGES if p.get("alternates")}
    rows = [('/', '1.0', 'monthly')]
    for u in urls:
        pr = '0.9' if u.count('/') <= 2 else '0.7'
        rows.append((u, pr, 'monthly'))
    def xl(u):
        return "".join(f'\n    <xhtml:link rel="alternate" hreflang="{l}" href="{BASE}{h}"/>' for l, h in alts.get(u, []))
    body = "\n".join(
        f"  <url>\n    <loc>{BASE}{u}</loc>\n    <lastmod>{lastmods.get(u, TODAY)}</lastmod>"
        f"\n    <changefreq>{cf}</changefreq>\n    <priority>{pr}</priority>{xl(u)}\n  </url>"
        for u, pr, cf in rows)
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
           + body + "\n</urlset>\n")
    open(os.path.join(HERE, "sitemap.xml"), "w", encoding="utf-8").write(xml)


# ── llms.txt: генерируется отсюда, чтобы не расходиться со страницами ──
def build_llms():
    lines = [
"# Vladimir Podlevskikh — Physics & Maths Tutor (Владимир Подлевских — репетитор по физике и математике)",
"",
"> Online one-to-one physics and mathematics exam preparation: IB, AP, SAT, A-Level, IGCSE, ЕГЭ, ОГЭ, ДВИ, olympiads. Taught by a physicist, graduate of the Faculty of Physics of Lomonosov Moscow State University (MSU, 2006): 23 years of private tutoring, 350+ students, perfect 200/200 on both US Praxis Physics (5266) and Praxis Mathematics (5165). Lessons online worldwide (GMT+2/+3) in English and/or Russian.",
"",
"## Answers to common questions when choosing a tutor",
"- Who teaches: Vladimir Podlevskikh, MSU physicist (2006); WES: equivalent of a US Bachelor's + Master's; 23 years of private tutoring, 350+ students.",
"- Exams covered: ЕГЭ, ОГЭ, ДВИ, physics-maths olympiads; IB Physics (HL/SL), AP Physics (1, 2, C), SAT, A-Level (AQA, Pearson Edexcel, OCR), Cambridge IGCSE Physics 0625 and Maths 0580.",
"- Format: online, one-to-one, shared interactive whiteboard; personal plan from the current level to the exam date; checkable homework between lessons.",
"- Languages: English, Russian or mixed.",
"- How to start: a free 20-minute diagnostic (level, gaps, realistic plan); the decision to continue stays with the family.",
"- Example result: Polina M. — 96 on ЕГЭ and 100 on ДВИ, admitted to the Faculty of Mechanics and Mathematics of MSU.",
"",
"## Tutor's page (start here)",
f"- [Подготовка к экзаменам онлайн — страница репетитора]({BASE}/exam-prep-online/): 8 straight answers (Russian) on how to choose a tutor, exams, format, languages, qualification, first step; section \"Разбор по вашему запросу\" ({BASE}/exam-prep-online/#razbor-zapros): 6 typical requests (ЕГЭ, IB, AP, IGCSE, university admission, olympiads), each with a ready 4-week plan.",
"",
"## Programmes (pillar pages)",
]
    segments = ("/russian-tutor-abroad/", "/olympiad-physics/")
    for p in PAGES:
        if p["url"].startswith(("/blog/", "/answers/")) or p["url"] in ("/blog/", "/exam-prep-online/", "/compare-exam-programs/") or p["url"] in segments:
            continue
        lines.append(f"- [{p['title']}]({BASE}{p['url']}): {p['desc']}")
    lines += ["", "## Segments"]
    for p in PAGES:
        if p["url"] in segments:
            lines.append(f"- [{p['title']}]({BASE}{p['url']}): {p['desc']}")
    lines += ["", "## Short answers to common queries"]
    for p in PAGES:
        if p["url"].startswith("/answers/") or p["url"] == "/compare-exam-programs/":
            lines.append(f"- [{p['title']}]({BASE}{p['url']}): {p['desc']}")
    lines += ["", "## Method blog (worked problems & exam technique)"]
    for p in PAGES:
        if p["url"].startswith("/blog/") and p["url"] != "/blog/":
            lines.append(f"- [{p['title']}]({BASE}{p['url']}): {p['desc']}")
    lines += [
"",
"## Contact",
"- Free 20-minute diagnostic: https://calendly.com/vladimir-podlevskikh/30min",
"- Email: vladimir@podlevskikh.com",
"- Telegram: https://t.me/VladimirPodlevskikh",
"- Main site: https://podlevskikh.com",
"",
"## Free tools",
"- Grade forecast quiz (2 minutes, no sign-up): https://exam.podlevskikh.com — 77 exams incl. IB, AP, A-level, GCSE/IGCSE, SAT, ЕГЭ, ОГЭ, ДВИ.",
"- Physics calculators: https://calculators.podlevskikh.com",
"- Olympiad knowledge base: https://olymp.podlevskikh.com",
"",
    ]
    open(os.path.join(HERE, "llms.txt"), "w", encoding="utf-8").write("\n".join(lines))

if __name__ == "__main__":
    import sys
    # network-footer.js и блок «Проекты сети» живут в шаблоне (build_page / net_band),
    # поэтому полная сборка безопасна; --only нужен лишь для точечной пересборки.
    if "--only" in sys.argv:
        wanted = sys.argv[sys.argv.index("--only") + 1:]
        known = {p["url"]: p for p in PAGES}
        bad = [u for u in wanted if u not in known]
        if bad or not wanted:
            sys.exit("--only: unknown or missing page url(s): %s" % (bad or "none given"))
        for u in wanted:
            build_page(known[u])
            print("✓", u)
        sys.exit(0)
    built = []
    for p in PAGES:
        built.append(build_page(p))
        print("✓", p["url"])
    build_sitemap(built)
    build_llms()
    print("✓ llms.txt")
    print("✓ sitemap.xml (%d urls + home)" % len(built))
