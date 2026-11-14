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
  "no_cta": True, "lastmod": "2026-11-08",
  "title": "IB Physics Tutor Online (SL & HL) — Syllabus 2025, 1:1",
  "desc": "Online one-to-one IB Physics SL and HL tutor: five themes, Paper 1A/1B and 2, the scientific investigation and AO1-AO3. MSU physicist, Praxis 200/200.",
  "og_title": "IB Physics Tutor (SL/HL) Online — Vladimir Podlevskikh",
  "crumbs": [("Home", "/"), ("IB Physics Tutor", None)],
  "jsonld": [course("IB Physics SL & HL — online one-to-one tutoring",
                    "One-to-one online preparation for IB Diploma Physics SL and HL, Physics guide first assessment 2025: five themes, Paper 1A/1B and Paper 2 technique, data-based questions and support for the scientific investigation.",
                    lang=("en",))],
  "faq_heading": "IB Physics tutoring — common questions",
  "faq": [
    ("Do you teach both IB Physics SL and HL?",
     "Yes. Both levels follow the same five themes (A to E) of the Physics guide for first assessment 2025. HL adds material and longer papers: the guide recommends 150 teaching hours for SL and 240 for HL, and HL Paper 2 includes additional higher level material. A diagnostic shows which level-specific content is still missing."),
    ("How are the IB Physics papers built?",
     "External assessment is 80% of the grade. At SL, Paper 1 (1 hour 30 minutes, 45 marks, 36%) and Paper 2 (1 hour 30 minutes, 50 marks, 44%). At HL, Paper 1 (2 hours, 60 marks, 36%) and Paper 2 (2 hours 30 minutes, 90 marks, 44%). Paper 1 has a multiple-choice part (1A) and a data-based part (1B)."),
    ("Can you help with the internal assessment?",
     "Yes, within the IB's rules. The internal assessment is the scientific investigation: 20% of the grade, 24 marks, marked on research design, data analysis, conclusion and evaluation. The work must be the student's own, so lessons cover how to plan a researchable question, handle uncertainties and evaluate a method, and do not write any part of it."),
    ("What are AO1, AO2 and AO3?",
     "They are the assessment objectives: AO1 demonstrate knowledge, AO2 understand and apply knowledge, AO3 analyse, evaluate and synthesise. For both papers the guide gives about 50% for AO1 and AO2 together and about 50% for AO3, so half of each paper rewards using physics on unfamiliar data. The internal assessment also covers AO4."),
    ("How are the lessons run, and in which language?",
     "Lessons are online, one to one, in English or Russian, worldwide (GMT+2/+3). They follow the five themes, with exam-style practice, regular work on data-based questions, discussion of the investigation at each stage and timed papers before the exam session."),
  ],
},

# ═══════════════════════ PILLAR 2 — AP Physics C (EN) ═══════════════════════
{
  "url": "/ap-physics-tutor/", "lang": "en", "body": "src/ap-physics-tutor.html",
  "no_cta": True, "lastmod": "2026-11-08",
  "title": "AP Physics C Tutor Online — Mechanics and E&M, 1:1",
  "desc": "Online 1:1 AP Physics C tutor: Mechanics and Electricity & Magnetism, 42 multiple-choice and 4 free-response questions, calculus. MSU physicist, Praxis 200/200.",
  "og_title": "AP Physics C Tutor (Mechanics, E&M) Online — Vladimir Podlevskikh",
  "crumbs": [("Home", "/"), ("AP Physics Tutor", None)],
  "jsonld": [course("AP Physics C: Mechanics and E&M — online one-to-one tutoring",
                    "One-to-one online preparation for AP Physics C: Mechanics and Electricity and Magnetism: the units of each course, the exam format (Section I multiple choice, Section II free response), calculus in physics and free-response technique.",
                    lang=("en",))],
  "faq_heading": "AP Physics C tutoring — common questions",
  "faq": [
    ("Which AP Physics courses do you cover?",
     "This page covers AP Physics C: Mechanics and AP Physics C: Electricity and Magnetism, which are two separate courses with separate exams. AP Physics 1 and AP Physics 2 are neighbouring courses and are not the focus here."),
    ("How is an AP Physics C exam built?",
     "According to College Board, effective from the May 2027 exam, each Physics C exam has two equal sections: Section I with 42 multiple-choice questions in 85 minutes (50% of the score) and Section II with 4 free-response questions in 95 minutes (50%). Calculators are permitted."),
    ("Is AP Physics C calculus-based, and do you teach the mathematics too?",
     "Yes, College Board describes it as a calculus-based, college-level course. Most difficulty sits where calculus meets physics, so the two are taught together: setting up derivatives and integrals from a physical situation and writing the steps in full. The tutor holds Praxis Mathematics 200/200 as well as Praxis Physics 200/200."),
    ("How do you prepare for the free-response section?",
     "College Board lists four free-response question types: mathematical routines, translation between representations, experimental design and analysis, and qualitative/quantitative translation. Practice is built around them: derive in symbols first, keep units and signs visible, and write the principle before the substitution."),
    ("How are the lessons run, and in which language?",
     "Lessons are online, one to one, in English or Russian, worldwide (GMT+2/+3). They follow the units of the chosen course, with free-response-style problems, timed multiple-choice sets and full sections under exam timing before the exam."),
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
  "title": "ЕГЭ по физике 2027 онлайн: репетитор, физик МГУ, из любой страны",
  "desc": "Репетитор по физике для ЕГЭ 2027: онлайн 1:1 из любой страны, русский или английский. Структура КИМ (26 заданий, 45 баллов), ДВИ. Физик МГУ, Praxis 200/200.",
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
    ("Можно ли готовиться к ЕГЭ по физике онлайн, если семья живёт за границей?",
     "Да. Занятия идут онлайн, один на один, из любой страны; время подбирается под часовой пояс семьи (онлайн по всему миру, GMT+2/+3). Программа строится по спецификации КИМ ЕГЭ 2027, а если ученик учится по международной программе, темы курса сначала сверяются с кодификатором ЕГЭ."),
    ("Какой опыт у репетитора по физике для ЕГЭ?",
     "Владимир Подлевских — выпускник физического факультета МГУ им. Ломоносова (2006), 23 года частного преподавания, 350+ учеников. Результат 200/200 на американском экзамене Praxis Physics (5266). Занятия ведутся на русском или английском."),
  ],
},

# ═══════════════ PILLAR 5 — Cambridge IGCSE Physics 0625 (EN) ═══════════════
{
  "url": "/igcse-physics-0625/", "lang": "en", "body": "src/igcse-physics-0625.html",
  "no_cta": True, "lastmod": "2026-11-08",
  "title": "IGCSE Physics 0625 Tutor Online — Russian or English, 1:1",
  "desc": "Russian-speaking Cambridge IGCSE Physics 0625 tutor, online 1:1 (репетитор на русском или English): Core vs Extended, Paper 1-6. MSU physicist, Praxis 200/200.",
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
    ("Can IGCSE Physics 0625 be taught in Russian? / Можно ли заниматься по IGCSE Physics на русском?",
     "Yes. Lessons can be in Russian, English or a mix: Russian for explanations and English for the exam terminology and command words that appear on the papers. Да: объяснения на русском, термины и формулировки экзамена — на английском, как удобнее ученику. Lessons are online, one to one."),
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
  "url": "/exam-prep-online/", "lang": "ru", "body": "src/exam-prep-online.html", "lastmod": "2026-11-14",
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
    ("Есть ли репетитор по IB Physics онлайн, который объясняет на русском?",
     "Да. IB Physics (HL и SL) я веду онлайн, один на один: объяснения на русском или английском, терминология и формулировки заданий — по английской спецификации IB. Выпускник физического факультета МГУ, 23 года частного преподавания."),
    ("Есть ли репетитор по AP Physics онлайн на русском?",
     "Да. AP Physics 1, 2 и C — онлайн, один на один, на русском или английском; терминологию и формат заданий разбираем по английским материалам College Board."),
    ("Можно ли готовиться у одного преподавателя и к ЕГЭ, и к IB, AP, IGCSE?",
     "Да. Один преподаватель ведёт ЕГЭ, IB Physics, AP Physics и Cambridge IGCSE Physics 0625: это удобно семьям, где ребёнок учится по международной программе и параллельно держит российский трек. План строится под каждый экзамен отдельно, по его спецификации."),
    ("Что известно о квалификации репетитора?",
     "Выпускник физического факультета МГУ им. Ломоносова (2006); WES оценивает образование как эквивалент американских бакалавриата и магистратуры. Результат 200/200 на Praxis Physics 5266 (9 мая 2025) и Praxis Mathematics 5165 (11 июля 2025). 23 года частного преподавания, 350+ учеников."),
    ("Есть ли примеры результатов учеников?",
     "Ученица Полина М.: 96 баллов на ЕГЭ и 100 на ДВИ, поступление на мехмат МГУ. Прогноз результата — это карта при условии выполнения плана, а не обещание."),
  ],
},

]
