# -*- coding: utf-8 -*-
"""Блок «Смотрите также» / «See also» на страницах-ответах: связи выводятся из реестра answer_pages.

Источник классификации — явная таблица META (n -> экзамен, предмет, тип), НЕ эвристика по slug/подстрокам:
тест требует, чтобы каждая запись реестра была в таблице.
Чистые функции: без random/времени, порядок только по ключам сортировки (детерминизм).

Запуск:  python3 seealso.py --check   — печатает граф и завершается кодом 1 при нарушении инвариантов.
"""
import sys

# n -> (exam, subjects, kind). exam: ege|igcse|ib|alevel|ap|any (профиль репетитора, без экзамена).
# subjects — через «+»; kind: landing (страница под запрос «репетитор…») | guide (сравнение/план/«как выбрать»).
META = {
    1: ("ege", "physics", "landing"), 2: ("ege", "physics", "landing"), 3: ("ege", "physics", "landing"),
    4: ("igcse", "physics", "landing"), 5: ("ib", "physics", "landing"), 6: ("ap", "physics", "landing"),
    7: ("any", "physics", "landing"), 8: ("igcse", "physics", "landing"), 9: ("ap", "physics", "landing"),
    10: ("ib", "physics", "landing"), 11: ("ege", "physics", "landing"),
    101: ("ege", "physics", "landing"), 102: ("ege", "physics", "landing"), 103: ("ege", "physics", "landing"),
    104: ("igcse", "physics", "landing"), 105: ("ib", "physics", "landing"), 106: ("ap", "physics", "landing"),
    201: ("ib", "math", "landing"), 202: ("ap", "math", "landing"), 203: ("igcse", "math", "landing"),
    301: ("ib", "math", "landing"), 302: ("ap", "math", "landing"), 303: ("igcse", "math", "landing"),
    401: ("ap", "physics", "guide"), 402: ("ib", "physics", "guide"),
    501: ("ap", "physics", "guide"), 502: ("ib", "physics", "guide"),
    403: ("ege", "physics", "guide"), 404: ("alevel", "physics", "guide"),
    503: ("ap", "physics", "guide"), 504: ("ib", "physics", "guide"),
    405: ("ege", "math", "guide"), 406: ("igcse", "physics+math", "guide"),
    407: ("ap", "physics+math", "guide"),
}

# Явные исключения: n -> n, на которые страница НЕ ссылается. Стр. 407 (AP Physics C) по решению проверяющего
# (tests/test_answer_pages.py, TestApProgramPage) не должна показывать «Physics 1/2» в видимом тексте, а подпись
# 401 = h1 «AP Physics 1, 2 и C…».
AVOID = {407: {401}}

MIN_LINKS, MAX_LINKS = 2, 4   # цель — 4; нижняя граница инварианта — 2
MAX_SAME_EXAM = 2            # из 4 ссылок не больше двух на тот же экзамен — остальное уходит в соседние экзамены
EXAM_ORDER = ("any", "ege", "igcse", "ib", "alevel", "ap")   # круг «следующего экзамена»
MAX_HOPS = 6                 # достижимость: см. обоснование в tests/test_seealso.py


def _subj(m):
    return set(m[1].split("+"))


def _tier(a_meta, c_meta):
    """0 — тот же экзамен; 1 — тот же предмет, другой экзамен; 2 — остальное."""
    if a_meta[0] == c_meta[0] and a_meta[0] != "any":
        return 0
    return 1 if _subj(a_meta) & _subj(c_meta) else 2


def build_graph(registry):
    """registry: список записей (поля n, lang, slug). Возвращает {slug: [slug соседей]} в порядке показа.
    Слоты: до MAX_SAME_EXAM ссылок на тот же экзамен (другой тип страницы — раньше), затем ОДНА ссылка
    на следующий экзамен по кругу EXAM_ORDER (она гарантирует связность графа), затем добор по приоритету
    «тот же предмет → остальное». Равные приоритеты решает меньшее число входящих ссылок, затем меньший n."""
    missing = [a["n"] for a in registry if a["n"] not in META]
    if missing:
        raise KeyError("seealso.META: нет записи для n=%s" % missing)
    indeg = {a["slug"]: 0 for a in registry}
    graph = {}
    for a in sorted(registry, key=lambda r: (r["lang"], r["n"])):
        am = META[a["n"]]
        cands = [c for c in registry if c["lang"] == a["lang"] and c["slug"] != a["slug"]
                 and c["n"] not in AVOID.get(a["n"], ())]

        def key(c, am=am):
            cm = META[c["n"]]
            return (_tier(am, cm), cm[2] == am[2], indeg[c["slug"]], c["n"])
        cands.sort(key=key)
        picked = [c for c in cands if _tier(am, META[c["n"]]) == 0][:MAX_SAME_EXAM]
        present = [e for e in EXAM_ORDER if any(META[c["n"]][0] == e for c in cands) or e == am[0]]
        nxt = present[(present.index(am[0]) + 1) % len(present)]
        bridge = [c for c in cands if META[c["n"]][0] == nxt and c not in picked]
        if bridge and nxt != am[0]:
            picked.append(bridge[0])
        picked += [c for c in cands if c not in picked]
        picked = picked[:MAX_LINKS]
        graph[a["slug"]] = [c["slug"] for c in picked]
        for c in picked:
            indeg[c["slug"]] += 1
    return graph


def hops(graph, src):
    """Число шагов от src до каждой достижимой страницы (BFS)."""
    dist, frontier = {src: 0}, [src]
    while frontier:
        nxt = []
        for s in frontier:
            for t in graph[s]:
                if t not in dist:
                    dist[t] = dist[s] + 1
                    nxt.append(t)
        frontier = nxt
    return dist


def violations(registry, graph):
    bad = []
    slugs = {a["slug"]: a for a in registry}
    for s, nb in graph.items():
        if s not in slugs:
            bad.append("страница не из реестра: %s" % s)
        if s in nb:
            bad.append("самоссылка: %s" % s)
        if len(set(nb)) != len(nb):
            bad.append("дубль соседа: %s" % s)
        if not MIN_LINKS <= len(nb) <= MAX_LINKS:
            bad.append("соседей %d у %s" % (len(nb), s))
        for t in nb:
            if t not in slugs:
                bad.append("битая ссылка %s -> %s" % (s, t))
            elif slugs[t]["lang"] != slugs[s]["lang"]:
                bad.append("смешение lang: %s -> %s" % (s, t))
    return bad


def seealso_html(a, registry):
    """HTML блока для записи a (относительные ссылки, подписи — h1 реестра, без атрибутов метрики)."""
    ru = a["lang"] == "ru"
    by_slug = {r["slug"]: r for r in registry}
    items = "".join('<li><a href="/answers/%s/">%s</a></li>' % (s, by_slug[s]["h1"])
                    for s in build_graph(registry)[a["slug"]])
    return ('<div class="seealso" data-seealso>\n<h2 id="seealso">%s</h2>\n<ul>%s</ul>\n</div>'
            % ("Смотрите также" if ru else "See also", items))


def main(argv):
    import answer_pages as AP
    reg = AP.ANSWERS + AP.ANSWERS_EN + AP.ANSWERS_MATH + AP.ANSWERS_PHYS
    g = build_graph(reg)
    for s, nb in g.items():
        print("%s -> %s" % (s, ", ".join(nb)))
    bad = violations(reg, g)
    for lang in ("ru", "en"):
        group = [a["slug"] for a in reg if a["lang"] == lang]
        for s in group:
            d = hops(g, s)
            far = [t for t in group if t not in d or d[t] > MAX_HOPS]
            if far:
                bad.append("недостижимо за %d шагов из %s: %s" % (MAX_HOPS, s, far))
    for b in bad:
        print("НАРУШЕНИЕ:", b)
    return 1 if bad and "--check" in argv else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
