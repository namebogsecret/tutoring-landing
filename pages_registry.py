# -*- coding: utf-8 -*-
"""Page registry for the content layer. Edit prose in src/*.html; edit
meta/FAQ/schema here, then run `python3 build.py`."""

PROVIDER = {
    "@type": "Person",
    "name": "Vladimir Podlevskikh",
    "url": "https://tutor.podlevskikh.com/",
    "alumniOf": {"@type": "CollegeOrUniversity", "name": "Lomonosov Moscow State University", "alternateName": "MSU"},
}

def course(name, desc):
    return {
        "@context": "https://schema.org", "@type": "Course", "name": name, "description": desc,
        "provider": {"@type": "Person", "name": "Vladimir Podlevskikh", "url": "https://tutor.podlevskikh.com/"},
        "hasCourseInstance": {"@type": "CourseInstance", "courseMode": "online",
                              "courseWorkload": "PT1H", "instructor": {"@type": "Person", "name": "Vladimir Podlevskikh"}},
        "inLanguage": ["en", "ru"],
    }

def service(name, desc, area="Worldwide"):
    return {
        "@context": "https://schema.org", "@type": "Service", "serviceType": "Online tutoring",
        "name": name, "description": desc, "areaServed": area,
        "provider": {"@type": "Person", "name": "Vladimir Podlevskikh", "url": "https://tutor.podlevskikh.com/"},
    }

PAGES = [

# ═══════════════════════ PILLAR 1 — IB Physics (EN) ═══════════════════════
{
  "url": "/ib-physics-tutor/", "lang": "en", "body": "src/ib-physics-tutor.html",
  "title": "IB Physics Tutor (HL & SL) Online — MSU Physicist, 200/200 Praxis",
  "desc": "Online IB Physics HL & SL tutor. MSU physicist, 23+ years, 350+ students. Paper 1/2/3 technique, IA support and the jump on the 1–7 scale. Free 20-min diagnostic.",
  "og_title": "IB Physics Tutor (HL/SL) Online — Vladimir Podlevskikh",
  "crumbs": [("Home", "/"), ("IB Physics Tutor", None)],
  "jsonld": [course("IB Physics HL & SL — online exam preparation",
                    "Structured one-to-one IB Physics tutoring (HL and SL): full syllabus, Internal Assessment support, Paper 1/2/3 technique and grade-boundary work, online worldwide.")],
  "faq_heading": "IB Physics tutoring — common questions",
  "faq": [
    ("Do you teach IB Physics HL and SL?",
     "Yes — both levels, to the current IB syllabus. HL adds the extra topics and the deeper Paper-3 (Option/data) work; SL focuses on core mastery and exam technique. Lessons are mapped to your exact subject guide and the assessment objectives (AO1–AO3)."),
    ("Can you help with the Internal Assessment (IA)?",
     "Yes. The IA is 20% of the grade and the most reliable place to add marks. I help you choose a researchable question, design the method, handle uncertainties and error propagation correctly, and structure the analysis and evaluation against the IB rubric — without writing it for you."),
    ("How much does IB Physics tutoring cost?",
     "Standard is $390/month (one weekly 1:1 lesson); Intensive is $680/month (two lessons/week, about $85/session). A one-off trial is $90 for 60 minutes; a self-paced study plan starts at $49. Premium IB HL coaching is $120–135/hour. The exact plan is set on the free consultation."),
    ("How quickly can an IB Physics grade improve?",
     "It depends on the starting point and time to the exam, but most students who follow the weekly plan move at least one band on the 1–7 scale. The fastest gains come from Paper-1 (multiple-choice) timing, the IA, and command-term discipline on Paper 2."),
    ("Which time zones do you cover?",
     "Based in Yerevan (GMT+4), which works cleanly for IB families across the Gulf, Europe, the UK, Africa and most of Asia. Lessons are online 1:1 over Zoom with a shared whiteboard, in English."),
  ],
},

# ═══════════════════════ PILLAR 2 — AP Physics (EN) ═══════════════════════
{
  "url": "/ap-physics-tutor/", "lang": "en", "body": "src/ap-physics-tutor.html",
  "title": "AP Physics Tutor Online — Physics 1, 2 & C (Mechanics, E&M)",
  "desc": "Online AP Physics tutor for Physics 1, 2 and C. MSU physicist, perfect 200/200 US Praxis Physics. FRQ technique and a clear route to the 5. Free 20-min diagnostic.",
  "og_title": "AP Physics Tutor (1, 2, C) Online — Vladimir Podlevskikh",
  "crumbs": [("Home", "/"), ("AP Physics Tutor", None)],
  "jsonld": [course("AP Physics 1, 2 & C — online exam preparation",
                    "One-to-one AP Physics tutoring for Physics 1, Physics 2 and Physics C (Mechanics and E&M): unit mastery, free-response technique and full-exam simulation toward a 5.")],
  "faq_heading": "AP Physics tutoring — common questions",
  "faq": [
    ("Which AP Physics courses do you cover?",
     "All of them: Physics 1 (algebra-based mechanics), Physics 2 (fluids, thermodynamics, electricity, optics, modern), and Physics C — both Mechanics and Electricity &amp; Magnetism, including the calculus the C exams assume."),
    ("Is AP Physics C calculus-based — can you teach the maths too?",
     "Yes. Physics C is calculus-based, and most students lose marks where the calculus and the physics meet (derivatives of motion, integrals for fields and potentials). I teach both together, so the maths becomes a tool rather than a separate hurdle. Perfect 200/200 on US Praxis Maths as well as Physics."),
    ("How do you prepare for the free-response (FRQ) section?",
     "FRQs reward a specific way of writing: state the principle, show the relation, then substitute. We drill released College Board FRQs, mark them against the official rubric point-by-point, and fix the habits that quietly cost points — units, sign conventions, and 'explain' vs 'justify'."),
    ("How much does AP Physics tutoring cost?",
     "Standard is $390/month (one weekly lesson), Intensive is $680/month (two lessons/week). A one-off trial is $90/60 min; a self-paced plan starts at $49. The exact plan is set on the free consultation, once we know the course, the gap and the exam date."),
    ("When should we start before the May exam?",
     "Ideally by autumn for a full build, but a focused 8–12 week sprint before May still moves most students up a grade — we prioritise the highest-weight units and the FRQ technique first."),
  ],
},

# ═══════════════ PILLAR 3 — Репетитор по физике онлайн (RU) ═══════════════
{
  "url": "/physics-tutor-online/", "lang": "ru", "body": "src/physics-tutor-online.html",
  "title": "Репетитор по физике онлайн — физик МГУ, 23 года, 350+ учеников",
  "desc": "Репетитор по физике онлайн: физик МГУ, 23 года опыта, 350+ учеников. Подготовка к ЕГЭ, ОГЭ, ДВИ, олимпиадам, IB, AP, A-Level. Структурный план к экзамену. Бесплатная диагностика.",
  "og_title": "Репетитор по физике онлайн — Владимир Подлевских (физик МГУ)",
  "crumbs": [("Главная", "/"), ("Репетитор по физике онлайн", None)],
  "jsonld": [service("Репетитор по физике онлайн",
                     "Индивидуальные онлайн-занятия по физике: ЕГЭ, ОГЭ, ДВИ, олимпиады, IB, AP, A-Level. Физик МГУ, 23 года опыта, структурный план к экзамену.")],
  "faq_heading": "Частые вопросы о занятиях по физике",
  "faq": [
    ("К каким экзаменам по физике вы готовите?",
     "ЕГЭ и ОГЭ, ДВИ МГУ и внутренние экзамены вузов, олимпиады, а также международные программы — IB Physics (HL/SL), AP Physics (1, 2, C), A-Level и IGCSE. Под каждый экзамен — отдельная программа по официальной спецификации и критериям."),
    ("Сколько стоит занятие с репетитором по физике?",
     "Формат «к результату», а не «по часам». Пакет Standard — $390/мес (одно занятие в неделю), Intensive — $680/мес (два занятия). Разовое пробное — $90/60 мин, самостоятельный план — от $49. Точную цену и план определяем на бесплатной диагностике. Оплата в USD/EUR через Payoneer или карту."),
    ("Как проходят онлайн-занятия?",
     "Индивидуально 1:1 в Zoom с общей интерактивной доской. Каждое занятие привязано к личному плану подготовки и к структуре конкретного экзамена. Между занятиями — проверяемые домашние задания и доступ к авторскому банку задач."),
    ("На сколько баллов реально поднять результат?",
     "Зависит от старта и времени до экзамена, но при соблюдении плана типичный прирост — десятки баллов за год. Например: физика 82 → 96 на госэкзамене; SAT 1620 → 2060 за два месяца. Прогноз — это карта при условии выполнения плана, а не обещание."),
    ("Вы преподаёте на русском и английском?",
     "Да, билингвально. РФ-программы (ЕГЭ/ОГЭ/ДВИ) — на русском; международные (IB/AP/A-Level) — на английском или смешанно, как удобнее ученику. Это удобно русскоязычным семьям за рубежом, перешедшим в международную школу."),
  ],
},

# ═══════════════ PILLAR 4 — Подготовка к ЕГЭ по физике (RU) ═══════════════
{
  "url": "/ege-physics/", "lang": "ru", "body": "src/ege-physics.html",
  "title": "Подготовка к ЕГЭ по физике онлайн — физик МГУ, план до экзамена",
  "desc": "Подготовка к ЕГЭ по физике онлайн с физиком МГУ. Разбор всех типов заданий первой и второй части, план по неделям до экзамена, банк задач, прогноз балла. Бесплатная диагностика.",
  "og_title": "Подготовка к ЕГЭ по физике онлайн — Владимир Подлевских",
  "crumbs": [("Главная", "/"), ("Подготовка к ЕГЭ по физике", None)],
  "jsonld": [course("Подготовка к ЕГЭ по физике (онлайн)",
                    "Онлайн-подготовка к ЕГЭ по физике: разбор всех типов заданий, план по неделям до экзамена, тренировка второй части и оформление, прогноз балла.")],
  "faq_heading": "Подготовка к ЕГЭ по физике — частые вопросы",
  "faq": [
    ("За сколько до экзамена начинать подготовку к ЕГЭ по физике?",
     "Оптимально — с начала 11 класса (полный цикл с запасом на повторение). Но и интенсив за 4–6 месяцев даёт результат: в этом случае начинаем с самых «дорогих» по баллам тем и второй части, а первую часть закрываем параллельно тренировкой на скорость и точность."),
    ("Как устроена вторая часть и почему на ней теряют баллы?",
     "Вторая часть — задачи с развёрнутым решением, где эксперт оценивает не только ответ, но и оформление: дано, физические законы, рисунок, обоснование. Чаще всего баллы теряют не на физике, а на оформлении и логике. Мы отрабатываем решения строго по критериям проверки ФИПИ."),
    ("Сколько стоит подготовка к ЕГЭ по физике?",
     "Standard — $390/мес (одно занятие в неделю + личный план), Intensive — $680/мес (два занятия в неделю с проверкой домашних работ). Разовое занятие — $90/60 мин, самостоятельный план — от $49. Точную программу подбираем на бесплатной диагностике."),
    ("Готовите ли вы одновременно к ЕГЭ и ДВИ?",
     "Да. ДВИ МГУ и внутренние экзамены вузов требуют более глубокого уровня, чем ЕГЭ, — это отдельный трек поверх ЕГЭ-программы. Пример: ученица сдала ЕГЭ на 96 и ДВИ на 100 — поступление на мехмат."),
    ("Что входит в подготовку, кроме занятий?",
     "Личный план по неделям до даты экзамена, авторский банк задач по каждой теме, проверяемые домашние задания, трекер прогресса и ежемесячный отчёт для родителей с текущим прогнозом балла."),
  ],
},

# ═══════════════ SEGMENT 1 — Русскоязычным за рубежом (RU) ════════════════
{
  "url": "/russian-tutor-abroad/", "lang": "ru", "body": "src/russian-tutor-abroad.html",
  "title": "Репетитор по физике и математике для русскоязычных за рубежом",
  "desc": "Репетитор по физике и математике для русскоязычных семей за границей. Поможет ребёнку в международной школе: IB, AP, A-Level, IGCSE — на русском и английском. Любой часовой пояс, оплата в USD/EUR.",
  "og_title": "Репетитор для русскоязычных за рубежом — физика и математика",
  "crumbs": [("Главная", "/"), ("Русскоязычным за рубежом", None)],
  "jsonld": [service("Репетитор по физике и математике для русскоязычных за рубежом",
                     "Онлайн-репетитор для русскоязычных детей в международных школах за границей: IB, AP, A-Level, IGCSE на русском и английском, любой часовой пояс.", "Worldwide")],
  "faq_heading": "Русскоязычным семьям за рубежом — частые вопросы",
  "faq": [
    ("Ребёнок перешёл из российской школы в международную — поможете адаптироваться?",
     "Это мой ключевой профиль. Я сам преподаю физику на английском в международной школе и одновременно носитель русской физической школы. Помогаю перейти с российской программы на IB/AP/A-Level: закрыть терминологические разрывы, перестроиться на формат экзамена и критерии, не теряя сильную математическую базу."),
    ("На каком языке идут занятия?",
     "Как удобно ребёнку: можно полностью на английском (тогда заодно подтягиваем академический английский по предмету), полностью на русском, или смешанно — объясняю сложное на русском, термины и оформление закрепляем на английском. Это снимает языковой барьер в первый год за рубежом."),
    ("Как быть с разными часовыми поясами?",
     "Я в Ереване (GMT+4), и это удобная точка для семей в Европе, Великобритании, Персидском заливе, Африке и большей части Азии. Время занятий подбираем под ваш пояс; всё онлайн 1:1 в Zoom."),
    ("Как происходит оплата из-за рубежа?",
     "В USD или EUR через Payoneer или защищённую ссылку на карту — удобно из любой страны. Способ подтверждаем на консультации до первого занятия."),
    ("Можно совмещать школьную программу за рубежом и подготовку к российским экзаменам?",
     "Да. Некоторые семьи держат «российский трек» (ЕГЭ/ОГЭ/ДВИ) параллельно международной школе — на случай возвращения или поступления в вуз РФ. Я веду оба, согласовав нагрузку, чтобы не перегрузить ребёнка."),
  ],
},

# ═══════════════ SEGMENT 2 — Подготовка к олимпиадам (RU) ═════════════════
{
  "url": "/olympiad-physics/", "lang": "ru", "body": "src/olympiad-physics.html",
  "title": "Подготовка к олимпиадам по физике и математике — онлайн",
  "desc": "Подготовка к олимпиадам по физике и математике онлайн: Всероссийская олимпиада, перечневые олимпиады, Physics Olympiad. Физик МГУ, 20+ призёров. Нестандартные задачи и техника решения.",
  "og_title": "Подготовка к олимпиадам по физике и математике — Владимир Подлевских",
  "crumbs": [("Главная", "/"), ("Подготовка к олимпиадам", None)],
  "jsonld": [course("Подготовка к олимпиадам по физике и математике",
                    "Онлайн-подготовка к олимпиадам по физике и математике: Всероссийская и перечневые олимпиады, международные Physics Olympiad. Нестандартные задачи, техника решения, разбор прошлых лет.")],
  "faq_heading": "Подготовка к олимпиадам — частые вопросы",
  "faq": [
    ("К каким олимпиадам вы готовите?",
     "Всероссийская олимпиада школьников (ВсОШ) по физике и математике, перечневые олимпиады (Физтех, «Покори Воробьёвы горы», Росатом, ОММО и др.), а также международные форматы — Physics Olympiad / IPhO-стиль. За 20+ лет — более 20 призёров и победителей."),
    ("Чем подготовка к олимпиаде отличается от подготовки к ЕГЭ?",
     "ЕГЭ проверяет надёжность на типовых задачах, олимпиада — способность к нестандартному ходу и глубину модели. Это разные навыки: на олимпиаде нужны нетабличные методы, оценки порядка величины, красивые приёмы и умение довести длинное решение. Поэтому олимпиадный трек строится отдельно, поверх прочной школьной базы."),
    ("С какого возраста и уровня имеет смысл начинать?",
     "Математические олимпиады я веду уже с 4–6 класса — там закладывается вкус к задаче. По физике осмысленно начинать, когда есть базовая механика. Главный критерий — не оценки, а интерес: с мотивированным ребёнком прогресс быстрый."),
    ("Как проходят занятия по олимпиадной подготовке?",
     "Разбор задач прошлых лет по темам, авторские подборки нарастающей сложности, техника оформления длинного решения и работа над типовыми «ловушками». Между занятиями — задачи на подумать, без жёстких дедлайнов, но с разбором каждой."),
    ("Олимпиада помогает с поступлением?",
     "Да — призовые места дают льготы при поступлении (БВИ или 100 баллов за предмет во многих вузах РФ), а олимпиадный опыт сильно усиливает заявку в зарубежные университеты. Пример: олимпиадная подготовка → поступление в МГТУ им. Баумана, диплом с отличием."),
  ],
},

# ═══════════════════════════ BLOG INDEX ══════════════════════════════════
{
  "url": "/blog/", "lang": "en", "body": "src/blog-index.html",
  "title": "Physics & Maths Method Blog — worked problems, exam technique",
  "desc": "Worked-problem walkthroughs and exam-technique notes for IB, AP, SAT, A-Level and ЕГЭ physics and maths — from an MSU physicist. Each article links to free calculators and the olympiad knowledge base.",
  "og_title": "Method Blog — physics & maths worked problems and exam technique",
  "og_type": "website",
  "crumbs": [("Home", "/"), ("Blog", None)],
  "jsonld": [{
    "@context": "https://schema.org", "@type": "Blog",
    "name": "Podlevskikh — Physics & Maths Method Blog",
    "url": "https://tutor.podlevskikh.com/blog/",
    "author": {"@type": "Person", "name": "Vladimir Podlevskikh"},
    "description": "Worked-problem walkthroughs and exam-technique notes for IB, AP, SAT, A-Level and ЕГЭ physics and maths.",
  }],
},

# ════════════════════ BLOG POST 1 — kinematics graphs (RU) ════════════════
{
  "url": "/blog/kinematics-grafiki/", "lang": "ru", "body": "src/post-kinematics-grafiki.html",
  "title": "Как читать графики движения: разбор типовых задач кинематики",
  "desc": "Графики x(t), v(t), a(t) в задачах по кинематике: как переходить от одного к другому, где наклон, а где площадь, и какие ловушки встречаются на ЕГЭ, ОГЭ и IB/AP. Разбор с примерами.",
  "og_title": "Как читать графики движения — кинематика по шагам",
  "crumbs": [("Home", "/"), ("Blog", "/blog/"), ("Графики движения", None)],
  "jsonld": [{
    "@context": "https://schema.org", "@type": "Article",
    "headline": "Как читать графики движения: разбор типовых задач кинематики",
    "author": {"@type": "Person", "name": "Vladimir Podlevskikh", "url": "https://tutor.podlevskikh.com/"},
    "datePublished": "2026-06-14", "inLanguage": "ru",
    "publisher": {"@type": "Person", "name": "Vladimir Podlevskikh"},
    "mainEntityOfPage": "https://tutor.podlevskikh.com/blog/kinematics-grafiki/",
    "about": ["Kinematics", "Physics graphs", "ЕГЭ физика"],
  }],
},

# ═══════════════════ BLOG POST 2 — Newton's laws (RU) ═════════════════════
{
  "url": "/blog/newton-zakony-zadachi/", "lang": "ru", "body": "src/post-newton-zakony.html",
  "title": "Второй закон Ньютона: типовые задачи и частые ошибки",
  "desc": "Второй закон Ньютона на практике: как правильно расставлять силы, выбирать оси и решать задачи с наклонной плоскостью, связанными телами и трением. Разбор типовых ошибок для ЕГЭ, A-Level, AP.",
  "og_title": "Второй закон Ньютона — типовые задачи и ошибки",
  "crumbs": [("Home", "/"), ("Blog", "/blog/"), ("Законы Ньютона", None)],
  "jsonld": [{
    "@context": "https://schema.org", "@type": "Article",
    "headline": "Второй закон Ньютона: типовые задачи и частые ошибки",
    "author": {"@type": "Person", "name": "Vladimir Podlevskikh", "url": "https://tutor.podlevskikh.com/"},
    "datePublished": "2026-06-14", "inLanguage": "ru",
    "publisher": {"@type": "Person", "name": "Vladimir Podlevskikh"},
    "mainEntityOfPage": "https://tutor.podlevskikh.com/blog/newton-zakony-zadachi/",
    "about": ["Newton's laws", "Dynamics", "Physics problem solving"],
  }],
},

# ═════════════════ BLOG POST 3 — IB Paper 2 technique (EN) ════════════════
{
  "url": "/blog/ib-physics-paper-2/", "lang": "en", "body": "src/post-ib-paper-2.html",
  "title": "IB Physics Paper 2: how to structure long-answer questions",
  "desc": "IB Physics Paper 2 technique: decode command terms, structure extended-response answers, handle data and uncertainties, and stop losing marks you already know. A worked method from an MSU physicist.",
  "og_title": "IB Physics Paper 2 — structuring long-answer questions",
  "crumbs": [("Home", "/"), ("Blog", "/blog/"), ("IB Physics Paper 2", None)],
  "jsonld": [{
    "@context": "https://schema.org", "@type": "Article",
    "headline": "IB Physics Paper 2: how to structure long-answer questions",
    "author": {"@type": "Person", "name": "Vladimir Podlevskikh", "url": "https://tutor.podlevskikh.com/"},
    "datePublished": "2026-06-14", "inLanguage": "en",
    "publisher": {"@type": "Person", "name": "Vladimir Podlevskikh"},
    "mainEntityOfPage": "https://tutor.podlevskikh.com/blog/ib-physics-paper-2/",
    "about": ["IB Physics", "Exam technique", "Command terms"],
  }],
},

]
