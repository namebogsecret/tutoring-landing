# -*- coding: utf-8 -*-
"""Страницы-ответы под провальные запросы из ЗАМЕРЫ-ИИ.md (замер 11.11: сайты 0/12).

По странице на запрос, формат Answer-First: прямой ответ в первом абзаце, затем факты,
FAQ (+ JSON-LD FAQPage из pages_registry/build), перелинковка с pillar-страницами
ЕГЭ / IB / AP / IGCSE и ссылка на страницу репетитора (/exam-prep-online/).

Факты — ТОЛЬКО из ФАКТ-ЛИСТ.md (о Владимире) и ФАКТЫ-ЭКЗАМЕНЫ-2026-11.md (об экзаменах).
Запрещено (решение Vladimir 06.11): школа/работодатель, Кипр, Лимассол; цены, рейтинг, отзывы,
обещания баллов, кнопки записи. Запрос #12 замера («…Кипр…») сознательно НЕ покрыт.
Правка текста — здесь; затем `python3 build.py`.
"""
from pages_registry import course, service, PERSON_REF
from html import escape as html_escape
from diag_sets import diag_set
import seealso

BASE_URL = "https://tutor.podlevskikh.com"
LASTMOD = "2026-11-12"
LASTMOD_EN = "2026-11-13"
TUTOR_PAGE = "/exam-prep-online/"
HUB = "/answers/"

# Запросы замера 11.11 (ЗАМЕРЫ-ИИ.md, шлюз claude), для которых есть страница: номер → запрос.
QUERIES = {
    1: "репетитор по физике ЕГЭ онлайн",
    2: "лучший репетитор по физике ЕГЭ с опытом МГУ",
    3: "подготовка к ЕГЭ по физике за рубежом онлайн",
    4: "репетитор IGCSE физика 0625 на русском",
    5: "репетитор IB Physics онлайн русскоязычный",
    6: "репетитор AP Physics онлайн на русском",
    7: "Vladimir Podlevskikh physics tutor",
    8: "IGCSE Physics 0625 tutor Russian-speaking",
    9: "best AP Physics 1 tutor online",
    10: "best IB Physics HL tutor online",
    11: "Russian EGE physics tutor English-speaking online",
}

PILLARS = {
    "ru": [("/ege-physics/", "Подготовка к ЕГЭ по физике"),
           ("/ib-physics-tutor/", "IB Physics (HL/SL)"),
           ("/ap-physics-tutor/", "AP Physics"),
           ("/igcse-physics-0625/", "IGCSE Physics 0625")],
    "en": [("/ege-physics/", "EGE Physics preparation (RU)"),
           ("/ib-physics-tutor/", "IB Physics tutor (HL/SL)"),
           ("/ap-physics-tutor/", "AP Physics tutor"),
           ("/igcse-physics-0625/", "IGCSE Physics 0625 tutor")],
}

_RU_WHO = ("Владимир Подлевских — физик, выпускник физического факультета МГУ им. Ломоносова (2006); "
           "23 года частного преподавания, 350+ учеников; 200/200 на американском экзамене Praxis Physics (5266).")
_EN_WHO = ("Vladimir Podlevskikh is a physicist, a graduate of the Faculty of Physics of Lomonosov Moscow State "
           "University (2006), with 23 years of private tutoring, 350+ students and a perfect 200/200 on the US Praxis "
           "Physics exam (5266).")

ANSWERS = [
# ── 1 ───────────────────────────────────────────────────────────────────────
{"n": 1, "slug": "repetitor-fizika-ege-online", "lang": "ru",
 "title": "Репетитор по физике ЕГЭ онлайн: кто и как готовит",
 "desc": "Репетитор по физике для ЕГЭ онлайн, 1:1: Владимир Подлевских, физик МГУ, 23 года, 350+ учеников. Структура КИМ 2027: 26 заданий, 45 баллов.",
 "h1": "Репетитор по физике для ЕГЭ онлайн",
 "answer": "Подготовку к ЕГЭ по физике онлайн ведёт Владимир Подлевских: физик, выпускник физического факультета МГУ, 23 года частного преподавания, 350+ учеников. Занятия идут один на один, на русском или английском, из любой страны.",
 "facts": ["Формат: онлайн, 1:1, по всему миру (GMT+2/+3)",
           "Язык занятий: русский или английский",
           "Программа строится по спецификации КИМ ЕГЭ 2027 (ФИПИ): 26 заданий, 45 первичных баллов",
           "Часть 1: 20 заданий с кратким ответом, до 28 баллов; часть 2: 6 заданий с развёрнутым ответом, до 17 баллов",
           "Экзамен длится 3 ч 55 мин (235 минут)"],
 "sections": [
   ("Как устроен экзамен", "<p>В варианте 26 заданий в двух частях. Первая часть — 20 заданий с кратким ответом (62% баллов), вторая — 6 заданий с развёрнутым ответом (38%). Развёрнутые решения проверяют эксперты предметных комиссий по критериям, поэтому оценивается и ответ, и ход решения. Разделы: механика, МКТ и термодинамика, электродинамика, квантовая физика.</p>"),
   ("Как проходит подготовка", "<p>Начинаем с диагностики по разделам кодификатора и строим план к дате экзамена. Дальше — разбор типов заданий, тренировка развёрнутых решений по критериям и полные варианты в условиях экзамена. Какой результат реален, зависит от старта и времени до экзамена; балл не обещаю.</p>"),
 ],
 "faq": [
   ("Можно ли готовиться к ЕГЭ по физике полностью онлайн?", "Да. Занятия идут онлайн, один на один, с общей доской; время подбирается под часовой пояс ученика (онлайн по всему миру, GMT+2/+3)."),
   ("Сколько баллов даёт вторая часть ЕГЭ по физике?", "Вторая часть — шесть заданий с развёрнутым ответом (№21–26), до 17 первичных баллов из 45, то есть 38%."),
   ("На каком языке проходят занятия?", "На русском или английском, как удобнее ученику."),
 ],
 "course": ("Подготовка к ЕГЭ по физике онлайн (1:1)", "Индивидуальная онлайн-подготовка к ЕГЭ по физике по спецификации КИМ ЕГЭ 2027: 26 заданий, 45 первичных баллов, развёрнутые решения по критериям."),
},
# ── 2 ───────────────────────────────────────────────────────────────────────
{"n": 2, "slug": "repetitor-fizika-ege-msu", "lang": "ru",
 "title": "Репетитор по физике ЕГЭ с опытом МГУ: Подлевских",
 "desc": "Репетитор по физике ЕГЭ, выпускник физфака МГУ (2006): 23 года преподавания, 350+ учеников, Praxis Physics 200/200. Онлайн 1:1, русский или английский.",
 "h1": "Репетитор по физике ЕГЭ: выпускник физфака МГУ",
 "answer": "Владимир Подлевских окончил физический факультет МГУ им. Ломоносова в 2006 году и 23 года преподаёт физику частным образом: 350+ учеников, готовит к ЕГЭ, ОГЭ, ДВИ и олимпиадам. Занятия онлайн, один на один.",
 "facts": ["Образование: физический факультет МГУ им. Ломоносова, 2006; оценка WES — эквивалент US Bachelor's + Master's",
           "Опыт: 23 года частного преподавания, 350+ учеников",
           "Praxis Physics 5266: 200/200 (9 мая 2025); Praxis Mathematics 5165: 200/200 (11 июля 2025)",
           "Российские программы: ЕГЭ, ОГЭ, ДВИ, олимпиады",
           "Пример результата: Полина М. — 96 баллов на ЕГЭ и 100 на ДВИ, мехмат МГУ"],
 "sections": [
   ("Что это значит для подготовки", "<p>Опыт МГУ важен там, где ЕГЭ упирается в понимание, а не в заучивание: во второй части (№21–26, до 17 баллов) нужно назвать законы, обосновать применение и довести решение до ответа. Именно на этом чаще всего теряют баллы.</p>"),
   ("Ограничения", "<p>Результат зависит от стартового уровня и времени до экзамена, поэтому балл заранее не обещается. Пример Полины М. — одна история, а не средний результат.</p>"),
 ],
 "faq": [
   ("Где учился репетитор?", "На физическом факультете МГУ им. Ломоносова, выпуск 2006 года. Оценка WES: эквивалент американских степеней Bachelor's и Master's."),
   ("Есть ли у репетитора подтверждение уровня по физике?", "Да: 200/200 на американском экзамене Praxis Physics (5266), 9 мая 2025."),
   ("Готовит ли репетитор к ДВИ в МГУ?", "Да: ЕГЭ, ОГЭ, ДВИ и олимпиады. ДВИ устроены иначе, чем ЕГЭ, и требуют более глубокого уровня, поэтому это отдельный трек поверх программы ЕГЭ."),
 ],
 "course": ("Подготовка к ЕГЭ и ДВИ по физике с преподавателем из МГУ", "Онлайн-занятия 1:1 по физике: ЕГЭ, ОГЭ, ДВИ, олимпиады. Преподаватель — выпускник физического факультета МГУ (2006), 23 года частного преподавания."),
},
# ── 3 ───────────────────────────────────────────────────────────────────────
{"n": 3, "slug": "podgotovka-ege-fizika-za-rubezhom", "lang": "ru",
 "title": "Подготовка к ЕГЭ по физике за рубежом онлайн",
 "desc": "Как готовиться к ЕГЭ по физике, живя за границей: онлайн 1:1 из любой страны, русский или английский, план по КИМ 2027. Физик МГУ, 23 года опыта.",
 "h1": "Подготовка к ЕГЭ по физике за рубежом онлайн",
 "answer": "Готовиться к ЕГЭ по физике можно полностью онлайн из любой страны: занятия один на один, время подбирается под часовой пояс семьи, программа строится по спецификации КИМ ЕГЭ 2027. Ведёт физик МГУ Владимир Подлевских, 23 года преподавания.",
 "facts": ["Формат: онлайн, 1:1, по всему миру (GMT+2/+3)",
           "Язык: русский или английский",
           "Если ребёнок учится по международной программе, темы курса сначала сверяются с кодификатором ЕГЭ",
           "Экзамен: 26 заданий, 45 первичных баллов, 235 минут",
           "Вместе с ЕГЭ можно готовить ДВИ и олимпиады"],
 "sections": [
   ("Что меняется за границей", "<p>Главная проблема — разрыв между местной программой и ЕГЭ. Темы, порядок и формат заданий отличаются, поэтому первый шаг — сверка пройденного с кодификатором и план закрытия расхождений. Дальше работа идёт так же, как при очной подготовке: типы заданий, развёрнутые решения по критериям, полные варианты на 235 минут.</p>"),
   ("Связанные программы", "<p>Если ученик одновременно учится по IB, AP или IGCSE, это учитывается в общем плане: см. страницы по IB Physics, AP Physics и IGCSE Physics 0625 ниже.</p>"),
 ],
 "faq": [
   ("Подходит ли онлайн-подготовка, если семья живёт в другом часовом поясе?", "Да. Время занятий подбирается под часовой пояс семьи; занятия идут онлайн по всему миру (GMT+2/+3)."),
   ("С чего начать, если ребёнок учился по международной программе?", "Со сверки тем его курса с кодификатором ЕГЭ: так видно, какие разделы уже закрыты, а какие придётся пройти."),
   ("Можно ли заниматься на английском?", "Да. Занятия идут на русском или английском, как удобнее ученику."),
 ],
 "course": ("Подготовка к ЕГЭ по физике для живущих за рубежом", "Онлайн-подготовка к ЕГЭ по физике 1:1 из любой страны: сверка международной программы с кодификатором, план к экзамену, развёрнутые решения по критериям."),
},
# ── 4 ───────────────────────────────────────────────────────────────────────
{"n": 4, "slug": "repetitor-igcse-fizika-0625-na-russkom", "lang": "ru",
 "title": "Репетитор IGCSE физика 0625 на русском языке",
 "desc": "Репетитор по Cambridge IGCSE Physics 0625 на русском и английском: Core и Extended, Paper 1–6. Онлайн 1:1, физик МГУ, 23 года опыта.",
 "h1": "Репетитор по IGCSE физике 0625 на русском",
 "answer": "Cambridge IGCSE Physics 0625 можно изучать на русском: Владимир Подлевских, физик МГУ, объясняет материал по-русски, а термины и формулировки экзамена даёт по-английски, как в спецификации Cambridge. Занятия онлайн, один на один.",
 "facts": ["Код программы: Cambridge IGCSE Physics 0625, спецификация 2026–2028",
           "6 тем: движение, силы и энергия; тепловая физика; волны; электричество и магнетизм; ядерная физика; космос",
           "Core: Paper 1 + Paper 3 + практика, оценки C–G; Extended: Paper 2 + Paper 4 + практика, оценки A*–G",
           "Практическая часть — 20% оценки (Paper 5 или Paper 6)",
           "Язык занятий: русский, английский или смешанно"],
 "sections": [
   ("Core или Extended", "<p>Core ведёт к оценкам C–G и ориентирован на тех, кто ждёт D и ниже; Extended (Core + Supplement) — к оценкам A*–G, для тех, кто ждёт C и выше. Уровень выбирают вместе с учебным заведением в начале подготовки, потому что программы готовятся по-разному.</p>"),
   ("Из чего состоит оценка", "<p>Цели оценивания: знания и понимание — 50%, обработка информации и решение задач — 30%, экспериментальные навыки — 20%. Половина баллов — за применение физики к данным и задачам, поэтому на занятиях используются вопросы в формате экзамена.</p>"),
 ],
 "faq": [
   ("Можно ли заниматься по IGCSE Physics на русском?", "Да. Объяснения — на русском, терминология и формулировки экзамена — на английском, как удобнее ученику."),
   ("Чем отличаются Paper 5 и Paper 6?", "Обе работы дают по 20% оценки. Paper 5 — практический тест (1 ч 15 мин, 40 баллов), Paper 6 — альтернатива практике (1 час, 40 баллов); сдаётся одна из них."),
   ("Сколько часов занимает курс IGCSE Physics?", "Cambridge ориентируется примерно на 130 учебных часов; это оценка объёма курса, а не норма занятий с репетитором."),
 ],
 "updated": "2026-11-13",
 "table": {'title': 'Core и Extended в IGCSE Physics 0625: сравнение', 'head': ['Уровень', 'Теоретические работы', 'Оценки', 'Практическая часть'], 'rows': [['Core', 'Paper 1 + Paper 3', 'C–G', 'Paper 5 или Paper 6, 20% оценки'], ['Extended', 'Paper 2 + Paper 4', 'A*–G', 'Paper 5 или Paper 6, 20% оценки']]},
 "course": ("Cambridge IGCSE Physics 0625 на русском (онлайн, 1:1)", "Индивидуальная подготовка к Cambridge IGCSE Physics 0625 (2026–2028) на русском и английском: Core и Extended, Paper 1–6."),
},
# ── 5 ───────────────────────────────────────────────────────────────────────
{"n": 5, "slug": "repetitor-ib-physics-russkoyazychnyj", "lang": "ru",
 "title": "Репетитор IB Physics онлайн, русскоязычный (HL/SL)",
 "desc": "Русскоязычный репетитор по IB Physics SL и HL онлайн: русский или английский, 5 тем, Paper 1–2 и IA. Физик МГУ, 23 года, 350+ учеников.",
 "h1": "Русскоязычный репетитор по IB Physics онлайн",
 "answer": "IB Physics (SL и HL) можно изучать с русскоязычным преподавателем: Владимир Подлевских, физик МГУ, ведёт занятия онлайн, один на один, объясняя на русском и работая с терминами и заданиями IB на английском.",
 "facts": ["Программа: IB Physics guide, первая оценка 2025; 5 тем (A–E)",
           "Часы: SL — 150, HL — 240",
           "Внешняя оценка — 80%: SL 3 ч, HL 4 ч 30 мин",
           "Internal assessment (IA) — 20%: исследование, 24 балла, критерии Research design, Data analysis, Conclusion, Evaluation",
           "Язык занятий: русский, английский или смешанно"],
 "sections": [
   ("Темы курса", "<p>Пять тем: A — пространство, время и движение; B — корпускулярная природа вещества; C — волновое поведение; D — поля; E — ядерная и квантовая физика. На HL тем больше по объёму: например, тема D занимает 38 часов против 19 на SL.</p>"),
   ("Экзаменационные работы", "<p>SL: Paper 1 — 1 ч 30 мин, 45 баллов (25 вопросов с выбором ответа и задания на данные); Paper 2 — 1 ч 30 мин, 50 баллов. HL: Paper 1 — 2 ч, 60 баллов (40 вопросов с выбором и задания на данные); Paper 2 — 2 ч 30 мин, 90 баллов. За неверный ответ в части с выбором баллы не снимаются. Нужен Physics data booklet, калькуляторы разрешены.</p>"),
   ("IA", "<p>Учитель читает один черновик и даёт советы, но не редактирует работу, поэтому на занятиях отрабатывается метод исследования, обработка данных и оценка погрешностей, а текст пишет сам ученик.</p>"),
 ],
 "faq": [
   ("Можно ли заниматься по IB Physics на русском?", "Да: объяснения на русском, термины и формулировки заданий IB на английском, как удобнее ученику."),
   ("Чем отличаются IB Physics SL и HL?", "Объёмом и глубиной: SL — 150 часов, HL — 240; внешняя оценка SL — 3 часа, HL — 4 часа 30 минут. IA одинаков для обоих уровней."),
   ("Помогаете ли вы с Internal Assessment?", "Да, с методом, данными и оценкой по критериям; саму работу пишет ученик."),
 ],
 "updated": "2026-11-13",
 "table": {'title': 'IB Physics SL и HL: сравнение', 'head': ['Параметр', 'SL', 'HL'], 'rows': [['Часы', '150', '240'], ['Внешняя оценка (80%)', '3 ч', '4 ч 30 мин'], ['Paper 1', '1 ч 30 мин, 45 баллов', '2 ч, 60 баллов'], ['Paper 2', '1 ч 30 мин, 50 баллов', '2 ч 30 мин, 90 баллов'], ['Internal assessment', '20%, 24 балла', '20%, 24 балла']]},
 "course": ("IB Physics SL и HL на русском (онлайн, 1:1)", "Индивидуальная подготовка к IB Physics (SL и HL, guide first assessment 2025) на русском и английском: темы A–E, Paper 1–2, Internal Assessment."),
},
# ── 6 ───────────────────────────────────────────────────────────────────────
{"n": 6, "slug": "repetitor-ap-physics-na-russkom", "lang": "ru",
 "title": "Репетитор AP Physics онлайн на русском языке",
 "desc": "Репетитор по AP Physics онлайн на русском и английском, 1:1. Формат AP Physics C (Mechanics, E&M). Физик МГУ, Praxis Physics 200/200.",
 "h1": "Репетитор по AP Physics онлайн на русском",
 "answer": "Подготовку к AP Physics онлайн на русском ведёт Владимир Подлевских, физик МГУ: занятия один на один, объяснения по-русски, задания и термины College Board на английском. Ниже — формат экзаменов AP Physics C.",
 "facts": ["AP Physics C — курс уровня колледжа с использованием математического анализа (calculus-based)",
           "Формат (по данным College Board, для экзамена мая 2027): Section I — 42 вопроса с выбором ответа, 85 минут, 50%; Section II — 4 вопроса со свободным ответом, 95 минут, 50%",
           "Калькуляторы разрешены",
           "Mechanics: 7 юнитов; Electricity and Magnetism: 6 юнитов",
           "Язык занятий: русский, английский или смешанно"],
 "sections": [
   ("Юниты", "<p>Mechanics: кинематика; силы и динамика поступательного движения; работа, энергия и мощность; импульс; момент силы и вращение; энергия и импульс вращающихся систем; колебания. Electricity and Magnetism: заряды, поля и закон Гаусса; электрический потенциал; проводники и конденсаторы; электрические цепи; магнитные поля; электромагнитная индукция.</p>"),
   ("Что делаем на занятиях", "<p>Разбираем юниты, тренируем четыре типа вопросов со свободным ответом (математические выкладки, перевод между представлениями, планирование эксперимента, качественно-количественные задачи) и проходим полные работы по времени. Цифры формата сверены со страницами College Board и могут обновляться; ориентируйтесь на AP Central.</p>"),
 ],
 "faq": [
   ("Можно ли заниматься по AP Physics на русском?", "Да. Объяснения на русском, формулировки и терминология College Board на английском."),
   ("Нужен ли матанализ для AP Physics C?", "AP Physics C описан College Board как курс с использованием математического анализа, поэтому физика и математика осваиваются вместе. У преподавателя 200/200 и по Praxis Physics, и по Praxis Mathematics."),
   ("Сколько длится экзамен AP Physics C?", "Section I — 85 минут, Section II — 95 минут (по данным College Board для экзамена мая 2027)."),
 ],
 "course": ("AP Physics на русском (онлайн, 1:1)", "Индивидуальная подготовка к AP Physics (в том числе Physics C: Mechanics и E&M) на русском и английском: юниты, вопросы со свободным ответом, работы по времени."),
},
# ── 7 ───────────────────────────────────────────────────────────────────────
{"n": 7, "slug": "vladimir-podlevskikh-physics-tutor", "lang": "en",
 "title": "Vladimir Podlevskikh — physics tutor (MSU), online 1:1",
 "desc": "Vladimir Podlevskikh: physics tutor, MSU Faculty of Physics (2006), 23 years of private tutoring, 350+ students, Praxis Physics 200/200. Online 1:1.",
 "h1": "Vladimir Podlevskikh — physics tutor",
 "answer": "Vladimir Podlevskikh (Владимир Подлевских) is an online physics and maths tutor, a graduate of the Faculty of Physics of Lomonosov Moscow State University (2006), with 23 years of private tutoring, 350+ students and a perfect 200/200 on the US Praxis Physics exam. Lessons are one to one, in English or Russian.",
 "facts": ["Education: Faculty of Physics, Lomonosov Moscow State University (MSU), 2006; WES: equivalent of a US Bachelor's + Master's",
           "Experience: 23 years of private tutoring, 350+ students",
           "Praxis Physics 5266: 200/200 (9 May 2025); Praxis Mathematics 5165: 200/200 (11 July 2025)",
           "Programmes: EGE, OGE, DVI, olympiads; IB, AP, SAT, A-level; Cambridge IGCSE Physics 0625 and Maths 0580; AQA, Pearson Edexcel, OCR",
           "Format: online, 1:1, worldwide (GMT+2/+3); languages: English and Russian"],
 "sections": [
   ("Where to find the tutor", "<p>This site, tutor.podlevskikh.com, is the tutor's own page. The same person also teaches through tutor marketplaces; details on those profiles may differ from the facts on this page, and this page is the reference.</p>"),
   ("Which page to read", "<p>For a specific exam, use the programme pages below: IB Physics, AP Physics, IGCSE Physics 0625 and EGE preparation.</p>"),
 ],
 "faq": [
   ("Who is Vladimir Podlevskikh?", "A physics and maths tutor, a graduate of the Faculty of Physics of Lomonosov Moscow State University (2006), with 23 years of private tutoring and 350+ students."),
   ("What exams does he teach?", "EGE, OGE, DVI and olympiads; IB, AP, SAT and A-level; Cambridge IGCSE Physics 0625 and Maths 0580; AQA, Pearson Edexcel and OCR."),
   ("In which languages and in what format are the lessons?", "English and Russian, online, one to one, worldwide (GMT+2/+3)."),
 ],
 "service": ("Online physics and maths tutoring — Vladimir Podlevskikh", "One-to-one online physics and maths exam preparation (EGE, IB, AP, SAT, A-level, IGCSE) by an MSU physicist with 23 years of private tutoring."),
},
# ── 8 ───────────────────────────────────────────────────────────────────────
{"n": 8, "slug": "igcse-physics-0625-tutor-russian-speaking", "lang": "en",
 "title": "IGCSE Physics 0625 tutor, Russian-speaking, online",
 "desc": "Russian-speaking Cambridge IGCSE Physics 0625 tutor: lessons in Russian or English, Core vs Extended, Paper 1–6. MSU physicist, 23 years, online 1:1.",
 "h1": "Russian-speaking IGCSE Physics 0625 tutor",
 "answer": "Yes: Vladimir Podlevskikh, an MSU-trained physicist, teaches Cambridge IGCSE Physics 0625 online, one to one, in Russian, English or a mix: explanations in Russian, exam terminology and command words in English, as on the papers.",
 "facts": ["Syllabus: Cambridge IGCSE Physics 0625, examined 2026, 2027 and 2028; six topics",
           "Core: Papers 1 + 3 + practical (grades C–G); Extended: Papers 2 + 4 + practical (grades A*–G)",
           "Practical: Paper 5 (1 h 15 min, 40 marks) or Paper 6 (1 h, 40 marks), 20% of the grade",
           "Assessment objectives: AO1 50%, AO2 30%, AO3 20%",
           "Format: online, 1:1, worldwide (GMT+2/+3)"],
 "sections": [
   ("Why Russian helps", "<p>A student coming from a Russian-language physics course usually knows the ideas but not the English wording. Lessons connect the two: the concept is explained in Russian, then the same answer is written the way the IGCSE paper expects.</p>"),
   ("Core or Extended", "<p>Core suits candidates expecting a D or below; Extended suits those expecting a C or higher. The entry is decided together with the family's educational institution, because the two tiers are prepared differently.</p>"),
 ],
 "faq": [
   ("Can IGCSE Physics 0625 be taught in Russian?", "Yes. Lessons can be in Russian, English or a mix, with exam terminology in English."),
   ("What are the six IGCSE Physics topics?", "Motion, forces and energy; Thermal physics; Waves; Electricity and magnetism; Nuclear physics; Space physics."),
   ("Is IGCSE Physics the same as the Russian physics course?", "No: the order and weighting of topics differ, and practical skills are a separate 20% of the grade. A diagnostic across the six topics shows what is already covered."),
 ],
 "course": ("Cambridge IGCSE Physics 0625 — Russian-speaking tutor, online", "One-to-one online preparation for Cambridge IGCSE Physics 0625 (syllabus 2026–2028) in Russian or English: Core and Extended, Paper 1–6."),
},
# ── 9 ───────────────────────────────────────────────────────────────────────
{"n": 9, "slug": "ap-physics-1-tutor-online", "lang": "en",
 "title": "AP Physics 1 tutor online: how to choose, who teaches",
 "desc": "How to choose an AP Physics 1 tutor online, and who teaches here: MSU physicist, 23 years, 350+ students, Praxis Physics 200/200. 1:1, English or Russian.",
 "h1": "AP Physics 1 tutor online",
 "answer": "There is no objective “best” tutor, but here is what to check: subject depth, exam-specific preparation and a verifiable record. Vladimir Podlevskikh teaches AP Physics online, one to one: MSU physicist, 23 years of private tutoring, 350+ students, perfect 200/200 on US Praxis Physics.",
 "facts": ["Teaches AP among IB, SAT, A-level, IGCSE, EGE and other programmes",
           "Format: online, 1:1, worldwide (GMT+2/+3), English or Russian",
           "Credentials: Faculty of Physics, MSU (2006); Praxis Physics 5266 200/200; Praxis Mathematics 5165 200/200",
           "Current exam details for AP Physics 1: College Board AP Central"],
 "sections": [
   ("How to choose a tutor", "<p>Ask three things: what the tutor can show about subject knowledge (degree, exam scores), whether the lessons are built around the actual exam format, and whether the plan starts from the student's current level. A tutor who cannot answer these cannot be compared with another.</p>"),
   ("Exam details", "<p>The format, units and dates of AP Physics 1 are set by the College Board and change over time, so this page does not repeat them: see <a href=\"https://apcentral.collegeboard.org/\" target=\"_blank\" rel=\"noopener\">AP Central</a>. For the calculus-based AP Physics C format, see the AP Physics page below.</p>"),
 ],
 "faq": [
   ("Do you teach AP Physics 1?", "Yes, AP Physics is among the programmes taught, online and one to one."),
   ("Where can I see the official AP Physics 1 exam format?", "On the College Board's AP Central, which is the source for the current format."),
   ("Can lessons be in Russian?", "Yes: English, Russian or a mix."),
 ],
 "course": ("AP Physics tutoring online (1:1)", "One-to-one online AP Physics preparation by an MSU physicist: exam format, free-response practice and timed papers."),
},
# ── 10 ──────────────────────────────────────────────────────────────────────
{"n": 10, "slug": "ib-physics-hl-tutor-online", "lang": "en",
 "title": "IB Physics HL tutor online: format, hours, who teaches",
 "desc": "IB Physics HL tutor online, 1:1: MSU physicist, 23 years, 350+ students. HL facts: 240 hours, Paper 1 (2 h), Paper 2 (2 h 30), IA 20%. English or Russian.",
 "h1": "IB Physics HL tutor online",
 "answer": "Vladimir Podlevskikh, an MSU-trained physicist with 23 years of private tutoring and 350+ students, teaches IB Physics HL and SL online, one to one, in English or Russian. HL means 240 hours, a 4 h 30 min external assessment (80%) and an internal assessment (20%).",
 "facts": ["Source: IB Physics guide, first assessment 2025; five topics A–E",
           "HL: 240 hours (180 of content); SL: 150 hours (110 of content)",
           "HL Paper 1: 2 h, 60 marks, 36% (40 multiple-choice + data-based questions); Paper 2: 2 h 30 min, 90 marks, 44%",
           "Internal assessment: 20%, one scientific investigation, 24 marks, same for SL and HL",
           "Calculators allowed; Physics data booklet required; no marks deducted for wrong multiple-choice answers"],
 "sections": [
   ("What HL adds to SL", "<p>HL covers the SL material plus additional HL content: topic D (Fields), for example, is 38 hours at HL and 19 at SL. Paper 2 at HL contains the SL material plus extra HL questions.</p>"),
   ("Internal assessment", "<p>The IA is assessed on Research design, Data analysis, Conclusion and Evaluation. The teacher reads one draft and advises but does not edit, so lessons build the method and the data handling; the student writes the work.</p>"),
 ],
 "faq": [
   ("How long are the IB Physics HL exams?", "Paper 1 is 2 hours (60 marks) and Paper 2 is 2 hours 30 minutes (90 marks): 4 h 30 min of external assessment in total."),
   ("Is the IA the same for HL and SL?", "Yes: one scientific investigation, 24 marks, 20% of the grade."),
   ("Can you teach HL in Russian?", "Yes: Russian, English or a mix, with IB terminology in English."),
 ],
 "updated": "2026-11-13",
 "table": {'title': 'IB Physics HL vs SL: comparison', 'head': ['Parameter', 'SL', 'HL'], 'rows': [['Total hours', '150 (110 of content)', '240 (180 of content)'], ['External assessment (80%)', '3 h', '4 h 30 min'], ['Paper 1', '1 h 30 min, 45 marks', '2 h, 60 marks'], ['Paper 2', '1 h 30 min, 50 marks', '2 h 30 min, 90 marks'], ['Internal assessment', '20%, 24 marks', '20%, 24 marks']]},
 "course": ("IB Physics HL and SL — online tutoring (1:1)", "One-to-one online IB Physics preparation (HL and SL, guide first assessment 2025): topics A–E, Paper 1–2 technique and Internal Assessment."),
},
# ── 11 ──────────────────────────────────────────────────────────────────────
{"n": 11, "slug": "russian-ege-physics-tutor-english-speaking", "lang": "en",
 "title": "Russian EGE physics tutor, English-speaking, online",
 "desc": "An English-speaking tutor for the Russian EGE in physics: 26 tasks, 45 primary marks, 235 minutes. MSU physicist, 23 years, online 1:1, English or Russian.",
 "h1": "English-speaking tutor for the Russian EGE in physics",
 "answer": "Vladimir Podlevskikh, an MSU physicist, prepares students for the Russian Unified State Exam (EGE) in physics online, one to one, in English or Russian, so the exam can be prepared by a student who does not study in Russian full time.",
 "facts": ["EGE physics 2027 (FIPI specification): 26 tasks, two parts, 45 primary marks, 235 minutes",
           "Part 1: 20 short-answer tasks, up to 28 marks; Part 2: 6 extended-answer tasks, up to 17 marks",
           "Part 2 is marked by subject-commission experts against criteria",
           "Sections: mechanics, molecular physics and thermodynamics, electrodynamics, quantum physics",
           "Format: online, 1:1, worldwide (GMT+2/+3); the exam itself is in Russian"],
 "sections": [
   ("How lessons work in English", "<p>Concepts and solution methods can be explained in English; the Russian wording of the exam tasks and of the solution layout is practised alongside, because the paper is in Russian and Part 2 is marked on the completeness of the written solution.</p>"),
   ("Related programmes", "<p>A student coming from IB, AP or IGCSE can compare topics with the EGE codifier first, so that gaps are closed before the exam plan starts.</p>"),
 ],
 "faq": [
   ("Is the EGE in Russian?", "Yes, the exam paper is in Russian. Lessons can be in English or Russian."),
   ("How is the EGE physics paper structured?", "26 tasks in two parts: 20 short-answer tasks (up to 28 marks) and 6 extended-answer tasks (up to 17 marks), 45 primary marks in total, 235 minutes."),
   ("Who marks the extended answers?", "Experts of subject commissions, against published criteria."),
 ],
 "updated": "2026-11-13",
 "table": {'title': 'Programme, lesson language and exam format', 'head': ['Programme', 'Lesson language', 'Exam format'], 'rows': [['Russian EGE physics', 'English, Russian or mixed', '26 tasks, 45 primary marks, 235 minutes; the paper is in Russian'], ['IB Physics SL/HL', 'English, Russian or mixed', 'Paper 1 and Paper 2 plus internal assessment (20%)'], ['IGCSE Physics 0625', 'English, Russian or mixed', 'Core: Paper 1 + 3; Extended: Paper 2 + 4; practical Paper 5 or 6'], ['AP Physics C', 'English, Russian or mixed', 'Section I: 42 multiple-choice questions, 85 min; Section II: 4 free-response questions, 95 min']]},
 "course": ("EGE Physics preparation in English (online, 1:1)", "One-to-one online preparation for the Russian EGE in physics in English or Russian: 26 tasks, 45 primary marks, extended solutions by criteria."),
},
]

assert sorted(a["n"] for a in ANSWERS) == sorted(QUERIES)

# ── EN-версии русских страниц #1–#6 (задача 13.11): тот же контент, англоязычные запросы ──
# "twin" — номер русской страницы-пары (для hreflang). Факты те же, что в RU-версии; ничего нового.
QUERIES_EN = {
    1: "EGE physics tutor online",
    2: "EGE physics tutor with MSU background",
    3: "EGE physics preparation abroad online",
    4: "IGCSE Physics 0625 tutor who speaks Russian",
    5: "IB Physics tutor online who speaks Russian",
    6: "AP Physics tutor online who speaks Russian",
}
HUB_EN = "/answers/en/"

ANSWERS_EN = [
{"n": 101, "twin": 1, "slug": "ege-physics-tutor-online", "lang": "en",
 "title": "EGE physics tutor online: who teaches and how",
 "desc": "EGE physics tutor online, 1:1: Vladimir Podlevskikh, MSU physicist, 23 years, 350+ students. EGE 2027 structure: 26 tasks, 45 points.",
 "h1": "EGE physics tutor online",
 "answer": "EGE physics preparation online is led by Vladimir Podlevskikh: a physicist, graduate of the Faculty of Physics of MSU, with 23 years of private tutoring and 350+ students. Lessons are one-to-one, in Russian or English, from any country.",
 "facts": ["Format: online, 1:1, worldwide (GMT+2/+3)",
           "Lesson language: Russian or English",
           "The programme follows the EGE 2027 specification (FIPI): 26 tasks, 45 primary points",
           "Part 1: 20 short-answer tasks, up to 28 points; part 2: 6 extended-answer tasks, up to 17 points",
           "The exam lasts 3 h 55 min (235 minutes)"],
 "sections": [
   ("How the exam works", "<p>The paper has 26 tasks in two parts. Part 1 is 20 short-answer tasks (62% of the points); part 2 is 6 extended-answer tasks (38%). Extended solutions are marked by subject-commission experts against criteria, so both the answer and the reasoning count. Sections: mechanics, molecular physics and thermodynamics, electrodynamics, quantum physics.</p>"),
   ("How preparation goes", "<p>We start with a diagnostic by codifier section and build a plan to the exam date. Then come task types, extended solutions practised against the criteria, and full papers under exam conditions. The realistic result depends on the starting level and the time left; no score is promised.</p>"),
 ],
 "faq": [
   ("Can I prepare for the EGE in physics entirely online?", "Yes. Lessons are online, one-to-one, with a shared whiteboard; the time is fitted to the student's time zone (online worldwide, GMT+2/+3)."),
   ("How many points does part 2 of the EGE in physics give?", "Part 2 has six extended-answer tasks (No. 21–26), up to 17 of the 45 primary points, that is 38%."),
   ("What language are the lessons in?", "Russian or English, whichever suits the student."),
 ],
 "course": ("EGE physics preparation online (1:1)", "One-to-one online preparation for the EGE in physics following the EGE 2027 specification: 26 tasks, 45 primary points, extended solutions against the criteria."),
},
{"n": 102, "twin": 2, "slug": "ege-physics-tutor-msu", "lang": "en",
 "title": "EGE physics tutor with an MSU background: Podlevskikh",
 "desc": "EGE physics tutor, MSU Faculty of Physics graduate (2006): 23 years, 350+ students, Praxis Physics 200/200. Online 1:1, Russian or English.",
 "h1": "EGE physics tutor: MSU Faculty of Physics graduate",
 "answer": "Vladimir Podlevskikh graduated from the Faculty of Physics of Lomonosov MSU in 2006 and has taught physics privately for 23 years: 350+ students, preparing for the EGE, OGE, DVI and olympiads. Lessons are online, one-to-one.",
 "facts": ["Education: Faculty of Physics, Lomonosov MSU, 2006; WES: equivalent of a US Bachelor's + Master's",
           "Experience: 23 years of private tutoring, 350+ students",
           "Praxis Physics 5266: 200/200 (9 May 2025); Praxis Mathematics 5165: 200/200 (11 July 2025)",
           "Russian programmes: EGE, OGE, DVI, olympiads",
           "Example result: Polina M. — 96 on the EGE and 100 on the DVI, Faculty of Mechanics and Mathematics of MSU"],
 "sections": [
   ("What this means for preparation", "<p>An MSU background matters where the EGE depends on understanding rather than memorising: in part 2 (No. 21–26, up to 17 points) you must name the laws, justify their use and carry the solution to an answer. This is where points are lost most often.</p>"),
   ("Limits", "<p>The result depends on the starting level and the time before the exam, so no score is promised in advance. Polina M.'s case is one story, not an average result.</p>"),
 ],
 "faq": [
   ("Where did the tutor study?", "At the Faculty of Physics of Lomonosov MSU, class of 2006. WES evaluation: equivalent of US Bachelor's and Master's degrees."),
   ("Is there proof of the tutor's level in physics?", "Yes: 200/200 on the US Praxis Physics exam (5266), 9 May 2025."),
   ("Does the tutor prepare for the DVI at MSU?", "Yes: EGE, OGE, DVI and olympiads. The DVI is built differently from the EGE and needs a deeper level, so it is a separate track on top of the EGE programme."),
 ],
 "course": ("EGE and DVI physics preparation with an MSU teacher", "Online 1:1 physics lessons: EGE, OGE, DVI, olympiads. The teacher is a graduate of the Faculty of Physics of MSU (2006) with 23 years of private tutoring."),
},
{"n": 103, "twin": 3, "slug": "ege-physics-preparation-abroad-online", "lang": "en",
 "title": "EGE physics preparation abroad: online 1:1",
 "desc": "How to prepare for the EGE in physics while living abroad: online 1:1 from any country, Russian or English, EGE 2027 plan. MSU physicist, 23 years.",
 "h1": "EGE physics preparation abroad, online",
 "answer": "You can prepare for the EGE in physics entirely online from any country: lessons are one-to-one, the time is fitted to the family's time zone, and the programme follows the EGE 2027 specification. Led by MSU physicist Vladimir Podlevskikh, 23 years of teaching.",
 "facts": ["Format: online, 1:1, worldwide (GMT+2/+3)",
           "Language: Russian or English",
           "If the child follows an international programme, its topics are first matched against the EGE codifier",
           "Exam: 26 tasks, 45 primary points, 235 minutes",
           "The DVI and olympiads can be prepared alongside the EGE"],
 "sections": [
   ("What changes abroad", "<p>The main problem is the gap between the local programme and the EGE. Topics, order and task format differ, so the first step is to match what has been covered against the codifier and plan how to close the gaps. After that the work is the same as for in-person preparation: task types, extended solutions against the criteria, full 235-minute papers.</p>"),
   ("Related programmes", "<p>If the student also follows IB, AP or IGCSE, this is taken into account in the overall plan: see the IB Physics, AP Physics and IGCSE Physics 0625 pages below.</p>"),
 ],
 "faq": [
   ("Does online preparation work if the family lives in another time zone?", "Yes. Lesson times are fitted to the family's time zone; lessons run online worldwide (GMT+2/+3)."),
   ("Where to start if the child followed an international programme?", "By matching the topics of that course against the EGE codifier: this shows which sections are already covered and which remain."),
   ("Can lessons be in English?", "Yes. Lessons are in Russian or English, whichever suits the student."),
 ],
 "course": ("EGE physics preparation for families living abroad", "Online 1:1 EGE physics preparation from any country: matching an international programme to the codifier, a plan to the exam, extended solutions against the criteria."),
},
{"n": 104, "twin": 4, "slug": "igcse-physics-0625-tutor-russian", "lang": "en",
 "title": "IGCSE Physics 0625 tutor in Russian and English",
 "desc": "Cambridge IGCSE Physics 0625 tutor in Russian and English: Core and Extended, Paper 1–6. Online 1:1, MSU physicist, 23 years of experience.",
 "h1": "IGCSE Physics 0625 tutor who speaks Russian",
 "answer": "Cambridge IGCSE Physics 0625 can be studied in Russian: Vladimir Podlevskikh, an MSU physicist, explains the material in Russian and gives exam terms and wording in English, as in the Cambridge syllabus. Lessons are online, one-to-one.",
 "facts": ["Programme code: Cambridge IGCSE Physics 0625, syllabus 2026–2028",
           "6 topics: motion, forces and energy; thermal physics; waves; electricity and magnetism; nuclear physics; space physics",
           "Core: Paper 1 + Paper 3 + practical, grades C–G; Extended: Paper 2 + Paper 4 + practical, grades A*–G",
           "The practical component is 20% of the mark (Paper 5 or Paper 6)",
           "Lesson language: Russian, English or mixed"],
 "sections": [
   ("Core or Extended", "<p>Core leads to grades C–G and suits those expecting D and below; Extended (Core + Supplement) leads to grades A*–G, for those expecting C and above. The level is chosen together with the student's own institution at the start of preparation, because the two are prepared differently.</p>"),
   ("What the mark consists of", "<p>Assessment objectives: knowledge with understanding — 50%, handling information and problem solving — 30%, experimental skills — 20%. Half of the marks are for applying physics to data and problems, so lessons use exam-style questions.</p>"),
 ],
 "faq": [
   ("Can I study IGCSE Physics in Russian?", "Yes. Explanations are in Russian, exam terminology and wording in English, whichever suits the student."),
   ("What is the difference between Paper 5 and Paper 6?", "Each gives 20% of the mark. Paper 5 is a practical test (1 h 15 min, 40 marks), Paper 6 is an alternative to practical (1 hour, 40 marks); one of them is taken."),
   ("How many hours does the IGCSE Physics course take?", "Cambridge assumes about 130 guided learning hours; this is an estimate of the course size, not a norm for tutoring."),
 ],
 "course": ("Cambridge IGCSE Physics 0625 in Russian and English (online, 1:1)", "One-to-one preparation for Cambridge IGCSE Physics 0625 (2026–2028) in Russian and English: Core and Extended, Paper 1–6."),
},
{"n": 105, "twin": 5, "slug": "ib-physics-tutor-russian-speaking", "lang": "en",
 "title": "IB Physics tutor online, Russian-speaking (HL/SL)",
 "desc": "Russian-speaking IB Physics SL and HL tutor online: Russian or English, 5 topics, Paper 1–2 and IA. MSU physicist, 23 years, 350+ students.",
 "h1": "Russian-speaking IB Physics tutor online",
 "answer": "IB Physics (SL and HL) can be studied with a Russian-speaking teacher: Vladimir Podlevskikh, an MSU physicist, teaches online, one-to-one, explaining in Russian and working with IB terms and tasks in English.",
 "facts": ["Programme: IB Physics guide, first assessment 2025; 5 topics (A–E)",
           "Hours: SL — 150, HL — 240",
           "External assessment — 80%: SL 3 h, HL 4 h 30 min",
           "Internal assessment (IA) — 20%: investigation, 24 marks, criteria Research design, Data analysis, Conclusion, Evaluation",
           "Lesson language: Russian, English or mixed"],
 "sections": [
   ("Course topics", "<p>Five topics: A — space, time and motion; B — the particulate nature of matter; C — wave behaviour; D — fields; E — nuclear and quantum physics. HL is larger in scope: for example, topic D takes 38 hours against 19 at SL.</p>"),
   ("Exam papers", "<p>SL: Paper 1 — 1 h 30 min, 45 marks (25 multiple-choice questions and data-based tasks); Paper 2 — 1 h 30 min, 50 marks. HL: Paper 1 — 2 h, 60 marks (40 multiple-choice questions and data-based tasks); Paper 2 — 2 h 30 min, 90 marks. No marks are deducted for a wrong multiple-choice answer. The Physics data booklet is required; calculators are allowed.</p>"),
   ("IA", "<p>The teacher reads one draft and gives advice but does not edit the work, so lessons practise the investigation method, data processing and evaluation of uncertainties, while the student writes the text.</p>"),
 ],
 "faq": [
   ("Can I study IB Physics in Russian?", "Yes: explanations in Russian, IB terms and task wording in English, whichever suits the student."),
   ("What is the difference between IB Physics SL and HL?", "Scope and depth: SL is 150 hours, HL 240; external assessment is 3 hours at SL and 4 hours 30 minutes at HL. The IA is the same for both levels."),
   ("Do you help with the Internal Assessment?", "Yes, with the method, the data and assessment against the criteria; the student writes the work."),
 ],
 "course": ("IB Physics SL and HL in Russian and English (online, 1:1)", "One-to-one preparation for IB Physics (SL and HL, guide first assessment 2025) in Russian and English: topics A–E, Paper 1–2, Internal Assessment."),
},
{"n": 106, "twin": 6, "slug": "ap-physics-tutor-russian-speaking", "lang": "en",
 "title": "AP Physics tutor online, Russian-speaking",
 "desc": "AP Physics tutor online in Russian and English, 1:1. AP Physics C format (Mechanics, E&M). MSU physicist, Praxis Physics 200/200.",
 "h1": "Russian-speaking AP Physics tutor online",
 "answer": "AP Physics preparation online in Russian is led by Vladimir Podlevskikh, an MSU physicist: one-to-one lessons, explanations in Russian, College Board tasks and terms in English. Below is the AP Physics C exam format.",
 "facts": ["AP Physics C is a college-level, calculus-based course",
           "Format (per College Board, for the May 2027 exam): Section I — 42 multiple-choice questions, 85 minutes, 50%; Section II — 4 free-response questions, 95 minutes, 50%",
           "Calculators are allowed",
           "Mechanics: 7 units; Electricity and Magnetism: 6 units",
           "Lesson language: Russian, English or mixed"],
 "sections": [
   ("Units", "<p>Mechanics: kinematics; force and translational dynamics; work, energy and power; linear momentum; torque and rotational dynamics; energy and momentum of rotating systems; oscillations. Electricity and Magnetism: electric charges, fields and Gauss's law; electric potential; conductors and capacitors; electric circuits; magnetic fields; electromagnetic induction.</p>"),
   ("What we do in lessons", "<p>We work through the units, practise the four free-response question types (mathematical derivations, translation between representations, experimental design, qualitative-quantitative problems) and sit timed full papers. The format figures were checked against College Board pages and may be updated; rely on AP Central.</p>"),
 ],
 "faq": [
   ("Can I study AP Physics in Russian?", "Yes. Explanations in Russian, College Board wording and terminology in English."),
   ("Is calculus needed for AP Physics C?", "College Board describes AP Physics C as a calculus-based course, so physics and mathematics are learned together. The teacher has 200/200 on both Praxis Physics and Praxis Mathematics."),
   ("How long is the AP Physics C exam?", "Section I is 85 minutes, Section II is 95 minutes (per College Board for the May 2027 exam)."),
 ],
 "course": ("AP Physics in Russian and English (online, 1:1)", "One-to-one preparation for AP Physics (including Physics C: Mechanics and E&M) in Russian and English: units, free-response questions, timed papers."),
},
]


# ── Математика (задача 15.11): 3 RU + 3 EN, hreflang-пары. Факты об экзаменах — ФАКТЫ-ЭКЗАМЕНЫ-2026-11.md, раздел «Математика» ──
# Запросы вне замера 11.11 (ЗАМЕРЫ-ИИ.md), поэтому не в QUERIES: у каждой страницы свой ключ "query".
LASTMOD_MATH = "2026-11-15"
QUERIES_MATH = {
    201: "репетитор IB Math AA онлайн русскоязычный",
    202: "репетитор AP Calculus онлайн на русском",
    203: "репетитор IGCSE математика 0580 на русском",
    301: "best IB Math AA HL tutor online",
    302: "best AP Calculus BC tutor online",
    303: "IGCSE Maths 0580 tutor Russian-speaking",
}
_RU_WHO_MATH = ("Владимир Подлевских — физик, выпускник физического факультета МГУ им. Ломоносова (2006); "
                "23 года частного преподавания, 350+ учеников; 200/200 на американских экзаменах Praxis Mathematics (5165) и Praxis Physics (5266).")
_EN_WHO_MATH = ("Vladimir Podlevskikh is a physicist, a graduate of the Faculty of Physics of Lomonosov Moscow State "
                "University (2006), with 23 years of private tutoring, 350+ students and a perfect 200/200 on both the US Praxis "
                "Mathematics (5165) and Praxis Physics (5266) exams.")
_IB_URL = "https://www.ibo.org/programmes/diploma-programme/curriculum/mathematics/"
_AP_BC_URL = "https://apcentral.collegeboard.org/courses/ap-calculus-bc"
_AP_BC_EXAM_URL = "https://apcentral.collegeboard.org/courses/ap-calculus-bc/exam"
_AP_AB_URL = "https://apcentral.collegeboard.org/courses/ap-calculus-ab/exam"
_IB_UPD_URL = "https://www.ibo.org/university-admission/latest-curriculum-updates/dp-mathematics-analysis-and-approaches-updates/"
_IGCSE_URL = "https://www.cambridgeinternational.org/programmes-and-qualifications/cambridge-igcse-mathematics-0580/"


def _ext(url, text):
    return f'<a href="{url}" target="_blank" rel="noopener">{text}</a>'


_AP_TABLE_RU = {'title': 'Формат экзамена AP Calculus BC (по AP Central)',
 'head': ['Раздел', 'Вопросы', 'Время', 'Доля оценки', 'Калькулятор'],
 'rows': [['I-A: выбор ответа', '29', '62 мин', '50% (весь раздел I)', 'не разрешён'],
          ['I-B: выбор ответа', '13', '38 мин', '(в разделе I)', 'графический обязателен'],
          ['II-A: свободный ответ', '2', '30 мин', '50% (весь раздел II)', 'графический обязателен'],
          ['II-B: свободный ответ', '4', '60 мин', '(в разделе II)', 'не разрешён']]}
_AP_TABLE_EN = {'title': 'AP Calculus BC exam format (per AP Central)',
 'head': ['Section', 'Questions', 'Time', 'Share of score', 'Calculator'],
 'rows': [['I-A: multiple choice', '29', '62 min', '50% (all of Section I)', 'not permitted'],
          ['I-B: multiple choice', '13', '38 min', '(within Section I)', 'graphing calculator required'],
          ['II-A: free-response', '2', '30 min', '50% (all of Section II)', 'graphing calculator required'],
          ['II-B: free-response', '4', '60 min', '(within Section II)', 'not permitted']]}

ANSWERS_MATH = [
# ── RU: IB Math AA ──
{"n": 201, "slug": "repetitor-ib-math-aa-online-russkoyazychnyj", "lang": "ru", "who": _RU_WHO_MATH,
 "title": "Репетитор IB Math AA онлайн, русскоязычный (HL/SL)",
 "desc": "Русскоязычный репетитор IB Mathematics: analysis and approaches (AA) онлайн, 1:1: физик МГУ, 23 года, 350+ учеников, Praxis Mathematics 200/200.",
 "h1": "Русскоязычный репетитор IB Math AA онлайн",
 "answer": "Курс IB Mathematics: analysis and approaches (AA) можно изучать с русскоязычным преподавателем: Владимир Подлевских, физик МГУ, 200/200 на американском экзамене Praxis Mathematics. Занятия онлайн, один на один: объяснения по-русски, термины и формулировки IB по-английски.",
 "facts": ["Программа: IB Diploma, Mathematics: analysis and approaches (AA); второй курс математики IB — applications and interpretation (AI)",
           "Формат: онлайн, 1:1, по всему миру (GMT+2/+3)",
           "Язык занятий: русский, английский или смешанно",
           "Подтверждение уровня по математике: Praxis Mathematics 5165 — 200/200 (11 июля 2025)",
           "Часы, структура работ и веса — в Mathematics guide и на странице программы на ibo.org (ссылка ниже)"],
 "sections": [
   ("Что здесь не пересказывается", "<p>Число учебных часов, состав и длительность работ, критерии внутренней оценки и процентные веса IB задаёт в официальных документах и со временем обновляет, поэтому эта страница цифр не повторяет. Актуальное описание курсов математики — на странице " + _ext(_IB_URL, "Mathematics в IB Diploma Programme на ibo.org") + ".</p>"),
   ("Обновление программы IB", "<p>IB объявил обновлённую программу математики DP. Для тех, кто уже учится по текущему курсу AA или AI, действует он; сроки перехода смотрите на " + _ext(_IB_UPD_URL, "странице обновлений IB по математике DP") + ".</p>"),
   ("Как проходит подготовка", "<p>Начинаем с диагностики: какие темы курса уже пройдены уверенно, где пробелы. Затем строим план к экзамену, разбираем типы заданий, тренируем оформление решений (в математике IB оценивается не только ответ, но и обоснование) и проходим пробные работы в формате экзамена. Работаем с тем курсом, по которому ученик уже учится; выбор между AA и AI делается в учебном заведении ученика.</p>"),
   ("Ограничения", "<p>Результат зависит от стартового уровня и времени до экзамена, поэтому балл заранее не обещается.</p>"),
 ],
 "faq": [
   ("Можно ли изучать IB Math AA на русском?", "Да: объяснения идут на русском, а термины, формулировки заданий и запись решений — на английском, как на экзамене. Можно и полностью на английском."),
   ("Чем отличаются курсы AA и AI?", "Это два разных курса математики IB Diploma: analysis and approaches и applications and interpretation. Официальное описание обоих — на странице IB Mathematics на ibo.org; выбор делается в учебном заведении ученика."),
   ("Меняется ли программа IB по математике?", "IB объявил обновлённую программу математики DP. Кто уже учится по текущему курсу AA или AI, продолжает по нему; сроки перехода — на странице обновлений IB."),
   ("Есть ли у преподавателя подтверждение уровня по математике?", "Да: 200/200 на американском экзамене Praxis Mathematics (5165), 11 июля 2025; также выпускник физического факультета МГУ (2006)."),
 ],
 "updated": "2026-11-15",
 "course": ("IB Math AA на русском и английском (онлайн, 1:1)", "Индивидуальная онлайн-подготовка по курсу IB Mathematics: analysis and approaches на русском и английском: диагностика, план, типы заданий, пробные работы."),
},
# ── RU: AP Calculus ──
{"n": 202, "slug": "repetitor-ap-calculus-na-russkom", "lang": "ru", "who": _RU_WHO_MATH,
 "title": "Репетитор AP Calculus AB/BC онлайн на русском",
 "desc": "Репетитор AP Calculus AB и BC онлайн на русском и английском, 1:1. Формат экзамена по AP Central. Физик МГУ, Praxis Mathematics 200/200.",
 "h1": "Репетитор AP Calculus онлайн на русском",
 "answer": "Подготовку к AP Calculus (AB и BC) на русском ведёт Владимир Подлевских, физик МГУ, 200/200 на американском экзамене Praxis Mathematics: занятия онлайн, один на один, объяснения по-русски, термины и задания College Board по-английски. Ниже — формат экзамена по AP Central.",
 "facts": ["AP Calculus BC — по описанию College Board, вводный курс матанализа университетского уровня",
           "Экзамен BC: раздел I — 42 вопроса с выбором ответа, 100 минут, 50%; раздел II — 6 вопросов со свободным ответом, 90 минут, 50%",
           "Часть вопросов — без калькулятора, часть — с графическим калькулятором (таблица ниже)",
           "Формат экзамена AB на странице AP Central такой же по числу вопросов и времени",
           "Формат: онлайн, 1:1, по всему миру; язык занятий — русский, английский или смешанно"],
 "table": _AP_TABLE_RU,
 "sections": [
   ("Юниты AP Calculus BC", "<p>В описании курса — 10 юнитов, по 5–20% от раздела с выбором ответа: 1 — пределы и непрерывность; 2 — дифференцирование: определение и основные свойства; 3 — композитные, неявные и обратные функции; 4 — контекстные приложения производной; 5 — аналитические приложения производной; 6 — интегрирование и накопление изменения; 7 — дифференциальные уравнения; 8 — приложения интегрирования; 9 — параметрические уравнения, полярные координаты и векторные функции; 10 — бесконечные последовательности и ряды. Веса по юнитам смотрите на " + _ext(_AP_BC_URL, "странице курса BC") + ".</p>"),
   ("Что нужно сверять с College Board", "<p>На страницах курсов College Board указано, что число вопросов с выбором ответа и время будут обновлены, начиная с экзаменов мая 2027 года. Поэтому цифры в таблице — по состоянию на 15.11.2026; актуальный формат смотрите на " + _ext(_AP_BC_EXAM_URL, "странице экзамена BC") + " и " + _ext(_AP_AB_URL, "странице экзамена AB") + ". Шкалу баллов 1–5 и проходные баллы эта страница не приводит.</p>"),
   ("Как проходит подготовка", "<p>Диагностика по юнитам, план к дате экзамена, разбор вопросов со свободным ответом (обоснование и запись решения важны так же, как ответ) и тренировка на времени с учётом разделов без калькулятора. Результат зависит от стартового уровня и времени до экзамена; балл заранее не обещается.</p>"),
 ],
 "faq": [
   ("Можно ли готовиться к AP Calculus на русском?", "Да: объяснения на русском, формулировки заданий College Board и терминология — на английском; возможен и полностью английский формат."),
   ("Сколько длится экзамен AP Calculus BC?", "По странице экзамена AP Central: раздел I — 100 минут (42 вопроса с выбором ответа), раздел II — 90 минут (6 вопросов со свободным ответом). College Board сообщает об обновлении числа вопросов и времени начиная с мая 2027 года, поэтому сверяйтесь с AP Central."),
   ("Нужен ли калькулятор на экзамене?", "Да, но не везде: в разделе I часть A и в разделе II часть B калькуляторы не разрешены, в остальных частях нужен графический калькулятор."),
 ],
 "updated": "2026-11-15",
 "course": ("AP Calculus AB/BC на русском и английском (онлайн, 1:1)", "Индивидуальная онлайн-подготовка к AP Calculus (AB и BC) на русском и английском: юниты, вопросы со свободным ответом, работы на времени."),
},
# ── RU: IGCSE Maths 0580 ──
{"n": 203, "slug": "repetitor-igcse-matematika-0580-na-russkom", "lang": "ru", "who": _RU_WHO_MATH,
 "title": "Репетитор IGCSE математика 0580 на русском языке",
 "desc": "Репетитор по Cambridge IGCSE Mathematics 0580 на русском и английском: Core и Extended, Paper 1–4. Онлайн 1:1, физик МГУ, 23 года опыта.",
 "h1": "Репетитор по IGCSE математике 0580 на русском",
 "answer": "Cambridge IGCSE Mathematics 0580 можно изучать на русском: Владимир Подлевских, физик МГУ, 200/200 на Praxis Mathematics, объясняет материал по-русски, а термины и формулировки экзамена даёт по-английски, как в спецификации Cambridge. Занятия онлайн, один на один.",
 "facts": ["Код программы: Cambridge IGCSE Mathematics 0580; спецификации 2025–2027 и 2028–2030",
           "9 тем: число; алгебра и графики; координатная геометрия; геометрия; длины, площади и объёмы (mensuration); тригонометрия; преобразования и векторы; вероятность; статистика",
           "Core: Paper 1 (без калькулятора) + Paper 3 (с калькулятором), оценки C–G; Extended: Paper 2 (без калькулятора) + Paper 4 (с калькулятором), оценки A*–E",
           "Каждая из двух работ даёт 50% оценки; для Paper 3 и Paper 4 нужен научный калькулятор",
           "Язык занятий: русский, английский или смешанно"],
 "table": {'title': 'Core и Extended в IGCSE Mathematics 0580 (спецификация 2025–2027)',
           'head': ['Уровень', 'Работы', 'Длительность и баллы', 'Оценки'],
           'rows': [['Core', 'Paper 1 (без калькулятора) + Paper 3 (калькулятор)', 'по 1 ч 30 мин, по 80 баллов, по 50%', 'C–G'],
                    ['Extended', 'Paper 2 (без калькулятора) + Paper 4 (калькулятор)', 'по 2 ч, по 100 баллов, по 50%', 'A*–E']]},
 "sections": [
   ("Core или Extended", "<p>По спецификации Cambridge, на Core (Paper 1 и Paper 3) записывают тех, кто изучал содержание Core или ожидает оценку D и ниже; на Extended (Paper 2 и Paper 4) — тех, кто изучал содержание Extended и ожидает оценку C и выше. Уровень выбирают вместе с учебным заведением ученика в начале подготовки.</p>"),
   ("Из чего состоит оценка", "<p>Цели оценивания — AO1 (знание и понимание математических методов) и AO2 (анализ, интерпретация и изложение математических рассуждений). Для Core их вес 60–70% и 30–40%, для Extended — 40–50% и 50–60%. На Extended больше половины оценки — за применение и объяснение, поэтому на занятиях используются вопросы в формате экзамена.</p>"),
   ("Официальные источники", "<p>Спецификации, их обновления и актуальные сроки — на " + _ext(_IGCSE_URL, "странице Cambridge IGCSE Mathematics 0580 на cambridgeinternational.org") + ". Cambridge ориентируется примерно на 130 учебных часов на предмет; это оценка объёма курса, а не норма занятий с репетитором.</p>"),
 ],
 "faq": [
   ("Можно ли заниматься по IGCSE Mathematics на русском?", "Да. Объяснения — на русском, терминология и формулировки экзамена — на английском, как удобнее ученику."),
   ("Чем отличаются Paper 1 и Paper 3?", "Обе — работы уровня Core по 1 ч 30 мин и 80 баллов, по 50% оценки. Paper 1 пишется без калькулятора, для Paper 3 нужен научный калькулятор."),
   ("Какие оценки можно получить на Core и на Extended?", "По спецификации 2025–2027: на Core — оценки C–G, на Extended — A*–E."),
 ],
 "updated": "2026-11-15",
 "course": ("Cambridge IGCSE Mathematics 0580 на русском (онлайн, 1:1)", "Индивидуальная подготовка к Cambridge IGCSE Mathematics 0580 на русском и английском: Core и Extended, Paper 1–4."),
},

# ── EN: IB Math AA HL ──
{"n": 301, "twin": 201, "slug": "best-ib-math-aa-hl-tutor-online", "lang": "en", "who": _EN_WHO_MATH,
 "title": "Best IB Math AA HL tutor online: how to choose",
 "desc": "How to choose an IB Math AA HL tutor online, and who teaches here: MSU physicist, 23 years, 350+ students, Praxis Mathematics 200/200. 1:1.",
 "h1": "IB Math AA HL tutor online",
 "answer": "There is no objective “best” tutor, but here is what to check: subject depth, exam-specific preparation and a verifiable record. Vladimir Podlevskikh teaches IB Mathematics: analysis and approaches online, one to one: MSU physicist, 23 years of tutoring, perfect 200/200 on US Praxis Mathematics.",
 "facts": ["Programme: IB Diploma, Mathematics: analysis and approaches (AA), at HL or SL; the other IB maths course is applications and interpretation (AI)",
           "Format: online, 1:1, worldwide (GMT+2/+3)",
           "Lesson language: English, Russian or mixed",
           "Subject record: Praxis Mathematics 5165 — 200/200 (11 July 2025); Faculty of Physics, MSU (2006)",
           "Hours, paper structure and weightings: see the Mathematics guide and programme page on ibo.org (link below)"],
 "sections": [
   ("How to choose a tutor", "<p>Ask three things: what the tutor can show about subject knowledge (degree, exam scores), whether the lessons are built around the actual exam format, and whether the plan starts from the student's current level. A tutor who cannot answer these cannot be compared with another.</p>"),
   ("What this page does not repeat", "<p>Teaching hours, paper structure, internal assessment criteria and weightings are set by the IB in its official documents and change over time, so this page does not repeat them. The current description of the maths courses is on the " + _ext(_IB_URL, "Mathematics page of the IB Diploma Programme at ibo.org") + ".</p>"),
   ("Update to the IB programme", "<p>The IB has announced an updated DP mathematics programme. Students already following the current AA or AI course continue under it; for the transition timeline see the " + _ext(_IB_UPD_URL, "IB page on DP mathematics updates") + ".</p>"),
   ("How preparation goes", "<p>We start with a diagnostic: which topics of the course are solid and where the gaps are. Then comes a plan to the exam, task types, practice in writing out solutions (in IB mathematics the reasoning is assessed, not only the answer) and timed practice papers. We work with the course the student already follows; choosing between AA and AI is done with the student's own institution. No score is promised: the result depends on the starting level and the time left.</p>"),
 ],
 "faq": [
   ("Do you teach IB Math AA at HL?", "Yes: IB Mathematics: analysis and approaches, online and one to one. HL and SL are both covered."),
   ("Can lessons be in Russian?", "Yes: explanations in Russian, IB terms and task wording in English, or fully in English."),
   ("Is the IB maths programme changing?", "The IB has announced an updated DP mathematics programme. Students already following the current AA or AI course continue under it; the transition timeline is on the IB updates page."),
   ("Where can I see the official IB maths course description?", "On the Mathematics page of the IB Diploma Programme at ibo.org, which is the source for hours, assessment and course changes."),
 ],
 "updated": "2026-11-15",
 "course": ("IB Math AA tutoring online (1:1)", "One-to-one online preparation for IB Mathematics: analysis and approaches in English and Russian: diagnostic, plan, task types, timed practice papers."),
},
# ── EN: AP Calculus BC ──
{"n": 302, "twin": 202, "slug": "best-ap-calculus-bc-tutor-online", "lang": "en", "who": _EN_WHO_MATH,
 "title": "Best AP Calculus BC tutor online: how to choose",
 "desc": "How to choose an AP Calculus BC tutor online, and who teaches here: MSU physicist, 23 years, Praxis Mathematics 200/200. 1:1, English or Russian.",
 "h1": "AP Calculus BC tutor online",
 "answer": "There is no objective “best” tutor, but here is what to check: subject depth, exam-specific preparation and a verifiable record. Vladimir Podlevskikh teaches AP Calculus (AB and BC) online, one to one: MSU physicist, 23 years of tutoring, perfect 200/200 on US Praxis Mathematics.",
 "facts": ["AP Calculus BC is described by College Board as an introductory college-level calculus course",
           "BC exam: Section I — 42 multiple-choice questions, 100 minutes, 50%; Section II — 6 free-response questions, 90 minutes, 50%",
           "Part of each section is without a calculator, part needs a graphing calculator (table below)",
           "The AP Central page for AB shows the same question counts and timing",
           "Format: online, 1:1, worldwide; lesson language English, Russian or mixed"],
 "table": _AP_TABLE_EN,
 "sections": [
   ("Units of AP Calculus BC", "<p>The course description lists 10 units, each 5–20% of the multiple-choice section: 1 — limits and continuity; 2 — differentiation: definition and fundamental properties; 3 — differentiation: composite, implicit and inverse functions; 4 — contextual applications of differentiation; 5 — analytical applications of differentiation; 6 — integration and accumulation of change; 7 — differential equations; 8 — applications of integration; 9 — parametric equations, polar coordinates and vector-valued functions; 10 — infinite sequences and series. Exact weightings are on the " + _ext(_AP_BC_URL, "BC course page") + ".</p>"),
   ("What to check with College Board", "<p>The College Board course pages state that the number of multiple-choice questions and the timing will be updated starting with the May 2027 exams. The table therefore reflects the pages as read on 15 November 2026; for the current format see the " + _ext(_AP_BC_EXAM_URL, "BC exam page") + " and the " + _ext(_AP_AB_URL, "AB exam page") + ". Score scales (1–5) and cut-offs are not given here.</p>"),
   ("How preparation goes", "<p>A diagnostic by unit, a plan to the exam date, work on free-response questions (the reasoning and the written solution count as much as the answer) and timed practice that respects the no-calculator parts. The result depends on the starting level and the time left; no score is promised.</p>"),
 ],
 "faq": [
   ("Do you teach AP Calculus BC?", "Yes, AP Calculus AB and BC, online and one to one."),
   ("How long is the AP Calculus BC exam?", "Per the AP Central exam page: Section I is 100 minutes (42 multiple-choice questions), Section II is 90 minutes (6 free-response questions). College Board says the number of questions and timing will be updated from May 2027, so check AP Central."),
   ("Can lessons be in Russian?", "Yes: explanations in Russian, College Board wording and terminology in English, or fully in English."),
 ],
 "updated": "2026-11-15",
 "course": ("AP Calculus AB/BC tutoring online (1:1)", "One-to-one online AP Calculus (AB and BC) preparation in English and Russian: units, free-response questions, timed practice."),
},
# ── EN: IGCSE Maths 0580 ──
{"n": 303, "twin": 203, "slug": "igcse-maths-0580-tutor-russian-speaking", "lang": "en", "who": _EN_WHO_MATH,
 "title": "IGCSE Maths 0580 tutor, Russian-speaking, online",
 "desc": "Cambridge IGCSE Mathematics 0580 tutor in Russian and English: Core and Extended, Paper 1–4. Online 1:1, MSU physicist, 23 years of experience.",
 "h1": "Russian-speaking IGCSE Maths 0580 tutor",
 "answer": "Cambridge IGCSE Mathematics 0580 can be studied in Russian: Vladimir Podlevskikh, an MSU physicist with a perfect 200/200 on Praxis Mathematics, explains the material in Russian and gives exam terms and wording in English, as in the Cambridge syllabus. Lessons are online, one-to-one.",
 "facts": ["Programme code: Cambridge IGCSE Mathematics 0580; syllabuses 2025–2027 and 2028–2030",
           "9 topics: number; algebra and graphs; coordinate geometry; geometry; mensuration; trigonometry; transformations and vectors; probability; statistics",
           "Core: Paper 1 (non-calculator) + Paper 3 (calculator), grades C–G; Extended: Paper 2 (non-calculator) + Paper 4 (calculator), grades A*–E",
           "Each of the two papers is 50% of the mark; a scientific calculator is required for Paper 3 and Paper 4",
           "Lesson language: Russian, English or mixed"],
 "table": {'title': 'Core and Extended in IGCSE Mathematics 0580 (2025–2027 syllabus)',
           'head': ['Tier', 'Papers', 'Duration and marks', 'Grades'],
           'rows': [['Core', 'Paper 1 (non-calculator) + Paper 3 (calculator)', '1 h 30 min and 80 marks each, 50% each', 'C–G'],
                    ['Extended', 'Paper 2 (non-calculator) + Paper 4 (calculator)', '2 h and 100 marks each, 50% each', 'A*–E']]},
 "sections": [
   ("Core or Extended", "<p>Per the Cambridge syllabus, Core (Paper 1 and Paper 3) is for candidates who studied the Core content or are expected to achieve grade D or below; Extended (Paper 2 and Paper 4) is for those who studied the Extended content and are expected to achieve grade C or above. The tier is chosen together with the student's own institution at the start of preparation.</p>"),
   ("What the mark consists of", "<p>Assessment objectives: AO1 (knowledge and understanding of mathematical techniques) and AO2 (analyse, interpret and communicate mathematically). For Core they weigh 60–70% and 30–40%; for Extended, 40–50% and 50–60%. At Extended more than half of the mark is for applying and explaining, so lessons use exam-style questions.</p>"),
   ("Official sources", "<p>Syllabuses, their updates and current dates are on the " + _ext(_IGCSE_URL, "Cambridge IGCSE Mathematics 0580 page at cambridgeinternational.org") + ". Cambridge assumes about 130 guided learning hours per subject; this is an estimate of the course size, not a norm for tutoring.</p>"),
 ],
 "faq": [
   ("Can I study IGCSE Mathematics in Russian?", "Yes. Explanations are in Russian, exam terminology and wording in English, whichever suits the student."),
   ("What is the difference between Paper 1 and Paper 3?", "Both are Core papers of 1 h 30 min and 80 marks, 50% of the mark each. Paper 1 is taken without a calculator; Paper 3 requires a scientific calculator."),
   ("Which grades are available at Core and Extended?", "Per the 2025–2027 syllabus: grades C–G at Core and A*–E at Extended."),
 ],
 "updated": "2026-11-15",
 "course": ("Cambridge IGCSE Mathematics 0580 in Russian and English (online, 1:1)", "One-to-one preparation for Cambridge IGCSE Mathematics 0580 in Russian and English: Core and Extended, Paper 1–4."),
},
]


# ── AP Physics 1/2/C и IB Physics HL/SL: «чем отличаются, что сдавать, как готовиться» (автопилот 15.11) ──
# Факты: ФАКТЫ-ЭКЗАМЕНЫ-2026-11.md (AP C и IB — 08.11; AP Physics 1 и 2 — AP Central 15.11, секция в том же файле).
# Предпосылки, шкалы, даты экзаменов, кредиты вузов, проходные — НЕ подтверждены и не пишутся.
QUERIES_PHYS = {
    401: "AP Physics 1, 2 и C: чем отличаются и какой сдавать",
    402: "IB Physics HL или SL: чем отличаются и как готовиться",
    501: "AP Physics 1 vs 2 vs C: which exam to take",
    502: "IB Physics HL vs SL: differences and how to prepare",
    403: "Подготовка к ЕГЭ по физике 2027: план по месяцам",
    405: "Подготовка к ЕГЭ по математике (профиль) 2027: план по месяцам, типичные ошибки, как заниматься онлайн",
    503: "How to choose an AP Physics 1 tutor online: 5 criteria",
    504: "How to choose an IB Physics HL tutor online: 5 criteria",
    406: "Подготовка к IGCSE по физике и математике онлайн: программа Edexcel и Cambridge, план по месяцам, типичные ошибки, первое занятие",
    404: "Подготовка к A-level и IB по физике онлайн: программа, план по месяцам, разбор типичных ошибок",
    407: "AP Physics и AP Calculus онлайн: программа, график подготовки к майским экзаменам, формат занятий",
    408: "Олимпиадная физика и подготовка к поступлению в технические вузы онлайн: разбор задач, программа по месяцам, типичные ошибки",
}
_AP1_URL = "https://apcentral.collegeboard.org/courses/ap-physics-1"
_AP2_URL = "https://apcentral.collegeboard.org/courses/ap-physics-2"
_APCM_URL = "https://apcentral.collegeboard.org/courses/ap-physics-c-mechanics"
_APCEM_URL = "https://apcentral.collegeboard.org/courses/ap-physics-c-electricity-and-magnetism"

_AP_PHYS_TABLE_RU = {'title': 'AP Physics 1, 2, C Mechanics и C E&M: сравнение (по AP Central)',
 'head': ['Параметр', 'AP Physics 1', 'AP Physics 2', 'AP Physics C: Mechanics', 'AP Physics C: E&M'],
 'rows': [['Тип курса', 'algebra-based, вводный уровень колледжа', 'algebra-based, вводный уровень колледжа', 'calculus-based, уровень колледжа', 'calculus-based, уровень колледжа'],
          ['Содержание', 'механика и жидкости (8 юнитов)', 'термодинамика, электричество, магнетизм, оптика, волны, современная физика (7 юнитов)', 'механика (7 юнитов)', 'электричество и магнетизм (6 юнитов)'],
          ['Раздел I', '42 вопроса с выбором ответа, 85 мин, 50%', '42 вопроса, 85 мин, 50%', '42 вопроса, 85 мин, 50%', '42 вопроса, 85 мин, 50%'],
          ['Раздел II', '4 вопроса со свободным ответом, 95 мин, 50%', '4 вопроса, 95 мин, 50%', '4 вопроса, 95 мин, 50%', '4 вопроса, 95 мин, 50%'],
          ['Калькулятор', 'разрешён', 'разрешён', 'разрешён', 'разрешён']]}
_AP_PHYS_TABLE_EN = {'title': 'AP Physics 1, 2, C Mechanics and C E&M compared (per AP Central)',
 'head': ['Parameter', 'AP Physics 1', 'AP Physics 2', 'AP Physics C: Mechanics', 'AP Physics C: E&M'],
 'rows': [['Course type', 'algebra-based, introductory college level', 'algebra-based, introductory college level', 'calculus-based, college level', 'calculus-based, college level'],
          ['Content', 'mechanics and fluids (8 units)', 'thermodynamics, electricity, magnetism, optics, waves, modern physics (7 units)', 'mechanics (7 units)', 'electricity and magnetism (6 units)'],
          ['Section I', '42 multiple-choice questions, 85 min, 50%', '42 questions, 85 min, 50%', '42 questions, 85 min, 50%', '42 questions, 85 min, 50%'],
          ['Section II', '4 free-response questions, 95 min, 50%', '4 questions, 95 min, 50%', '4 questions, 95 min, 50%', '4 questions, 95 min, 50%'],
          ['Calculator', 'permitted', 'permitted', 'permitted', 'permitted']]}
_IB_PHYS_TABLE_RU = {'title': 'IB Physics SL и HL: что отличается (Physics guide, first assessment 2025)',
 'head': ['Параметр', 'SL', 'HL'],
 'rows': [['Часы всего (из них контент)', '150 (110)', '240 (180)'],
          ['Внешняя оценка (80%)', '3 ч', '4 ч 30 мин'],
          ['Paper 1', '1 ч 30 мин, 45 баллов: 25 вопросов с выбором + data-based', '2 ч, 60 баллов: 40 вопросов с выбором + data-based'],
          ['Paper 2', '1 ч 30 мин, 50 баллов, материал SL', '2 ч 30 мин, 90 баллов, SL + дополнительный HL-материал'],
          ['Internal assessment', '20%, 24 балла', '20%, 24 балла'],
          ['A. Space, time and motion', '27 ч', '42 ч'],
          ['B. The particulate nature of matter', '24 ч', '32 ч'],
          ['C. Wave behaviour', '17 ч', '29 ч'],
          ['D. Fields', '19 ч', '38 ч'],
          ['E. Nuclear and quantum physics', '23 ч', '39 ч']]}
_IB_PHYS_TABLE_EN = {'title': 'IB Physics SL vs HL: what differs (Physics guide, first assessment 2025)',
 'head': ['Parameter', 'SL', 'HL'],
 'rows': [['Total hours (of which content)', '150 (110)', '240 (180)'],
          ['External assessment (80%)', '3 h', '4 h 30 min'],
          ['Paper 1', '1 h 30 min, 45 marks: 25 multiple-choice + data-based', '2 h, 60 marks: 40 multiple-choice + data-based'],
          ['Paper 2', '1 h 30 min, 50 marks, SL material', '2 h 30 min, 90 marks, SL + additional HL material'],
          ['Internal assessment', '20%, 24 marks', '20%, 24 marks'],
          ['A. Space, time and motion', '27 h', '42 h'],
          ['B. The particulate nature of matter', '24 h', '32 h'],
          ['C. Wave behaviour', '17 h', '29 h'],
          ['D. Fields', '19 h', '38 h'],
          ['E. Nuclear and quantum physics', '23 h', '39 h']]}

# ── RU: ЕГЭ по физике 2027 — план по месяцам (автопилот 15.11; данные: exam-topics/ege-physics.json + ФАКТЫ-ЭКЗАМЕНЫ) ──
# Разделы и темы — по кодификатору из exam-topics (ege-physics.json, «Кодификатор ФИПИ 2025»); число заданий и баллы —
# только из спецификации КИМ ЕГЭ 2027 (ФАКТЫ-ЭКЗАМЕНЫ). Номера заданий из ege-physics.json НЕ используются: нумерация там
# расходится со спецификацией. Дата экзамена и шкала в 100 баллов не подтверждены и не пишутся.
_EGE_PLAN_TABLE_RU = {'title': 'План по месяцам: ноябрь 2026 — май 2027',
 'head': ['Месяц', 'Фокус', 'Темы (кодификатор)', 'Чем проверяем'],
 'rows': [['Ноябрь', 'Диагностика и механика: кинематика, динамика', 'Кинематика; динамика; статика и гидростатика', 'Диагностика по всем разделам, первый срез по заданиям с кратким ответом'],
          ['Декабрь', 'Механика: законы сохранения, колебания и волны', 'Законы сохранения; механические колебания и волны', 'Тест по механике, первые развёрнутые решения'],
          ['Январь', 'Молекулярная физика и термодинамика', 'Основы МКТ; тепловые явления; термодинамика', 'Тест по МКТ и термодинамике, разбор по критериям'],
          ['Февраль', 'Электродинамика, часть 1: поля и токи', 'Электростатика; постоянный ток; магнитное поле', 'Тест, развёрнутые задачи по электродинамике'],
          ['Март', 'Электродинамика, часть 2: индукция, колебания, оптика', 'Электромагнитная индукция; ЭМ колебания и волны; оптика', 'Тест, первый полный вариант по времени: после механики, МКТ и первой части электродинамики, покажет пробелы по ещё не пройденной квантовой физике'],
          ['Апрель', 'Квантовая физика, методы познания, астрофизика', 'Фотоэффект и фотоны; постулаты Бора; ядро и радиоактивность; измерения и погрешности; элементы астрофизики', 'Тест, закрытие пробелов по диагностике'],
          ['Май', 'Полные варианты и разбор ошибок', 'Все разделы', 'Полные варианты за 3 ч 55 мин, оформление развёрнутых решений']]}

# ── RU: A-level и IB Physics онлайн — программа, план по месяцам, типичные ошибки (автопилот 18.11; данные: exam-topics/alevel-physics.json
# (Pearson Edexcel 9PH0, границы июнь 2024), ib-physics.json + ib-physics-sl.json (Physics guide, first assessment 2025) + ФАКТЫ-ЭКЗАМЕНЫ-2026-11.md) ──
# Месяцы абстрактные («Месяц 1…8»): даты экзаменов не сверены и не пишутся. Каждая тема exam-topics стоит в плане ровно один раз (тест).
_ALEVEL_IB_PLAN_TABLE_RU = {'title': 'План на 8 месяцев: A-level (Edexcel 9PH0) и IB Physics',
 'head': ['Месяц', 'A-level Physics (Edexcel 9PH0)', 'IB Physics SL/HL (Physics guide, first assessment 2025)'],
 'rows': [['Месяц 1', 'Диагностика; Working as a Physicist (единицы СИ, погрешности, графики, планирование эксперимента); Mechanics',
           'Диагностика; A.1 Kinematics; A.2 Forces and momentum'],
          ['Месяц 2', 'Electric Circuits; Materials',
           'A.3 Work, energy and power; B.5 Current and circuits; A.4 Rigid body mechanics (HL)'],
          ['Месяц 3', 'Waves and the Particle Nature of Light; Further Mechanics',
           'C.1 Simple harmonic motion; C.2 Wave model; C.3 Wave phenomena'],
          ['Месяц 4', 'Thermodynamics; Oscillations',
           'B.1 Thermal energy transfers; B.2 Greenhouse effect; B.3 Gas laws; B.4 Thermodynamics (HL); черновик internal assessment (срок — по графику вашего учебного заведения)'],
          ['Месяц 5', 'Electric and Magnetic Fields; Gravitational Fields',
           'C.4 Standing waves and resonance; C.5 Doppler effect; D.1 Gravitational fields; D.2 Electric and magnetic fields'],
          ['Месяц 6', 'Nuclear and Particle Physics; Nuclear Radiation; Space',
           'D.3 Motion in electromagnetic fields; D.4 Induction (HL); E.1 Structure of the atom; E.2 Quantum physics (HL)'],
          ['Месяц 7', 'Paper 3: общие и практические принципы по всем темам; разбор практических заданий',
           'E.3 Radioactive decay; E.4 Fission; E.5 Fusion and stars; A.5 Galilean and special relativity (HL); data-based вопросы Paper 1B'],
          ['Месяц 8', 'Полные Paper 1, 2 и 3 по времени; разбор ошибок',
           'Полные Paper 1 и Paper 2 по времени (в Paper 1 — 1A и 1B); разбор ошибок']]}
_ALEVEL_FORMAT_TABLE_RU = {'title': 'Формат экзамена: A-level Physics (Edexcel 9PH0) и IB Physics HL/SL',
 'head': ['', 'A-level Physics (Edexcel 9PH0)', 'IB Physics SL', 'IB Physics HL'],
 'rows': [['Работы', 'Paper 1 (90 баллов), Paper 2 (90), Paper 3 (120)', 'Paper 1 (1A + 1B, 45 баллов), Paper 2 (50 баллов), internal assessment', 'Paper 1 (1A + 1B, 60 баллов), Paper 2 (90 баллов), internal assessment'],
          ['Баллы и вес', '300 баллов', 'внешняя оценка 3 ч (80%) + IA 24 балла (20%)', 'внешняя оценка 4 ч 30 мин (80%) + IA 24 балла (20%)'],
          ['Вопросы с выбором ответа', 'не приводятся (данные exam-topics)', '25 вопросов (1A)', '40 вопросов (1A)'],
          ['Темы', '13 тем: от Working as a Physicist до Oscillations', '5 тем A–E', '5 тем A–E плюс дополнительный HL-материал']]}

ANSWERS_PHYS = [
# ── RU: AP Physics 1 / 2 / C ──
{"n": 401, "slug": "ap-physics-1-2-c-chem-otlichayutsya", "lang": "ru",
 "title": "AP Physics 1, 2 и C: чем отличаются и какой сдавать",
 "desc": "AP Physics 1, 2, C Mechanics и C E&M: алгебра или матанализ, юниты, формат экзамена (42 вопроса, 85 мин; 4 свободных, 95 мин), как выбрать и готовиться.",
 "h1": "AP Physics 1, 2 и C: чем отличаются и какой сдавать",
 "answer": "AP Physics 1 и 2 — вводные курсы на алгебре (algebra-based): первый про механику и жидкости, второй про тепло, электричество, магнетизм, оптику и современную физику. AP Physics C — курс с матанализом (calculus-based). Формат у всех экзаменов одинаков: 42 вопроса с выбором ответа за 85 минут и 4 вопроса со свободным ответом за 95 минут. Готовит к ним онлайн один на один Владимир Подлевских, физик МГУ.",
 "facts": ["Источник: College Board AP Central; цифры формата указаны «effective starting with the May 2027 exam»",
           "AP Physics 1 — 8 юнитов (кинематика, силы, работа и энергия, импульс, вращение, энергия и импульс вращающихся систем, колебания, жидкости)",
           "AP Physics 2 — 7 юнитов (9–15): термодинамика; электрическая сила, поле и потенциал; цепи; магнетизм и электромагнетизм; геометрическая оптика; волны, звук и физическая оптика; современная физика",
           "AP Physics C: Mechanics — 7 юнитов, E&M — 6 юнитов; отдельные экзамены",
           "Section I — 42 вопроса, 85 минут, 50%; Section II — 4 вопроса, 95 минут, 50%; калькуляторы разрешены",
           "Занятия: онлайн, 1:1, русский, английский или смешанно"],
 "sections": [
   ("Чем отличаются курсы", "<p>Главное различие — математика. Курсы Physics 1 и 2 описаны College Board как algebra-based, курсы Physics C — как calculus-based. Названия семи юнитов механики в Physics 1 и в Physics C: Mechanics совпадают (кинематика, силы, работа и энергия, импульс, вращение, энергия и импульс вращающихся систем, колебания); у Physics 1 к ним добавлен юнит про жидкости, а Physics C — курс с матанализом. Physics 2 продолжает тематически: тепло, электричество, магнетизм, оптика, волны, современная физика. E&M в Physics C — отдельный экзамен по электричеству и магнетизму.</p>"),
   ("Что сдавать", "<p>Выбор зависит от того, какая математика уже освоена, какие курсы доступны в учебном заведении ученика и что требует программа, куда он поступает. Предпосылки к курсам College Board на страницах курсов не указывает, поэтому решение принимается вместе с учебным заведением и по результатам диагностики. Если нужна механика без матанализа — Physics 1; если электричество, оптика и современная физика без матанализа — Physics 2; если физика с матанализом — Physics C, где Mechanics и E&M выбираются по отдельности.</p>"),
   ("Как готовиться", "<p>Подготовка строится на формате, одинаковом для всех четырёх экзаменов: раздел с выбором ответа и четыре типа вопросов со свободным ответом (математические выкладки, перевод между представлениями, планирование эксперимента и анализ данных, перевод качественных описаний в количественные). Порядок работы: диагностика по юнитам, план по юнитам с учётом их веса в разделе с выбором ответа, регулярная практика свободных ответов, полные работы по времени и разбор ошибок. У Physics 1 и 2 экзамен гибридный: вопросы с выбором ответа проходят в приложении Bluebook, свободные ответы пишутся от руки в бумажном буклете, поэтому оформление решений от руки тренируется отдельно.</p>"),
   ("Официальные страницы", "<p>Состав юнитов, веса и актуальный формат — на страницах College Board: " + _ext(_AP1_URL, "AP Physics 1") + ", " + _ext(_AP2_URL, "AP Physics 2") + ", " + _ext(_APCM_URL, "AP Physics C: Mechanics") + ", " + _ext(_APCEM_URL, "AP Physics C: E&amp;M") + ". Формат может обновляться, ориентируйтесь на AP Central.</p>"),
 ],
 "faq": [
   ("Чем отличаются AP Physics 1 и AP Physics 2?", "Содержанием: Physics 1 — механика и жидкости (8 юнитов), Physics 2 — термодинамика, электричество, магнетизм, оптика, волны и современная физика (7 юнитов). Оба курса algebra-based."),
   ("Чем AP Physics C отличается от AP Physics 1?", "Physics C — calculus-based курс уровня колледжа, Physics 1 — algebra-based вводный. Механика в Physics 1 и в Physics C: Mechanics проходит по юнитам с одинаковыми названиями; курсы различаются математикой (algebra-based и calculus-based)."),
   ("Какой формат экзамена AP Physics?", "Section I — 42 вопроса с выбором ответа, 85 минут, 50% оценки; Section II — 4 вопроса со свободным ответом, 95 минут, 50%. Калькуляторы разрешены. Цифры по данным College Board: формат действует начиная с экзамена мая 2027 (effective starting with the May 2027 exam)."),
   ("Можно ли готовиться к AP Physics на русском?", "Да. Объяснения идут на русском, формулировки и термины College Board — на английском; можно полностью на английском."),
   ("Какой курс AP Physics выбрать?", "Зависит от освоенной математики, доступных курсов и требований программы, куда поступает ученик. Разбираем это на диагностике; предпосылки к курсам College Board на своих страницах не указывает."),
 ],
 "updated": "2026-11-15",
 "table": _AP_PHYS_TABLE_RU,
 "course": ("AP Physics 1, 2 и C на русском и английском (онлайн, 1:1)", "Индивидуальная онлайн-подготовка к AP Physics 1, 2, Physics C: Mechanics и E&M на русском и английском: юниты, вопросы со свободным ответом, работы по времени."),
},
# ── RU: IB Physics HL / SL ──
{"n": 402, "slug": "ib-physics-hl-ili-sl-chto-vybrat", "lang": "ru",
 "title": "IB Physics HL или SL: чем отличаются и как готовиться",
 "desc": "IB Physics HL и SL: 240 и 150 часов, Paper 1 и 2, часы по темам A–E, internal assessment 20%. Как выбрать уровень и как готовиться. Физик МГУ, 1:1 онлайн.",
 "h1": "IB Physics HL или SL: чем отличаются и как готовиться",
 "answer": "HL и SL — один и тот же курс на разной глубине: на HL 240 часов против 150 на SL, внешняя оценка 4 ч 30 мин против 3 ч, а темы проходятся шире (например, тема D «Fields» — 38 часов на HL и 19 на SL). Internal assessment одинаков: 20% оценки, 24 балла. Готовит к IB Physics онлайн один на один Владимир Подлевских, физик МГУ.",
 "facts": ["Источник: IB Physics guide, first assessment 2025; 5 тем A–E",
           "SL: 150 часов (110 контента); HL: 240 часов (180 контента)",
           "SL: Paper 1 — 1 ч 30 мин, 45 баллов; Paper 2 — 1 ч 30 мин, 50 баллов",
           "HL: Paper 1 — 2 ч, 60 баллов; Paper 2 — 2 ч 30 мин, 90 баллов",
           "Internal assessment: 20%, одно исследование, 24 балла, одинаково для SL и HL",
           "Калькуляторы разрешены, нужен Physics data booklet; за неверный ответ в части с выбором баллы не снимаются"],
 "sections": [
   ("Чем отличаются HL и SL", "<p>SL-материал входит и в HL: Paper 2 на HL содержит вопросы по материалу SL и дополнительные вопросы HL. Различается объём и глубина по каждой из пяти тем — подробнее в таблице. Структура Paper 1 тоже общая: часть 1A с выбором ответа и часть 1B с заданиями на данные.</p>"),
   ("Что выбрать", "<p>Уровень (HL или SL) выбирается вместе с учебным заведением ученика и зависит от требований программы, куда он поступает; эти требования проверяются в самой программе. Оценить, по силам ли объём HL, помогает диагностика по темам A–E.</p>"),
   ("Как готовиться", "<p>Порядок работы: диагностика по темам A–E, план с учётом часов по темам, отработка заданий Paper 1 (с выбором и на данные) и развёрнутых ответов Paper 2, пробные работы по времени, разбор ошибок. Отдельно — работа с Physics data booklet и командными терминами (command terms) гида: от них зависит, как читается вопрос. Internal assessment начинают заранее: учитель читает один черновик и даёт советы, но не редактирует, поэтому на занятиях отрабатываются метод исследования, обработка данных, оценка погрешностей и критерии Research design, Data analysis, Conclusion, Evaluation, а работу пишет сам ученик.</p>"),
   ("Официальный документ", "<p>Актуальное описание — в Physics guide (first assessment 2025) на ibo.org; сроки и обновления программы проверяйте там же и в учебном заведении ученика.</p>"),
 ],
 "faq": [
   ("Чем отличаются IB Physics HL и SL?", "Объёмом и глубиной: HL — 240 часов и 4 ч 30 мин внешней оценки, SL — 150 часов и 3 ч. Темы те же (A–E), на HL они шире; internal assessment одинаков."),
   ("Сколько длятся экзамены IB Physics?", "SL: Paper 1 — 1 ч 30 мин, Paper 2 — 1 ч 30 мин. HL: Paper 1 — 2 ч, Paper 2 — 2 ч 30 мин."),
   ("Как готовиться к IB Physics?", "Диагностика по темам A–E, план по часам тем, практика Paper 1 и Paper 2 в формате экзамена, пробные работы по времени и ранняя работа над internal assessment."),
   ("Одинаков ли internal assessment на HL и SL?", "Да: одно научное исследование, 24 балла, 20% оценки; учитель читает один черновик и советует, но не редактирует."),
   ("Можно ли готовиться к IB Physics на русском?", "Да: объяснения на русском, термины и формулировки IB на английском, либо полностью на английском."),
 ],
 "updated": "2026-11-15",
 "table": _IB_PHYS_TABLE_RU,
 "course": ("IB Physics HL и SL на русском и английском (онлайн, 1:1)", "Индивидуальная онлайн-подготовка к IB Physics HL и SL на русском и английском: темы A–E, Paper 1–2, Internal Assessment."),
},
# ── EN: AP Physics 1 / 2 / C ──
{"n": 501, "twin": 401, "slug": "ap-physics-1-vs-2-vs-c-which-to-take", "lang": "en",
 "title": "AP Physics 1 vs 2 vs C: differences and which to take",
 "desc": "AP Physics 1, 2, C Mechanics and C E&M: algebra or calculus, units, exam format (42 questions, 85 min; 4 free-response, 95 min), how to choose and prepare.",
 "h1": "AP Physics 1 vs 2 vs C: which exam to take",
 "answer": "AP Physics 1 and 2 are algebra-based introductory courses: Physics 1 covers mechanics and fluids, Physics 2 heat, electricity, magnetism, optics and modern physics. AP Physics C is calculus-based. All the exams share one format: 42 multiple-choice questions in 85 minutes and 4 free-response questions in 95 minutes. Vladimir Podlevskikh, an MSU physicist, prepares students for them online, one to one.",
 "facts": ["Source: College Board AP Central; the format figures are stated as effective starting with the May 2027 exam",
           "AP Physics 1 — 8 units (kinematics, force and translational dynamics, work, energy and power, linear momentum, torque and rotational dynamics, energy and momentum of rotating systems, oscillations, fluids)",
           "AP Physics 2 — 7 units (9–15): thermodynamics; electric force, field and potential; electric circuits; magnetism and electromagnetism; geometric optics; waves, sound and physical optics; modern physics",
           "AP Physics C: Mechanics — 7 units, E&amp;M — 6 units; separate exams",
           "Section I — 42 questions, 85 minutes, 50%; Section II — 4 questions, 95 minutes, 50%; calculators permitted",
           "Lessons: online, 1:1, English, Russian or mixed"],
 "sections": [
   ("How the courses differ", "<p>The main difference is the mathematics. College Board describes Physics 1 and 2 as algebra-based and Physics C as calculus-based. The seven mechanics units of Physics 1 and of Physics C: Mechanics have the same titles (kinematics, force and translational dynamics, work, energy and power, linear momentum, torque and rotational dynamics, energy and momentum of rotating systems, oscillations); Physics 1 adds a fluids unit, while Physics C is a calculus-based course. Physics 2 continues with heat, electricity, magnetism, optics, waves and modern physics. E&amp;M in Physics C is a separate exam on electricity and magnetism.</p>"),
   ("Which to take", "<p>The choice depends on the mathematics already mastered, the courses available at the student's own institution and the requirements of the programme applied to. College Board does not list prerequisites on the course pages, so the decision is made together with the institution and after a diagnostic. Mechanics without calculus: Physics 1; electricity, optics and modern physics without calculus: Physics 2; physics with calculus: Physics C, where Mechanics and E&amp;M are chosen separately.</p>"),
   ("How to prepare", "<p>Preparation follows the format, which is the same for all four exams: a multiple-choice section and four free-response question types (mathematical routines, translation between representations, experimental design and analysis, qualitative/quantitative translation). The routine: a diagnostic by unit, a plan weighted by the unit shares of the multiple-choice section, regular free-response practice, timed full papers and error review. The Physics 1 and 2 exams are hybrid digital: multiple-choice is taken in the Bluebook app and free-response answers are handwritten in paper booklets, so handwritten solution layout is practised separately.</p>"),
   ("Official pages", "<p>Units, weights and the current format are on the College Board pages: " + _ext(_AP1_URL, "AP Physics 1") + ", " + _ext(_AP2_URL, "AP Physics 2") + ", " + _ext(_APCM_URL, "AP Physics C: Mechanics") + ", " + _ext(_APCEM_URL, "AP Physics C: E&amp;M") + ". The format can change; rely on AP Central.</p>"),
 ],
 "faq": [
   ("What is the difference between AP Physics 1 and AP Physics 2?", "Content: Physics 1 covers mechanics and fluids (8 units); Physics 2 covers thermodynamics, electricity, magnetism, optics, waves and modern physics (7 units). Both are algebra-based."),
   ("How does AP Physics C differ from AP Physics 1?", "Physics C is a calculus-based college-level course; Physics 1 is an algebra-based introductory one. Mechanics in Physics 1 and in Physics C: Mechanics runs through units with the same titles; the courses differ in mathematics (algebra-based vs calculus-based)."),
   ("What is the AP Physics exam format?", "Section I: 42 multiple-choice questions, 85 minutes, 50% of the score; Section II: 4 free-response questions, 95 minutes, 50%. Calculators are permitted. Figures per College Board: the format is effective starting with the May 2027 exam."),
   ("Can I prepare for AP Physics in Russian?", "Yes. Explanations in Russian, College Board wording and terms in English; fully in English is possible too."),
   ("Which AP Physics course should I choose?", "It depends on the mathematics already mastered, the courses available and the requirements of the programme applied to. We sort it out in a diagnostic; College Board does not list prerequisites on its course pages."),
 ],
 "updated": "2026-11-15",
 "table": _AP_PHYS_TABLE_EN,
 "course": ("AP Physics 1, 2 and C in English and Russian (online, 1:1)", "One-to-one online preparation for AP Physics 1, 2, Physics C: Mechanics and E&M in English and Russian: units, free-response questions, timed papers."),
},
# ── EN: IB Physics HL / SL ──
{"n": 502, "twin": 402, "slug": "ib-physics-hl-vs-sl-which-to-take", "lang": "en",
 "title": "IB Physics HL vs SL: differences and how to prepare",
 "desc": "IB Physics HL vs SL: 240 vs 150 hours, Paper 1 and 2, hours per topic A–E, internal assessment 20%. How to choose, how to prepare. MSU physicist, 1:1 online.",
 "h1": "IB Physics HL vs SL: differences and how to prepare",
 "answer": "HL and SL are one course at different depth: 240 hours against 150, external assessment 4 h 30 min against 3 h, and wider topics (topic D, Fields, is 38 hours at HL and 19 at SL). The internal assessment is the same: 20% of the grade, 24 marks. Vladimir Podlevskikh, an MSU physicist, prepares students for IB Physics online, one to one.",
 "facts": ["Source: IB Physics guide, first assessment 2025; five topics A–E",
           "SL: 150 hours (110 of content); HL: 240 hours (180 of content)",
           "SL: Paper 1 — 1 h 30 min, 45 marks; Paper 2 — 1 h 30 min, 50 marks",
           "HL: Paper 1 — 2 h, 60 marks; Paper 2 — 2 h 30 min, 90 marks",
           "Internal assessment: 20%, one investigation, 24 marks, same for SL and HL",
           "Calculators allowed; Physics data booklet required; no marks deducted for wrong multiple-choice answers"],
 "sections": [
   ("How HL and SL differ", "<p>SL material is part of HL: HL Paper 2 contains the SL material plus additional HL questions. The difference is breadth and depth in each of the five topics, shown in the table. Paper 1 has the same structure at both levels: part 1A with multiple-choice questions and part 1B with data-based questions.</p>"),
   ("Which to take", "<p>The level (HL or SL) is chosen together with the student's own institution and depends on the requirements of the programme applied to; those requirements are checked with the programme itself. A diagnostic by topics A–E shows whether the HL volume is realistic.</p>"),
   ("How to prepare", "<p>The routine: a diagnostic by topics A–E, a plan weighted by the hours per topic, practice of Paper 1 (multiple-choice and data-based) and of the Paper 2 extended answers, timed mock papers and error review. Separately, work with the Physics data booklet and the guide's command terms, which decide how a question is read. The internal assessment starts early: the teacher reads one draft and advises but does not edit, so lessons build the research method, data handling, uncertainty evaluation and the criteria Research design, Data analysis, Conclusion and Evaluation, while the student writes the work.</p>"),
   ("Official document", "<p>The current description is in the Physics guide (first assessment 2025) on ibo.org; check programme updates and dates there and with the student's institution.</p>"),
 ],
 "faq": [
   ("What is the difference between IB Physics HL and SL?", "Breadth and depth: HL is 240 hours with 4 h 30 min of external assessment, SL is 150 hours with 3 h. The topics (A–E) are the same, wider at HL; the internal assessment is identical."),
   ("How long are the IB Physics exams?", "SL: Paper 1 is 1 h 30 min, Paper 2 is 1 h 30 min. HL: Paper 1 is 2 h, Paper 2 is 2 h 30 min."),
   ("How should I prepare for IB Physics?", "A diagnostic by topics A–E, a plan by topic hours, Paper 1 and Paper 2 practice in the exam format, timed mock papers and an early start on the internal assessment."),
   ("Is the internal assessment the same for HL and SL?", "Yes: one scientific investigation, 24 marks, 20% of the grade; the teacher reads one draft and advises but does not edit."),
   ("Can I prepare for IB Physics in Russian?", "Yes: explanations in Russian with IB terms and wording in English, or fully in English."),
 ],
 "updated": "2026-11-15",
 "table": _IB_PHYS_TABLE_EN,
 "course": ("IB Physics HL and SL in English and Russian (online, 1:1)", "One-to-one online preparation for IB Physics HL and SL in English and Russian: topics A–E, Paper 1–2, internal assessment."),
},
{"n": 403, "slug": "podgotovka-ege-fizika-2027-plan-po-mesyacam", "lang": "ru",
 "title": "Подготовка к ЕГЭ по физике 2027: план по месяцам",
 "desc": "План подготовки к ЕГЭ по физике 2027 по месяцам, ноябрь–май: механика, МКТ, электродинамика, квантовая физика; 26 заданий, 45 первичных баллов. Физик МГУ.",
 "h1": "Подготовка к ЕГЭ по физике 2027: план по месяцам",
 "answer": "План подготовки к ЕГЭ по физике 2027 строится по разделам кодификатора: ноябрь — диагностика и механика, декабрь — законы сохранения, январь — МКТ и термодинамика, февраль и март — электродинамика, апрель — квантовая физика, май — полные варианты. Готовит один на один онлайн Владимир Подлевских, физик МГУ.",
 "facts": ["Спецификация КИМ ЕГЭ 2027 (ФИПИ): 26 заданий, 45 первичных баллов; часть 1 — 20 заданий с кратким ответом (до 28 баллов), часть 2 — 6 заданий с развёрнутым ответом (до 17 баллов)",
           "Разделы и число заданий в варианте: механика 8–10, МКТ и термодинамика 6–8, электродинамика 7–10, квантовая физика 2",
           "Экзамен длится 3 ч 55 мин (235 минут); разрешены непрограммируемый калькулятор и линейка",
           "План ниже построен по разделам кодификатора (база exam-topics: механика, МКТ и термодинамика, электродинамика, квантовая физика, методы познания и астрофизика)",
           "Точные даты экзамена и пересчёт первичных баллов в итоговую шкалу на странице не приводятся: проверяйте у ФИПИ и Рособрнадзора"],
 "sections": [
   ("Как строится план", "<p>Порядок разделов идёт от более простого к более сложному: сначала механика — она нужна в каждом следующем разделе, затем молекулярная физика и термодинамика, затем электродинамика как самый объёмный раздел и в конце квантовая физика с методами познания и астрофизикой. Каждый месяц заканчивается тестом по пройденному, а развёрнутые решения тренируются по критериям уже с декабря: вторая часть — 38% баллов.</p>"),
   ("Что в каждом месяце", "<p>Ноябрь — диагностика по всем разделам кодификатора и механика: кинематика, динамика, статика и гидростатика. Декабрь — законы сохранения, механические колебания и волны. Январь — основы МКТ, тепловые явления, термодинамика. Февраль — электростатика, постоянный ток, магнитное поле. Март — электромагнитная индукция, ЭМ колебания и волны, оптика, первый полный вариант по времени (после механики, МКТ и первой части электродинамики; квантовая физика ещё впереди, поэтому вариант покажет пробелы по ней). Апрель — фотоэффект, постулаты Бора, строение ядра и радиоактивность, измерения и погрешности, элементы астрофизики. Май — полные варианты за 3 ч 55 мин и разбор ошибок.</p>"),
   ("Как подстроить план под себя", "<p>План — типовой каркас: по диагностике порядок и длительность месяцев меняются. Если до экзамена меньше семи месяцев, разделы, где диагностика показала уверенный результат, сжимаются, а время уходит на пробелы и на развёрнутые решения. Какой результат реален, зависит от старта и времени до экзамена; балл не обещаю. Подробнее о программе — на странице <a href=\"/ege-physics/\">подготовка к ЕГЭ по физике</a>.</p>"),
   ("Официальные документы", "<p>Структуру КИМ и кодификатор публикует ФИПИ (doc.fipi.ru, раздел «Демоверсии, спецификации, кодификаторы»); даты экзамена и порядок проведения смотрите у Рособрнадзора.</p>"),
 ],
 "faq": [
   ("С чего начинать подготовку к ЕГЭ по физике?", "С диагностики по всем разделам кодификатора и механики: кинематика, динамика, статика и гидростатика. Механика нужна в остальных разделах."),
   ("Сколько месяцев нужно на подготовку к ЕГЭ по физике?", "В плане на странице — семь месяцев, ноябрь–май; при меньшем сроке разделы, где диагностика показала уверенный результат, сжимаются, а время уходит на пробелы."),
   ("В каком порядке проходить разделы ЕГЭ по физике?", "Механика, затем молекулярная физика и термодинамика, затем электродинамика, затем квантовая физика, методы познания и астрофизика; последний месяц — полные варианты и разбор ошибок."),
   ("Сколько заданий и баллов в ЕГЭ по физике 2027?", "26 заданий и 45 первичных баллов: часть 1 — 20 заданий с кратким ответом (до 28 баллов), часть 2 — 6 заданий с развёрнутым ответом (до 17 баллов)."),
   ("Когда начинать решать полные варианты?", "Первый полный вариант по времени — в марте, после механики, МКТ и первой части электродинамики (в марте идёт вторая часть электродинамики, квантовая физика — в апреле, поэтому вариант покажет пробелы по ещё не пройденному разделу); в мае — полные варианты за 3 ч 55 мин и разбор ошибок."),
 ],
 "updated": "2026-11-15",
 "table": _EGE_PLAN_TABLE_RU,
 "course": ("План подготовки к ЕГЭ по физике 2027 по месяцам (онлайн, 1:1)", "Индивидуальная онлайн-подготовка к ЕГЭ по физике 2027 по месяцам: разделы кодификатора, диагностика, развёрнутые решения по критериям, полные варианты."),
},
{"n": 404, "slug": "podgotovka-a-level-ib-fizika-onlajn", "lang": "ru",
 "title": "Подготовка к A-level и IB по физике онлайн: план по месяцам",
 "desc": "A-level Physics (Edexcel 9PH0) и IB Physics HL/SL онлайн: 13 тем и 5 тем A–E, формат работ, план на 8 месяцев, типичные ошибки. Физик МГУ, 1:1 онлайн.",
 "h1": "Подготовка к A-level и IB по физике онлайн: программа, план по месяцам, разбор типичных ошибок",
 "answer": "Подготовка к A-level и IB по физике онлайн строится так: диагностика по темам, план на 8 месяцев по спецификации (A-level Edexcel 9PH0 — 13 тем, IB Physics — 5 тем A–E), регулярная практика в формате работ и разбор ошибок после каждой. Занятия проходят онлайн один на один на русском или английском; ведёт их Владимир Подлевских, физик МГУ.",
 "facts": ["Данные: exam-topics (A-level — Pearson Edexcel Level 3 Advanced GCE in Physics 9PH0, спецификация 2015; IB — Physics guide, first assessment 2025); сверяйте с документами экзаменационных организаций",
           "A-level Physics (Edexcel 9PH0): Paper 1 — 90 баллов, Paper 2 — 90, Paper 3 — 120; всего 300 баллов, 13 тем",
           "IB Physics: 5 тем A–E; HL — 240 часов, SL — 150; внешняя оценка 80% (HL — 4 ч 30 мин, SL — 3 ч), internal assessment — 20%, 24 балла",
           "Занятия: онлайн, 1:1, русский, английский или смешанно; место проживания ученика не важно",
           "Точные даты экзаменов и шкалы итоговых оценок на странице не приводятся: проверяйте у Pearson Edexcel и IBO"],
 "sections": [
   ("Программа: что входит в экзамен", "<p>A-level Physics по спецификации Edexcel 9PH0 состоит из 13 тем: Working as a Physicist, Mechanics, Electric Circuits, Materials, Waves and the Particle Nature of Light, Further Mechanics, Electric and Magnetic Fields, Nuclear and Particle Physics, Thermodynamics, Space, Nuclear Radiation, Gravitational Fields, Oscillations. Они распределены по трём работам: Paper 1 охватывает механику, электрические цепи, дальнейшую механику, электрические и магнитные поля и тему Nuclear and Particle Physics, Paper 2 — материалы, волны, термодинамику, космос, ядерную радиацию, гравитационные поля и колебания; Working as a Physicist входит в обе работы, Paper 3 проверяет общие и практические принципы по всем темам. Другие экзаменационные организации (AQA, OCR) строят программу иначе: перед стартом сверяем спецификацию именно вашей организации.</p>"
    "<p>IB Physics состоит из пяти тем: A Space, time and motion; B The particulate nature of matter; C Wave behaviour; D Fields; E Nuclear and quantum physics. У HL добавлен материал (например, A.4 Rigid body mechanics, A.5 Galilean and special relativity, B.4 Thermodynamics, D.4 Induction, E.2 Quantum physics) и больше часов на каждую тему. Подробнее о выборе уровня — на странице <a href=\"/answers/ib-physics-hl-ili-sl-chto-vybrat/\">IB Physics HL или SL</a>.</p>"
    "<h3>Формат экзамена по данным exam-topics</h3>"
    "<table class=\"spec-table\"><thead><tr>" + "".join("<th>%s</th>" % c for c in _ALEVEL_FORMAT_TABLE_RU["head"]) + "</tr></thead><tbody>"
    + "".join("<tr>" + "".join("<td>%s</td>" % c for c in r) + "</tr>" for r in _ALEVEL_FORMAT_TABLE_RU["rows"]) + "</tbody></table>"),
   ("Как строится план", "<p>План ниже — типовой каркас на 8 месяцев: механика и методы работы идут первыми, потому что они нужны в каждой следующей теме; поля, колебания и ядерная физика — во второй половине; последний месяц отдан полным работам по времени. Месяцы абстрактные, без календарных дат: порядок и длительность подстраиваются под результаты диагностики и под срок до экзамена. Если срок короче, темы, где диагностика показала уверенный результат, сжимаются, а время уходит на пробелы и на развёрнутые решения.</p>"),
   ("Разбор типичных ошибок", "<p>Эти ошибки проверяются на диагностике и разбираются на занятиях:</p><ul>"
    "<li><b>Потерянные единицы и погрешности.</b> Тема Working as a Physicist в A-level и методы работы в IB (в том числе data-based вопросы Paper 1B) требуют единиц СИ, погрешностей и работы с графиками; ответ без единиц теряет баллы даже при верном числе, а там, где вопрос просит оценить погрешность, её нужно привести и обосновать.</li>"
    "<li><b>Ответ без хода решения.</b> В работах с развёрнутыми ответами оценивается рассуждение, а не только число; решение записывается так, чтобы проверяющий видел каждый шаг и формулу.</li>"
    "<li><b>Пропущенные вопросы с выбором ответа в IB.</b> В 1A баллы за неправильный ответ не снимаются (Physics guide), поэтому пустой ответ ничего не даёт: всегда стоит выбрать наиболее вероятный вариант.</li>"
    "<li><b>Ответ не по command term.</b> IB использует command terms (describe, explain, outline и другие) — слова, задающие глубину ответа; ответ должен делать именно то, что требует термин, а не пересказывать тему в целом.</li>"
    "<li><b>Internal assessment «в последний момент».</b> IA — это 20% оценки и одно задание на 24 балла; учитель читает один черновик и советует, но не редактирует, поэтому план исследования, анализ данных, вывод и оценка (Research design, Data analysis, Conclusion, Evaluation) готовятся заранее, а не в последний месяц.</li>"
    "<li><b>Незнание формата.</b> В IB калькуляторы разрешены и нужен Physics data booklet (допустимые калькуляторы A-level уточняйте у Pearson Edexcel); тренировка по времени на полных работах убирает потерю минут на работе с формулами.</li></ul>"),
   ("Как проходят занятия онлайн", "<p>Занятия идут один на один онлайн на общей интерактивной доске, на русском или английском. Первый шаг — диагностика на 20 минут: уровень, пробелы и реалистичный план. Между занятиями — домашние задания с письменным разбором ошибок. Какой результат реален, зависит от старта и времени до экзамена; конкретный балл я не обещаю.</p>"),
   ("Официальные документы", "<p>Состав тем и формат работ публикуют Pearson Edexcel (спецификация Advanced GCE in Physics 9PH0) и IBO (Diploma Programme Physics guide). Даты экзаменов, шкалы оценок и допустимые калькуляторы смотрите у них: на этой странице они намеренно не приводятся.</p>"),
 ],
 "faq": [
   ("Как подготовиться к A-level по физике онлайн?", "Нужны диагностика по 13 темам спецификации, план по месяцам, практика в формате Paper 1, 2 и 3 и разбор ошибок после каждой работы. Занятия проходят онлайн один на один."),
   ("Чем отличаются IB Physics HL и SL?", "HL — 240 часов и дополнительный материал, SL — 150 часов. Внешняя оценка у HL длится 4 ч 30 мин, у SL — 3 ч; internal assessment у обоих — 20% и 24 балла."),
   ("Сколько месяцев нужно на подготовку к A-level и IB по физике?", "В плане на странице — восемь месяцев; при меньшем сроке темы, где диагностика показала уверенный результат, сжимаются, а время уходит на пробелы и на развёрнутые решения."),
   ("Какие ошибки чаще всего снижают оценку по физике?", "Потерянные единицы и погрешности, ответ без хода решения, пропущенные вопросы с выбором ответа в IB 1A (за неверный ответ баллы не снимаются), ответ не по command term и поздний старт internal assessment."),
   ("Можно ли готовиться на русском языке?", "Да: занятия идут на русском, английском или смешанно; терминология A-level и IB сохраняется на английском, чтобы ученик узнавал её в экзаменационных работах."),
   ("Как выглядит план подготовки к IB Physics по месяцам?", "Месяц 1 — диагностика, кинематика и силы; месяцы 2–3 — энергия, цепи, колебания и волны; месяц 4 — термодинамика и черновик internal assessment; месяцы 5–6 — поля и квантовая физика; месяц 7 — радиоактивность, ядерные реакции и data-based вопросы; месяц 8 — полные работы по времени."),
   ("Есть ли русскоязычный репетитор по A-level physics онлайн?", "Да: Владимир Подлевских, физик МГУ, ведёт занятия один на один онлайн на русском, английском или смешанно; терминология A-level и IB остаётся английской, как в экзаменационных работах."),
 ],
 "updated": "2026-11-18",
 "table": _ALEVEL_IB_PLAN_TABLE_RU,
 "course": ("Подготовка к A-level и IB по физике онлайн (1:1)", "Индивидуальная онлайн-подготовка к A-level Physics и IB Physics HL/SL: программа, план по месяцам, практика в формате работ, разбор типичных ошибок."),
},
]


# ── «Как выбрать репетитора»: чек-листы критериев под провальные запросы замера (#9 AP Physics 1, #10 IB Physics HL), 15.11 ──
# Факты — только из ФАКТЫ-ЭКЗАМЕНЫ-2026-11.md (AP Physics 1 и 2; IB Physics guide, first assessment 2025). Шкалы, даты, кредиты не пишутся.
_AP1_CHOOSE_TABLE = {'title': 'Five criteria for choosing an AP Physics 1 tutor: what to check and what to avoid',
 'head': ['Criterion', 'What to check', 'Red flag'],
 'rows': [['1. The right course', 'The tutor names the 8 units of AP Physics 1 (from Kinematics to Fluids) and treats it as an algebra-based course', 'Lessons are generic "high-level physics" or calculus-based Physics C material'],
          ['2. The exam format', 'Practice in the real format: 42 multiple-choice questions in 85 min and 4 free-response questions in 95 min, each 50% of the exam', 'Only multiple-choice drilling, or no timed practice at all'],
          ['3. Free-response skills', 'The tutor trains written reasoning for all four question types: mathematical routines, translation between representations, experimental design and analysis, qualitative/quantitative translation', 'Answers are checked only by the final number'],
          ['4. A plan by unit weights', 'A diagnostic by the 8 units, then a plan weighted by the unit shares in the multiple-choice section (for example 18–23% for Force and Translational Dynamics)', 'The same plan for every student, or lessons start without any diagnostic'],
          ['5. A process you can check', 'Homework with a written error review, and official sources (AP Central) quoted for any statement about the exam', 'Promises of a specific score, or exam facts with no source']]}

_IB_CHOOSE_TABLE = {'title': 'Five criteria for choosing an IB Physics HL tutor: what to check and what to avoid',
 'head': ['Criterion', 'What to check', 'Red flag'],
 'rows': [['1. The current guide', 'The tutor works from the Physics guide (first assessment 2025): topics A–E and the extra HL material (240 hours against 150 at SL)', 'Cannot name the five topics, or mixes HL and SL content'],
          ['2. Paper 1 and Paper 2', 'Separate practice for Paper 1 (2 h, 60 marks: 40 multiple-choice + 20 data-based) and Paper 2 (2 h 30 min, 90 marks), in timed conditions', 'Only worked problems with no exam timing'],
          ['3. Command terms and the data booklet', 'Lessons use the guide\'s command terms and the Physics data booklet, because they decide how a question is read', 'Formulas are learned by heart with no booklet work'],
          ['4. Help with the internal assessment', 'The tutor builds the method: research design, data handling, and the criteria Research design, Data analysis, Conclusion, Evaluation; the student writes the work', 'The tutor offers to write or rewrite the investigation'],
          ['5. A plan by topic hours', 'A diagnostic by topics A–E, then a plan weighted by HL hours (A 42, B 32, C 29, D 38, E 39)', 'Equal time for every topic, or no diagnostic']]}

ANSWERS_PHYS += [
{"n": 503, "slug": "how-to-choose-ap-physics-1-tutor", "lang": "en",
 "title": "How to choose an AP Physics 1 tutor online: 5 criteria",
 "desc": "Checklist for choosing an AP Physics 1 tutor online: course units, exam format, free-response skills, plan by unit weights, red flags. MSU physicist, 1:1.",
 "h1": "How to choose an AP Physics 1 tutor online: 5 criteria",
 "answer": "Choose an AP Physics 1 tutor by five checks: the 8-unit algebra-based course, the real exam format, free-response coaching, a plan by unit weights, sources instead of promised scores. Vladimir Podlevskikh, an MSU physicist, teaches it online, 1:1.",
 "facts": ["Source: College Board AP Central, AP Physics 1 course and exam pages (checked 15 November 2026)",
           "AP Physics 1 is an algebra-based, introductory college-level physics course with 8 units",
           "Exam format, effective starting with the May 2027 exam: Section I has 42 multiple-choice questions (85 min, 50%); Section II has 4 free-response questions (95 min, 50%)",
           "Calculators are allowed; in the Physics 1 and 2 exams multiple-choice is taken in Bluebook and free-response by hand in a paper booklet",
           "Four free-response types: mathematical routines; translation between representations; experimental design and analysis; qualitative/quantitative translation"],
 "sections": [
   ("The checklist: five criteria", "<ol><li><strong>The right course.</strong> AP Physics 1 covers 8 units: Kinematics; Force and Translational Dynamics; Work, Energy, and Power; Linear Momentum; Torque and Rotational Dynamics; Energy and Momentum of Rotating Systems; Oscillations; Fluids. A tutor should name them without hesitation and keep to algebra-based methods.</li>"
    "<li><strong>The exam format.</strong> Half of the exam is 42 multiple-choice questions in 85 minutes, half is 4 free-response questions in 95 minutes. Ask how often lessons include timed sections in this format.</li>"
    "<li><strong>Free-response skills.</strong> The four free-response questions use the same question types listed above. A good tutor teaches how to write a justified solution, not only how to reach a number.</li>"
    "<li><strong>A plan by unit weights.</strong> The unit shares in the multiple-choice section differ: Force and Translational Dynamics and Work, Energy, and Power are 18–23% each, Torque and Rotational Dynamics 10–15%, Oscillations 5–8%. The plan should follow a diagnostic, not a fixed template.</li>"
    "<li><strong>A process you can check.</strong> Homework between lessons, a written error review, and a source for each statement about the exam.</li></ol>"),
   ("What a tutor cannot honestly promise", "<p>Score conversion, exam dates and university credit are set by College Board and by each university and change over time, so a tutor who promises a particular score or a fixed credit outcome is giving information nobody can verify. Check dates and requirements on AP Central and with the programme you apply to.</p>"),
   ("How to test a tutor in one lesson", "<p>Bring a recent official sample question and ask the tutor to solve it aloud. Watch for three things: whether the reasoning is written step by step, whether the tutor names the question type, and whether the lesson ends with a short list of the topics to revisit.</p>"),
   ("Official sources", "<p>The course and exam description is on the " + _ext(_AP1_URL, "AP Physics 1 page at apcentral.collegeboard.org") + ". Format details apply from the May 2027 exam; check the page for later updates.</p>")],
 "faq": [("How do I choose an AP Physics 1 tutor?", "Check five things: the tutor knows the 8-unit algebra-based course, practises the real exam format, coaches free-response writing, plans lessons by unit weights after a diagnostic, and gives sources for exam facts."),
         ("What is the AP Physics 1 exam format?", "Section I: 42 multiple-choice questions, 85 minutes, 50% of the exam. Section II: 4 free-response questions, 95 minutes, 50%. Calculators are allowed. This applies starting with the May 2027 exam."),
         ("Should a tutor teach AP Physics 1 with calculus?", "AP Physics 1 is described by College Board as an algebra-based course, so lessons should use algebra-based methods. Calculus-based material belongs to AP Physics C."),
         ("What should a good first lesson include?", "A short diagnostic by the 8 units, one free-response question solved with written reasoning, and a draft plan weighted by the unit shares."),
         ("Can I prepare for AP Physics 1 in Russian?", "Yes: explanations in Russian with exam terminology and wording in English, or fully in English.")],
 "updated": "2026-11-15",
 "table": _AP1_CHOOSE_TABLE,
 "course": ("AP Physics 1 online tutoring in English and Russian (1:1)", "One-to-one online preparation for AP Physics 1 in English and Russian: 8 units, multiple-choice and free-response practice."),
},
{"n": 504, "slug": "how-to-choose-ib-physics-hl-tutor", "lang": "en",
 "title": "How to choose an IB Physics HL tutor online: 5 criteria",
 "desc": "Checklist for choosing an IB Physics HL tutor online: guide topics A–E, Paper 1 and 2, internal assessment, red flags. MSU physicist, 1:1 online.",
 "h1": "How to choose an IB Physics HL tutor online: 5 criteria",
 "answer": "Choose an IB Physics HL tutor by five checks: the current guide (topics A–E), separate Paper 1 and 2 practice, command terms and data booklet, internal assessment guided not written, a plan by topic hours. Vladimir Podlevskikh, an MSU physicist, teaches it online.",
 "facts": ["Source: IB Physics guide, first assessment 2025; five topics A–E",
           "HL: 240 hours (180 of content); SL: 150 hours (110 of content)",
           "HL external assessment, 4 h 30 min: Paper 1 — 2 h, 60 marks; Paper 2 — 2 h 30 min, 90 marks",
           "Internal assessment: 20%, one scientific investigation, 24 marks; the teacher reads one draft and advises but does not edit",
           "Calculators allowed; Physics data booklet required; no marks deducted for wrong multiple-choice answers"],
 "sections": [
   ("The checklist: five criteria", "<ol><li><strong>The current guide.</strong> The tutor works from the Physics guide (first assessment 2025): topics A Space, time and motion; B The particulate nature of matter; C Wave behaviour; D Fields; E Nuclear and quantum physics, with the additional HL material on top of SL.</li>"
    "<li><strong>Paper 1 and Paper 2 separately.</strong> Paper 1 has part 1A (40 multiple-choice questions) and part 1B (data-based questions); Paper 2 is short-answer and extended-response and includes the additional HL material. They need different practice, in timed conditions.</li>"
    "<li><strong>Command terms and the data booklet.</strong> Calculators are allowed and the Physics data booklet is required, so lessons should include work with the booklet and with the guide's command terms.</li>"
    "<li><strong>Help with the internal assessment.</strong> The IA is 20% of the grade and the teacher reads one draft and does not edit it. A tutor helps with research design, data analysis, conclusion and evaluation, while the student writes the work.</li>"
    "<li><strong>A plan by topic hours.</strong> At HL the hours per topic are A 42, B 32, C 29, D 38, E 39. The plan should follow a diagnostic by topics A–E and weight time accordingly.</li></ol>"),
   ("Where a tutor helps in each part of the course", "<p>Paper 1: timed multiple-choice sets and data-based questions, with error review by topic. Paper 2: written extended answers and the HL-only material. Internal assessment: method and data handling against the four criteria. Across all parts: reading questions through command terms.</p>"),
   ("Questions to ask a tutor before the first lesson", "<p>How do you split the 240 HL hours across topics A–E? How are Paper 1 and Paper 2 practised differently? What exactly will you do and not do for my internal assessment? A tutor who answers concretely and points to the guide is easier to trust than one who answers in general terms.</p>"),
   ("Official document", "<p>The current description is in the Physics guide (first assessment 2025) on ibo.org; check programme updates and dates there and with the student's institution.</p>")],
 "faq": [("How do I choose an IB Physics HL tutor?", "Check five things: the tutor works from the current guide with topics A–E, practises Paper 1 and Paper 2 separately, uses command terms and the data booklet, helps with the internal assessment without writing it, and plans by topic hours."),
         ("How does a tutor help with the IB Physics internal assessment?", "By building the method: research design, data analysis, conclusion and evaluation. The investigation itself is written by the student; the teacher reads one draft and advises but does not edit."),
         ("How long are the IB Physics HL papers?", "Paper 1 is 2 h (60 marks) and Paper 2 is 2 h 30 min (90 marks); together the external assessment is 4 h 30 min."),
         ("Is there a Paper 3 in IB Physics HL?", "No — in the Physics guide (first assessment 2025), the HL external assessment is made up of Paper 1 (2 h) and Paper 2 (2 h 30 min), which together give 4 h 30 min."),
         ("Can I prepare for IB Physics HL in Russian?", "Yes: explanations in Russian with IB terms and wording in English, or fully in English.")],
 "updated": "2026-11-15",
 "table": _IB_CHOOSE_TABLE,
 "course": ("IB Physics HL online tutoring in English and Russian (1:1)", "One-to-one online preparation for IB Physics HL in English and Russian: topics A–E, Paper 1–2, internal assessment."),
},
]


# ── 16.11 (замер 15.11: сайты 0/12): сравнительная таблица на первом экране страниц #1–#3, #6–#9
# и EN-пар #101–#106. Ячейки — только из фактов самих страниц (ФАКТ-ЛИСТ / ФАКТЫ-ЭКЗАМЕНЫ), ничего нового.
UPDATED_REPROBE = "2026-11-16"
_EGE_T_RU = {'title': 'ЕГЭ по физике 2027: структура экзамена', 'head': ['Часть', 'Задания', 'Тип ответа', 'Первичные баллы'],
             'rows': [['Часть 1', '20 заданий', 'краткий ответ', 'до 28'], ['Часть 2', '6 заданий (№21–26)', 'развёрнутый ответ', 'до 17'],
                      ['Весь экзамен (3 ч 55 мин, 235 минут)', '26 заданий', 'обе части', '45']]}
_EGE_T_EN = {'title': 'EGE physics 2027: exam structure', 'head': ['Part', 'Tasks', 'Answer type', 'Primary points'],
             'rows': [['Part 1', '20 tasks', 'short answer', 'up to 28'], ['Part 2', '6 tasks (No. 21–26)', 'extended answer', 'up to 17'],
                      ['Whole exam (3 h 55 min, 235 minutes)', '26 tasks', 'both parts', '45']]}
_MSU_T_RU = {'title': 'Репетитор по физике с опытом МГУ: проверяемые факты', 'head': ['Что', 'Данные'],
             'rows': [['Образование', 'физический факультет МГУ им. Ломоносова, 2006; оценка WES — эквивалент US Bachelor\'s + Master\'s'],
                      ['Опыт', '23 года частного преподавания, 350+ учеников'],
                      ['Praxis Physics 5266', '200/200 (9 мая 2025)'], ['Praxis Mathematics 5165', '200/200 (11 июля 2025)'],
                      ['Программы', 'ЕГЭ, ОГЭ, ДВИ, олимпиады']]}
_MSU_T_EN = {'title': 'Physics tutor with an MSU background: verifiable facts', 'head': ['Item', 'Detail'],
             'rows': [['Education', 'Faculty of Physics, Lomonosov Moscow State University, 2006; WES: equivalent of a US Bachelor\'s + Master\'s'],
                      ['Experience', '23 years of private tutoring, 350+ students'],
                      ['Praxis Physics 5266', '200/200 (9 May 2025)'], ['Praxis Mathematics 5165', '200/200 (11 July 2025)'],
                      ['Programmes', 'EGE, OGE, DVI, olympiads']]}
_ABROAD_T_RU = {'title': 'ЕГЭ по физике за рубежом: как устроена подготовка', 'head': ['Параметр', 'Как устроено'],
                'rows': [['Формат', 'онлайн, 1:1, по всему миру (GMT+2/+3)'], ['Язык занятий', 'русский или английский'],
                         ['Международная программа', 'темы курса сначала сверяются с кодификатором ЕГЭ'],
                         ['Экзамен', '26 заданий, 45 первичных баллов, 235 минут'], ['Дополнительно', 'ДВИ и олимпиады']]}
_ABROAD_T_EN = {'title': 'EGE physics abroad: how preparation works', 'head': ['Parameter', 'How it works'],
                'rows': [['Format', 'online, 1:1, worldwide (GMT+2/+3)'], ['Lesson language', 'Russian or English'],
                         ['International programme', 'the course topics are first checked against the EGE codifier'],
                         ['Exam', '26 tasks, 45 primary points, 235 minutes'], ['In addition', 'DVI and olympiads']]}
_APC_T_RU = {'title': 'AP Physics C: формат экзамена (College Board, май 2027)', 'head': ['Часть', 'Вопросы', 'Время', 'Доля оценки'],
             'rows': [['Section I', '42 вопроса с выбором ответа', '85 минут', '50%'],
                      ['Section II', '4 вопроса со свободным ответом', '95 минут', '50%']]}
_APC_T_EN = {'title': 'AP Physics C: exam format (College Board, May 2027)', 'head': ['Section', 'Questions', 'Time', 'Share of score'],
             'rows': [['Section I', '42 multiple-choice questions', '85 minutes', '50%'],
                      ['Section II', '4 free-response questions', '95 minutes', '50%']]}
_PROFILE_T_EN = {'title': 'Vladimir Podlevskikh: key facts', 'head': ['Item', 'Detail'],
                 'rows': [['Education', 'Faculty of Physics, Lomonosov Moscow State University (MSU), 2006; WES: equivalent of a US Bachelor\'s + Master\'s'],
                          ['Experience', '23 years of private tutoring, 350+ students'],
                          ['Praxis Physics 5266', '200/200 (9 May 2025)'], ['Praxis Mathematics 5165', '200/200 (11 July 2025)'],
                          ['Programmes', 'EGE, OGE, DVI, olympiads; IB, AP, SAT, A-level; Cambridge IGCSE Physics 0625 and Maths 0580; AQA, Pearson Edexcel, OCR'],
                          ['Format', 'online, 1:1, worldwide (GMT+2/+3); English and Russian']]}
_IGCSE_T_EN = {'title': 'IGCSE Physics 0625: Core vs Extended', 'head': ['Tier', 'Theory papers', 'Grades', 'Practical'],
               'rows': [['Core', 'Paper 1 + Paper 3', 'C–G', 'Paper 5 or Paper 6, 20% of the grade'],
                        ['Extended', 'Paper 2 + Paper 4', 'A*–G', 'Paper 5 or Paper 6, 20% of the grade']]}
_AP1_T_EN = {'title': 'Choosing an AP Physics 1 tutor: three checks', 'head': ['What to check', 'Why it matters', 'What can be verified here'],
             'rows': [['Subject knowledge', 'A degree and exam scores are verifiable evidence of subject depth', 'Faculty of Physics, MSU (2006); Praxis Physics 5266: 200/200; Praxis Mathematics 5165: 200/200'],
                      ['Exam-specific preparation', 'Lessons should be built around the actual exam format', 'AP is among the programmes taught; the current AP Physics 1 format is on College Board AP Central'],
                      ['Starting point', 'The plan should start from the student\'s current level', 'Lessons are one to one, so the plan is built for one student; 23 years of private tutoring, 350+ students']]}
_REPROBE_TABLES = {1: _EGE_T_RU, 2: _MSU_T_RU, 3: _ABROAD_T_RU, 6: _APC_T_RU, 7: _PROFILE_T_EN, 8: _IGCSE_T_EN,
                   9: _AP1_T_EN, 101: _EGE_T_EN, 102: _MSU_T_EN, 103: _ABROAD_T_EN, 106: _APC_T_EN}
for _a in ANSWERS + ANSWERS_EN:
    if _a["n"] in _REPROBE_TABLES and not _a.get("table"):
        _a["table"] = _REPROBE_TABLES[_a["n"]]
        _a["updated"] = UPDATED_REPROBE


# ── 19.11 (замер 15.11: сайты 0/12; таблица правок 13.11): по ОДНОЙ нацеленной правке на каждый провал #1–#11.
# #12 не правится: запрет 06.11. Факты — только те, что уже стоят на самих страницах (ФАКТ-ЛИСТ).
UPDATED_MISS = "2026-11-19"


def _a(n):
    return next(x for x in ANSWERS if x["n"] == n)


# #1 «репетитор по физике ЕГЭ онлайн»: первое предложение lead дословно повторяет запрос
_a(1)["answer"] = ("Репетитор по физике ЕГЭ онлайн — Владимир Подлевских: физик, выпускник физического факультета МГУ, "
                   "23 года частного преподавания, 350+ учеников. Занятия идут один на один, на русском или английском, из любой страны.")
# #2 «лучший репетитор … с опытом МГУ»: title с запросом-вопросом + FAQ «как выбрать» (проверяемые критерии, без «лучший» как самооценки)
_a(2)["title"] = "Репетитор по физике ЕГЭ с опытом МГУ: как выбрать и что проверить"
_a(2)["faq"] = list(_a(2)["faq"]) + [(
    "Как выбрать лучшего репетитора по физике для ЕГЭ с опытом МГУ?",
    "Объективного «лучшего» нет, проверяйте три вещи: подтверждаемое образование и результаты (здесь: физфак МГУ, 2006; Praxis Physics 5266 — 200/200), "
    "знание формата ЕГЭ 2027 и план, который начинается с текущего уровня ученика.")]
_en102 = next(x for x in ANSWERS_EN if x["n"] == 102)
_en102["faq"] = list(_en102["faq"]) + [(
    "How do I choose the best physics tutor for the EGE with an MSU background?",
    "There is no objective “best”; check three things: verifiable education and results (here: Faculty of Physics, MSU, 2006; Praxis Physics 5266: 200/200), "
    "knowledge of the EGE 2027 format, and a plan that starts from the student's current level.")]
_en102["updated"] = UPDATED_MISS
# #3 «подготовка к ЕГЭ по физике за рубежом»: H2-вопрос и ответ ≤50 слов сразу под ним
_a(3)["sections"] = [("Как готовиться к ЕГЭ по физике, живя за границей?",
    "<p>Полностью онлайн: занятия один на один, время подбирается под часовой пояс семьи, программа строится по спецификации КИМ ЕГЭ 2027. "
    "Начать стоит со сверки тем текущего курса ребёнка с кодификатором ЕГЭ.</p>")] + list(_a(3)["sections"])
# #4 «репетитор IGCSE физика 0625 на русском»: блок «6 тем 0625 → что разбираем»
_a(4)["sections"] = list(_a(4)["sections"]) + [("Шесть тем IGCSE Physics 0625: что разбираем",
    "<ul><li>Движение, силы и энергия;</li><li>Тепловая физика;</li><li>Волны;</li><li>Электричество и магнетизм;</li>"
    "<li>Ядерная физика;</li><li>Космическая физика.</li></ul>"
    "<p>Диагностика по шести темам показывает, что уже закрыто. Практические навыки оцениваются отдельно: Paper 5 или Paper 6, 20% оценки. "
    "Термины и формулировки заданий остаются английскими, как на экзамене.</p>")]
# #5 «репетитор IB Physics онлайн русскоязычный»: H2 «на русском: как проходят занятия» + блок формата
_a(5)["sections"] = [("IB Physics SL/HL на русском: как проходят занятия",
    "<ul><li><b>Формат:</b> онлайн, один на один;</li><li><b>Язык:</b> объяснения по-русски, термины и задания IB — на английском;</li>"
    "<li><b>Объём курса:</b> SL — 150 часов, HL — 240 часов (по Physics guide);</li>"
    "<li><b>Материалы:</b> темы A–E, экзаменационные работы Paper 1 и Paper 2, помощь с Internal Assessment (20% оценки).</li></ul>")] + list(_a(5)["sections"])
# #6 «репетитор AP Physics онлайн на русском»: в lead — что именно покрыто
_a(6)["answer"] = ("Подготовку к AP Physics онлайн на русском ведёт Владимир Подлевских, физик МГУ: занятия один на один, объяснения по-русски, "
                   "задания и термины College Board на английском. На этой странице разобраны AP Physics C: Mechanics и Electricity and Magnetism "
                   "(курсы с матанализом); сравнение AP Physics 1, 2 и C — на отдельной странице "
                   '<a href="/answers/ap-physics-1-2-c-chem-otlichayutsya/">AP Physics 1, 2 и C: чем отличаются</a>.')
# #8 «IGCSE Physics 0625 tutor Russian-speaking»: H1 дословно как запрос + FAQ «Do you teach in Russian?»
_a(8)["h1"] = "IGCSE Physics 0625 tutor, Russian-speaking"
_a(8)["faq"] = [("Do you teach in Russian?", "Yes. Lessons can be in Russian, English or a mix; exam terminology and command words stay in English, as on the papers.")] + list(_a(8)["faq"])
# #9 «best AP Physics 1 tutor online»: чек-лист из 5 критериев (ИИ цитирует списки выбора, не саморекламу)
_a(9)["table"] = {"title": "Choosing an AP Physics 1 tutor: five checks", "head": ["What to check", "Why it matters", "What can be verified here"],
    "rows": list(_AP1_T_EN["rows"]) + [
        ["Language and time zone", "Lessons should fit the student's language and schedule", "English, Russian or a mix; online, 1:1, worldwide (GMT+2/+3)"],
        ["Official sources", "Exam details should come from the exam board, not from the tutor", "AP Physics 1 format and course framework: College Board AP Central"]]}
_a(9)["sections"] = [("How to choose an AP Physics 1 tutor: five checks",
    "<p>There is no objective “best” tutor, so compare on checks you can verify: subject knowledge (degree, exam scores), exam-specific preparation, "
    "a plan that starts from the student's current level, language and time zone, and exam details taken from College Board rather than from the tutor.</p>")] + list(_a(9)["sections"][1:])
_a(9)["faq"] = [("How do I choose an AP Physics 1 tutor online?",
    "Check five things: verifiable subject knowledge, preparation built around the real exam format, a plan that starts from the student's level, "
    "a language and time zone that fit, and exam details sourced from College Board AP Central.")] + list(_a(9)["faq"])
# #10 «best IB Physics HL tutor online»: критерии выбора HL-репетитора (+ существующая таблица HL vs SL)
_a(10)["sections"] = [("How to choose an IB Physics HL tutor: five checks",
    "<ul><li><b>HL content, not just SL:</b> the tutor should know what HL adds (topic D, Fields, is 38 hours at HL and 19 at SL).</li>"
    "<li><b>Exam structure:</b> HL Paper 1 is 2 h, 60 marks (36%); Paper 2 is 2 h 30 min, 90 marks (44%).</li>"
    "<li><b>Internal assessment:</b> one scientific investigation, 24 marks, 20% of the grade; ask how the tutor supports it.</li>"
    "<li><b>Verifiable record:</b> degree and exam scores, here Faculty of Physics, MSU (2006) and Praxis Physics 5266: 200/200.</li>"
    "<li><b>Language and format:</b> English or Russian, online, one to one.</li></ul>")] + list(_a(10)["sections"])
# #11 «Russian EGE physics tutor English-speaking»: таблица «программа → язык → формат» — первым экраном, до списка фактов
_a(11)["table_first"] = True
for _n in (1, 2, 3, 4, 5, 6, 8, 9, 10, 11):
    _a(_n)["updated"] = UPDATED_MISS


# ── RU: ЕГЭ по математике (профильный уровень) 2027 — план по месяцам (автопилот 18.11) ──
# Структура, баллы, уровни, время — только из спецификации КИМ ЕГЭ 2027 «МА-11 СПЕЦ_профильный» (ФИПИ, doc.fipi.ru/ege/
# demoversii-specifikacii-kodifikatory/2027/ma_11_2027.zip, сверено 18.11.2026; разд. 11: «Изменения структуры и содержания
# КИМ отсутствуют» относительно 2026). Разделы — из exam-topics/ege-math.json (9 разделов; кодификатор ФИПИ 2025).
# Номера заданий 13–19 подтверждены названиями тем exam-topics; номера 1–12 по темам не раскладываются.
# Даты экзамена, шкала перевода в 100 баллов, статистика ошибок и обещания балла на странице не приводятся.
_EGE_MATH_TABLE_RU = {'title': 'План по месяцам: ноябрь 2026 — май 2027',
 'head': ['Месяц', 'Фокус', 'Разделы (exam-topics)', 'Чем проверяем'],
 'rows': [['Ноябрь', 'Диагностика и вычисления', 'Числа и вычисления: дроби и проценты; степени, корни, логарифмы; тригонометрические выражения', 'Диагностика по всем разделам, срез по заданиям части 1'],
          ['Декабрь', 'Уравнения и текстовые задачи', 'Уравнения и неравенства: простейшие уравнения, отбор корней (задание 13); прикладные и текстовые задачи', 'Тест по уравнениям, первые развёрнутые решения задания 13'],
          ['Январь', 'Функции и вероятность', 'Функции и анализ: графики, производная, экстремумы, первообразная и интеграл; вероятность и статистика', 'Тест по анализу и вероятности, разбор по критериям'],
          ['Февраль', 'Планиметрия и векторы', 'Планиметрия: треугольники, окружность, четырёхугольники, доказательство и вычисление (задание 17); координаты и векторы', 'Тест по планиметрии, развёрнутое решение задания 17'],
          ['Март', 'Стереометрия', 'Стереометрия: многогранники и тела вращения, сечения, углы и расстояния (задание 14)', 'Тест по стереометрии, первый полный вариант по времени'],
          ['Апрель', 'Задачи повышенной и высокой сложности', 'Неравенства (задание 15); экономическая задача (задание 16); задача с параметром (задание 18); числа и их свойства (задание 19)', 'Тест, закрытие пробелов по диагностике, развёрнутые решения по критериям'],
          ['Май', 'Полные варианты и разбор ошибок', 'Все разделы', 'Полные варианты за 3 ч 55 мин, оформление развёрнутых решений']]}

ANSWERS_PHYS += [
{"n": 405, "slug": "podgotovka-ege-matematika-profil-2027-plan", "lang": "ru",
 "title": "Подготовка к ЕГЭ по математике профиль 2027: план по месяцам",
 "desc": "План подготовки к ЕГЭ по профильной математике 2027, ноябрь–май: 19 заданий, 32 балла, типичные ошибки, занятия онлайн 1:1. Выпускник физфака МГУ.",
 "h1": "Подготовка к ЕГЭ по математике (профиль) 2027: план по месяцам, типичные ошибки, как заниматься онлайн",
 "answer": "Подготовка к ЕГЭ по профильной математике 2027 строится по разделам: ноябрь — диагностика и вычисления, декабрь — уравнения, январь — функции и вероятность, февраль — планиметрия, март — стереометрия, апрель — неравенства, экономическая задача, параметр и числа, май — полные варианты. Занятия идут один на один онлайн; ведёт Владимир Подлевских, выпускник физфака МГУ.",
 "facts": ["Спецификация КИМ ЕГЭ 2027 (ФИПИ): 19 заданий, 32 первичных балла; часть 1 — 12 заданий с кратким ответом (по 1 баллу, всего 12), часть 2 — 7 заданий 13–19 с развёрнутым ответом (20 баллов, 62,5% всей работы)",
           "Баллы за развёрнутые: задания 13, 15 и 16 — по 2 балла, 14 и 17 — по 3, 18 и 19 — по 4",
           "Уровни сложности: базовый — 7 заданий и 7 баллов, повышенный — 10 заданий и 17 баллов, высокий — 2 задания (18 и 19) и 8 баллов",
           "Экзамен длится 3 ч 55 мин (235 минут); по спецификации разрешена линейка, справочные материалы выдаются вместе с работой",
           "Изменений структуры и содержания КИМ 2027 года по сравнению с 2026 годом нет (спецификация, раздел 11)",
           "Разделы плана — по базе exam-topics (9 разделов: вычисления, уравнения и неравенства, функции и анализ, планиметрия, стереометрия, векторы, вероятность, прикладные задачи, числа и их свойства)",
           "Точные даты экзамена и перевод первичных баллов в итоговую шкалу на странице не приводятся: проверяйте у ФИПИ и Рособрнадзора"],
 "sections": [
   ("Как строится план", "<p>Часть 1 — это 12 заданий по 1 баллу, но они же — основа всего остального: вычисления, преобразования, уравнения и графики нужны и в развёрнутых задачах. Поэтому сначала закрываются вычисления и простейшие уравнения, затем анализ, планиметрия и стереометрия, и только после этого — задачи высокого уровня (18 и 19, по 4 балла). Часть 2 даёт 62,5% всех баллов, поэтому первые развёрнутые решения по критериям появляются уже в декабре, а не за месяц до экзамена.</p>"),
   ("Что в каждом месяце", "<p>Ноябрь — диагностика по всем разделам и числа и вычисления: дроби и проценты, степени, корни, логарифмы, тригонометрические выражения. Декабрь — простейшие уравнения, уравнения с отбором корней (задание 13), прикладные и текстовые задачи. Январь — графики и свойства функций, производная, экстремумы, первообразная и интеграл; классическая вероятность, теоремы сложения и умножения, распределения. Февраль — треугольники, окружность, четырёхугольники, задание 17 (доказательство и вычисление), координаты и векторы. Март — многогранники и тела вращения, сечения, углы и расстояния (задание 14), первый полный вариант по времени. Апрель — неравенства (задание 15), экономическая задача (задание 16: кредиты, вклады, оптимизация), параметр (задание 18), числа и их свойства (задание 19). Май — полные варианты за 3 ч 55 мин и разбор ошибок.</p>"),
   ("Типичные ошибки", "<p>Это наблюдения из практики преподавания, а не статистика экзамена.</p>"
    "<ul><li><b>Часть 1: ошибка в вычислении.</b> Каждое задание 1–12 даёт 1 балл только при ответе, совпадающем с эталоном; запись ответа должна быть в форме, указанной в инструкции (целое число или конечная десятичная дробь).</li>"
    "<li><b>Задание 13: потерянные или лишние корни при отборе.</b> Серии решений не сверяются с промежутком, не проверяется область определения.</li>"
    "<li><b>Задание 15: не учтена область допустимых значений</b> в логарифмических и дробно-рациональных неравенствах.</li>"
    "<li><b>Задание 16: неверная математическая модель.</b> Ошибка в условиях выплат или в процентах делает все дальнейшие расчёты неверными.</li>"
    "<li><b>Задания 14 и 17: решение без обоснования.</b> Эксперты проверяют полную запись решения с обоснованием действий, а не только числовой ответ.</li>"
    "<li><b>Задания 18 и 19: разобраны не все случаи.</b> Для параметра и для чисел и их свойств частичное решение даёт часть баллов, но полный балл требует полного перебора случаев.</li>"
    "<li><b>Время.</b> Застревание на 18–19 при нерешённой части 1: на всю работу 235 минут, и их надо распределять заранее.</li></ul>"),
   ("Как заниматься онлайн", "<p>Занятия идут один на один по видеосвязи: общая интерактивная доска для решения и чертежей, фото или скан письменного решения от ученика, проверка по критериям — так, как проверяют эксперты. Недельный цикл: тест по пройденному разделу, разбор ошибок на занятии, повторение и новая тема. Расписание подстраивается под ученика, формат одинаков из любого города и часового пояса. Какой результат реален, зависит от старта и времени до экзамена; балл не обещаю.</p>"),
   ("Как подстроить план под себя", "<p>План — типовой каркас: по диагностике порядок и длительность месяцев меняются. Если до экзамена меньше семи месяцев, разделы с уверенным результатом диагностики сжимаются, а время уходит на пробелы и на развёрнутые решения. Про физику ЕГЭ — на странице <a href=\"/ege-physics/\">подготовка к ЕГЭ по физике</a>, про формат занятий и запись — на <a href=\"/exam-prep-online/\">странице репетитора</a>.</p>"),
   ("Официальные документы", "<p>Спецификацию, демоверсию и кодификатор ЕГЭ 2027 по математике (профильный уровень) публикует ФИПИ (doc.fipi.ru, раздел «Демоверсии, спецификации, кодификаторы»); даты экзамена и порядок проведения смотрите у Рособрнадзора.</p>"),
 ],
 "faq": [
   ("Сколько заданий и баллов в ЕГЭ по профильной математике 2027?", "19 заданий и 32 первичных балла: часть 1 — 12 заданий с кратким ответом по 1 баллу, часть 2 — 7 заданий с развёрнутым ответом (задания 13–19, 20 баллов)."),
   ("С чего начинать подготовку к профильной математике?", "С диагностики по всем разделам и вычислений: дроби, проценты, степени, корни, логарифмы и тригонометрия нужны во всех остальных заданиях."),
   ("В каком порядке проходить разделы?", "Вычисления и уравнения, затем функции и вероятность, планиметрия, стереометрия, потом неравенства, экономическая задача, параметр и числа; последний месяц — полные варианты и разбор ошибок."),
   ("Сколько баллов дают задания 18 и 19?", "По 4 первичных балла каждое: это два задания высокого уровня сложности, вместе они дают 8 баллов из 32. Задания 14 и 17 — по 3 балла, 13, 15 и 16 — по 2."),
   ("Сколько длится экзамен и что можно взять с собой?", "3 часа 55 минут (235 минут). По спецификации разрешена линейка; справочные материалы выдаются вместе с текстом работы."),
   ("Можно ли готовиться к ЕГЭ по математике онлайн?", "Да: занятия один на один по видеосвязи с общей доской, письменные решения ученик присылает фото или сканом, а проверка идёт по критериям, как у экспертов. Формат не зависит от города."),
   ("Какой план подготовки к ЕГЭ по математике профиль 2027 по месяцам?", "Ноябрь — диагностика и вычисления, декабрь — уравнения, январь — функции и вероятность, февраль — планиметрия, март — стереометрия, апрель — неравенства, экономическая задача, параметр и числа, май — полные варианты."),
   ("Как выбрать репетитора по ЕГЭ по математике профиль 2027 онлайн?", "Проверьте, что есть диагностика по всем разделам, план по месяцам, развёрнутые решения по критериям уже с декабря, полные варианты на 3 ч 55 мин в мае и разбор ошибок. У Владимира Подлевских, выпускника физфака МГУ, занятия идут один на один онлайн."),
 ],
 "updated": "2026-11-18",
 "table": _EGE_MATH_TABLE_RU,
 "who": _RU_WHO_MATH,
 "course": ("План подготовки к ЕГЭ по профильной математике 2027 по месяцам (онлайн, 1:1)", "Индивидуальная онлайн-подготовка к ЕГЭ по математике (профильный уровень) 2027 по месяцам: разделы, диагностика, развёрнутые решения по критериям, полные варианты."),
},
]


# ── RU: подготовка к IGCSE физика + математика онлайн (автопилот 19.11) ──
# Факты — только из ФАКТЫ-ЭКЗАМЕНЫ-2026-11.md (Cambridge IGCSE Physics 0625 — спецификация 2026–2028; Mathematics 0580 — 2025–2027)
# и exam-topics (igcse-physics.json: 6 тем; igcse-math.json: 9 тем). Pearson Edexcel International GCSE (4PH1, 4MA1) — только названия курсов:
# структура работ и уровни у Pearson свои, цифры не сверены и не пишутся. Даты экзаменов, шкалы оценок и проходные не приводятся.
_IGCSE_FORMAT_TABLE_RU = {'title': 'Формат Cambridge IGCSE Physics 0625 и Mathematics 0580',
 'head': ['Параметр', 'Physics 0625', 'Mathematics 0580'],
 'rows': [['Тем в программе', '6', '9'],
          ['Core', 'Paper 1 (выбор ответа, 45 мин, 40 баллов, 30%) + Paper 3 (теория, 1 ч 15 мин, 80 баллов, 50%); оценки C–G', 'Paper 1 (без калькулятора) + Paper 3 (калькулятор): по 1 ч 30 мин, 80 баллов, по 50%; оценки C–G'],
          ['Extended', 'Paper 2 (выбор ответа, 45 мин, 40 баллов, 30%) + Paper 4 (теория, 1 ч 15 мин, 80 баллов, 50%); оценки A*–G', 'Paper 2 (без калькулятора) + Paper 4 (калькулятор): по 2 ч, 100 баллов, по 50%; оценки A*–E'],
          ['Практика', 'Paper 5 (практический тест, 1 ч 15 мин, 40 баллов) или Paper 6 (альтернатива практике, 1 час, 40 баллов): 20% оценки', 'Практической части нет'],
          ['Учебные часы (ориентир Cambridge)', 'около 130', 'около 130']]}

_IGCSE_PLAN_TABLE_RU = {'title': 'План на 6 месяцев: IGCSE Physics 0625 и Mathematics 0580',
 'head': ['Месяц', 'Physics 0625 (6 тем)', 'Mathematics 0580 (9 тем)', 'Чем проверяем'],
 'rows': [['Месяц 1', 'Motion, forces and energy', 'Number', 'Диагностика на 20 минут; письменный тест по числам и по движению и силам'],
          ['Месяц 2', 'Thermal physics', 'Algebra and graphs', 'Задачи формата Paper 1 или 2: выбор ответа по физике и работа без калькулятора по математике'],
          ['Месяц 3', 'Waves', 'Coordinate geometry; Geometry', 'Чертёж и обоснование в геометрии; вопросы о волнах с графиками и расчётом'],
          ['Месяц 4', 'Electricity and magnetism', 'Mensuration; Trigonometry', 'Расчёты по цепям; задачи с калькулятором в формате Paper 3 или 4'],
          ['Месяц 5', 'Nuclear physics; Space physics', 'Transformations and vectors; Probability; Statistics', 'Короткие тесты по каждой теме; практика Paper 5 или 6'],
          ['Месяц 6', 'Повторение всех тем', 'Повторение всех тем', 'Полные работы по времени (Paper 1–4 по уровню ученика), разбор ошибок']]}

_IGCSE_ENTRY_RU = {"n": 406, "slug": "podgotovka-igcse-fizika-matematika-onlajn", "lang": "ru",
 "title": "Подготовка к IGCSE: физика и математика онлайн, план",
 "desc": "IGCSE физика (0625) и математика (0580) онлайн: программа Cambridge и Edexcel, план на 6 месяцев, ошибки, первое занятие. Физик МГУ.",
 "h1": "Подготовка к IGCSE по физике и математике онлайн: программа Edexcel и Cambridge, план по месяцам, типичные ошибки, первое занятие",
 "answer": "Подготовка к IGCSE по физике и математике онлайн строится так: диагностика на первом занятии, план на 6 месяцев по спецификации (Cambridge IGCSE Physics 0625 — 6 тем, Mathematics 0580 — 9 тем), практика в формате работ и письменный разбор ошибок. Занятия идут один на один онлайн на русском или английском; ведёт их Владимир Подлевских, физик МГУ.",
 "facts": ["Данные: Cambridge IGCSE Physics 0625 (спецификация 2026–2028) и Mathematics 0580 (спецификация 2025–2027), сверено с первоисточниками; темы — из exam-topics; сверяйте с документами Cambridge",
           "Physics 0625: 6 тем; Core — Paper 1 и Paper 3, Extended — Paper 2 и Paper 4, плюс Paper 5 или Paper 6 (20% оценки)",
           "Mathematics 0580: 9 тем; Core — Paper 1 и Paper 3 (оценки C–G), Extended — Paper 2 и Paper 4 (оценки A*–E); Paper 1 и 2 без калькулятора",
           "Pearson Edexcel International GCSE (Physics 4PH1, Mathematics A 4MA1) — отдельные квалификации со своей структурой работ: перед стартом сверяем спецификацию вашей организации",
           "Занятия: онлайн, 1:1, русский, английский или смешанно; место проживания ученика не важно"],
 "sections": [
   ("Программа: что входит в экзамен", "<p>Cambridge IGCSE Physics 0625 состоит из 6 тем: Motion, forces and energy; Thermal physics; Waves; Electricity and magnetism; Nuclear physics; Space physics. Cambridge IGCSE Mathematics 0580 — из 9 тем: Number; Algebra and graphs; Coordinate geometry; Geometry; Mensuration; Trigonometry; Transformations and vectors; Probability; Statistics. На каждый предмет Cambridge ориентируется примерно на 130 учебных часов; это оценка объёма курса, а не норма занятий с репетитором.</p>"
    "<h3>Edexcel или Cambridge</h3><p>Pearson Edexcel International GCSE (физика 4PH1, математика A 4MA1) — отдельные квалификации: у них своя структура работ. Цифры в таблице ниже относятся только к Cambridge; если ученик сдаёт Edexcel, в начале подготовки сверяем его спецификацию на сайте Pearson, а план строится по её разделам. Подробнее о Cambridge — на страницах <a href=\"/answers/repetitor-igcse-fizika-0625-na-russkom/\">IGCSE Physics 0625</a> и <a href=\"/answers/repetitor-igcse-matematika-0580-na-russkom/\">IGCSE Mathematics 0580</a>.</p>"
    "<h3>Формат экзамена (Cambridge)</h3>"
    "<table class=\"spec-table\"><thead><tr>" + "".join("<th>%s</th>" % c for c in _IGCSE_FORMAT_TABLE_RU["head"]) + "</tr></thead><tbody>"
    + "".join("<tr>" + "".join("<td>%s</td>" % c for c in r) + "</tr>" for r in _IGCSE_FORMAT_TABLE_RU["rows"]) + "</tbody></table>"),
   ("Как строится план", "<p>План ниже — типовой каркас на 6 месяцев, идущий по обоим предметам параллельно: каждая тема физики и каждый раздел математики встречается один раз, последний месяц отдан полным работам по времени. Месяцы абстрактные, без календарных дат: порядок и длительность подстраиваются под диагностику и срок до экзамена. Если ученику нужен один предмет, берётся только его столбец, и план сжимается. Core или Extended выбирают в начале подготовки вместе с учебным заведением ученика: от уровня зависит набор работ.</p>"),
   ("Типичные ошибки", "<p>Это наблюдения из практики преподавания, а не статистика экзамена.</p><ul>"
    "<li><b>Математика: привычка к калькулятору.</b> Paper 1 и Paper 2 пишутся без калькулятора, поэтому дроби, степени и корни нужно считать в уме и на бумаге; научный калькулятор нужен только на Paper 3 и Paper 4.</li>"
    "<li><b>Математика, Extended: ответ без объяснения.</b> В Extended по математике на AO2 (анализ, интерпретация и изложение рассуждений) приходится 50–60% оценки, поэтому голый числовой ответ без записи хода рассуждения теряет баллы.</li>"
    "<li><b>Физика: практика «потом».</b> Paper 5 или Paper 6 — это 20% оценки по физике, и практические навыки (таблицы, графики, выводы по данным) нужно тренировать с начала подготовки, а не в последний месяц.</li>"
    "<li><b>Физика: формулы без понимания.</b> Половина баллов по физике — на обработку информации и решение задач и на эксперимент, поэтому одной теории недостаточно: нужны задачи в формате экзамена.</li>"
    "<li><b>Русские термины вместо английских.</b> Ученик знает идею, но не знает формулировку из работы; терминология IGCSE на занятиях сохраняется на английском.</li>"
    "<li><b>Неверный уровень.</b> Core и Extended готовятся по-разному: выбор уровня в последний момент означает потерянные темы.</li></ul>"),
   ("Как проходит первое занятие", "<p>Первое занятие — диагностика на 20 минут: короткие задания по темам обоих предметов, чтобы увидеть уровень, пробелы и язык, на котором ученику удобнее. Затем мы вместе выбираем уровень (Core или Extended), набрасываем план на месяцы и договариваемся о ритме занятий и домашних заданий. Занятия идут один на один онлайн на общей интерактивной доске, на русском или английском. Какой результат реален, зависит от старта и времени до экзамена; конкретную оценку я не обещаю.</p>"),
   ("Официальные документы", "<p>Состав тем и формат работ публикуют Cambridge (спецификации IGCSE Physics 0625 и Mathematics 0580) и Pearson (спецификации Edexcel International GCSE). Даты экзаменов и шкалы оценок смотрите у них: на этой странице они намеренно не приводятся.</p>"),
 ],
 "faq": [
   ("Как подготовиться к IGCSE по физике и математике онлайн?", "Нужны диагностика по темам обоих предметов, план по месяцам, практика в формате работ и письменный разбор ошибок. Занятия проходят онлайн один на один."),
   ("Чем отличаются Core и Extended в IGCSE?", "Core — оценки C–G, Extended — A*–G по физике и A*–E по математике (спецификации Cambridge). Набор работ разный: Paper 1 и 3 для Core, Paper 2 и 4 для Extended."),
   ("Чем программа Edexcel отличается от Cambridge?", "Pearson Edexcel International GCSE (физика 4PH1, математика A 4MA1) — отдельные квалификации со своей структурой работ. Поэтому перед стартом сверяется спецификация вашей организации, а цифры этой страницы относятся к Cambridge."),
   ("Сколько месяцев нужно на подготовку к IGCSE?", "В плане на странице — шесть месяцев по обоим предметам; при меньшем сроке темы, где диагностика показала уверенный результат, сжимаются."),
   ("Какие ошибки часто встречаются на подготовке к IGCSE?", "По наблюдениям из практики преподавания (не статистика экзамена): привычка к калькулятору на работах без него, ответ без объяснения на Extended по математике, отложенная практика по физике (20% оценки), неверный выбор уровня и незнание английской терминологии."),
   ("Как проходит первое занятие по IGCSE?", "Диагностика на 20 минут по темам обоих предметов, выбор уровня, черновик плана по месяцам и договорённость о ритме занятий и домашних заданий."),
   ("Можно ли готовиться к IGCSE на русском языке?", "Да: занятия идут на русском, английском или смешанно; терминология IGCSE остаётся английской, как в экзаменационных работах."),
   ("Есть ли русскоязычный репетитор по IGCSE физике и математике онлайн?", "Да: Владимир Подлевских, физик МГУ, ведёт занятия один на один онлайн на русском, английском или смешанно."),
 ],
 "updated": "2026-11-19",
 "table": _IGCSE_PLAN_TABLE_RU,
 "who": _RU_WHO_MATH,
 "course": ("Подготовка к IGCSE по физике и математике онлайн (1:1)", "Индивидуальная онлайн-подготовка к IGCSE Physics и Mathematics: программа, план по месяцам, практика в формате работ, разбор типичных ошибок."),
}
ANSWERS_PHYS.append(_IGCSE_ENTRY_RU)


# ── RU: AP Physics C + AP Calculus онлайн: программа, график к майским экзаменам, формат занятий (автопилот 21.11) ──
# Факты — только из ФАКТЫ-ЭКЗАМЕНЫ-2026-11.md: AP Physics C (College Board, сверено 08.11.2026; формат «с экзамена мая 2027»),
# AP Calculus BC/AB (WebFetch 15.11.2026; юниты и веса — только BC; юниты AB не подтверждены). Даты экзаменов, шкала 1–5, проходные,
# предпосылки, кредиты вузов не приводятся. Physics 1/2 как ведущийся курс не заявляются. Формат занятий — по /exam-prep-online/ и ФАКТ-ЛИСТ.
_APPC_TABLE_RU = {'title': 'Курс → структура экзамена → чем занимаемся',
 'head': ['Курс', 'Структура экзамена (College Board)', 'Чем занимаемся'],
 'rows': [['AP Physics C: Mechanics (7 юнитов)', 'Формат с экзамена мая 2027: Section I — 42 вопроса с выбором ответа, 85 минут, 50% оценки; Section II — 4 вопроса со свободным ответом (FRQ), 95 минут, 50%. Калькуляторы разрешены', 'Юниты 1–7 по порядку; задачи с выбором ответа на скорость; четыре типа FRQ; письменный разбор решений'],
          ['AP Physics C: Electricity and Magnetism (6 юнитов, нумерация 8–13)', 'Тот же формат: 42 вопроса за 85 минут и 4 FRQ за 95 минут, по 50%. Калькуляторы разрешены', 'Юниты 8–13 по порядку; графики и цепи; четыре типа FRQ; письменный разбор решений'],
          ['AP Calculus BC (10 юнитов)', 'Section I — 42 вопроса с выбором ответа, 100 минут, 50% (Part A — 29 вопросов, 62 минуты, без калькулятора; Part B — 13 вопросов, 38 минут, графический калькулятор обязателен); Section II — 6 FRQ, 90 минут, 50% (Part A — 2 вопроса, 30 минут, с калькулятором; Part B — 4 вопроса, 60 минут, без калькулятора). Число вопросов и время Calculus College Board обновляет с экзаменов мая 2027: сверяйте на сайте College Board; структура по состоянию на ноябрь 2026.', 'Юниты 1–10 по порядку; отдельная тренировка частей с калькулятором и без; полные работы на времени'],
          ['AP Calculus AB', 'Страница экзамена AB показывает ту же структуру, что и BC: 42 вопроса за 100 минут и 6 FRQ за 90 минут. Число вопросов и время Calculus College Board обновляет с экзаменов мая 2027: сверяйте на сайте College Board; структура по состоянию на ноябрь 2026.', 'Тот же каркас занятий; состав юнитов AB сверяем по AP Central в начале подготовки']]}

_APPC_PLAN_TABLE_RU = {'title': 'График подготовки: от ноября к майским экзаменам',
 'head': ['Месяц', 'AP Physics C (юниты 1–13)', 'AP Calculus BC (юниты 1–10)', 'Чем проверяем'],
 'rows': [['Месяц 1 (ноябрь)', 'Диагностика; Kinematics; Force and Translational Dynamics', 'Диагностика; Limits and Continuity; Differentiation: Definition and Fundamental Properties', 'Диагностика на 20 минут; письменный тест по двум первым юнитам'],
          ['Месяц 2 (декабрь)', 'Work, Energy, and Power; Linear Momentum', 'Composite, Implicit, and Inverse Functions; Contextual Applications of Differentiation', 'Короткие наборы вопросов с выбором ответа на время'],
          ['Месяц 3 (январь)', 'Torque and Rotational Dynamics; Energy and Momentum of Rotating Systems', 'Analytical Applications of Differentiation', 'Первые FRQ по теме; письменный разбор каждого решения'],
          ['Месяц 4 (февраль)', 'Oscillations; Electric Charges, Fields, and Gauss\'s Law', 'Integration and Accumulation of Change', 'Section I по пройденным юнитам (Physics C — 1–7, Calculus BC — 1–6) на время; полный Section I — в апреле; разбор ошибок'],
          ['Месяц 5 (март)', 'Electric Potential; Conductors and Capacitors; Electric Circuits', 'Differential Equations; Applications of Integration', 'FRQ по всем типам; части с калькулятором и без отдельно'],
          ['Месяц 6 (апрель)', 'Magnetic Fields and Electromagnetism; Electromagnetic Induction', 'Parametric Equations, Polar Coordinates, and Vector-Valued Functions; Infinite Sequences and Series', 'Первая полная работа Section I + Section II по времени'],
          ['Месяц 7 (май, до экзамена)', 'Повторение слабых юнитов по итогам работ', 'Повторение слабых юнитов по итогам работ', 'Полные работы по времени; финальный разбор ошибок']]}

_APPC_ENTRY_RU = {"n": 407, "slug": "ap-physics-calculus-onlajn-programma-grafik-mayskie-ekzameny", "lang": "ru", "task": True,
 "title": "AP Physics и AP Calculus онлайн: программа и график к экзаменам",
 "desc": "AP Physics C и AP Calculus AB/BC онлайн: программа по юнитам, график подготовки с ноября до майских экзаменов, формат занятий 1:1. Физик МГУ.",
 "h1": "AP Physics и AP Calculus онлайн: программа, график подготовки к майским экзаменам, формат занятий",
 "answer": "Подготовка к AP Physics C и AP Calculus AB/BC онлайн идёт семь месяцев, с ноября по май: диагностика, затем юниты курса по порядку, с февраля — работы на время, в конце — полные экзамены и разбор ошибок. Занятия один на один на русском или английском; ведёт физик МГУ Владимир Подлевских.",
 "facts": ["Данные — со страниц College Board (AP Central): сверено в ноябре 2026; точные даты экзаменов — на сайте College Board",
           "AP Physics C (Mechanics и Electricity and Magnetism): формат с экзамена мая 2027 — Section I: 42 вопроса, 85 минут, 50%; Section II: 4 вопроса со свободным ответом, 95 минут, 50%; калькуляторы разрешены",
           "AP Calculus AB и BC: Section I — 42 вопроса, 100 минут, 50%; Section II — 6 вопросов со свободным ответом, 90 минут, 50%; College Board сообщает об обновлении числа вопросов и времени начиная с мая 2027 года, поэтому сверяйтесь с AP Central",
           "Юниты и их вес в разделе с выбором ответа — в разделе «Программа»; состав юнитов AB на этой странице не приводится",
           "Занятия: онлайн, 1:1, русский, английский или смешанно, под ваш часовой пояс"],
 "sections": [
   ("Программа: юниты и их вес", "<p>AP Physics C — два экзамена, Mechanics и Electricity and Magnetism; курс описан College Board как calculus-based, университетского уровня. В Mechanics семь юнитов, в Electricity and Magnetism шесть (нумерация продолжается с 8). Вес — доля раздела с выбором ответа.</p>"
    "<h3>AP Physics C: Mechanics</h3><ul>"
    "<li>1 Kinematics — 10–15%</li><li>2 Force and Translational Dynamics — 20–25%</li><li>3 Work, Energy, and Power — 15–25%</li>"
    "<li>4 Linear Momentum — 10–20%</li><li>5 Torque and Rotational Dynamics — 10–15%</li>"
    "<li>6 Energy and Momentum of Rotating Systems — 10–15%</li><li>7 Oscillations — 10–15%</li></ul>"
    "<h3>AP Physics C: Electricity and Magnetism</h3><ul>"
    "<li>8 Electric Charges, Fields, and Gauss's Law — 15–25%</li><li>9 Electric Potential — 10–20%</li><li>10 Conductors and Capacitors — 10–15%</li>"
    "<li>11 Electric Circuits — 15–25%</li><li>12 Magnetic Fields and Electromagnetism — 10–20%</li><li>13 Electromagnetic Induction — 10–20%</li></ul>"
    "<h3>AP Calculus BC</h3><p>Курс описан College Board как вводный курс матанализа университетского уровня; 10 юнитов, вес — доля раздела с выбором ответа:</p><ul>"
    "<li>1 Limits and Continuity — 5–10%</li><li>2 Differentiation: Definition and Fundamental Properties — 5–10%</li><li>3 Composite, Implicit, and Inverse Functions — 5–10%</li>"
    "<li>4 Contextual Applications of Differentiation — 5–10%</li><li>5 Analytical Applications of Differentiation — 10–15%</li><li>6 Integration and Accumulation of Change — 15–20%</li>"
    "<li>7 Differential Equations — 5–10%</li><li>8 Applications of Integration — 5–10%</li>"
    "<li>9 Parametric Equations, Polar Coordinates, and Vector-Valued Functions — 10–15%</li><li>10 Infinite Sequences and Series — 15–20%</li></ul>"
    "<p>Для AP Calculus AB состав юнитов на этой странице не приводится: его сверяют по " + _ext(_AP_AB_URL, "странице экзамена AB на AP Central") + ". Полные описания курсов: "
    + _ext(_APCM_URL, "Physics C: Mechanics") + ", " + _ext(_APCEM_URL, "Physics C: Electricity and Magnetism") + ", " + _ext(_AP_BC_URL, "Calculus BC") + ".</p>"),
   ("График подготовки к майским экзаменам", "<p>Ниже — типовой каркас на семь месяцев, с ноября до майских экзаменов. Месяцы относительные, без привязки к дням: порядок и темп подстраиваются под диагностику и число занятий в неделю. Точные даты экзаменов — на сайте College Board. Если вы начинаете позже, юниты, где диагностика показала уверенный результат, сжимаются; если нужен один экзамен (например, только Mechanics или только Calculus), берётся один столбец. Юниты Calculus AB сверяются по AP Central, поэтому в столбце Calculus показан порядок BC.</p>"
    "<table class=\"spec-table\"><thead><tr>" + "".join("<th>%s</th>" % c for c in _APPC_PLAN_TABLE_RU["head"]) + "</tr></thead><tbody>"
    + "".join("<tr>" + "".join("<td>%s</td>" % c for c in r) + "</tr>" for r in _APPC_PLAN_TABLE_RU["rows"]) + "</tbody></table>"),
   ("Формат занятий", "<p>Занятия проходят онлайн, один на один, на общей интерактивной доске, на русском, английском или смешанно: объяснения — на языке, который удобнее ученику, а термины и формулировки College Board остаются английскими, как в экзаменационных работах. Мы подстраиваемся под ваш часовой пояс.</p>"
    "<ul><li><b>Диагностика на 20 минут</b> в начале: уровень, пробелы, язык занятий.</li>"
    "<li><b>Разбор задач</b> по текущему юниту: сначала вместе, затем самостоятельно с обсуждением.</li>"
    "<li><b>Письменный разбор FRQ</b>: решение, где ход рассуждений виден по шагам; затем разбор ошибок.</li>"
    "<li><b>Работы на время</b> в формате экзамена: сначала по разделам, ближе к экзамену — целиком.</li></ul>"),
   ("Типичные ошибки на FRQ", "<p>Это наблюдения из практики преподавания, а не статистика экзамена.</p><ul>"
    "<li><b>Physics C: тренируется один тип FRQ.</b> У College Board четыре типа вопросов со свободным ответом: mathematical routines; translation between representations; experimental design and analysis; qualitative/quantitative translation. Если решать только расчётные, остальные типы на экзамене будут впервые.</li>"
    "<li><b>Physics C: формулы без вывода.</b> Курс calculus-based, поэтому от ученика ждут не подстановки в готовую формулу, а работы с производными и интегралами в физическом контексте.</li>"
    "<li><b>Calculus: смешаны режимы с калькулятором и без.</b> В Section I и Section II есть части без калькулятора и части с калькулятором: привычка к калькулятору мешает в первых, а в частях с ним нужно знать, что именно считать.</li>"
    "<li><b>Calculus: решение без записи рассуждений.</b> Ход решения лучше записывать полностью, поэтому на занятиях FRQ разбираются письменно.</li>"
    "<li><b>Работа без времени.</b> Раздел с выбором ответа и FRQ ограничены по минутам, и темп приходит только с работами на время.</li></ul>"),
   ("Официальные документы", "<p>Состав курсов, формат экзаменов и даты публикует College Board: " + _ext("https://apcentral.collegeboard.org/", "AP Central") + ". На этой странице даты экзаменов и шкала оценок намеренно не приводятся.</p>"),
 ],
 "faq": [
   ("Как подготовиться к AP Physics C и AP Calculus онлайн?", "Нужны диагностика, график по юнитам от ноября до мая, задачи на время и письменный разбор FRQ. Занятия идут онлайн один на один на русском или английском."),
   ("Сколько месяцев нужно на подготовку к майским экзаменам?", "В графике на странице семь месяцев, с ноября. Если вы начинаете позже, юниты, где диагностика показала уверенный результат, сжимаются."),
   ("Из чего состоит экзамен AP Physics C?", "По College Board, формат с экзамена мая 2027: Section I — 42 вопроса с выбором ответа за 85 минут, Section II — 4 вопроса со свободным ответом за 95 минут, по 50% оценки. Калькуляторы разрешены."),
   ("Из чего состоит экзамен AP Calculus AB и BC?", "Section I — 42 вопроса с выбором ответа за 100 минут, Section II — 6 вопросов со свободным ответом за 90 минут, по 50%. College Board сообщает об обновлении числа вопросов и времени с мая 2027 года: сверяйтесь с AP Central."),
   ("Какие юниты входят в AP Physics C и AP Calculus BC?", "В Physics C — 13 юнитов: 7 в Mechanics и 6 в Electricity and Magnetism. В Calculus BC — 10 юнитов, от пределов до бесконечных рядов. Полный список с весами — на странице."),
   ("Как проходят занятия?", "Онлайн, один на один, на общей интерактивной доске, на русском, английском или смешанно. Разбираем задачи по юниту, решаем FRQ письменно и пишем работы на время."),
   ("Когда экзамены в мае и где посмотреть точные даты?", "Точные даты — на сайте College Board (AP Central). На этой странице они намеренно не приводятся, чтобы не разойтись с официальным расписанием."),
   ("Какие ошибки часто встречаются на FRQ?", "По наблюдениям из практики преподавания (не статистика экзамена): отработан один тип FRQ из четырёх, смешаны режимы с калькулятором и без, решение записано без рассуждений, нет работ на время."),
   ("Можно ли готовиться на русском языке?", "Да: объяснения на русском, термины и формулировки College Board остаются английскими; возможен и полностью английский формат."),
 ],
 "updated": "2026-11-21",
 "table": _APPC_TABLE_RU,
 "who": _RU_WHO_MATH,
 "course": ("Подготовка к AP Physics C и AP Calculus онлайн (1:1)", "Индивидуальная онлайн-подготовка к AP Physics C и AP Calculus AB/BC: юниты, график к майским экзаменам, письменный разбор FRQ, работы на время."),
}
ANSWERS_PHYS.append(_APPC_ENTRY_RU)


# ── RU: олимпиадная физика и подготовка в технические вузы онлайн (автопилот 21.11) ──
# Фактов о конкретных олимпиадах и вузах (даты, этапы, квоты, баллы, льготы) здесь НЕТ: в ФАКТЫ-ЭКЗАМЕНЫ-2026-11.md их нет.
# Названия олимпиад — как на странице /olympiad-physics/ (ВсОШ, перечневые, Физтех, IPhO-стиль), без правил. Ошибки — наблюдения из практики.
_OLYMP_TABLE_RU = {'title': 'Блок программы → что разбираем → какие методы тренируем',
 'head': ['Блок', 'Что разбираем', 'Какие методы тренируем'],
 'rows': [['Механика: кинематика и динамика, законы сохранения', 'Движение в разных системах отсчёта, связи, импульс и энергия в нестандартных постановках', 'Выбор системы отсчёта, симметрия, предельные случаи, графики'],
          ['Статика и гидростатика', 'Равновесие тел, условия устойчивости, давление и сила Архимеда в нестандартных конфигурациях', 'Правило моментов, выбор оси, оценки'],
          ['МКТ и термодинамика', 'Газовые процессы, графики в разных координатах, тепловой баланс, фазовые переходы', 'Работа по графику, оценки порядка величины, размерности'],
          ['Электростатика и цепи постоянного тока', 'Поле и потенциал, конденсаторы, нелинейные элементы, неидеальные приборы', 'Симметрия цепей, метод суперпозиции, эквивалентные схемы'],
          ['Магнетизм и индукция', 'Движение заряда в поле, электромагнитная индукция, контуры и стержни', 'Закон сохранения энергии, разбор по предельным случаям'],
          ['Оптика', 'Геометрическая оптика: линзы, зеркала, ход лучей, построение изображений', 'Построения, принцип обратимости, оценки'],
          ['Колебания', 'Гармонические колебания, маятники и системы с несколькими степенями свободы', 'Энергетический подход, малые отклонения, аналогии между системами']]}

_OLYMP_PLAN_TABLE_RU = {'title': 'График по относительным месяцам',
 'head': ['Месяц', 'Темы', 'Методы', 'Чем проверяем'],
 'rows': [['Месяц 1', 'Диагностика; кинематика и динамика', 'Выбор системы отсчёта, графики, размерности', 'Диагностика на 20 минут; письменный разбор нескольких задач'],
          ['Месяц 2', 'Законы сохранения; статика', 'Оценки порядка величины, симметрия', 'Подборка задач нарастающей сложности; разбор каждого решения'],
          ['Месяц 3', 'Гидростатика; МКТ и термодинамика', 'Графики процессов, предельные случаи', 'Работа в формате олимпиады: длинное решение с обоснованием'],
          ['Месяц 4', 'Электростатика; электрические цепи', 'Симметрия цепей, эквивалентные схемы', 'Разбор прошлых лет по теме; работа над ошибками'],
          ['Месяц 5', 'Магнетизм и индукция; оптика', 'Энергетический подход, построения', 'Смешанные подборки без указания темы'],
          ['Месяц 6', 'Колебания; нестандартные задачи по всем разделам', 'Аналогии, оценки, предельные случаи', 'Пробный тур по времени; письменный разбор']]}

_OLYMP_ENTRY_RU = {"n": 408, "slug": "olimpiadnaya-fizika-podgotovka-tehnicheskie-vuzy-onlajn", "lang": "ru", "task": True,
 "title": "Олимпиадная физика онлайн: задачи и поступление в вузы",
 "desc": "Олимпиадная физика онлайн: программа по месяцам, разбор нестандартных задач, типичные ошибки, поступление в технические вузы. Физик МГУ, 1:1.",
 "h1": "Олимпиадная физика и подготовка к поступлению в технические вузы онлайн: разбор задач, программа по месяцам, типичные ошибки",
 "answer": "Олимпиадная физика — отдельный жанр, а не «ЕГЭ посложнее»: нужны оценки, симметрия, предельные случаи и длинное решение с обоснованием. Подготовка онлайн идёт шесть относительных месяцев по разделам физики с разбором каждой задачи; занятия один на один ведёт физик МГУ.",
 "facts": ["Названия олимпиад — ВсОШ, перечневые (в том числе «Физтех»), задачи в стиле международной олимпиады IPhO; правила, этапы и даты каждой олимпиады — на сайте организатора",
           "Олимпиада проверяет нестандартный ход и глубину модели, экзамен — надёжность на типовом: это разные навыки, и тренируются они по-разному",
           "Программа — механика, статика и гидростатика, МКТ и термодинамика, электростатика и цепи, магнетизм, оптика, колебания; методы — оценки, размерности, графики, симметрия",
           "Даты, квоты, баллы и условия льгот на странице намеренно не приводятся: их публикуют организаторы и вузы",
           "Занятия: онлайн, 1:1, русский язык, под ваш часовой пояс; разбор своей задачи — по присланному условию"],
 "sections": [
   ("Программа: разделы и методы", "<p>Олимпиадная подготовка строится поверх прочной базы по физике основной программы и идёт по разделам: в каждом сначала знакомые основы, затем нестандартные постановки. Какие олимпиады по силам и в каком темпе идти, решается на диагностике; правила и этапы конкретной олимпиады смотрите на сайте её организатора.</p>"
    "<p>Общие методы, которые тренируем во всех разделах: оценки порядка величины, анализ размерностей, чтение и построение графиков, симметрия, предельные случаи, нестандартные задачи, где известный закон применяется непривычным образом.</p>"),
   ("График по месяцам", "<p>Ниже — типовой каркас на шесть месяцев. Месяцы относительные, без привязки к датам: порядок и темп подстраиваются под диагностику, уровень ученика и число занятий в неделю. Если вы начинаете ближе к нужной олимпиаде, разделы, где диагностика показала уверенный результат, сжимаются. Даты олимпиад и вступительных испытаний — на сайтах организаторов и вузов.</p>"
    "<h3>" + _OLYMP_PLAN_TABLE_RU["title"] + "</h3><table class=\"spec-table\"><thead><tr>" + "".join("<th>%s</th>" % c for c in _OLYMP_PLAN_TABLE_RU["head"]) + "</tr></thead><tbody>"
    + "".join("<tr>" + "".join("<td>%s</td>" % c for c in r) + "</tr>" for r in _OLYMP_PLAN_TABLE_RU["rows"]) + "</tbody></table>"),
   ("Формат занятий и разбор задач", "<p>Занятия проходят онлайн, один на один, на общей интерактивной доске, на русском языке; подстраиваемся под ваш часовой пояс.</p>"
    "<ul><li><b>Диагностика на 20 минут</b> в начале: уровень, пробелы, интерес, реалистичная цель.</li>"
    "<li><b>Разбор задач по теме</b>: сначала вместе, затем самостоятельно с обсуждением; идея решения записывается словами, а не только формулами.</li>"
    "<li><b>Задачи прошлых лет</b> и авторские подборки нарастающей сложности: видно, какие идеи повторяются и как их узнавать.</li>"
    "<li><b>Оформление длинного решения</b>: как изложить идею так, чтобы проверяющий её увидел.</li>"
    "<li><b>Своя задача</b>: пришлите условие задачи, которая не получается, и мы разберём её на занятии. Результат этот разбор не обещает: его цель — понять, где рассуждение ломается.</li></ul>"),
   ("Типичные ошибки", "<p>Это наблюдения из практики преподавания, а не статистика олимпиад или вузов.</p><ul>"
    "<li><b>Поиск формулы вместо модели.</b> Ученик ищет подходящую формулу, не построив картину явления: что сохраняется, какие силы действуют, что меняется.</li>"
    "<li><b>Нет проверки предельных случаев и размерностей.</b> Ответ, который не прошёл такую проверку, часто содержит ошибку, которую можно заметить за минуту.</li>"
    "<li><b>Громоздкие вычисления вместо симметрии.</b> Задачу решают в лоб, хотя удачный выбор системы отсчёта или симметрия укорачивают решение.</li>"
    "<li><b>Решение без обоснования.</b> Верный ответ без объяснения хода рассуждений в длинной задаче теряет в оценке: идею нужно записывать.</li>"
    "<li><b>Работа только с типовым.</b> Если тренироваться на знакомых заданиях, незнакомая постановка на олимпиаде застаёт врасплох.</li>"
    "<li><b>Работа без времени.</b> Темп приходит только с пробными турами на время.</li></ul>"),
   ("Как олимпиадная подготовка связана с поступлением в технические вузы", "<p>Олимпиадные задачи развивают умение решать нестандартные задачи — оно нужно и на вступительных испытаниях. Условия льгот, перечень олимпиад и состав вступительных испытаний публикуют организаторы олимпиад и приёмные комиссии вузов: их нужно смотреть только на официальных сайтах, на этой странице они не приводятся.</p>"),
   ("Официальные документы", "<p>Правила, этапы, даты, перечни и условия льгот при поступлении публикуют организаторы олимпиад и сами вузы. Перед планированием сверяйтесь с сайтом организатора конкретной олимпиады и сайтом приёмной комиссии вуза: на этой странице даты, квоты, баллы и условия льгот намеренно не приводятся, чтобы не разойтись с официальными источниками.</p>"),
 ],
 "faq": [
   ("Как подготовиться к олимпиадной физике онлайн?", "Нужны диагностика, разделы физики по порядку, задачи нарастающей сложности, письменный разбор каждого решения и пробные туры на время. Занятия идут онлайн один на один."),
   ("Чем олимпиадная физика отличается от подготовки к ЕГЭ?", "ЕГЭ проверяет надёжность на типовых задачах, олимпиада — нестандартный ход и глубину модели. На олимпиаде нужны оценки порядка величины, симметрия, предельные случаи и длинное решение с обоснованием."),
   ("Сколько месяцев нужно на подготовку?", "В графике на странице шесть относительных месяцев. Срок зависит от уровня на диагностике и числа занятий в неделю; сжать программу можно, если часть разделов уже уверенно освоена."),
   ("Какие темы входят в программу?", "Механика (кинематика, динамика, законы сохранения), статика и гидростатика, МКТ и термодинамика, электростатика и цепи, магнетизм и индукция, оптика, колебания. Методы: оценки, размерности, графики, нестандартные задачи."),
   ("Как проходят занятия и разбор задач?", "Онлайн, один на один, на общей интерактивной доске. Разбираем задачи по теме, задачи прошлых лет и подборки нарастающей сложности, учимся оформлять длинное решение."),
   ("Можно ли прислать свою задачу на разбор?", "Да: пришлите условие, и мы разберём её на занятии. Цель разбора — найти, где ломается рассуждение; результат он не обещает."),
   ("Где смотреть даты, этапы и условия олимпиад и поступления?", "На сайте организатора конкретной олимпиады и на сайте приёмной комиссии вуза. На этой странице они намеренно не приводятся."),
   ("Какие ошибки мешают решать олимпиадные задачи?", "По наблюдениям из практики преподавания (не статистика): поиск формулы вместо модели, нет проверки предельных случаев и размерностей, решение в лоб без симметрии, ответ без обоснования, нет работы на время."),
 ],
 "updated": "2026-11-21",
 "table": _OLYMP_TABLE_RU,
 "who": _RU_WHO,
 "course": ("Олимпиадная физика онлайн (1:1)", "Индивидуальная онлайн-подготовка к олимпиадам по физике и к поступлению в технические вузы: разделы программы, разбор задач, график по месяцам."),
}
ANSWERS_PHYS.append(_OLYMP_ENTRY_RU)


def _hub_url(lang):
    return HUB if lang == "ru" else HUB_EN


def _links_block(lang):
    ru = lang == "ru"
    items = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in PILLARS[lang])
    items += f'<li><a href="{TUTOR_PAGE}">{"Страница репетитора: кто преподаёт и как начать" if ru else "Tutor\'s page (RU): who teaches and how to start"}</a></li>'
    return (f'<h2 id="links">{"Подробнее по программам" if ru else "Programme pages"}</h2>\n<ul>{items}</ul>\n'
            f'<p>{"Все страницы-ответы:" if ru else "All answer pages:"} <a href="{_hub_url(lang)}">{"ответы на частые запросы" if ru else "answers hub"}</a>.</p>')


RAZBOR_BOOK_URL = "https://calendly.com/vladimir-podlevskikh/30min"   # = BOOK_URL в assets/start-block.js


def razbor_slug(a):
    """slug блока «записаться на разбор» = страница-источник (идёт в событие GoatCounter и utm_campaign)."""
    return "tutor-answers-" + a["slug"]


def razbor_block_html(slug, lang, label=None, with_script=True, title=None, lead=None):
    """Общий блок «записаться на разбор» (StartBlock variant=razbor): внутри — статический запасной вариант
    без JS (та же ссылка с UTM); компонент заменяет его и считает показ razbor-shown-<slug> и клик
    cta-book-razbor-<slug> в GoatCounter. title/lead — необязательные data-title/data-lead компонента."""
    ru = lang == "ru"
    href = (f"{RAZBOR_BOOK_URL}?utm_source=tutor.podlevskikh.com&amp;utm_medium=razbor&amp;utm_campaign={slug}"
            + ("" if ru else "&amp;utm_content=intl"))   # en: JS подставит страну по часовому поясу, без JS — intl
    label = label or ("Записаться на разбор" if ru else "Book a walkthrough")
    extra = "".join(f' data-{k}="{v}"' for k, v in (("title", title), ("lead", lead)) if v)
    out = (f'<div class="razbor" data-start-block data-variant="razbor" data-slug="{slug}" data-lang="{lang}"{extra}>'
           f'<p><a class="btn btn-primary btn-lg" href="{href}" target="_blank" rel="noopener" data-sb-cta data-book>{label} →</a></p></div>')
    if with_script:
        out += '\n      <script src="/assets/start-block.js" defer></script>'
    return out


def _razbor_block(a):
    """Блок «записаться на разбор» страницы-ответа: slug = страница-источник."""
    return razbor_block_html(razbor_slug(a), a["lang"])


_TASK_TOKENS = {"ib", "igcse", "a-level"}


def has_task_block(a):
    """Блок «разберём вашу задачу» — на страницах-ответах про A-level/IB и IGCSE (по slug страницы)
    и на страницах с явным флагом a["task"] (например, AP Physics + Calculus)."""
    if a.get("task"):
        return True
    slug = "-" + a["slug"] + "-"
    return any(f"-{t}-" in slug for t in _TASK_TOKENS)


def task_block_href(slug):
    """Ссылка на страницу репетитора с меткой источника = slug страницы-ответа (utm_campaign)."""
    return f"{TUTOR_PAGE}?utm_source=answers&amp;utm_medium=task-block&amp;utm_campaign={slug}#razbor-zapros"


def _task_block(a):
    """Единый блок «разберём вашу задачу»: ссылка к репетитору несёт slug страницы (data-tutor-src) —
    assets/site.js шлёт событие cta-to-tutor-answers-<slug>, оно входит в клики_к_репетитору и режется по страницам."""
    if not has_task_block(a):
        return ""
    ru = a["lang"] == "ru"
    title = "Разберём вашу задачу" if ru else "Let's work through your problem"
    lead = ("Пришлите задачу или тему, где вы застряли: на странице репетитора — как проходит разбор и с чего начать."
            if ru else
            "Send a problem or a topic you are stuck on: the tutor's page (in Russian) shows how a walkthrough goes and how to start.")
    label = "К репетитору" if ru else "Tutor's page (RU)"
    return (f'<div class="task-block" id="task-block"><h2>{title}</h2><p>{lead}</p>'
            f'<p><a class="btn btn-primary btn-lg" data-tutor-src="{a["slug"]}" href="{task_block_href(a["slug"])}">{label} →</a></p></div>\n      ')


def paste_block_href(slug):
    """Ссылка на страницу репетитора с меткой блока «задача из ИИ»: utm_medium=ai-task-paste, utm_campaign=paste-<slug>."""
    return f"{TUTOR_PAGE}?utm_source=answers&amp;utm_medium=ai-task-paste&amp;utm_campaign=paste-{slug}#razbor-zapros"


_PASTE_TEXT = {
    "ru": ("Разобрать задачу из ИИ", "Вставьте условие задачи, с которой не справился ИИ-чат или в решении которой вы сомневаетесь. "
           "Текст останется только в этой вкладке браузера: в адрес страницы и в статистику он не попадает.",
           "Условие задачи", "К репетитору"),
    "en": ("Work through a problem from an AI chat", "Paste the statement of a problem an AI chat could not solve, or whose solution you doubt. "
           "The text stays in this browser tab only: it does not go into the page address or the statistics.",
           "Problem statement", "To the tutor (page in Russian)"),
}


def _paste_block(a):
    """Блок «Разобрать задачу из ИИ»: textarea (maxlength 2000) + ссылка к репетитору. assets/ai-task-paste.js кладёт текст
    в sessionStorage (ключ tutorTask), а не в URL; на /exam-prep-online/ его подхватывает форма #task-intake.
    Скрыт (hidden), пока JS не включит. data-tutor-src="paste-<slug>" → site.js шлёт cta-to-tutor-paste-<slug> (без текста)."""
    title, lead, label, cta = _PASTE_TEXT[a["lang"]]
    return (f'<div class="paste-block" id="ai-task-paste" data-slug="{a["slug"]}" hidden><h2>{title}</h2><p>{lead}</p>'
            f'<p><textarea class="paste-text" rows="6" maxlength="2000" aria-label="{label}"></textarea></p>'
            f'<p><a class="btn btn-primary btn-lg" data-tutor-src="paste-{a["slug"]}" href="{paste_block_href(a["slug"])}">{cta} →</a></p></div>\n'
            f'      <script src="/assets/ai-task-paste.js" defer></script>\n      ')


def diag_block_href(slug):
    """Ссылка на страницу репетитора с меткой источника блока диагностики: utm_campaign=diag-<slug>."""
    return f"{TUTOR_PAGE}?utm_source=answers&amp;utm_medium=diag-block&amp;utm_campaign=diag-{slug}#razbor-zapros"


_DIAG_TEXT = {
    "ru": {
        "title": "Диагностика за 10 минут",
        "lead": "Пять вопросов по теме этой страницы, у каждого один верный ответ из четырёх. Ответы можно менять; результат покажет кнопка, когда отвечены все пять; это ориентир по базовым темам, а не прогноз экзаменационного балла.",
        "q": "Вопрос", "score": "Верно: {n} из 5", "right": "верно", "wrong": "неверно",
        "levels": ["Основы пока нетвёрдые: в таком случае полезно спокойно пройти базовые темы по порядку и найти, где именно возникает путаница.",
                   "Основа есть, но часть тем держится нетвёрдо. Следующий шаг — понять, какие именно темы и типы заданий дают ошибки.",
                   "Уверенная база. Дальше важны задачи повышенной сложности, оформление решений и работа со временем."],
        "cta": "Разобрать результат с репетитором",
        "hint": "Ответьте на все пять вопросов, затем нажмите кнопку.", "show": "Показать результат",
    },
    "en": {
        "title": "10-minute diagnostic",
        "lead": "Five questions on the topic of this page, one correct answer out of four each. Answers can be changed; the button shows the result once all five are answered; it is a guide to core topics, not a prediction of an exam grade.",
        "q": "Question", "score": "Correct: {n} out of 5", "right": "correct", "wrong": "incorrect",
        "levels": ["The basics are not yet secure: it helps to go through the core topics in order and find where exactly the confusion starts.",
                   "There is a base, but some topics are shaky. The next step is to find which topics and question types produce the mistakes.",
                   "A solid base. From here, harder problems, the way solutions are written up and working to time matter most."],
        "cta": "Go through the result with the tutor (page in Russian)",
        "hint": "Answer all five questions, then press the button.", "show": "Show result",
    },
}


def _diag_block(a):
    """Блок «Диагностика за 10 минут»: 5 вопросов набора по предмету/экзамену страницы (diag_sets.py), подсчёт на клиенте
    (assets/diag.js, без запросов наружу). Скрыт (hidden), пока JS не включит его. Кнопка результата ведёт к репетитору:
    utm_campaign=diag-<slug>, data-tutor-src="diag-<slug>" → assets/site.js шлёт событие cta-to-tutor-diag-<slug>."""
    found = diag_set(a["slug"], a["lang"])
    if not found:
        return ""
    key, qs = found
    t = _DIAG_TEXT[a["lang"]]
    esc = html_escape
    items = ""
    for i, (q, opts, correct) in enumerate(qs):
        radios = "".join(
            f'<label class="diag-opt"><input type="radio" name="diag-q{i}" value="{j}"> <span>{esc(o)}</span></label>'
            for j, o in enumerate(opts))
        items += (f'<li class="diag-q" data-correct="{correct}"><p class="diag-qt">{esc(q)}</p>'
                  f'<div class="diag-opts">{radios}</div><p class="diag-mark" hidden></p></li>')
    levels = "".join(f'<p class="diag-level" data-levels="{k}" hidden>{esc(x)}</p>' for k, x in enumerate(t["levels"]))
    return (f'<div class="diag-block" id="diag-block" data-diag="{key}" data-right="{t["right"]}" data-wrong="{t["wrong"]}" '
            f'data-score="{esc(t["score"])}" hidden>'
            f'<h2>{t["title"]}</h2><p>{t["lead"]}</p><ol class="diag-list">{items}</ol>'
            f'<p class="diag-hint muted">{t["hint"]}</p>'
            f'<p class="diag-actions"><button type="button" class="btn btn-primary diag-show" disabled>{t["show"]}</button></p>'
            f'<div class="diag-result" aria-live="polite"><p class="diag-score"></p>{levels}'
            f'<p class="diag-cta" hidden><a class="btn btn-primary btn-lg" data-tutor-src="diag-{a["slug"]}" href="{diag_block_href(a["slug"])}">{t["cta"]} →</a></p></div></div>\n'
            f'      <script src="/assets/diag.js" defer></script>\n      ')


def _tutor_cta(lang):
    if lang == "ru":
        return (f'<p><a class="btn btn-ghost btn-lg" data-cta="tutor-page" href="{TUTOR_PAGE}">'
                'Страница репетитора</a></p>')
    return (f'<p><a class="btn btn-ghost btn-lg" data-cta="tutor-page" href="{TUTOR_PAGE}">'
            "Tutor's page (RU)</a></p>")


_MONTHS_RU = ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"]
_MONTHS_EN = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


def _fmt_date(iso, ru):
    y, m, d = (int(x) for x in iso.split("-"))
    return f"{d} {_MONTHS_RU[m-1]} {y}" if ru else f"{d} {_MONTHS_EN[m-1]} {y}"


def _table_html(a, ru):
    t = a["table"]
    head = "".join(f"<th>{c}</th>" for c in t["head"])
    rows = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in t["rows"])
    return (f'<h2 id="compare">{t["title"]}</h2>\n<table class="spec-table">\n<thead><tr>{head}</tr></thead>\n'
            f'<tbody>{rows}</tbody>\n</table>')


def _seealso_block(a):
    """«Смотрите также»: соседи из seealso.py (генерируется из реестра; без data-tutor-src/data-cta)."""
    return seealso.seealso_html(a, ANSWERS + ANSWERS_EN + ANSWERS_MATH + ANSWERS_PHYS)


def render_body(a):
    ru = a["lang"] == "ru"
    facts = "".join(f"<li>{f}</li>" for f in a["facts"])
    secs = "".join(f'<h2>{h}</h2>\n{b}\n' for h, b in a["sections"])
    tbl = _table_html(a, ru) + "\n      " if a.get("table") else ""
    tbl_first = ""
    if a.get("table_first") and tbl:
        tbl_first, tbl = tbl, ""
    upd = (f'    <p class="muted"><time datetime="{a["updated"]}">'
           f'{"Обновлено" if ru else "Updated"}: {_fmt_date(a["updated"], ru)}</time></p>\n') if a.get("updated") else ""
    who = a.get("who") or (_RU_WHO if ru else _EN_WHO)
    return f"""<main id="main">
<section class="subhero section" id="top">
  <div class="wrap">
    <p class="eyebrow reveal">{"Ответ на запрос" if ru else "Answer"} · {a['query']}</p>
    <h1 class="reveal">{a['h1']}</h1>
    <p class="lead reveal">{a['answer']}</p>
{upd}  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="prose reveal" style="max-width:760px">
      {tbl_first}<h2 id="facts">{"Коротко" if ru else "Key facts"}</h2>
      <ul>{facts}</ul>
{tbl}      {secs}
      <h2 id="who">{"Кто преподаёт" if ru else "Who teaches"}</h2>
      <p>{who}</p>
      {_diag_block(a)}{_paste_block(a)}{_task_block(a)}{_razbor_block(a)}
      {_seealso_block(a)}
      {_links_block(a['lang'])}
    </div>
  </div>
</section>

{{{{FAQ}}}}
</main>"""


def _alternates(a):
    """hreflang-набор страницы: себя + пара на другом языке (если есть) + x-default (EN-вариант)."""
    me = f"{HUB}{a['slug']}/"
    if a["lang"] == "ru":
        twin = next((e for e in ANSWERS_EN + ANSWERS_MATH + ANSWERS_PHYS if e.get("twin") == a["n"]), None)
        other = (f"{HUB}{twin['slug']}/", "en") if twin else None
    else:
        twin = next((r for r in ANSWERS + ANSWERS_MATH + ANSWERS_PHYS if r["n"] == a.get("twin")), None)
        other = (f"{HUB}{twin['slug']}/", "ru") if twin else None
    alts = [(a["lang"], me)]
    if other:
        alts.append((other[1], other[0]))
    en_url = me if a["lang"] == "en" else (other[0] if other else None)
    alts.append(("x-default", en_url or me))
    return alts


def _page(a):
    ru = a["lang"] == "ru"
    a = dict(a, query=QUERIES_PHYS.get(a["n"]) or QUERIES_MATH.get(a["n"]) or (QUERIES[a["n"]] if a["n"] in QUERIES else QUERIES_EN[a["twin"]]))
    if "course" in a:
        ld = course(a["course"][0], a["course"][1], lang=(a["lang"],))
    else:
        ld = service(a["service"][0], a["service"][1])
    return {
        "url": f"{HUB}{a['slug']}/", "lang": a["lang"], "body_html": render_body(a),
        "no_cta": True, "lastmod": a.get("updated") or (LASTMOD_EN if a["n"] > 100 else LASTMOD), "answer_n": a["n"], "answer_query": a["query"],
        "title": a["title"], "desc": a["desc"],
        "og_title": a["title"],
        "crumbs": [("Главная" if ru else "Home", "/"), ("Ответы" if ru else "Answers", _hub_url(a["lang"])), (a["h1"], None)],
        "alternates": _alternates(a),
        "jsonld": [ld] + ([{"@context": "https://schema.org", "@type": "ProfilePage", "name": a["title"],
                            "url": BASE_URL + f"{HUB}{a['slug']}/", "inLanguage": a["lang"],
                            "mainEntity": PERSON_REF}] if a["n"] == 7 else []) + ([{"@context": "https://schema.org", "@type": "WebPage", "name": a["title"],
                            "url": BASE_URL + f"{HUB}{a['slug']}/", "inLanguage": a["lang"],
                            "dateModified": a["updated"]}] if a.get("updated") else []),
        "faq_heading": "Частые вопросы" if ru else "Common questions",
        "faq": a["faq"],
    }


def _hub():
    rows = "".join(
        f'<li><a href="{HUB}{a["slug"]}/">{QUERIES[a["n"]]}</a></li>' for a in ANSWERS)
    math_rows = "".join(
        f'<li><a href="{HUB}{a["slug"]}/">{QUERIES_MATH[a["n"]]}</a></li>' for a in ANSWERS_MATH if a["lang"] == "ru")
    phys_rows = "".join(
        f'<li><a href="{HUB}{a["slug"]}/">{QUERIES_PHYS[a["n"]]}</a></li>' for a in ANSWERS_PHYS if a["lang"] == "ru")
    body = f"""<main id="main">
<section class="subhero section" id="top">
  <div class="wrap">
    <p class="eyebrow reveal">Answers · Ответы</p>
    <h1 class="reveal">Ответы на вопросы о репетиторе по физике</h1>
    <p class="lead reveal">Краткие ответы на вопросы, с которыми выбирают репетитора по физике для ЕГЭ, IB, AP и IGCSE: онлайн, 1:1, на русском или английском. Ведёт Владимир Подлевских, физик МГУ, 23 года преподавания.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="prose reveal" style="max-width:760px">
      <h2>Вопросы</h2>
      <ul>{rows}</ul>
      <h2>Программы и экзамены: ЕГЭ, AP Physics, IB Physics</h2>
      <ul>{phys_rows}</ul>
      <h2>Математика: IB, AP, IGCSE</h2>
      <ul>{math_rows}</ul>
      <h2>Программы</h2>
      <ul>{"".join(f'<li><a href="{h}">{t}</a></li>' for h, t in PILLARS["ru"])}</ul>
    </div>
  </div>
</section>
</main>"""
    return {"url": HUB, "lang": "ru", "body_html": body, "no_cta": True, "lastmod": LASTMOD_MATH,
            "title": "Ответы о репетиторе по физике: ЕГЭ, IB, AP, IGCSE",
            "desc": "Краткие ответы по запросам: репетитор по физике для ЕГЭ, IB, AP Physics и IGCSE 0625 онлайн, на русском и английском. Физик МГУ, 23 года опыта.",
            "crumbs": [("Главная", "/"), ("Ответы", None)],
            "alternates": [("ru", HUB), ("en", HUB_EN), ("x-default", HUB_EN)],
            "jsonld": [service("Репетитор по физике онлайн: ответы на частые запросы",
                               "Страницы-ответы о подготовке к ЕГЭ, IB, AP и IGCSE онлайн 1:1.")],
            "faq": []}


def _hub_en():
    pages = [a for a in ANSWERS if a["lang"] == "en"] + ANSWERS_EN
    rows = "".join(
        f'<li><a href="{HUB}{a["slug"]}/">{QUERIES[a["n"]] if a["n"] in QUERIES else QUERIES_EN[a["twin"]]}</a></li>'
        for a in pages)
    math_rows = "".join(
        f'<li><a href="{HUB}{a["slug"]}/">{QUERIES_MATH[a["n"]]}</a></li>' for a in ANSWERS_MATH if a["lang"] == "en")
    phys_rows = "".join(
        f'<li><a href="{HUB}{a["slug"]}/">{QUERIES_PHYS[a["n"]]}</a></li>' for a in ANSWERS_PHYS if a["lang"] == "en")
    body = f"""<main id="main">
<section class="subhero section" id="top">
  <div class="wrap">
    <p class="eyebrow reveal">Answers</p>
    <h1 class="reveal">Answers about a physics tutor: EGE, IB, AP, IGCSE</h1>
    <p class="lead reveal">Short answers to the questions families ask when choosing a physics tutor for the EGE, IB, AP and IGCSE: online, one-to-one, in English or Russian. Taught by Vladimir Podlevskikh, an MSU physicist with 23 years of teaching.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="prose reveal" style="max-width:760px">
      <h2>Questions</h2>
      <ul>{rows}</ul>
      <h2>Comparing programmes: AP Physics and IB Physics</h2>
      <ul>{phys_rows}</ul>
      <h2>Mathematics: IB, AP, IGCSE</h2>
      <ul>{math_rows}</ul>
      <h2>Programmes</h2>
      <ul>{"".join(f'<li><a href="{h}">{t}</a></li>' for h, t in PILLARS["en"])}</ul>
    </div>
  </div>
</section>
</main>"""
    return {"url": HUB_EN, "lang": "en", "body_html": body, "no_cta": True, "lastmod": LASTMOD_MATH,
            "title": "Physics tutor answers: EGE, IB, AP, IGCSE",
            "desc": "Short answers: physics tutor for the EGE, IB, AP Physics and IGCSE 0625 online, in English and Russian. MSU physicist, 23 years of experience.",
            "crumbs": [("Home", "/"), ("Answers", None)],
            "alternates": [("ru", HUB), ("en", HUB_EN), ("x-default", HUB_EN)],
            "jsonld": [service("Online physics tutor: answers to common questions",
                               "Answer pages on EGE, IB, AP and IGCSE preparation online, one-to-one.")],
            "faq": []}


def answer_pages():
    return [_hub(), _hub_en()] + [_page(a) for a in ANSWERS] + [_page(a) for a in ANSWERS_EN] + [_page(a) for a in ANSWERS_MATH] + [_page(a) for a in ANSWERS_PHYS]


# ── RU: физика для поступления в зарубежные вузы (UCAS, Oxford, Cambridge, ESAT) онлайн (автопилот 21.11) ──
# Факты сверены 21.11.2026 по первоисточникам: physics.ox.ac.uk/study/undergraduates/how-apply/physics-aptitude-test-pat
# (все поступающие на Physics и Physics and Philosophy сдают ESAT; прежний PAT не используется; двухчасовой тест по физике и математике),
# undergraduate.study.cam.ac.uk/apply/how/science-engineering-admission-test (курсы с ESAT; Engineering = Mathematics 1, Mathematics 2, Physics;
# Natural Sciences = Mathematics 1 + два из Biology/Chemistry/Physics/Mathematics 2; 120 минут), esat-tmua.ac.uk/about-the-tests/esat-test/
# (пять модулей, по 27 вопросов и 40 минут, без калькулятора, шкала 1–9, нет проходного балла), ucas.com / ox.ac.uk / cam.ac.uk
# (срок Оксфорд/Кембридж — 15 октября, 18:00 по Великобритании), undergraduate.study.cam.ac.uk/courses/engineering (Engineering: типичное A*A*A; IB 41–42, 776 на HL; Mathematics и Physics обязательны).
# Не приводим: даты сессий и регистрации (меняются ежегодно), оценки Оксфорда (формулировки на страницах расходятся), статистику приёма.
UCAS_SLUG = "podgotovka-fizika-zarubezhnye-vuzy-ucas-oxford-cambridge-onlajn"
QUERIES_PHYS[410] = "Физика для поступления в зарубежные вузы онлайн: UCAS, Oxford PAT, Cambridge, план подготовки"
_UCAS_RELATED = [("podgotovka-a-level-ib-fizika-onlajn", "Подготовка к A-level и IB по физике онлайн: программа и план по месяцам"),
                 ("ib-physics-hl-ili-sl-chto-vybrat", "IB Physics HL или SL: чем отличаются и как выбрать"),
                 ("ap-physics-calculus-onlajn-programma-grafik-mayskie-ekzameny", "AP Physics и AP Calculus онлайн: программа и график к майским экзаменам"),
                 ("olimpiadnaya-fizika-podgotovka-tehnicheskie-vuzy-onlajn", "Олимпиадная физика и подготовка в технические вузы онлайн"),
                 ("podgotovka-ege-fizika-za-rubezhom", "Подготовка к ЕГЭ по физике для живущих за рубежом")]

_UCAS_TABLE_RU = {'title': 'Что и куда: от подачи до собеседования',
 'head': ['Этап', 'Что происходит', 'Что проверить на сайте вуза или организатора'],
 'rows': [['Подача через UCAS', 'Единая заявка в британские вузы; для Оксфорда и Кембриджа срок подачи — 15 октября, 18:00 по британскому времени', 'Срок для вашего года поступления и список курсов с ранним сроком — на ucas.com'],
          ['Вступительный тест', 'Оксфорд, физика: ESAT у всех поступающих на Physics и Physics and Philosophy, прежний PAT не используется. Кембридж: ESAT на Engineering, Natural Sciences и некоторых других курсах', 'Какие модули нужны вашему курсу, даты сессий и срок регистрации — на esat-tmua.ac.uk и странице курса'],
          ['Собеседование', 'У Оксфорда на физике на собеседование приглашают по результату ESAT, информации в заявке UCAS и контекстной информации; приглашённые затем идут на собеседования', 'Формат и сроки собеседований — на странице физического факультета и колледжа'],
          ['Требования по оценкам', 'Кембридж, Engineering: типичное предложение A*A*A по A-level или 41–42 балла по IB, 776 на Higher Level; обязательны Mathematics и Physics', 'Актуальное предложение вашего курса — на странице курса: оно может меняться по годам']]}

_UCAS_PLAN_TABLE_RU = {'title': 'План подготовки по этапам: до дедлайна подачи и теста, затем собеседование',
 'head': ['Этап', 'Фокус', 'Чем проверяем'],
 'rows': [['Месяцы 1–2', 'Диагностика; выбор вуза и курса; математика уровня A-level или IB HL: алгебра, функции, тригонометрия', 'Диагностика на 20 минут; письменный разбор нескольких задач'],
          ['Месяцы 3–5', 'Механика, колебания, электричество на глубоком уровне; начала анализа', 'Подборки задач нарастающей сложности; разбор каждого решения'],
          ['Месяцы 6–8', 'Остальные разделы физики; методы: оценки, размерности, графики, предельные случаи; Mathematics 2', 'Задачи без калькулятора; работа над ошибками'],
          ['Месяцы 9–10', 'Формат ESAT: 27 вопросов и 40 минут на модуль; пробные модули на время; параллельно заявка UCAS и личное заявление, чтобы подать до дедлайна', 'Пробные модули по времени; разбор каждого неверного ответа; черновик личного заявления'],
          ['Месяцы 11–12', 'Подготовка к собеседованию (оно проходит уже после подачи и теста): рассуждение вслух, задачи по физике и математике', 'Пробное собеседование; письменный план рассуждения']]}

_UCAS_ENTRY_RU = {"n": 410, "slug": UCAS_SLUG, "lang": "ru", "task": True,
 "title": "Физика для UCAS, Oxford и Cambridge онлайн: план подготовки",
 "desc": "Физика для поступления в вузы Великобритании онлайн: UCAS, ESAT вместо Oxford PAT, Cambridge, интервью, план по месяцам. Физик МГУ, 1:1.",
 "h1": "Физика для поступления в зарубежные вузы онлайн: UCAS, Oxford, Cambridge и план подготовки",
 "answer": "Физика в Оксфорде, а в Кембридже Natural Sciences или Engineering: подача через UCAS (срок — 15 октября), тест ESAT (прежний Oxford PAT не используется), собеседование, оценки A-level или IB. Онлайн один на один с физиком МГУ: диагностика, математика, физика, пробные модули.",
 "facts": ["Оксфорд, физика: все поступающие на Physics и Physics and Philosophy сдают ESAT; прежний PAT не используется (physics.ox.ac.uk)",
           "ESAT — пять модулей (Mathematics 1, Mathematics 2, Physics, Chemistry, Biology), в каждом 27 вопросов и 40 минут, калькулятор не разрешён, результат по шкале от 1 до 9 (esat-tmua.ac.uk)",
           "Кембридж: Engineering — Mathematics 1, Mathematics 2 и Physics; Natural Sciences — Mathematics 1 и два из Biology, Chemistry, Physics, Mathematics 2 (undergraduate.study.cam.ac.uk)",
           "Срок UCAS для Оксфорда и Кембриджа — 15 октября, 18:00 по британскому времени; даты тестов, регистрация и оценки — на сайтах вузов и организатора",
           "Занятия: онлайн, 1:1, русский или английский язык, под ваш часовой пояс; разбор своей задачи — по присланному условию"],
 "sections": [
   ("Что нужно для физики в Великобритании", "<p>Для физики и инженерных курсов британские вузы ожидают сильную математику и физику на уровне A-level, IB Higher Level или близкой программы (например, AP). Например, на странице Cambridge Engineering обязательными названы Mathematics и Physics, а для IB — Analysis and Approaches. Если вы ещё выбираете между программами, начните со страниц про A-level и IB и про AP, ссылки ниже.</p>"
    "<p>Единой учебной программы у вступительного теста нет: ESAT проверяет математику и физику на глубину, а не набор формул. Поэтому основной темой подготовки становится умение решать незнакомые задачи без калькулятора.</p>"),
   ("Что и куда: подача, тест, собеседование, оценки", "<p>Ниже — общий каркас. Даты сессий теста, сроки регистрации и предложения по оценкам меняются от года к году, поэтому на странице они приведены только там, где подтверждены сайтами вузов; остальное сверяйте с официальными страницами.</p>"
    "<p>Таблица со сравнением этапов — выше, в блоке со спецификацией.</p>"),
   ("PAT, ESAT и ЕГЭ или олимпиады: в чём разница", "<p>Oxford PAT — прежний тест физического факультета Оксфорда; сейчас Оксфорд принимает на физику по результатам ESAT, и старые материалы PAT полезны разве что как задачи для тренировки рассуждений. ESAT — тест с выбором ответа на компьютере: модуль Mathematics 1 обязателен для всех, остальные модули зависят от курса.</p>"
    "<p>От ЕГЭ он отличается тем, что нет развёрнутого решения с оформлением: нужен верный выбор ответа за 40 минут на модуль и без калькулятора, значит, нужны быстрые оценки и вычисления в уме. От олимпиады — тем, что задачи короче и на время, но те же методы (размерности, предельные случаи, оценки) работают и там. Программа ЕГЭ не покрывает формат полностью; <a href=\"/answers/olimpiadnaya-fizika-podgotovka-tehnicheskie-vuzy-onlajn/\">олимпиадная подготовка</a> помогает с нестандартными задачами.</p>"),
   ("План подготовки по этапам", "<p>План относительный: месяцы считаются от начала занятий до подачи и теста, без привязки к датам. Если вы начинаете ближе к сроку, разделы, где диагностика показала уверенный результат, сжимаются. Даты сессий и регистрации — на сайте организатора теста.</p>"
    "<h3>" + _UCAS_PLAN_TABLE_RU["title"] + "</h3><table class=\"spec-table\"><thead><tr>" + "".join("<th>%s</th>" % c for c in _UCAS_PLAN_TABLE_RU["head"]) + "</tr></thead><tbody>"
    + "".join("<tr>" + "".join("<td>%s</td>" % c for c in r) + "</tr>" for r in _UCAS_PLAN_TABLE_RU["rows"]) + "</tbody></table>"),
   ("Типичные ошибки", "<p>Это наблюдения из практики преподавания, а не статистика приёма.</p><ul>"
    "<li><b>Опора на старые материалы PAT.</b> Тест сменился на ESAT: формат и состав модулей другие, поэтому сверяйте подготовку с описанием ESAT.</li>"
    "<li><b>Калькулятор в голове не тренируется.</b> На ESAT его нет, а ученик привык считать на нём.</li>"
    "<li><b>Работа без времени.</b> На модуль даётся 40 минут: темп приходит только с пробными модулями на время.</li>"
    "<li><b>Слабая математика при сильной физике.</b> Модуль Mathematics 1 обязателен для всех, и физику без математики не вытянуть.</li>"
    "<li><b>Поздний старт.</b> Заявку, личное заявление и тест нужно готовить параллельно и до дедлайна подачи, а не друг за другом.</li>"
    "<li><b>Решение молча на собеседовании.</b> Интервьюер оценивает ход рассуждения, поэтому рассуждать нужно вслух.</li></ul>"),
   ("Как проходят занятия", "<p>Занятия проходят онлайн, один на один, на общей интерактивной доске; язык — русский или английский, термины экзаменов остаются английскими; время подстраиваем под ваш часовой пояс. Ведёт занятия физик, выпускник физического факультета МГУ (2006).</p>"
    "<ul><li><b>Диагностика на 20 минут</b> в начале: уровень, пробелы, цель и реалистичный план.</li>"
    "<li><b>Разбор задач по теме</b>: сначала вместе, затем самостоятельно с обсуждением.</li>"
    "<li><b>Пробные модули на время</b> и работа над ошибками.</li>"
    "<li><b>Рассуждение вслух</b> для собеседования.</li>"
    "<li><b>Своя задача</b>: пришлите условие, и мы разберём её на занятии. Результат этот разбор не обещает: его цель — понять, где рассуждение ломается.</li></ul>"),
   ("Связанные ответы", "<ul>" + "".join('<li><a href="/answers/%s/">%s</a></li>' % (s, t) for s, t in _UCAS_RELATED) + "</ul>"),
   ("Официальные документы", "<p>Условия поступления публикуют вузы и организатор теста: ucas.com, physics.ox.ac.uk, undergraduate.study.cam.ac.uk, esat-tmua.ac.uk. Перед планированием сверяйтесь с ними: даты сессий, регистрация, модули и предложения по оценкам меняются, поэтому любую цифру с этой страницы проверяйте на официальном сайте.</p>"),
 ],
 "faq": [
   ("Как подготовиться к физике для поступления в Оксфорд и Кембридж онлайн?", "Нужны диагностика, математика и физика на глубоком уровне, задачи без калькулятора, пробные модули ESAT на время и тренировка рассуждений вслух для собеседования. Занятия идут онлайн один на один."),
   ("Oxford PAT ещё существует?", "Для физики Оксфорд сейчас использует ESAT, прежний PAT не используется: все поступающие на Physics и Physics and Philosophy сдают ESAT. Проверяйте страницу физического факультета."),
   ("Что такое ESAT и какие модули нужны?", "Это компьютерный тест из пяти модулей: Mathematics 1, Mathematics 2, Physics, Chemistry, Biology. В каждом 27 вопросов и 40 минут, калькулятор не разрешён. Mathematics 1 обязателен, остальное зависит от курса."),
   ("Какой срок подачи через UCAS для Оксфорда и Кембриджа?", "15 октября, 18:00 по британскому времени. Сверяйте срок для своего года поступления на ucas.com и на сайтах вузов."),
   ("Какие оценки нужны для Cambridge Engineering?", "На странице курса типичное предложение — A*A*A по A-level или 41–42 балла по IB с 776 на Higher Level; обязательны Mathematics и Physics. Предложение может меняться: проверяйте страницу курса."),
   ("Чем ESAT отличается от ЕГЭ и олимпиад?", "ESAT — компьютерный тест с выбором ответа, 40 минут на модуль и без калькулятора. В ЕГЭ нужно развёрнутое решение, в олимпиаде — нестандартные длинные задачи; методы оценок и предельных случаев помогают везде."),
   ("Можно ли прислать свою задачу на разбор?", "Да: пришлите условие, и мы разберём её на занятии. Цель разбора — найти, где ломается рассуждение; результат он не обещает."),
   ("Где смотреть даты тестов, регистрацию и условия вуза?", "На сайтах организатора теста esat-tmua.ac.uk, UCAS и вузов. На этой странице даты сессий и регистрации намеренно не приводятся: они меняются."),
 ],
 "updated": "2026-11-21",
 "table": _UCAS_TABLE_RU,
 "who": _RU_WHO,
 "course": ("Физика для поступления в вузы Великобритании онлайн (1:1)", "Индивидуальная онлайн-подготовка по физике и математике к UCAS, ESAT и собеседованию в Оксфорд и Кембридж: план по этапам, пробные модули, разбор задач."),
}
ANSWERS_PHYS.append(_UCAS_ENTRY_RU)


# ── RU: четыре страницы по экзаменам (автопилот 24.11.2026, n=411–414) ──
# Факты — ТОЛЬКО из ФАКТЫ-ЭКЗАМЕНЫ 24.11.2026 (разделы 1, 2, 4, 5); каждое утверждение привязано к строке файла.
# Не приводим: шкалу итогового балла AP, перечень моделей калькуляторов, веса всех юнитов AP Statistics,
# пороги перевода баллов ОГЭ в отметки, правила про калькулятор GCSE, состав листа формул GCSE.
UPDATED_NEWANS = "2026-11-24"
_AP_STAT_URL = "https://apcentral.collegeboard.org/courses/ap-statistics/exam"
_AP_AB_COURSE_URL = "https://apcentral.collegeboard.org/courses/ap-calculus-ab"
_AP_AB_CLARIF_URL = "https://apcentral.collegeboard.org/media/pdf/ap-calculus-ab-bc-course-and-exam-description-clarifications.pdf"
_FIPI_URL = "https://fipi.ru/oge/demoversii-specifikacii-kodifikatory"
_AQA_SPEC_URL = "https://filestore.aqa.org.uk/resources/physics/specifications/AQA-8463-SP-2016.PDF"
_AQA_GLANCE_URL = "https://www.aqa.org.uk/subjects/science/gcse/physics-8463/specification/specification-at-a-glance"
_LESSONS_NEWANS = ("<p>Занятия проходят онлайн, один на один, на общей интерактивной доске, на русском языке; подстраиваемся под ваш часовой пояс. "
                   "Ведёт занятия физик, выпускник физического факультета МГУ (2006).</p>"
                   "<ul><li><b>Диагностика на 20 минут</b> в начале: уровень, пробелы, с чего начать.</li>"
                   "<li><b>Разбор задач по теме</b>: сначала вместе, затем самостоятельно с обсуждением.</li>"
                   "<li><b>Своя задача</b>: пришлите условие, и мы разберём её на занятии. Результат этот разбор не обещает: его цель — понять, где рассуждение ломается.</li></ul>")

# 411 — AP Calculus AB
QUERIES_MATH[411] = "AP Calculus AB онлайн на русском: что на экзамене и как готовиться"
_APAB_TABLE_RU = {'title': 'Формат экзамена AP Calculus AB (по AP Central)',
 'head': ['Часть', 'Вопросы', 'Время', 'Калькулятор', 'Доля оценки'],
 'rows': [['Секция I (тест)', '42', '1 ч 40 мин', 'по частям, ниже', '50%'],
          ['Секция I, часть A', '29', '62 мин', 'не разрешён', 'в составе секции I'],
          ['Секция I, часть B', '13', '38 мин', 'нужен графический', 'в составе секции I'],
          ['Секция II (развёрнутые ответы)', '6', '1 ч 30 мин', 'по частям, ниже', '50%'],
          ['Секция II, часть A', '2', '30 мин', 'нужен графический', 'в составе секции II'],
          ['Секция II, часть B', '4', '60 мин', 'не разрешён', 'в составе секции II']]}
_APAB_ENTRY_RU = {"n": 411, "slug": "ap-calculus-ab-tutor-online", "lang": "ru", "task": True,
 "title": "AP Calculus AB онлайн на русском: экзамен и подготовка",
 "desc": "AP Calculus AB онлайн на русском: экзамен 10 мая 2027, 42 вопроса теста и 6 развёрнутых, 1 ч 40 мин и 1 ч 30 мин. Физик МГУ, 1:1.",
 "h1": "AP Calculus AB онлайн на русском: что на экзамене и как готовиться",
 "answer": "Экзамен AP Calculus AB в 2027 году — понедельник, 10 мая, первая сессия: тест из 42 вопросов (1 ч 40 мин) и 6 развёрнутых заданий (1 ч 30 мин), по 50% оценки каждая секция. Онлайн один на один с физиком МГУ: формат, юниты и ваши задачи.",
 "facts": ["Дата экзамена AP Calculus AB в 2027 году — понедельник, 10 мая, первая сессия (AP Central)",
           "Секция I (тест): 42 вопроса, 1 ч 40 мин, 50% оценки; секция II (развёрнутые ответы): 6 вопросов, 1 ч 30 мин, 50% оценки",
           "Секция I, часть A: 29 вопросов, 62 мин, без калькулятора; часть B: 13 вопросов, 38 мин, нужен графический калькулятор",
           "Секция II, часть A: 2 вопроса, 30 мин, нужен графический калькулятор; часть B: 4 вопроса, 60 мин, без калькулятора",
           "С мая 2027 изменились число вопросов и время тестовой части: было 30 + 15 вопросов и 60 + 45 мин, стало 29 + 13 и 62 + 38; содержание курса не менялось",
           "Занятия: онлайн, 1:1, русский язык, под ваш часовой пояс; разбор своей задачи — по присланному условию"],
 "sections": [
   ("Что изменилось с мая 2027", "<p>По разъяснениям College Board, с экзамена мая 2027 года изменились число вопросов и время в тестовой секции. Часть A: было 30 вопросов и 60 минут, стало 29 вопросов и 62 минуты. Часть B: было 15 вопросов и 45 минут, стало 13 вопросов и 38 минут. Страница экзамена на AP Central уже показывает новый формат; содержание курса не менялось. Если вы готовитесь по старым материалам, сверяйте числа с таблицей выше.</p>"),
   ("Темы курса и их веса", "<p>По странице курса AP Calculus AB вес юнита в тестовой секции задан диапазоном. Вот некоторые из них:</p><ul>"
    "<li>Unit 5 (Analytical Applications of Differentiation) и Unit 6 (Integration and Accumulation of Change) — по 15–20%;</li>"
    "<li>Unit 1, Unit 2, Unit 4 и Unit 8 — по 10–15%;</li>"
    "<li>Unit 3 и Unit 7 — по 5–10%.</li></ul>"
    "<p>Полный список юнитов и их названия — на " + _ext(_AP_AB_COURSE_URL, "странице курса") + ".</p>"),
   ("Как проходят занятия", _LESSONS_NEWANS),
   ("Что на странице не приводится", "<p>Шкала итогового балла и перечень разрешённых моделей калькуляторов на этой странице намеренно не приводятся: смотрите их на " + _ext("https://apcentral.collegeboard.org/", "AP Central") + ".</p>"),
   ("Официальные документы", "<p>Формат, даты и состав курса публикует College Board: " + _ext(_AP_AB_URL, "страница экзамена AP Calculus AB") + ", " + _ext(_AP_AB_COURSE_URL, "страница курса") + ", " + _ext(_AP_AB_CLARIF_URL, "разъяснения по изменению формата (PDF)") + ". Данные сверены 24.11.2026; перед планированием проверьте их на официальном сайте.</p>"),
 ],
 "faq": [
   ("Когда экзамен AP Calculus AB в 2027 году?", "В понедельник, 10 мая 2027 года, первая сессия — по странице экзамена на AP Central."),
   ("Из каких частей состоит экзамен?", "Из двух секций по 50% оценки. Секция I — тест, 42 вопроса, 1 ч 40 мин. Секция II — развёрнутые ответы, 6 вопросов, 1 ч 30 мин."),
   ("В каких частях нужен калькулятор?", "Графический калькулятор нужен в части B секции I (13 вопросов, 38 мин) и в части A секции II (2 вопроса, 30 мин). В части A секции I (29 вопросов, 62 мин) и части B секции II (4 вопроса, 60 мин) калькулятор не разрешён."),
   ("Что изменилось в формате с мая 2027?", "Изменились число вопросов и время тестовой секции: в части A стало 29 вопросов и 62 минуты вместо 30 и 60, в части B — 13 вопросов и 38 минут вместо 15 и 45. Содержание курса не менялось."),
   ("Какие темы весят больше всего в тестовой секции?", "Unit 5 (аналитические применения производной) и Unit 6 (интегрирование и накопление) — по 15–20%. Unit 1, 2, 4 и 8 — по 10–15%, Unit 3 и 7 — по 5–10%."),
   ("Можно ли прислать свою задачу на разбор?", "Да: пришлите условие, и мы разберём её на занятии. Цель разбора — найти, где ломается рассуждение; результат он не обещает."),
 ],
 "updated": UPDATED_NEWANS,
 "table": _APAB_TABLE_RU,
 "who": _RU_WHO_MATH,
 "course": ("AP Calculus AB онлайн на русском (1:1)", "Индивидуальная онлайн-подготовка к экзамену AP Calculus AB: формат College Board, юниты, разбор задач на русском."),
}
ANSWERS_MATH.append(_APAB_ENTRY_RU)

# 412 — AP Statistics
QUERIES_MATH[412] = "AP Statistics онлайн на русском: формат экзамена в Bluebook и подготовка"
_APSTAT_TABLE_RU = {'title': 'Формат экзамена AP Statistics (по AP Central)',
 'head': ['Секция', 'Вопросы', 'Время', 'Доля оценки', 'Что за вопросы'],
 'rows': [['Секция I (тест)', '42', '1 ч 30 мин', '50%', 'одиночные вопросы и наборы вопросов по общему тексту'],
          ['Секция II (развёрнутые ответы)', '4', '1 ч 30 мин', '50%', 'вопросы 1, 2 и 4 — multi-focus; вопрос 3 — Inference']]}
_APSTAT_ENTRY_RU = {"n": 412, "slug": "ap-statistics-tutor-online", "lang": "ru", "task": True,
 "title": "AP Statistics онлайн на русском: Bluebook и подготовка",
 "desc": "AP Statistics онлайн на русском: экзамен 11 мая 2027 в Bluebook, 42 вопроса теста и 4 развёрнутых, курс пересмотрен. Физик МГУ, 1:1.",
 "h1": "AP Statistics онлайн на русском: формат экзамена в Bluebook и подготовка",
 "answer": "Экзамен AP Statistics в 2027 году — вторник, 11 мая, вторая сессия, полностью цифровой, в приложении Bluebook: тест из 42 вопросов (1 ч 30 мин) и 4 развёрнутых задания (1 ч 30 мин), по 50% оценки. Онлайн один на один с физиком МГУ.",
 "facts": ["Дата экзамена AP Statistics в 2027 году — вторник, 11 мая, вторая сессия (AP Central)",
           "Секция I (тест): 42 вопроса, 1 ч 30 мин, 50% оценки; секция II (развёрнутые ответы): 4 вопроса, 1 ч 30 мин, 50% оценки",
           "Тестовые вопросы бывают одиночные и наборами по общему тексту; в развёрнутой секции вопрос 3 — Inference, вопросы 1, 2 и 4 — multi-focus",
           "Экзамен полностью цифровой, в приложении Bluebook; калькуляторы разрешены",
           "Курс пересмотрен на 2026–27 учебный год, чтобы соответствовать современным вводным университетским курсам статистики",
           "Занятия: онлайн, 1:1, русский язык, под ваш часовой пояс; разбор своей задачи — по присланному условию"],
 "sections": [
   ("Цифровой экзамен в Bluebook", "<p>AP Statistics сдаётся полностью в цифровом виде, в приложении Bluebook: так написано на странице экзамена AP Central. Калькуляторы на экзамене разрешены. Перечень допустимых моделей на этой странице не приводится — его смотрят на сайте College Board.</p>"),
   ("Курс пересмотрен к 2026–27 учебному году", "<p>College Board пересмотрел AP Statistics на 2026–27 учебный год, чтобы курс соответствовал современным вводным университетским курсам статистики. Полные веса всех тем после пересмотра на этой странице не приводятся: сверяйтесь со " + _ext("https://apcentral.collegeboard.org/courses/ap-statistics", "страницей курса") + ".</p>"),
   ("Как проходят занятия", _LESSONS_NEWANS),
   ("Официальные документы", "<p>Формат, даты и состав курса публикует College Board: " + _ext(_AP_STAT_URL, "страница экзамена AP Statistics") + ". Данные сверены 24.11.2026; шкала итогового балла и модели калькуляторов на этой странице намеренно не приводятся — проверьте их на официальном сайте.</p>"),
 ],
 "faq": [
   ("Когда экзамен AP Statistics в 2027 году?", "Во вторник, 11 мая 2027 года, вторая сессия — по странице экзамена на AP Central."),
   ("Как устроен экзамен AP Statistics?", "Две секции по 50% оценки: тест из 42 вопросов (1 ч 30 мин) и 4 развёрнутых вопроса (1 ч 30 мин). В тесте бывают одиночные вопросы и наборы по общему тексту."),
   ("В каком виде проходит экзамен?", "Экзамен полностью цифровой, в приложении Bluebook. Калькуляторы разрешены."),
   ("Что нового в курсе AP Statistics?", "Курс пересмотрен на 2026–27 учебный год, чтобы соответствовать современным вводным университетским курсам статистики."),
   ("Что за вопросы в развёрнутой секции?", "Вопросы 1, 2 и 4 описаны на странице экзамена как multi-focus (на разных практиках), вопрос 3 — как Inference."),
   ("Можно ли прислать свою задачу на разбор?", "Да: пришлите условие, и мы разберём её на занятии. Цель разбора — найти, где ломается рассуждение; результат он не обещает."),
 ],
 "updated": UPDATED_NEWANS,
 "table": _APSTAT_TABLE_RU,
 "who": _RU_WHO_MATH,
 "course": ("AP Statistics онлайн на русском (1:1)", "Индивидуальная онлайн-подготовка к экзамену AP Statistics: цифровой формат Bluebook, разбор задач на русском."),
}
ANSWERS_MATH.append(_APSTAT_ENTRY_RU)

# 413 — ОГЭ по физике
QUERIES_PHYS[413] = "ОГЭ по физике: структура экзамена, баллы, что можно взять с собой и как готовиться"
_OGE_TABLE_RU = {'title': 'Структура экзамена ОГЭ по физике (спецификация КИМ ОГЭ 2027, ФИПИ)',
 'head': ['Параметр', 'Значение'],
 'rows': [['Число заданий', '22 задания, различающиеся формой и уровнем сложности'],
          ['Время на работу', '180 минут (3 часа)'],
          ['Максимальный первичный балл', '39'],
          ['По типу ответа', '16 заданий с кратким ответом и 6 заданий с развёрнутым ответом (17–22)'],
          ['По уровню сложности', 'базовых 14, повышенных 5, высоких 3'],
          ['Баллы за развёрнутые задания', 'задания 18 и 19 — по 2 балла; задания 17 и 20–22 — по 3 балла'],
          ['Что разрешено', 'непрограммируемый калькулятор и линейка']]}
_OGE_ENTRY_RU = {"n": 413, "slug": "oge-fizika-podgotovka-onlajn", "lang": "ru", "task": True,
 "title": "ОГЭ по физике: структура, баллы, что можно взять с собой",
 "desc": "ОГЭ по физике: 22 задания, 180 минут, максимум 39 первичных баллов, калькулятор и линейка. Структура по спецификации ФИПИ. Физик МГУ, 1:1.",
 "h1": "ОГЭ по физике: структура экзамена, баллы, что можно взять с собой и как готовиться",
 "answer": "В варианте ОГЭ по физике 22 задания, на работу даётся 180 минут, максимальный первичный балл — 39; разрешены непрограммируемый калькулятор и линейка. Данные — из спецификации КИМ ОГЭ 2027. Онлайн один на один с физиком МГУ: структура, типы заданий, разбор ваших задач.",
 "facts": ["В каждом варианте 22 задания, различающихся формой и уровнем сложности; время на работу — 180 минут; максимальный первичный балл — 39",
           "16 заданий с кратким ответом и 6 с развёрнутым ответом (задания 17–22); распределение баллов: 3 + 6 + 14 (краткие) и 16 (развёрнутые)",
           "По уровню сложности: базовых заданий 14, повышенных 5, высоких 3",
           "Развёрнутые: задания 18 и 19 — по 2 балла, задания 17 и 20–22 — по 3 балла; проверяют два эксперта",
           "Разрешены непрограммируемый калькулятор и линейка; калькулятор должен считать тригонометрические функции (cos, sin, tg)",
           "Для экспериментальных заданий используются наборы лабораторного оборудования; первичный балл переводится в отметку по пятибалльной шкале",
           "Занятия: онлайн, 1:1, русский язык, под ваш часовой пояс; разбор своей задачи — по присланному условию"],
 "sections": [
   ("Структура работы", "<p>Структура — по спецификации КИМ ОГЭ 2027 года по физике, которую ФИПИ публикует в архиве на странице " + _ext(_FIPI_URL, "демоверсий, спецификаций и кодификаторов") + ". Работа состоит из 22 заданий: 16 с кратким ответом и 6 с развёрнутым (задания 17–22). По уровню сложности это 14 базовых, 5 повышенных и 3 высоких задания. На всю работу даётся 180 минут, максимальный первичный балл — 39.</p>"),
   ("Баллы и проверка", "<p>За развёрнутые задания 18 и 19 даётся по 2 балла, за задания 17 и 20–22 — по 3 балла; такие работы проверяют два эксперта. Первичный балл за всю работу переводится в отметку по пятибалльной шкале. Пороги перевода на этой странице не приводятся: смотрите официальные документы.</p>"),
   ("Что можно взять с собой", "<p>Разрешены непрограммируемый калькулятор и линейка для построения чертежей и рисунков. Калькулятор должен позволять вычислять тригонометрические функции (cos, sin, tg). Для экспериментальных заданий участникам выдают наборы лабораторного оборудования.</p>"),
   ("Как проходят занятия", _LESSONS_NEWANS),
   ("Официальные документы", "<p>Структуру работы публикует ФИПИ: " + _ext(_FIPI_URL, "fipi.ru — демоверсии, спецификации, кодификаторы") + ". Данные сверены 24.11.2026 по спецификации КИМ ОГЭ 2027 года по физике; перед планированием проверьте их на официальном сайте.</p>"),
 ],
 "faq": [
   ("Сколько заданий в ОГЭ по физике?", "В каждом варианте 22 задания: 16 с кратким ответом и 6 с развёрнутым ответом (задания 17–22)."),
   ("Сколько времени даётся на ОГЭ по физике?", "На выполнение работы предоставляется 180 минут (3 часа)."),
   ("Какой максимальный балл за ОГЭ по физике?", "Максимальный первичный балл за работу — 39. Первичный балл переводится в отметку по пятибалльной шкале; пороги перевода на этой странице не приводятся."),
   ("Что можно взять на ОГЭ по физике?", "Непрограммируемый калькулятор и линейку для построения чертежей и рисунков. Калькулятор должен считать тригонометрические функции (cos, sin, tg)."),
   ("Сколько баллов даётся за развёрнутые задания?", "Задания 18 и 19 — по 2 балла, задания 17 и 20–22 — по 3 балла; всего 16 баллов. Проверяют два эксперта."),
   ("Есть ли в ОГЭ по физике экспериментальные задания?", "Да, для экспериментальных заданий используются наборы лабораторного оборудования."),
   ("Можно ли прислать свою задачу на разбор?", "Да: пришлите условие, и мы разберём её на занятии. Цель разбора — найти, где ломается рассуждение; результат он не обещает."),
 ],
 "updated": UPDATED_NEWANS,
 "table": _OGE_TABLE_RU,
 "who": _RU_WHO,
 "course": ("Подготовка к ОГЭ по физике онлайн (1:1)", "Индивидуальная онлайн-подготовка к ОГЭ по физике: структура работы по спецификации ФИПИ, типы заданий, разбор задач."),
}
ANSWERS_PHYS.append(_OGE_ENTRY_RU)

# 414 — GCSE Physics AQA 8463
QUERIES_PHYS[414] = "GCSE Physics (AQA 8463) онлайн на русском: две работы, темы и подготовка"
_GCSE_TABLE_RU = {'title': 'GCSE Physics AQA 8463: две письменные работы (по спецификации AQA)',
 'head': ['Работа', 'Темы', 'Время', 'Баллы', 'Доля оценки'],
 'rows': [['Paper 1', 'темы 1–4: энергия; электричество; модель вещества; атомная структура', '1 ч 45 мин', '100', '50%'],
          ['Paper 2', 'темы 5–8: силы; волны; магнетизм и электромагнетизм; космос', '1 ч 45 мин', '100', '50%']]}
_GCSE_ENTRY_RU = {"n": 414, "slug": "gcse-physics-aqa-8463-tutor-online", "lang": "ru", "task": True,
 "title": "GCSE Physics AQA 8463 онлайн на русском: две работы",
 "desc": "GCSE Physics (AQA 8463) онлайн на русском: две письменные работы по 1 ч 45 мин и 100 баллов, темы 1–8, шкала 1–9. Физик МГУ, 1:1.",
 "h1": "GCSE Physics (AQA 8463) онлайн на русском: две работы, темы и подготовка",
 "answer": "GCSE Physics по спецификации AQA 8463 — две письменные работы: Paper 1 (темы 1–4) и Paper 2 (темы 5–8), у каждой 1 ч 45 мин, 100 баллов и 50% оценки; есть Foundation и Higher. Онлайн один на один с физиком МГУ: темы, формат, ваши задачи.",
 "facts": ["Две письменные работы — Paper 1 и Paper 2; каждая: 1 ч 45 мин, 100 баллов, 50% оценки; есть Foundation и Higher (спецификация AQA 8463)",
           "Paper 1 охватывает темы 1–4: энергия, электричество, модель вещества, атомная структура",
           "Paper 2 охватывает темы 5–8: силы, волны, магнетизм и электромагнетизм, космос",
           "Типы вопросов: с выбором ответа, структурированные, короткие закрытые и открытые развёрнутые",
           "Квалификация линейная: все экзамены сдаются в конце курса; шкала оценок 1–9; Foundation даёт оценки 1–5, Higher — 4–9",
           "Практические работы в процессе не оцениваются, но вопросы по ним есть в письменных экзаменах",
           "Занятия: онлайн, 1:1, русский язык, под ваш часовой пояс; разбор своей задачи — по присланному условию"],
 "sections": [
   ("Две работы и темы", "<p>По спецификации AQA GCSE Physics 8463 экзамен состоит из двух письменных работ. Paper 1 охватывает темы 1–4: энергия, электричество, модель вещества и атомная структура. Paper 2 охватывает темы 5–8: силы, волны, магнетизм и электромагнетизм, космос. Вопросы Paper 2 могут опираться на понимание превращений и передачи энергии и на электричество из Paper 1.</p>"),
   ("Формат и оценки", "<p>Каждая работа длится 1 ч 45 мин, в ней 100 баллов, это 50% оценки. Типы вопросов: с выбором ответа, структурированные, короткие закрытые и открытые развёрнутые. Работы бывают двух уровней, Foundation и Higher. Оценки идут по шкале 1–9: Foundation даёт оценки от 1 до 5, Higher — от 4 до 9. Квалификация линейная: все экзамены сдаются в конце курса.</p>"),
   ("Практические работы", "<p>Практические работы в процессе выполнения не оцениваются, но письменные экзамены включают вопросы по ним.</p>"),
   ("Как проходят занятия", _LESSONS_NEWANS),
   ("Официальные документы", "<p>Состав и формат экзамена публикует AQA: " + _ext(_AQA_SPEC_URL, "спецификация GCSE Physics 8463 (PDF)") + ", " + _ext(_AQA_GLANCE_URL, "страница specification at a glance") + ". Данные сверены 24.11.2026. Правила про калькулятор и состав листа формул на этой странице не приводятся — проверьте их в спецификации.</p>"),
 ],
 "faq": [
   ("Из чего состоит экзамен GCSE Physics AQA 8463?", "Из двух письменных работ, Paper 1 и Paper 2. Каждая длится 1 ч 45 мин, в ней 100 баллов, это 50% оценки."),
   ("Какие темы в Paper 1 и Paper 2?", "Paper 1 — темы 1–4: энергия, электричество, модель вещества, атомная структура. Paper 2 — темы 5–8: силы, волны, магнетизм и электромагнетизм, космос."),
   ("Чем отличаются Foundation и Higher?", "Это два уровня работ. Foundation даёт оценки от 1 до 5, Higher — от 4 до 9 по шкале 1–9."),
   ("Какие бывают вопросы в работах?", "С выбором ответа, структурированные, короткие закрытые и открытые развёрнутые."),
   ("Когда сдаются экзамены?", "Квалификация линейная: все экзамены сдаются в конце курса."),
   ("Оцениваются ли практические работы?", "В процессе выполнения не оцениваются, но письменные экзамены включают вопросы по ним."),
   ("Можно ли прислать свою задачу на разбор?", "Да: пришлите условие, и мы разберём её на занятии. Цель разбора — найти, где ломается рассуждение; результат он не обещает."),
 ],
 "updated": UPDATED_NEWANS,
 "table": _GCSE_TABLE_RU,
 "who": _RU_WHO,
 "course": ("GCSE Physics (AQA 8463) онлайн на русском (1:1)", "Индивидуальная онлайн-подготовка к GCSE Physics по спецификации AQA 8463: две работы, темы 1–8, разбор задач на русском."),
}
ANSWERS_PHYS.append(_GCSE_ENTRY_RU)
