/* «Разобрать задачу из ИИ» (блок #ai-task-paste на страницах-ответах) и форма #task-intake на /exam-prep-online/.
   Страница-ответ: по клику (в т.ч. средней кнопкой и «открыть в новой вкладке») текст задачи кладётся в localStorage
   (ключ tutorTask, JSON {text, slug, ts}; запасной вариант при ошибке — sessionStorage); в адрес и в статистику он не
   попадает (событие шлёт site.js по data-tutor-src="paste-<slug>", без текста). Запись живёт 30 минут и стирается при
   подхвате. Пустое поле переход не блокирует, но стирает ранее сохранённый текст. Форма заявки: подхватывает запись,
   готовит письмо (mailto, тело не длиннее лимита адреса) и копирование. Текст пользователя вставляется только через
   value/textContent. Без JS блок и форма скрыты (hidden); при недоступном хранилище всё молча работает без переноса. */
(function () {
  "use strict";
  var KEY = "tutorTask", MAX = 2000, TTL = 30 * 60 * 1000, BODY_MAX = 1800;
  var CUT = "\u2026(текст обрезан, полный текст — в кнопке «Скопировать текст»)";
  /* Форма живёт на русской странице; читатель английских страниц-ответов приходит с ?lang=en. {a} = адрес репетитора. */
  var RU = {
    subj: "Задача из ИИ: ",
    long: "Текст длинный: в письмо войдёт только его начало. Лучше нажмите «Скопировать текст» и вставьте его в письмо целиком.",
    empty: "Сначала вставьте условие задачи.",
    mailed: "Если почта не открылась, нажмите «Скопировать текст» и отправьте его на {a}",
    copied: "Скопировано. Отправьте текст письмом на {a}",
    fail: "Не удалось скопировать: выделите текст, скопируйте вручную и отправьте на {a}"
  };
  var EN = {
    subj: "Problem from an AI chat: ",
    cut: "\u2026(text cut off, use the \u201cCopy text\u201d button for the full text)",
    long: "The text is long: only its beginning fits into the email. Press \u201cCopy text\u201d and paste it into the email in full.",
    empty: "Paste the problem statement first.",
    mailed: "If your mail app did not open, press \u201cCopy text\u201d and send it to {a}",
    copied: "Copied. Now email the text to {a}",
    fail: "Could not copy: select the text, copy it manually and send it to {a}",
    title: "Your problem",
    intro: "Paste the problem statement: it is stored only in your browser, for a short time, and is not sent anywhere until you send the email yourself.",
    mail: "Send by email",
    copy: "Copy text",
    addr: "Email: {a}. If your mail app did not open, copy the text and send it to this address from your own email: the reply will come there."
  };
  var booked = false;
  /* одно событие записи на загрузку страницы; текст задачи в путь не идёт */
  function book(channel) {
    if (booked || !window.pdlCta) return;
    booked = true;
    window.pdlCta("book-task-intake-" + channel);
  }
  function markEnglishLinks() {
    if (document.documentElement.lang !== "en") return;
    Array.prototype.forEach.call(document.querySelectorAll('a[href*="/exam-prep-online/"]'), function (a) {
      try {
        var u = new URL(a.getAttribute("href"), document.baseURI);
        if (u.host !== location.host) return;
        u.searchParams.set("lang", "en");
        a.setAttribute("href", u.pathname + u.search + u.hash);
      } catch (e) {}
    });
  }

  function drop() {
    try { localStorage.removeItem(KEY); } catch (e) {}
    try { sessionStorage.removeItem(KEY); } catch (e) {}
  }
  function store(text, slug) {
    var v = JSON.stringify({ text: text, slug: slug, ts: Date.now() });
    try { localStorage.setItem(KEY, v); return; } catch (e) {}
    try { sessionStorage.setItem(KEY, v); } catch (e) {}
  }
  function raw() {
    var r = null;
    try { r = localStorage.getItem(KEY); } catch (e) {}
    if (!r) { try { r = sessionStorage.getItem(KEY); } catch (e) {} }
    return r;
  }
  function take() {
    var r = raw(), o = null;
    drop();
    if (!r) return null;
    try { o = JSON.parse(r); } catch (e) { return null; }
    if (!o || typeof o.text !== "string" || typeof o.ts !== "number") return null;
    var age = Date.now() - o.ts;
    if (age < 0 || age > TTL) return null;
    return { text: o.text.slice(0, MAX), slug: typeof o.slug === "string" ? o.slug.slice(0, 120) : "" };
  }
  function mailBody(t, CUT) {
    if (encodeURIComponent(t).length <= BODY_MAX) return { body: t, cut: false };
    var lo = 0, hi = t.length;
    while (lo < hi) {
      var mid = (lo + hi + 1) >> 1, c = t.charCodeAt(mid - 1);
      var part = t.slice(0, mid - ((c >= 0xD800 && c <= 0xDBFF) ? 1 : 0));
      if (encodeURIComponent(part + "\n" + CUT).length <= BODY_MAX) lo = mid; else hi = mid - 1;
    }
    var end = lo, last = t.charCodeAt(end - 1);
    if (last >= 0xD800 && last <= 0xDBFF) end--;
    return { body: t.slice(0, end) + "\n" + CUT, cut: true };
  }

  function initPaste(box) {
    var ta = box.querySelector("textarea");
    var link = box.querySelector("a[data-tutor-src]");
    if (!ta || !link) return;
    box.hidden = false;
    var save = function () {
      var text = ta.value.slice(0, MAX);
      if (text.replace(/\s+/g, "") !== "") store(text, box.getAttribute("data-slug") || ""); else drop();
    };
    /* click покрывает и Enter по ссылке, и Ctrl/Cmd+клик; auxclick — средняя кнопка; contextmenu — «открыть в новой вкладке» */
    link.addEventListener("click", save);
    link.addEventListener("auxclick", function (e) { if (e.button === 1) save(); });
    link.addEventListener("contextmenu", save);
  }

  function initIntake(form) {
    var ta = form.querySelector("textarea");
    var mail = form.querySelector("#task-mail");
    var copy = form.querySelector("#task-copy");
    var note = form.querySelector("#task-copied");
    var hint = form.querySelector("#task-long");
    if (!ta || !mail) return;
    form.hidden = false;
    var slug = "";
    var got = take();
    if (got) { ta.value = got.text; slug = got.slug; }
    var addr = form.getAttribute("data-mail") || "";
    var en = /[?&]lang=en(&|$)/.test(location.search || "");
    var T = en ? EN : RU;
    var say = function (key) { if (note) note.textContent = T[key].replace("{a}", addr); };
    var blank = function () { return ta.value.replace(/\s+/g, "") === ""; };
    if (en) {
      var put = function (sel, text) { var el = form.querySelector(sel); if (el) el.textContent = text; };
      form.setAttribute("lang", "en");
      put("h3", EN.title); put("#task-intro", EN.intro); put("#task-mail", EN.mail); put("#task-copy", EN.copy);
      var where = form.querySelector("#task-addr");
      if (where) {
        var parts = EN.addr.split("{a}"), strong = document.createElement("strong");
        strong.textContent = addr;
        where.textContent = parts[0];
        where.appendChild(strong);
        where.appendChild(document.createTextNode(parts[1]));
      }
      ta.setAttribute("aria-label", EN.title);
    }
    function refresh() {
      var subj = T.subj + (slug || "exam-prep");
      var m = mailBody(ta.value, en ? EN.cut : CUT);
      mail.setAttribute("href", "mailto:" + addr + "?subject=" + encodeURIComponent(subj) + "&body=" + encodeURIComponent(m.body));
      if (hint) {
        hint.textContent = m.cut ? T.long : "";
        hint.hidden = !m.cut;
      }
    }
    ta.addEventListener("input", function () { if (note) note.textContent = ""; refresh(); });
    refresh();
    mail.addEventListener("click", function (e) {
      if (blank()) { e.preventDefault(); say("empty"); ta.focus(); return; }
      say("mailed"); book("mail");
    });
    if (copy) copy.addEventListener("click", function () {
      if (blank()) { say("empty"); ta.focus(); return; }
      var done = function (ok) { say(ok ? "copied" : "fail"); if (ok) book("copy"); };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(ta.value).then(function () { done(true); }, function () { done(false); });
      } else {
        try { ta.select(); done(document.execCommand("copy")); } catch (e) { done(false); }
      }
    });
    arrive(form, ta, /[?&]utm_medium=ai-task-paste(&|$)/.test(location.search || ""));
  }

  /* Приход по ссылке с хешем: форма встаёт под липкую шапку. Родной переход по хешу гонится с появлением формы
     (она была hidden) и сдвигом вёрстки, поэтому ставим позицию после load, шрифтов и ещё раз чуть позже —
     пока человек сам не начал прокручивать или нажимать. */
  function arrive(form, ta, focus) {
    if (!focus && !/#(razbor-zapros|task-intake)$/.test(document.URL)) return;
    try { var n = performance.getEntriesByType("navigation")[0]; if (n && n.type !== "navigate") return; } catch (e) {}
    var touched = false;
    ["touchstart", "wheel", "keydown", "pointerdown"].forEach(function (t) {
      window.addEventListener(t, function () { touched = true; }, { once: true, passive: true });
    });
    var place = function () { if (!touched) try { form.scrollIntoView({ block: "start", behavior: "instant" }); } catch (e) {} };
    var go = function () {
      setTimeout(function () { place(); if (focus && !touched) try { ta.focus({ preventScroll: true }); } catch (e) {} }, 0);
      if (document.fonts && document.fonts.ready) document.fonts.ready.then(function () { setTimeout(place, 50); });
      setTimeout(place, 700);
    };
    if (document.readyState === "complete") go(); else window.addEventListener("load", go);
  }

  function run() {
    markEnglishLinks();
    var p = document.getElementById("ai-task-paste");
    if (p) initPaste(p);
    var f = document.getElementById("task-intake");
    if (f) initIntake(f);
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", run); else run();
})();
