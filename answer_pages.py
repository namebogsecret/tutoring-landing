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
    404: "Подготовка к A-level и IB по физике онлайн: программа, план по месяцам, разбор типичных ошибок",
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
    "<ul><li><b>Движение, силы и энергия</b> — задачи на кинематику, силы, работу и энергию;</li>"
    "<li><b>Тепловая физика</b> — теплоёмкость, агрегатные состояния, газовые законы;</li>"
    "<li><b>Волны</b> — свойства волн, свет и звук;</li>"
    "<li><b>Электричество и магнетизм</b> — цепи, поля, электромагнитные явления;</li>"
    "<li><b>Ядерная физика</b> — строение атома, радиоактивность;</li>"
    "<li><b>Космическая физика</b> — Солнечная система, звёзды, Вселенная.</li></ul>"
    "<p>Практические навыки оцениваются отдельно: Paper 5 или Paper 6, 20% оценки. Термины и формулировки заданий остаются английскими, как на экзамене.</p>")]
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
      {_razbor_block(a)}
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
