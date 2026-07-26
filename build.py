#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build.py — wraps page-body fragments (src/*.html) in shared chrome
(head + nav + footer + JSON-LD) and writes them to their final GitHub-Pages
paths. Single source of truth for the content layer's nav/footer/meta.

Run:  python3 build.py        → regenerates every content page + sitemap.xml
The homepage (index.html) is hand-maintained and NOT touched here.
"""
import json, os, re, datetime
from pages_registry import NETWORK_SITES

BASE = "https://tutor.podlevskikh.com"
HERE = os.path.dirname(os.path.abspath(__file__))
TODAY = "2026-06-14"

# ── shared nav ───────────────────────────────────────────────────────────
def nav():
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
def footer(lang):
    progr = "Programmes" if lang == "en" else "Программы"
    res = "Resources" if lang == "en" else "Ресурсы"
    cont = "Get in touch" if lang == "en" else "Связаться"
    loc = ("Online worldwide · Based in Yerevan, Armenia (GMT+4)"
           if lang == "en" else
           "Онлайн по всему миру · Ереван, Армения (GMT+4)")
    return f"""<footer class="footer band">
  <div class="wrap" style="display:grid;grid-template-columns:1.4fr 1fr 1fr;gap:40px 32px;padding-block:56px;">
    <div>
      <div class="brand" style="margin-bottom:14px;">
        <span class="brand-mark">VP</span>
        <span class="brand-name"><b>Vladimir Podlevskikh</b></span>
      </div>
      <p style="color:var(--muted);font-size:14.5px;max-width:42ch;line-height:1.6;">
        MSU physicist · 23+ years · 350+ students · perfect 200/200 on both US Praxis Physics &amp; Maths.
        Structured online preparation for IB, AP, SAT, A-Level, IGCSE &amp; ЕГЭ.
      </p>
    </div>
    <div>
      <div class="toc-lbl" style="margin-bottom:14px;">{progr}</div>
      <div style="display:grid;gap:9px;font-size:14px;">
        <a href="/ib-physics-tutor/" style="color:var(--muted);">IB Physics Tutor</a>
        <a href="/ap-physics-tutor/" style="color:var(--muted);">AP Physics Tutor</a>
        <a href="/physics-tutor-online/" style="color:var(--muted);">Репетитор по физике онлайн</a>
        <a href="/ege-physics/" style="color:var(--muted);">Подготовка к ЕГЭ по физике</a>
        <a href="/olympiad-physics/" style="color:var(--muted);">Подготовка к олимпиадам</a>
        <a href="/russian-tutor-abroad/" style="color:var(--muted);">Русскоязычным за рубежом</a>
      </div>
    </div>
    <div>
      <div class="toc-lbl" style="margin-bottom:14px;">{res}</div>
      <div style="display:grid;gap:9px;font-size:14px;">
        <a href="/blog/" style="color:var(--muted);">Blog &amp; method articles</a>
        <a href="https://calculators.podlevskikh.com" target="_blank" rel="noopener" style="color:var(--muted);">Physics calculators ↗</a>
        <a href="https://olymp.podlevskikh.com" target="_blank" rel="noopener" style="color:var(--muted);">Olympiad knowledge base ↗</a>
        <a data-cta="mainsite" href="https://podlevskikh.com" style="color:var(--muted);">podlevskikh.com ↗</a>
      </div>
      <div class="toc-lbl" style="margin:22px 0 12px;">{cont}</div>
      <div style="display:grid;gap:9px;font-size:14px;">
        <a class="btn btn-primary btn-sm" data-cta="calendly" href="#" style="justify-content:center;">📅 Book a free diagnostic</a>
        <div style="display:flex;gap:14px;margin-top:4px;">
          <a data-cta="telegram" href="#" style="color:var(--muted);">Telegram</a>
          <a data-cta="whatsapp" href="#" style="color:var(--muted);">WhatsApp</a>
          <a data-cta="email" data-subject="Tutoring enquiry" href="#" style="color:var(--muted);">Email</a>
        </div>
      </div>
    </div>
    <div class="loc" style="grid-column:1/-1;">© <span data-year>2026</span> Vladimir Podlevskikh · {loc} · Last updated: <time datetime="2026-06">June 2026</time></div>
  </div>
</footer>""" + net_band()

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

# ── page assembly ────────────────────────────────────────────────────────
def build_page(p):
    body = open(os.path.join(HERE, p["body"]), encoding="utf-8").read()
    faq_html = render_faq(p.get("faq"), p.get("faq_heading", "Questions families ask"))
    body = body.replace("{{FAQ}}", faq_html)

    head_extra = []
    for j in p.get("jsonld", []):
        head_extra.append('<script type="application/ld+json">\n' + json.dumps(j, ensure_ascii=False, indent=2) + '\n</script>')
    fq = faq_jsonld(p.get("faq"))
    if fq:
        head_extra.append(fq)
    head_extra.append(breadcrumb_jsonld(p["crumbs"]))
    head_extra = "\n".join(head_extra)

    canonical = BASE + p["url"]
    html_lang = p["lang"]
    favicon = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E"
               "%3Crect width='64' height='64' rx='8' fill='%23f6f3ec'/%3E%3Crect x='3' y='3' width='58' height='58' rx='6'"
               " fill='none' stroke='%239a7724' stroke-width='2'/%3E%3Ctext x='32' y='43' font-family='Georgia,serif'"
               " font-size='28' font-weight='600' fill='%239a7724' text-anchor='middle'%3EVP%3C/text%3E%3C/svg%3E")

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
<link rel="icon" href="{favicon}" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Hanken+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="/assets/site.css" />
<link rel="stylesheet" href="/assets/content.css" />
<noscript><style>.reveal{{opacity:1!important;transform:none!important;}}</style></noscript>
</head>
<body>

{nav()}

{render_crumbs(p['crumbs'])}

{body}

{footer(html_lang)}

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
    rows = [('/', '1.0', 'monthly')]
    for u in urls:
        pr = '0.9' if u.count('/') <= 2 else '0.7'
        rows.append((u, pr, 'monthly'))
    body = "\n".join(
        f"  <url>\n    <loc>{BASE}{u}</loc>\n    <lastmod>{TODAY}</lastmod>"
        f"\n    <changefreq>{cf}</changefreq>\n    <priority>{pr}</priority>\n  </url>"
        for u, pr, cf in rows)
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           + body + "\n</urlset>\n")
    open(os.path.join(HERE, "sitemap.xml"), "w", encoding="utf-8").write(xml)

if __name__ == "__main__":
    built = []
    for p in PAGES:
        built.append(build_page(p))
        print("✓", p["url"])
    build_sitemap(built)
    print("✓ sitemap.xml (%d urls + home)" % len(built))
