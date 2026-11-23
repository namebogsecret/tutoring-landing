#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Валидатор schema.org JSON-LD на страницах answers/**/index.html (stdlib only).

Проверяет: JSON валиден, есть @context schema.org; нет дублей script-блоков, повторов @type и @id
среди top-level узлов страницы (вложенные Question/Answer/ListItem/Offer не считаются);
FAQPage есть тогда и только тогда, когда на странице виден FAQ-блок; страница имеет Course или Service.
Запуск:  python3 tools/validate_answers_schema.py [--root DIR] [--json]
Код выхода: 0 — нарушений нет, 1 — есть нарушения.
"""
import argparse
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LD_RE = re.compile(r'<script\b[^>]*\btype\s*=\s*["\']?application/ld\+json["\']?[^>]*>(.*?)</script>', re.I | re.S)
FAQ_VISIBLE_RE = re.compile(r'class="[^"]*\bfaq-(?:list|item)\b[^"]*"|id="faq"')
COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
HIDDEN_RE = re.compile(
    r"<(\w+)\b[^>]*(?:\shidden(?=[\s>/=])|aria-hidden\s*=\s*[\"']?true|"
    r"style\s*=\s*[\"'][^\"']*display\s*:\s*none)[^>]*>.*?</\1\s*>", re.I | re.S)
SCHEMA_CTX = ("https://schema.org", "http://schema.org")


def _types(node):
    t = node.get("@type")
    if t is None:
        return []
    return [str(x) for x in t] if isinstance(t, list) else [str(t)]


def ctx_ok(ctx):
    """@context: строка, список или объект (@vocab и пр.), где встречается schema.org."""
    if isinstance(ctx, str):
        return ctx.strip().rstrip("/") in SCHEMA_CTX
    if isinstance(ctx, list):
        return any(ctx_ok(x) for x in ctx)
    if isinstance(ctx, dict):
        return any(ctx_ok(x) for x in ctx.values())
    return False


def walk_nodes(obj):
    """Все dict-узлы на любой глубине (mainEntity, @graph, вложенные списки)."""
    if isinstance(obj, dict):
        yield obj
        for v in obj.values():
            yield from walk_nodes(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from walk_nodes(v)


def visible_faq(html):
    """FAQ-маркер вне HTML-комментариев и hidden-секций."""
    h = COMMENT_RE.sub("", html)
    prev = None
    while prev != h:  # вложенные hidden
        prev, h = h, HIDDEN_RE.sub("", h)
    return bool(FAQ_VISIBLE_RE.search(h))


def top_nodes(block):
    """Top-level узлы блока: сам объект или элементы @graph / списка."""
    items = block if isinstance(block, list) else [block]
    out = []
    for it in items:
        if not isinstance(it, dict):
            continue
        if isinstance(it.get("@graph"), list):
            out.extend(n for n in it["@graph"] if isinstance(n, dict))
        else:
            out.append(it)
    return out


def check_html(html):
    """Список строк-нарушений для одного HTML."""
    errs = []
    raws = [r.strip() for r in LD_RE.findall(html)]
    mentions = html.lower().count("application/ld+json")
    if mentions != len(raws):
        errs.append("упоминаний application/ld+json %d, распознанных script-блоков %d" % (mentions, len(raws)))
    parsed, nodes = [], []
    for i, raw in enumerate(raws, 1):
        try:
            b = json.loads(raw)
        except ValueError as e:
            errs.append("блок #%d: невалидный JSON (%s)" % (i, e))
            continue
        parsed.append(b)
        ctxs = [b] if isinstance(b, dict) else [x for x in b if isinstance(x, dict)] if isinstance(b, list) else []
        if not ctxs or any(not ctx_ok(c.get("@context")) for c in ctxs):
            errs.append("блок #%d: нет @context schema.org" % i)
        nodes.extend(top_nodes(b))
    canon = [json.dumps(b, sort_keys=True, ensure_ascii=False) for b in parsed]
    for c in sorted({c for c in canon if canon.count(c) > 1}):
        errs.append("дубль идентичных script-блоков x%d: %s" % (canon.count(c), c[:60]))
    all_types = [t for n in nodes for t in _types(n)]
    for t in sorted({t for t in all_types if all_types.count(t) > 1 and t != "FAQPage"}):
        errs.append("повтор top-level @type %s x%d" % (t, all_types.count(t)))
    ids = [n["@id"] for n in nodes if isinstance(n.get("@id"), str)]
    for i in sorted({i for i in ids if ids.count(i) > 1}):
        errs.append("повтор top-level @id %s x%d" % (i, ids.count(i)))
    faq_n = sum(t == "FAQPage" for b in parsed for n in walk_nodes(b) for t in _types(n))
    if faq_n > 1:
        errs.append("повтор FAQPage x%d (включая вложенные)" % faq_n)
    has_faq_ld = faq_n > 0
    faq_visible = visible_faq(html)
    if faq_visible and not has_faq_ld:
        errs.append("FAQ виден на странице, но FAQPage нет")
    if has_faq_ld and not faq_visible:
        errs.append("FAQPage есть, но видимого FAQ-блока нет")
    if not ({"Course", "Service"} & set(all_types)):
        errs.append("нет Course или Service")
    return errs


def find_pages(root):
    base = os.path.join(root, "answers")
    out = []
    for d, _, files in os.walk(base):
        if "index.html" in files:
            out.append(os.path.join(d, "index.html"))
    return sorted(out)


def validate(root):
    """{относительный путь: [нарушения]} по всем страницам."""
    res = {}
    for f in find_pages(root):
        with open(f, encoding="utf-8") as fh:
            res[os.path.relpath(f, root)] = check_html(fh.read())
    return res


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--root", default=ROOT, help="корень сайта (содержит answers/)")
    ap.add_argument("--json", action="store_true", help="вывод в JSON")
    a = ap.parse_args(argv)
    res = validate(a.root)
    bad = {p: e for p, e in res.items() if e}
    if not res:
        bad = {"answers/": ["страницы не найдены"]}
    if a.json:
        print(json.dumps({"ok": not bad, "pages": len(res), "violations": bad}, ensure_ascii=False, indent=2))
    elif bad:
        for p, errs in bad.items():
            for e in errs:
                print("%s: %s" % (p, e))
        print("FAIL: нарушений на страницах: %d из %d" % (len(bad), len(res)))
    else:
        print("OK: %d страниц, JSON-LD без нарушений" % len(res))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
