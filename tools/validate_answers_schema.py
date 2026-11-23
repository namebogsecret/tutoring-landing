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
LD_RE = re.compile(r'<script\s+type="application/ld\+json"\s*>(.*?)</script>', re.S)
FAQ_VISIBLE_RE = re.compile(r'class="[^"]*\bfaq-(?:list|item)\b[^"]*"|id="faq"')
SCHEMA_CTX = ("https://schema.org", "http://schema.org", "https://schema.org/", "http://schema.org/")


def _types(node):
    t = node.get("@type")
    if t is None:
        return []
    return [str(x) for x in t] if isinstance(t, list) else [str(t)]


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
    parsed, nodes = [], []
    for i, raw in enumerate(raws, 1):
        try:
            b = json.loads(raw)
        except ValueError as e:
            errs.append("блок #%d: невалидный JSON (%s)" % (i, e))
            continue
        parsed.append(b)
        ctxs = [b] if isinstance(b, dict) else [x for x in b if isinstance(x, dict)] if isinstance(b, list) else []
        if not ctxs or any(c.get("@context") not in SCHEMA_CTX for c in ctxs):
            errs.append("блок #%d: нет @context schema.org" % i)
        nodes.extend(top_nodes(b))
    canon = [json.dumps(b, sort_keys=True, ensure_ascii=False) for b in parsed]
    for c in sorted({c for c in canon if canon.count(c) > 1}):
        errs.append("дубль идентичных script-блоков x%d: %s" % (canon.count(c), c[:60]))
    all_types = [t for n in nodes for t in _types(n)]
    for t in sorted({t for t in all_types if all_types.count(t) > 1}):
        errs.append("повтор top-level @type %s x%d" % (t, all_types.count(t)))
    ids = [n["@id"] for n in nodes if isinstance(n.get("@id"), str)]
    for i in sorted({i for i in ids if ids.count(i) > 1}):
        errs.append("повтор top-level @id %s x%d" % (i, ids.count(i)))
    has_faq_ld = "FAQPage" in all_types
    faq_visible = bool(FAQ_VISIBLE_RE.search(html))
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
