# -*- coding: utf-8 -*-
"""Page registry for the content layer. Edit prose in src/*.html; edit
meta/FAQ/schema here, then run `python3 build.py`."""

# Канонический узел бренд-сущности — один @id на всю сеть сайтов (GEO entity graph).
PERSON_ID = "https://tutor.podlevskikh.com/#vladimir"

# ── ЕДИНЫЙ ИСТОЧНИК ИСТИНЫ для сети podlevskikh.com ───────────────────────
# Живые проекты сети (кроме самого tutor — это self, покрыт Person.url).
# Из этого списка рендерится видимый футер «Проекты сети» (net-band в build.py).
# В Person.sameAs они НЕ входят: сайт-проект — не этот человек. Машинно связь выражена
# через Person.subjectOf -> WebSite (creator/author = {"@id": PERSON_ID}).
# Добавляешь новый сайт в сеть → правишь ТОЛЬКО этот список (+ вручную index.html: главная не проходит через build.py).
NETWORK_SITES = [
    {"url": "https://physics.podlevskikh.com/",     "label": "Физика — теория и практика"},
    {"url": "https://calc.podlevskikh.com/",        "label": "Баллы ЕГЭ/ОГЭ"},
    {"url": "https://calculators.podlevskikh.com/", "label": "Калькуляторы"},
    {"url": "https://olymp.podlevskikh.com/",       "label": "Олимпиады физ-мат"},
    {"url": "https://exam.podlevskikh.com/",        "label": "Экспресс-тест по экзаменам"},
    {"url": "https://graph.podlevskikh.com/",       "label": "Графический калькулятор"},
    {"url": "https://python.podlevskikh.com/",      "label": "Python Learning Game"},
    {"url": "https://praxis.podlevskikh.com/",      "label": "Praxis 5266"},
    {"url": "https://rocket.podlevskikh.com/",      "label": "RocketSim"},
    {"url": "https://space.podlevskikh.com/",       "label": "Interstellar"},
    {"url": "https://podlevskikh.com/",             "label": "Главный сайт"},
]
# Внешние профили, являющиеся самим человеком (LinkedIn / Preply / Telegram / Profi.ru /
# Lessonface / Superprof; последние два подтверждены владельцем 08.11.2026).
EXTERNAL_PROFILES = [
    "https://linkedin.com/in/vladimir-podlevskikh",
    "https://preply.in/VLADIMIR6EN2958527510",
    "https://t.me/VladimirPodlevskikh",
    "https://profi.ru/profile/PodlevskihVN/",
    "https://www.lessonface.com/node/133512",
    "https://www.superprof.com/mathematics-msu-superprof-super-tutor-for-gcse-igcse-level-sat.html",
]
PERSON_SAMEAS = list(EXTERNAL_PROFILES)
# Собственные проекты — отдельным свойством: WebSite-узлы, автор — тот же @id.
PERSON_SUBJECT_OF = [
    {"@type": "WebSite", "url": s["url"], "name": s["label"],
     "creator": {"@id": "https://tutor.podlevskikh.com/#vladimir"}}
    for s in NETWORK_SITES
]
PROVIDER = {
    "@type": "Person",
    "@id": PERSON_ID,
    "name": "Vladimir Podlevskikh",
    "alternateName": "Владимир Подлевских",
    "url": "https://tutor.podlevskikh.com/",
    "alumniOf": {"@type": "CollegeOrUniversity", "name": "Lomonosov Moscow State University", "alternateName": "MSU"},
    "sameAs": PERSON_SAMEAS,
    "subjectOf": PERSON_SUBJECT_OF,
}
# Лёгкая ссылка на ту же сущность по @id (для author/provider/instructor на дочерних страницах).
PERSON_REF = {"@id": PERSON_ID}

def course(name, desc, lang=("en", "ru")):
    return {
        "@context": "https://schema.org", "@type": "Course", "name": name, "description": desc,
        "provider": PROVIDER,
        "hasCourseInstance": {"@type": "CourseInstance", "courseMode": "online",
                              "courseWorkload": "PT1H", "instructor": PERSON_REF},
        "inLanguage": list(lang),
    }

def service(name, desc, area="Worldwide"):
    return {
        "@context": "https://schema.org", "@type": "Service", "serviceType": "Online tutoring",
        "name": name, "description": desc, "areaServed": area,
        "provider": PROVIDER,
    }

PAGES = [

# ═══════════════════════ PILLAR 1 — IB Physics (EN) ═══════════════════════
{
  "url": "/ib-physics-tutor/", "lang": "en", "body": "src/ib-physics-tutor.html",
  "title": "IB Physics Tutor (HL & SL) Online — MSU Physicist, 200/200 Praxis",
  "desc": "Online IB Physics HL & SL tutor. MSU physicist, 23 years of private tutoring, 350+ students. Paper 1/2/3 technique, IA support and the jump on the 1–7 scale. Free 20-min diagnostic.",
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
     "Available worldwide (GMT+2/+3), which works cleanly for IB families across the Gulf, Europe, the UK, Africa and most of Asia. Lessons are online 1:1 over Zoom with a shared whiteboard, in English."),
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
     "Зависит от старта и времени до экзамена, поэтому балл не обещаю. Пример: Полина М. — 96 ЕГЭ и 100 ДВИ, мехмат МГУ. Прогноз — это карта при условии выполнения плана, а не обещание."),
    ("Вы преподаёте на русском и английском?",
     "Да, билингвально. РФ-программы (ЕГЭ/ОГЭ/ДВИ) — на русском; международные (IB/AP/A-Level) — на английском или смешанно, как удобнее ученику. Это удобно русскоязычным семьям за рубежом, перешедшим в международную школу."),
  ],
},

# ═══════════════ PILLAR 4 — Подготовка к ЕГЭ по физике (RU) ═══════════════
{
  "url": "/ege-physics/", "lang": "ru", "body": "src/ege-physics.html",
  "no_cta": True, "lastmod": "2026-11-08",
  "title": "ЕГЭ по физике 2027: структура КИМ и подготовка онлайн 1:1",
  "desc": "Подготовка к ЕГЭ по физике 2027 онлайн, 1:1: структура КИМ (26 заданий, 45 баллов, 235 минут), вторая часть и критерии, ДВИ. Физик МГУ, Praxis 200/200.",
  "og_title": "Подготовка к ЕГЭ по физике 2027 онлайн — Владимир Подлевских",
  "crumbs": [("Главная", "/"), ("Подготовка к ЕГЭ по физике", None)],
  "jsonld": [course("Подготовка к ЕГЭ по физике (онлайн, 1:1)",
                    "Онлайн-подготовка к ЕГЭ по физике по спецификации КИМ ЕГЭ 2027: 26 заданий, две части, 45 первичных баллов; разбор типов заданий, тренировка развёрнутых решений по критериям, варианты в условиях экзамена.",
                    lang=("ru",))],
  "faq_heading": "Подготовка к ЕГЭ по физике — частые вопросы",
  "faq": [
    ("Когда начинать подготовку к ЕГЭ по физике?",
     "Оптимально — с начала 11 класса: тогда хватает времени на весь курс, повторение и тренировочные варианты. Если времени меньше, начинаем с тех тем, которые дают больше всего баллов, и со второй части, а первую часть закрываем параллельно. Что реально успеть к вашей дате, видно после входной диагностики."),
    ("Что такое вторая часть и почему на ней теряют баллы?",
     "Вторая часть — шесть заданий с развёрнутым ответом (№21–26), в сумме 17 баллов из 45. Их проверяют эксперты предметных комиссий по критериям, поэтому оценивается не только ответ, но и полнота решения: названные законы, обоснование, ход рассуждений. Чаще всего баллы теряются на оформлении и логике, а не на незнании физики."),
    ("Можно ли готовиться к ЕГЭ и ДВИ одновременно?",
     "Да. ДВИ и вступительные испытания вузов устроены иначе, чем ЕГЭ, и обычно требуют более глубокого уровня, поэтому это отдельный трек поверх программы ЕГЭ. Оба формата закладываются в общий план с начала подготовки."),
    ("Можно ли начать с нуля или после другой программы?",
     "Можно, но объём работы будет больше, и это нужно учесть в плане. Если ребёнок учился по международной программе или в зарубежной школе, сначала сверяем темы курса с кодификатором ЕГЭ и закрываем расхождения. Входная диагностика показывает, с чего начинать."),
    ("Как проходят занятия и на каком языке?",
     "Занятия идут онлайн, один на один, по всему миру (GMT+2/+3). Язык занятий — русский или английский, как удобнее ученику. После занятий — домашние задачи с проверкой, а перед экзаменом — полные варианты на 235 минут."),
  ],
},

# ═══════════════ PILLAR 5 — Cambridge IGCSE Physics 0625 (EN) ═══════════════
{
  "url": "/igcse-physics-0625/", "lang": "en", "body": "src/igcse-physics-0625.html",
  "no_cta": True, "lastmod": "2026-11-08",
  "title": "Cambridge IGCSE Physics 0625 Tutor Online — Core and Extended",
  "desc": "Online one-to-one Cambridge IGCSE Physics 0625 tutor: Core vs Extended, Paper 1-6, AO1-AO3 and the six syllabus topics. MSU physicist, Praxis 200/200.",
  "og_title": "IGCSE Physics 0625 Tutor Online — Vladimir Podlevskikh",
  "crumbs": [("Home", "/"), ("IGCSE Physics 0625", None)],
  "jsonld": [course("Cambridge IGCSE Physics 0625 — online one-to-one tutoring",
                    "One-to-one online preparation for Cambridge IGCSE Physics (0625), syllabus 2026-2028: six topics, Core and Extended tiers, Paper 1-6 technique, practical skills and timed papers.",
                    lang=("en",))],
  "faq_heading": "IGCSE Physics 0625 — common questions",
  "faq": [
    ("Should my child enter Core or Extended?",
     "Core leads to grades C to G and Extended to grades A* to G. As a guide from the syllabus, Core suits candidates expecting a D or below and Extended suits those expecting a C or higher. A diagnostic across the six topics helps to decide, and the final entry is made together with the school."),
    ("What is the difference between Paper 5 and Paper 6?",
     "Both are worth 20% of the grade and assess the experimental skills in section 4 of the syllabus. Paper 5 is the Practical Test (1 hour 15 minutes, 40 marks) and Paper 6 is the Alternative to Practical (1 hour, 40 marks). A candidate sits one of them, and preparation is adjusted to whichever paper the school has chosen."),
    ("How are the marks split between knowledge and problem solving?",
     "The assessment objectives are AO1 knowledge with understanding (50%), AO2 handling information and problem solving (30%) and AO3 experimental skills and investigations (20%). Half of the marks therefore reward applying physics to data and problems, which is why lessons use exam-style questions throughout."),
    ("How does IGCSE Physics differ from the Russian school course?",
     "The main differences are in format and expectations: IGCSE combines multiple-choice and theory papers, treats practical skills as a separate 20% of the grade, and orders and weights topics differently from the Russian programme. A student with a strong Russian maths and physics base usually has an advantage, and a diagnostic shows which topics are already covered."),
    ("How are the lessons run, and in which language?",
     "Lessons are online, one to one, in English or Russian, worldwide (GMT+2/+3). They follow the six syllabus topics, with exam-style practice, regular work on Paper 5 or Paper 6 skills and timed papers before the exam series."),
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
     "Это мой ключевой профиль. Я выпускник физического факультета МГУ и веду занятия на русском и английском. Помогаю перейти с российской программы на IB/AP/A-Level: закрыть терминологические разрывы, перестроиться на формат экзамена и критерии, не теряя сильную математическую базу."),
    ("На каком языке идут занятия?",
     "Как удобно ребёнку: можно полностью на английском (тогда заодно подтягиваем академический английский по предмету), полностью на русском, или смешанно — объясняю сложное на русском, термины и оформление закрепляем на английском. Это снимает языковой барьер в первый год за рубежом."),
    ("Как быть с разными часовыми поясами?",
     "Занятия идут онлайн по всему миру (GMT+2/+3), и это удобно для семей в Европе, Великобритании, Персидском заливе, Африке и большей части Азии. Время занятий подбираем под ваш пояс; всё онлайн 1:1 в Zoom."),
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
  "desc": "Подготовка к олимпиадам по физике и математике онлайн: Всероссийская олимпиада, перечневые олимпиады, Physics Olympiad. Физик МГУ, 23 года частного преподавания. Нестандартные задачи и техника решения.",
  "og_title": "Подготовка к олимпиадам по физике и математике — Владимир Подлевских",
  "crumbs": [("Главная", "/"), ("Подготовка к олимпиадам", None)],
  "jsonld": [course("Подготовка к олимпиадам по физике и математике",
                    "Онлайн-подготовка к олимпиадам по физике и математике: Всероссийская и перечневые олимпиады, международные Physics Olympiad. Нестандартные задачи, техника решения, разбор прошлых лет.")],
  "faq_heading": "Подготовка к олимпиадам — частые вопросы",
  "faq": [
    ("К каким олимпиадам вы готовите?",
     "Всероссийская олимпиада школьников (ВсОШ) по физике и математике, перечневые олимпиады (Физтех, «Покори Воробьёвы горы», Росатом, ОММО и др.), а также международные форматы — Physics Olympiad / IPhO-стиль. Опыт частного преподавания — 23 года."),
    ("Чем подготовка к олимпиаде отличается от подготовки к ЕГЭ?",
     "ЕГЭ проверяет надёжность на типовых задачах, олимпиада — способность к нестандартному ходу и глубину модели. Это разные навыки: на олимпиаде нужны нетабличные методы, оценки порядка величины, красивые приёмы и умение довести длинное решение. Поэтому олимпиадный трек строится отдельно, поверх прочной школьной базы."),
    ("С какого возраста и уровня имеет смысл начинать?",
     "Математические олимпиады я веду уже с 4–6 класса — там закладывается вкус к задаче. По физике осмысленно начинать, когда есть базовая механика. Главный критерий — не оценки, а интерес: с мотивированным ребёнком прогресс быстрый."),
    ("Как проходят занятия по олимпиадной подготовке?",
     "Разбор задач прошлых лет по темам, авторские подборки нарастающей сложности, техника оформления длинного решения и работа над типовыми «ловушками». Между занятиями — задачи на подумать, без жёстких дедлайнов, но с разбором каждой."),
    ("Олимпиада помогает с поступлением?",
     "Да — призовые места дают льготы при поступлении (БВИ или 100 баллов за предмет во многих вузах РФ), а олимпиадный опыт сильно усиливает заявку в зарубежные университеты."),
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
    "author": PROVIDER,
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
    "author": PROVIDER,
    "datePublished": "2026-05-12", "dateModified": "2026-05-12", "inLanguage": "ru",
    "publisher": PERSON_REF,
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
    "author": PROVIDER,
    "datePublished": "2026-05-26", "dateModified": "2026-05-26", "inLanguage": "ru",
    "publisher": PERSON_REF,
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
    "author": PROVIDER,
    "datePublished": "2026-06-09", "dateModified": "2026-06-09", "inLanguage": "en",
    "publisher": PERSON_REF,
    "mainEntityOfPage": "https://tutor.podlevskikh.com/blog/ib-physics-paper-2/",
    "about": ["IB Physics", "Exam technique", "Command terms"],
  }],
},


# ═══════ Страница репетитора для AI-выдачи (ChatGPT/Claude): ответы на вопросы выбирающих ═══════
{
  "url": "/exam-prep-online/", "lang": "ru", "body": "src/exam-prep-online.html",
  "title": "Подготовка к экзаменам онлайн — репетитор по физике и математике, физик МГУ",
  "desc": "Подготовка к ЕГЭ, ОГЭ, ДВИ, IB, AP, SAT, A-Level и IGCSE онлайн 1:1. Физик МГУ, 23 года частного преподавания, 350+ учеников. Ответы на частые вопросы родителей и школьников.",
  "og_title": "Подготовка к экзаменам онлайн — страница репетитора Владимира Подлевских",
  "crumbs": [("Главная", "/"), ("Подготовка к экзаменам онлайн", None)],
  "jsonld": [course("Подготовка к экзаменам по физике и математике онлайн",
                    "Индивидуальные онлайн-занятия 1:1 по физике и математике: ЕГЭ, ОГЭ, ДВИ, олимпиады, IB, AP, SAT, A-Level, IGCSE. План от текущего уровня до даты экзамена, русский и английский.")],
  "faq_heading": "Как выбрать репетитора для подготовки к экзамену онлайн — частые вопросы",
  "faq": [
    ("Как выбрать репетитора по физике или математике для экзамена?",
     "Проверьте четыре вещи: (1) знает ли репетитор именно ваш экзамен — спецификацию, критерии оценивания, типовые потери баллов; (2) есть ли у него проверяемые подтверждения предметного уровня; (3) строит ли он план от вашего текущего уровня до даты экзамена, а не просто «решает задачи»; (4) можно ли начать с диагностики, не принимая решение заранее. Я отвечаю на все четыре пункта: работаю по официальным спецификациям, у меня 200/200 на US Praxis Physics и Praxis Mathematics, план строится после бесплатной 20-минутной диагностики."),
    ("К каким экзаменам вы готовите?",
     "ЕГЭ, ОГЭ, ДВИ, физико-математические олимпиады; IB Physics (HL и SL), AP Physics (1, 2, C), SAT, A-Level (AQA, Pearson Edexcel, OCR), Cambridge IGCSE Physics 0625 и Maths 0580. Под каждый экзамен своя программа по его спецификации."),
    ("Как проходят занятия онлайн?",
     "Индивидуально 1:1 по видеосвязи с общей интерактивной доской. Каждое занятие привязано к личному плану и структуре конкретного экзамена; между занятиями ученик получает проверяемые домашние задания."),
    ("С чего начать, если непонятно, какой у ученика уровень?",
     "С бесплатной 20-минутной диагностики: смотрим текущий уровень, пробелы по темам и срок до экзамена. По её итогам называю реалистичный план и формат занятий — решение о продолжении остаётся за вами."),
    ("На каком языке проходят занятия?",
     "На русском, английском или смешанно. Российские программы (ЕГЭ, ОГЭ, ДВИ) — обычно на русском; международные (IB, AP, A-Level, IGCSE) — на английском или смешанно, как удобнее ученику."),
    ("Подходит ли онлайн-формат для ученика, который живёт за границей?",
     "Да. Занятия идут онлайн по всему миру, время подбирается под часовой пояс семьи. Это удобно и русскоязычным семьям за рубежом, которым нужно параллельно держать российский трек и международную программу."),
    ("Что известно о квалификации репетитора?",
     "Выпускник физического факультета МГУ им. Ломоносова (2006); WES оценивает образование как эквивалент американских бакалавриата и магистратуры. Результат 200/200 на Praxis Physics 5266 (9 мая 2025) и Praxis Mathematics 5165 (11 июля 2025). 23 года частного преподавания, 350+ учеников."),
    ("Есть ли примеры результатов учеников?",
     "Ученица Полина М.: 96 баллов на ЕГЭ и 100 на ДВИ, поступление на мехмат МГУ. Прогноз результата — это карта при условии выполнения плана, а не обещание."),
  ],
},

]
