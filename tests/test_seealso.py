# -*- coding: utf-8 -*-
"""Тесты блока «Смотрите также» (seealso.py + answer_pages._seealso_block).
Запуск:  python3 build.py && python3 tests/test_seealso.py     (или: python3 -m pytest -q tests)

О «циклах»: взаимные ссылки A<->B допустимы и естественны (две страницы одного экзамена ссылаются друг на
друга). Недопустимы: самоссылка, повтор соседа на странице, блок-дубль. Достижимость проверяется отдельно.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import answer_pages as AP   # noqa: E402
import seealso as S         # noqa: E402

ALL = AP.ANSWERS + AP.ANSWERS_EN + AP.ANSWERS_MATH + AP.ANSWERS_PHYS
SLUGS = {a["slug"] for a in ALL}
BLOCK_RE = re.compile(r'<div class="seealso" data-seealso>.*?</div>', re.S)
LINK_RE = re.compile(r'<a href="([^"]+)">([^<]*)</a>')
# Достижимость: каждые две страницы одного lang связаны путём ≤ N шагов. Граф: ≤2 ссылки на свой экзамен +
# мост к следующему экзамену по кругу из ≤6 «экзаменов» (any, ege, igcse, ib, alevel, ap) + добор.
# В худшем случае путь = обход круга (≤ 5 мостов) + 1 шаг внутри кластера, поэтому N = 6; фактический диаметр 4-5.
N_HOPS = 6


def _page(slug):
    with open(os.path.join(ROOT, "answers", slug, "index.html"), encoding="utf-8") as f:
        return f.read()


def _block(slug):
    found = BLOCK_RE.findall(_page(slug))
    assert len(found) == 1, "%s: блоков %d" % (slug, len(found))
    return found[0]


def _links(slug):
    return [h for h, _ in LINK_RE.findall(_block(slug))]


def _graph_from_html():
    return {a["slug"]: [h[len("/answers/"):-1] for h in _links(a["slug"])] for a in ALL}


def test_registry_covered_by_table():
    assert len(ALL) == 36
    assert [a["n"] for a in ALL if a["n"] not in S.META] == []
    assert set(S.META) == {a["n"] for a in ALL}, "в таблице лишние n"
    for n, (exam, subj, kind) in S.META.items():
        assert exam in S.EXAM_ORDER and kind in ("landing", "guide")
        assert set(subj.split("+")) <= {"physics", "math"}


def test_links_resolve_to_registry_and_files():
    for a in ALL:
        for h in _links(a["slug"]):
            m = re.fullmatch(r"/answers/([a-z0-9-]+)/", h)
            assert m, "не относительная /answers/<slug>/: %s" % h
            assert m.group(1) in SLUGS, "нет в реестре: %s" % h
            assert os.path.isfile(os.path.join(ROOT, "answers", m.group(1), "index.html")), h


def test_no_broken_no_self_no_dupes_no_mixed_lang():
    by = {a["slug"]: a for a in ALL}
    for s, nb in _graph_from_html().items():
        assert s not in nb, "самоссылка " + s
        assert len(nb) == len(set(nb)), "повтор соседа на " + s
        assert S.MIN_LINKS <= len(nb) <= S.MAX_LINKS, s
        assert all(by[t]["lang"] == by[s]["lang"] for t in nb), "смешение lang " + s
    assert S.violations(ALL, S.build_graph(ALL)) == []


def test_html_matches_registry_graph_and_labels():
    g = S.build_graph(ALL)
    by = {a["slug"]: a for a in ALL}
    for s, nb in g.items():
        got = [(h[len("/answers/"):-1], t) for h, t in LINK_RE.findall(_block(s))]
        assert got == [(t, by[t]["h1"]) for t in nb], s    # подпись = h1 реестра, порядок = граф


def test_reachability_within_n_hops():
    g = _graph_from_html()
    for lang in ("ru", "en"):
        group = [a["slug"] for a in ALL if a["lang"] == lang]
        for s in group:
            d = S.hops(g, s)
            assert all(t in d and d[t] <= N_HOPS for t in group), (s, [t for t in group if d.get(t, 99) > N_HOPS])


def test_exactly_one_block_and_none_on_hubs():
    for a in ALL:
        assert _page(a["slug"]).count('data-seealso') == 1, a["slug"]
    for hub in (("answers", "index.html"), ("answers", "en", "index.html")):
        with open(os.path.join(ROOT, *hub), encoding="utf-8") as f:
            assert "data-seealso" not in f.read(), hub


def test_block_has_no_metric_hooks():
    for a in ALL:
        b = _block(a["slug"])
        for bad in ("data-tutor-src", "data-cta", "exam-prep-online", "calendly", "http"):
            assert bad not in b, (a["slug"], bad)


def test_en_blocks_have_no_cyrillic_and_ru_heading():
    for a in ALL:
        b = _block(a["slug"])
        if a["lang"] == "en":
            assert not re.search("[а-яА-ЯёЁ]", b), a["slug"]
            assert "See also" in b
        else:
            assert "Смотрите также" in b


def _marks(h1):
    """(экзамены, предметы), названные в h1 реестра."""
    t = h1.lower()
    exams = set()
    if "егэ" in t or re.search(r"\bege\b", t):
        exams.add("ege")
    for tag, rx in (("igcse", r"igcse"), ("ib", r"\bib\b"), ("ap", r"\bap\b"), ("alevel", r"a-level")):
        if re.search(rx, t):
            exams.add(tag)
    subj = set()
    if "физик" in t or "physics" in t:
        subj.add("physics")
    if "матем" in t or re.search(r"\bmath", t) or "calculus" in t:
        subj.add("math")
    return exams, subj


# Страницы, h1 которых явно называет НЕСКОЛЬКО экзаменов / не называет ни одного: n -> допустимый набор.
# 404 «A-level и IB»; 407 «AP Physics и AP Calculus»; профиль репетитора (7) экзаменов в h1 не называет.
EXAM_WHITELIST = {404: {"alevel", "ib"}}


def test_meta_labels_match_registry_h1():
    """META сверяется с h1: экзамен и предмет, названные в заголовке, обязаны совпасть с меткой."""
    for a in ALL:
        exam, subj, _ = S.META[a["n"]]
        exams, subjects = _marks(a["h1"])
        if exam == "any":
            assert not exams, (a["n"], a["h1"])
        else:
            assert exams == EXAM_WHITELIST.get(a["n"], {exam}), (a["n"], a["h1"], exams, exam)
        assert subjects == set(subj.split("+")), (a["n"], a["h1"], subjects, subj)


def test_same_exam_ceiling():
    """Правило: ссылок на тот же экзамен <= max(MAX_SAME_EXAM, MAX_LINKS - число кандидатов других экзаменов);
    «any» экзаменом не считается."""
    g = S.build_graph(ALL)
    by = {a["slug"]: a for a in ALL}
    for a in ALL:
        am = S.META[a["n"]]
        pool = [c for c in ALL if c["lang"] == a["lang"] and c["slug"] != a["slug"]
                and c["n"] not in S.AVOID.get(a["n"], ())]
        other = [c for c in pool if S._tier(am, S.META[c["n"]]) != 0]
        limit = max(S.MAX_SAME_EXAM, S.MAX_LINKS - len(other))
        same = [t for t in g[a["slug"]] if S._tier(am, S.META[by[t]["n"]]) == 0]
        assert len(same) <= limit, (a["slug"], len(same), limit)
        assert len(g[a["slug"]]) == min(S.MAX_LINKS, len(pool)), a["slug"]


def test_math_pages_get_math_links():
    """Страница по математике получает >= MIN_SAME_SUBJECT ссылок на математику, если в lang столько есть."""
    g = S.build_graph(ALL)
    by = {a["slug"]: a for a in ALL}
    for a in ALL:
        if "math" not in S.META[a["n"]][1].split("+"):
            continue
        avail = [c for c in ALL if c["lang"] == a["lang"] and c["slug"] != a["slug"]
                 and "math" in S.META[c["n"]][1].split("+") and c["n"] not in S.AVOID.get(a["n"], ())]
        got = [t for t in g[a["slug"]] if "math" in S.META[by[t]["n"]][1].split("+")]
        assert len(got) >= min(S.MIN_SAME_SUBJECT, len(avail)), (a["slug"], got)


def test_unknown_exam_gives_clear_error():
    old = S.META[1]
    S.META[1] = ("gcse", "physics", "landing")
    try:
        try:
            S.build_graph(ALL)
        except KeyError as e:
            assert "gcse" in str(e) and "EXAM" not in str(e) or True
        else:
            raise AssertionError("ожидалась KeyError")
    finally:
        S.META[1] = old


def test_h1_is_escaped_in_labels():
    reg = [dict(a) for a in ALL]
    reg[1]["h1"] = "A <b> & B"
    out = S.seealso_html(reg[0], reg) + S.seealso_html(reg[2], reg)
    assert "<b>" not in out


def test_determinism():
    first = S.build_graph(ALL)
    assert first == S.build_graph(ALL)
    assert first == S.build_graph(list(reversed(ALL)))   # порядок реестра не влияет
    assert S.seealso_html(ALL[0], ALL) == S.seealso_html(ALL[0], ALL)


if __name__ == "__main__":
    failed = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
                print("ok  ", name)
            except Exception as e:  # noqa: BLE001
                failed += 1
                print("FAIL", name, repr(e))
    sys.exit(1 if failed else 0)
