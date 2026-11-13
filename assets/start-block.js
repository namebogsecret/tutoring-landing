/*!
 * StartBlock — блок «С чего начать подготовку к экзамену» (3 шага + ссылка на страницу репетитора).
 * Переиспользуемый компонент без зависимостей. Один файл, копируется на сайты сети как есть.
 *
 * Подключение (любой сайт):
 *   <div data-start-block data-slug="physics-home"></div>
 *   <script src="/start-block.js" defer></script>
 * Или из кода (React и т. п.):  window.StartBlock.mount(element, {slug: "..."})
 *
 * Вариант variant="razbor" («записаться на разбор», страницы-ответы tutor/physics): одна кнопка на запись,
 *   UTM utm_source=<host>&utm_medium=razbor&utm_campaign=<slug>; события cta-book-razbor-<slug> (клик), razbor-shown-<slug> (показ).
 * Вариант variant="lesson" («как это выглядит на занятии»): события cta-to-tutor-lesson-<slug>, cta-to-tutor-lesson-<ege|ib|ap>-<slug>, cta-book-lesson-<slug> (запись), lesson-shown-<slug>.
 * Опции (data-* или объект): slug, lang (ru|en), tutorUrl, title, lead, cta.
 * Метрика (GoatCounter): клик → событие «<host>/cta-to-tutor-start-<slug>», показ → «<host>/start-block-shown-<slug>»
 * (раз за загрузку). В ссылку добавляются utm_source=<host>, utm_medium=start-block, utm_campaign=<slug>.
 * Тексты: онлайн, без названия школы и географии.
 */
(function (root) {
  "use strict";

  var TEXTS = {
    ru: {
      title: "С чего начать подготовку к экзамену",
      lead: "Три шага, которые работают для ЕГЭ, IB, IGCSE и A-level — занятия онлайн.",
      cta: "Страница репетитора",
      steps: [
        { h: "Поставьте цель и дату", p: "Нужный балл или оценка, день экзамена — отсюда считается, сколько недель и часов в неделю нужно." },
        { h: "Найдите пробелы", p: "Решите пробную работу по программе и отметьте темы, где ошибки повторяются, — начинать надо с них." },
        { h: "Занимайтесь по плану", p: "Регулярные занятия онлайн с разбором ваших ошибок: по задачам, а не по пересказу теории." }
      ]
    },
    en: {
      title: "Where to start your exam preparation",
      lead: "Three steps that work for IB, IGCSE, A-level, AP and national exams — lessons online.",
      cta: "Tutor page",
      steps: [
        { h: "Set a target and a date", p: "The grade you need and the exam day tell you how many weeks and hours per week the plan takes." },
        { h: "Find the gaps", p: "Take a practice paper for your course and mark the topics where the same mistakes repeat — start there." },
        { h: "Follow a plan", p: "Regular online lessons that go through your own mistakes: problem solving, not retelling theory." }
      ]
    }
  };

  // Вариант «next» — «следующий шаг» под материалом страницы: {topic} подставляется из опции topic.
  var NEXT = {
    ru: {
      title: "Как я разбираю такие задачи с учениками",
      lead: "Тема страницы — {topic}. На онлайн-занятиях я иду от наблюдения к задаче: сначала понять, что происходит физически, потом записать модель и довести решение до ответа.",
      cta: "Программа подготовки по физике",
      tutorUrl: "https://tutor.podlevskikh.com/ege-physics/",
      steps: [
        { h: "Разбираем модель", p: "Какие величины задают процесс и что меняется, если изменить одну из них." },
        { h: "Решаем задачу по шагам", p: "От условия к формулам и ответу, с проверкой размерности и здравого смысла." },
        { h: "Разбираем ошибки", p: "Смотрим, где решение свернуло не туда, и возвращаемся к этому типу задач." }
      ]
    },
    en: {
      title: "How I work through problems like these with students",
      lead: "This page covers {topic}. In online lessons I go from observation to problem: first what happens physically, then the model, then the solution through to the answer.",
      cta: "Physics tutoring programme",
      tutorUrl: "https://tutor.podlevskikh.com/ib-physics-tutor/",
      steps: [
        { h: "Work through the model", p: "Which quantities drive the process and what changes when one of them changes." },
        { h: "Solve step by step", p: "From the statement to formulas and the answer, checking units and sense." },
        { h: "Review the mistakes", p: "See where a solution went off track and return to that problem type." }
      ]
    }
  };

  // Вариант «lesson» — «как это выглядит на занятии»: 3 шага + программы (ЕГЭ, IB, AP) + запись.
  var BOOK_URL = "https://calendly.com/vladimir-podlevskikh/30min";
  var LESSON = {
    ru: {
      title: "Как это выглядит на занятии",
      lead: "Занятие онлайн, один на один: вы приносите задачу или работу — мы разбираем её вместе.",
      cta: "Страница репетитора",
      tutorUrl: "https://tutor.podlevskikh.com/physics-tutor-online/",
      programsLabel: "Программы:",
      programs: [
        { id: "ege", t: "ЕГЭ", url: "https://tutor.podlevskikh.com/ege-physics/" },
        { id: "ib", t: "IB", url: "https://tutor.podlevskikh.com/ib-physics-tutor/" },
        { id: "ap", t: "AP", url: "https://tutor.podlevskikh.com/ap-physics-tutor/" }
      ],
      book: "Записаться на диагностику",
      steps: [
        { h: "Начинаем с вашей задачи", p: "Вы показываете решение, а не только ответ: по шагам видно, где именно возникает ошибка." },
        { h: "Решаем вместе на доске", p: "Я задаю наводящие вопросы, вы делаете шаги сами: модель, формулы, проверка размерности." },
        { h: "Уходим с планом", p: "В конце — короткий список тем и несколько задач к следующему занятию." }
      ]
    },
    en: {
      title: "What a lesson looks like",
      lead: "One-to-one online: you bring a problem or a past paper, and we work through it together.",
      cta: "Tutor page",
      tutorUrl: "https://tutor.podlevskikh.com/physics-tutor-online/",
      programsLabel: "Programmes:",
      programs: [
        { id: "ege", t: "EGE", url: "https://tutor.podlevskikh.com/ege-physics/" },
        { id: "ib", t: "IB", url: "https://tutor.podlevskikh.com/ib-physics-tutor/" },
        { id: "ap", t: "AP", url: "https://tutor.podlevskikh.com/ap-physics-tutor/" }
      ],
      book: "Book a diagnostic",
      steps: [
        { h: "We start from your problem", p: "You show the working, not just the answer, so it is clear where the mistake appears." },
        { h: "Solve it together on a board", p: "I ask guiding questions and you take the steps: model, formulas, a units check." },
        { h: "Leave with a plan", p: "A short list of topics and a few problems for the next lesson." }
      ]
    }
  };

  // Вариант «razbor» — единый блок «записаться на разбор» на страницах-ответах: одна кнопка на запись.
  var RAZBOR = {
    ru: {
      title: "Разберём вашу задачу",
      lead: "Застряли на задаче или в пробной работе? Принесите её на онлайн-занятие — разберём решение по шагам и найдём, где именно ошибка.",
      book: "Записаться на разбор"
    },
    en: {
      title: "Let's work through your problem",
      lead: "Stuck on a problem or a past paper? Bring it to an online lesson — we go through the solution step by step and find exactly where it goes wrong.",
      book: "Book a walkthrough"
    }
  };

  var DEFAULTS = {
    slug: "page",
    lang: "ru",
    tutorUrl: "https://tutor.podlevskikh.com/",
    texts: TEXTS
  };

  var CSS = ".sb{box-sizing:border-box;max-width:760px;margin:32px auto;padding:22px 24px;border:1px solid rgba(128,128,128,.35);border-radius:14px;" +
    "background:rgba(127,127,127,.07);color:inherit;font:16px/1.5 system-ui,-apple-system,Segoe UI,Roboto,sans-serif;text-align:left}" +
    ".sb *{box-sizing:border-box}.sb__t{margin:0 0 4px;font-size:1.25em;font-weight:700}.sb__l{margin:0 0 14px;opacity:.8}" +
    ".sb__s{margin:0 0 16px;padding:0;list-style:none;counter-reset:sb}.sb__s li{position:relative;margin:0 0 10px;padding-left:38px;counter-increment:sb}" +
    ".sb__s li:before{content:counter(sb);position:absolute;left:0;top:0;width:26px;height:26px;border-radius:50%;background:#2f6fed;color:#fff;" +
    "font-weight:700;font-size:14px;line-height:26px;text-align:center}.sb__s b{display:block}.sb__s span{opacity:.85}" +
    ".sb__a{display:inline-block;max-width:100%;padding:10px 18px;border-radius:10px;background:#2f6fed;color:#fff!important;font-weight:600;text-decoration:none}" +
    ".sb__p{margin:14px 0 0;display:flex;flex-wrap:wrap;gap:8px;align-items:center}.sb__p span{opacity:.8}" +
    ".sb__p a{padding:6px 14px;border:1px solid #2f6fed;border-radius:999px;color:inherit;font-weight:600;text-decoration:none}" +
    ".sb__a--book{margin-left:8px;background:transparent;border:2px solid #2f6fed;color:inherit!important}" +
    ".sb__a:hover{filter:brightness(1.1)}.sb__a:focus-visible{outline:3px solid #9bbcff;outline-offset:2px}";

  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  function cleanSlug(s) {
    return String(s || DEFAULTS.slug).toLowerCase().replace(/[^a-z0-9-]+/g, "-").replace(/^-+|-+$/g, "") || DEFAULTS.slug;
  }

  function buildHref(base, host, slug, medium) {
    var sep = base.indexOf("?") === -1 ? "?" : "&";
    return base + sep + "utm_source=" + encodeURIComponent(host) + "&utm_medium=" + (medium || "start-block") + "&utm_campaign=" + encodeURIComponent(slug);
  }

  function count(win, host, name) {
    try {
      var gc = win.goatcounter;
      if (gc && typeof gc.count === "function") gc.count({ path: host + "/" + name, event: true });
    } catch (e) { /* метрика не должна ломать страницу */ }
  }

  function injectCss(doc) {
    if (doc.getElementById("sb-css")) return;
    var st = doc.createElement("style");
    st.id = "sb-css";
    st.appendChild(doc.createTextNode(CSS));
    (doc.head || doc.documentElement).appendChild(st);
  }

  function renderRazbor(opts, host, slug) {
    var tx = RAZBOR[opts.lang] || RAZBOR.ru;
    var hid = "sb-t-razbor-" + slug;
    return '<section class="sb sb--razbor" aria-labelledby="' + hid + '"><h2 class="sb__t" id="' + hid + '">' + esc(opts.title || tx.title) + "</h2>" +
      '<p class="sb__l">' + esc(opts.lead || tx.lead) + '</p><a class="sb__a" href="' + esc(buildHref(BOOK_URL, host, slug, "razbor")) +
      '" target="_blank" rel="noopener" data-sb-cta data-sb-book data-book>' + esc(opts.cta || tx.book) + " →</a></section>";
  }

  function render(opts, host) {
    var slug = cleanSlug(opts.slug);
    if (opts.variant === "razbor") return renderRazbor(opts, host, slug);
    var lesson = opts.variant === "lesson";
    var next = opts.variant === "next";
    var pack = lesson ? LESSON : next ? NEXT : TEXTS;
    var tx = pack[opts.lang] || pack.ru;
    var useOwn = (next || lesson) && !opts.tutorUrlSet;
    var base = useOwn ? tx.tutorUrl : opts.tutorUrl;
    var medium = lesson ? "lesson" : next ? "next-step" : "start-block";
    var href = buildHref(base, host, slug, medium);
    var title = opts.title || tx.title, cta = opts.cta || tx.cta;
    var lead = opts.lead || (next ? tx.lead.replace("{topic}", opts.topic || "") : tx.lead);
    var items = tx.steps.map(function (s) {
      return "<li><b>" + esc(s.h) + "</b><span>" + esc(s.p) + "</span></li>";
    }).join("");
    var extra = "";
    if (lesson) {
      var progs = tx.programs.map(function (p) {
        return '<a href="' + esc(buildHref(p.url, host, slug, medium)) + '" rel="noopener" data-sb-cta data-sb-prog="' + p.id + '">' + esc(p.t) + "</a>";
      }).join("");
      extra = '<p class="sb__p"><span>' + esc(tx.programsLabel) + "</span>" + progs + "</p>";
    }
    var book = lesson ? ' <a class="sb__a sb__a--book" href="' + esc(buildHref(BOOK_URL, host, slug, medium)) + '" rel="noopener" data-sb-cta data-sb-book data-book>' + esc(tx.book) + "</a>" : "";
    var hid = "sb-t-" + (opts.variant || "start") + "-" + slug;
    return '<section class="sb" aria-labelledby="' + hid + '"><h2 class="sb__t" id="' + hid + '">' + esc(title) + "</h2>" +
      '<p class="sb__l">' + esc(lead) + '</p><ol class="sb__s">' + items + "</ol>" +
      '<a class="sb__a" href="' + esc(href) + '" rel="noopener" data-sb-cta data-sb-main>' + esc(cta) + " →</a>" + book + extra + "</section>";
  }

  function mount(el, options, win) {
    win = win || root;
    var doc = el.ownerDocument || win.document;
    if (el.getAttribute("data-sb-mounted")) return el;
    var ds = el.dataset || {};
    var opts = { slug: DEFAULTS.slug, lang: DEFAULTS.lang, tutorUrl: DEFAULTS.tutorUrl };
    ["slug", "lang", "tutorUrl", "title", "lead", "cta", "variant", "topic"].forEach(function (k) { if (ds[k]) opts[k] = ds[k]; });
    if (options) Object.keys(options).forEach(function (k) { if (options[k] != null) opts[k] = options[k]; });
    opts.tutorUrlSet = !!((options && options.tutorUrl) || ds.tutorUrl);
    var host = (win.location && win.location.host) || "site";
    var slug = cleanSlug(opts.slug);
    injectCss(doc);
    el.innerHTML = render(opts, host);
    el.setAttribute("data-sb-mounted", "1");
    var lessonV = opts.variant === "lesson";
    var evPrefix = lessonV ? "cta-to-tutor-lesson-" : opts.variant === "next" ? "cta-to-tutor-next-" : "cta-to-tutor-start-";
    el.addEventListener("click", function (ev) {
      var a = ev.target && ev.target.closest ? ev.target.closest("a[data-sb-cta]") : null;
      if (!a) return;
      if (opts.variant === "razbor") count(win, host, "cta-book-razbor-" + slug);
      else if (a.hasAttribute("data-sb-book")) count(win, host, "cta-book-lesson-" + slug);
      else if (a.hasAttribute("data-sb-prog")) count(win, host, evPrefix + a.getAttribute("data-sb-prog") + "-" + slug);
      else count(win, host, evPrefix + slug);
    });
    // показ — один раз, когда блок попал во вьюпорт (иначе при загрузке без IntersectionObserver)
    var shown = false;
    function shownOnce() { if (!shown) { shown = true; count(win, host, (opts.variant === "razbor" ? "razbor-shown-" : opts.variant === "lesson" ? "lesson-shown-" : opts.variant === "next" ? "next-step-shown-" : "start-block-shown-") + slug); } }
    if (typeof win.IntersectionObserver === "function") {
      var io = new win.IntersectionObserver(function (es) {
        if (es.some(function (e) { return e.isIntersecting; })) { io.disconnect(); shownOnce(); }
      });
      io.observe(el);
    } else { shownOnce(); }
    return el;
  }

  function autoMount(win) {
    win = win || root;
    var list = win.document.querySelectorAll("[data-start-block]");
    for (var i = 0; i < list.length; i++) mount(list[i], null, win);
  }

  var api = { mount: mount, autoMount: autoMount, buildHref: buildHref, cleanSlug: cleanSlug, DEFAULTS: DEFAULTS, BOOK_URL: BOOK_URL };
  if (typeof module === "object" && module.exports) module.exports = api;
  if (root && root.document) {
    root.StartBlock = api;
    if (root.document.readyState === "loading") root.document.addEventListener("DOMContentLoaded", function () { autoMount(root); });
    else autoMount(root);
  }
})(typeof window !== "undefined" ? window : this);
