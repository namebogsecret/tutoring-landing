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
from pages_registry import course, service

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
    href = (f"{RAZBOR_BOOK_URL}?utm_source=tutor.podlevskikh.com&amp;utm_medium=razbor&amp;utm_campaign={slug}")
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
    upd = (f'    <p class="muted"><time datetime="{a["updated"]}">'
           f'{"Обновлено" if ru else "Updated"}: {_fmt_date(a["updated"], ru)}</time></p>\n') if a.get("updated") else ""
    who = _RU_WHO if ru else _EN_WHO
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
      <h2 id="facts">{"Коротко" if ru else "Key facts"}</h2>
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
        twin = next((e for e in ANSWERS_EN if e["twin"] == a["n"]), None)
        other = (f"{HUB}{twin['slug']}/", "en") if twin else None
    else:
        twin = next((r for r in ANSWERS if r["n"] == a.get("twin")), None)
        other = (f"{HUB}{twin['slug']}/", "ru") if twin else None
    alts = [(a["lang"], me)]
    if other:
        alts.append((other[1], other[0]))
    en_url = me if a["lang"] == "en" else (other[0] if other else None)
    alts.append(("x-default", en_url or me))
    return alts


def _page(a):
    ru = a["lang"] == "ru"
    a = dict(a, query=QUERIES[a["n"]] if a["n"] in QUERIES else QUERIES_EN[a["twin"]])
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
        "jsonld": [ld] + ([{"@context": "https://schema.org", "@type": "WebPage", "name": a["title"],
                            "url": BASE_URL + f"{HUB}{a['slug']}/", "inLanguage": a["lang"],
                            "dateModified": a["updated"]}] if a.get("updated") else []),
        "faq_heading": "Частые вопросы" if ru else "Common questions",
        "faq": a["faq"],
    }


def _hub():
    rows = "".join(
        f'<li><a href="{HUB}{a["slug"]}/">{QUERIES[a["n"]]}</a></li>' for a in ANSWERS)
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
      <h2>Программы</h2>
      <ul>{"".join(f'<li><a href="{h}">{t}</a></li>' for h, t in PILLARS["ru"])}</ul>
    </div>
  </div>
</section>
</main>"""
    return {"url": HUB, "lang": "ru", "body_html": body, "no_cta": True, "lastmod": LASTMOD,
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
      <h2>Programmes</h2>
      <ul>{"".join(f'<li><a href="{h}">{t}</a></li>' for h, t in PILLARS["en"])}</ul>
    </div>
  </div>
</section>
</main>"""
    return {"url": HUB_EN, "lang": "en", "body_html": body, "no_cta": True, "lastmod": LASTMOD_EN,
            "title": "Physics tutor answers: EGE, IB, AP, IGCSE",
            "desc": "Short answers: physics tutor for the EGE, IB, AP Physics and IGCSE 0625 online, in English and Russian. MSU physicist, 23 years of experience.",
            "crumbs": [("Home", "/"), ("Answers", None)],
            "alternates": [("ru", HUB), ("en", HUB_EN), ("x-default", HUB_EN)],
            "jsonld": [service("Online physics tutor: answers to common questions",
                               "Answer pages on EGE, IB, AP and IGCSE preparation online, one-to-one.")],
            "faq": []}


def answer_pages():
    return [_hub(), _hub_en()] + [_page(a) for a in ANSWERS] + [_page(a) for a in ANSWERS_EN]
