# -*- coding: utf-8 -*-
"""Блок «Смотрите также» / «See also» на страницах-ответах: связи выводятся из реестра answer_pages.

Источник классификации — явная таблица META (n -> экзамен, предмет, тип), НЕ эвристика по slug/подстрокам:
тест требует, чтобы каждая запись реестра была в таблице.
Чистые функции: без random/времени, порядок только по ключам сортировки (детерминизм).

Запуск:  python3 seealso.py --check   — печатает граф и завершается кодом 1 при нарушении инвариантов.
"""
import html
import sys

# n -> (exam, subjects, kind). exam: ege|igcse|ib|alevel|ap|sat|any (профиль репетитора, без экзамена).
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
    # 408 (олимпиадная физика, техвузы) и 410 (UCAS/Oxford/Cambridge): h1 не называет экзамен → any
    # (тест test_meta_labels_match_registry_h1 сверяет метку с h1).
    408: ("any", "physics", "guide"), 410: ("any", "physics", "guide"),
    # 411/412: AP (математика); 413 (ОГЭ) и 414 (GCSE): h1 не называет ни один из экзаменов EXAM_ORDER → any
    411: ("ap", "math", "landing"), 412: ("ap", "math", "landing"),
    413: ("any", "physics", "landing"), 414: ("any", "physics", "landing"),
    # 415/418: A-level (математика); 416 (STEP): h1 экзамен из EXAM_ORDER не называет → any; 417: AP (математика)
    415: ("alevel", "math", "landing"), 416: ("any", "math", "landing"),
    417: ("ap", "math", "landing"), 418: ("alevel", "math", "landing"),
    409: ("sat", "physics+math", "guide"),       # SAT Math + ACT Science (естествознание → physics); оба экзамена в одном кластере «sat»
}

# Явные исключения: n -> n, на которые страница НЕ ссылается. Стр. 407 (AP Physics C) по решению проверяющего
# (tests/test_answer_pages.py, TestApProgramPage) не должна показывать «Physics 1/2» в видимом тексте, а подпись
# 401 = h1 «AP Physics 1, 2 и C…».
# Стр. 201 (IB Math AA) по тесту TestMathPages не должна содержать дат 2027+ в видимом тексте (нет «дат перехода»),
# а h1 403/405 содержат «2027».
AVOID = {407: {401}, 201: {403, 405}}

MIN_LINKS, MAX_LINKS = 2, 4   # цель — 4; нижняя граница инварианта — 2
MAX_SAME_EXAM = 2            # из 4 ссылок не больше двух на тот же экзамен (больше — только если других кандидатов не хватает)
MIN_SAME_SUBJECT = 2         # гарантия предмета: минимум столько ссылок на тот же предмет, если они есть в lang
EXAM_ORDER = ("any", "ege", "igcse", "ib", "alevel", "ap", "sat")   # круг «следующего экзамена»
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
    Слоты по порядку (везде первыми идут страницы того же предмета, затем другой тип страницы, затем меньше
    входящих ссылок, затем меньший n):
      1. до MAX_SAME_EXAM ссылок на тот же экзамен И тот же предмет;
      2. ОДНА ссылка на следующий экзамен по кругу EXAM_ORDER (гарантирует связность графа);
      3. гарантия предмета: до MIN_SAME_SUBJECT ссылок на КАЖДЫЙ предмет страницы (другие экзамены), если они есть
         в lang — страница по математике получает математические ссылки, а не только физические;
      4. тот же экзамен, другой предмет — пока ссылок на тот же экзамен меньше MAX_SAME_EXAM;
      5. добор из ДРУГИХ экзаменов (тот же предмет раньше), и только затем — из того же экзамена.
    Точное правило потолка: ссылок на тот же экзамен (кроме «any») не больше MAX_SAME_EXAM, а больше — лишь если
    иначе не набрать MAX_LINKS, т.е. не больше max(MAX_SAME_EXAM, MAX_LINKS - число кандидатов других экзаменов)."""
    missing = [a["n"] for a in registry if a["n"] not in META]
    if missing:
        raise KeyError("seealso.META: нет записи для n=%s" % missing)
    unknown = sorted((n, m[0]) for n, m in META.items() if m[0] not in EXAM_ORDER)
    if unknown:
        raise KeyError("seealso.META: неизвестный exam %s; допустимы %s" % (unknown, list(EXAM_ORDER)))
    indeg = {a["slug"]: 0 for a in registry}
    graph = {}
    for a in sorted(registry, key=lambda r: (r["lang"], r["n"])):
        am = META[a["n"]]
        cands = [c for c in registry if c["lang"] == a["lang"] and c["slug"] != a["slug"]
                 and c["n"] not in AVOID.get(a["n"], ())]

        def key(c, am=am):
            cm = META[c["n"]]
            return (not (_subj(am) & _subj(cm)), cm[2] == am[2], indeg[c["slug"]], c["n"])
        cands.sort(key=key)

        def same_exam(c, am=am):
            return _tier(am, META[c["n"]]) == 0

        def same_subj(c, am=am):
            return bool(_subj(am) & _subj(META[c["n"]]))
        picked = []

        def add(c):
            if c not in picked and len(picked) < MAX_LINKS:
                picked.append(c)
        for c in [c for c in cands if same_exam(c) and same_subj(c)][:MAX_SAME_EXAM]:
            add(c)
        present = [e for e in EXAM_ORDER if any(META[c["n"]][0] == e for c in cands) or e == am[0]]
        nxt = present[(present.index(am[0]) + 1) % len(present)]
        bridge = [c for c in cands if META[c["n"]][0] == nxt and c not in picked]
        if bridge and nxt != am[0]:
            add(bridge[0])
        for sub in sorted(_subj(am)):   # для «physics+math» гарантия действует по каждому предмету отдельно
            for c in [c for c in cands if sub in _subj(META[c["n"]]) and not same_exam(c) and c not in picked]:
                if sum(sub in _subj(META[p["n"]]) for p in picked) >= MIN_SAME_SUBJECT:
                    break
                add(c)
        for c in [c for c in cands if same_exam(c) and c not in picked]:
            if sum(same_exam(p) for p in picked) >= MAX_SAME_EXAM:
                break
            add(c)
        for c in [c for c in cands if not same_exam(c)]:
            add(c)
        for c in cands:
            add(c)
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
    items = "".join('<li><a href="/answers/%s/">%s</a></li>' % (s, html.escape(by_slug[s]["h1"]))
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
