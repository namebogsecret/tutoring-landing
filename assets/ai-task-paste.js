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
  function mailBody(t) {
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
    function refresh() {
      var subj = "Задача из ИИ: " + (slug || "exam-prep");
      var m = mailBody(ta.value);
      mail.setAttribute("href", "mailto:" + addr + "?subject=" + encodeURIComponent(subj) + "&body=" + encodeURIComponent(m.body));
      if (hint) {
        hint.textContent = m.cut ? "Текст длинный: в письмо войдёт только его начало. Лучше нажмите «Скопировать текст» и вставьте его в письмо целиком." : "";
        hint.hidden = !m.cut;
      }
    }
    ta.addEventListener("input", function () { if (note) note.textContent = ""; refresh(); });
    refresh();
    if (copy) copy.addEventListener("click", function () {
      var done = function (ok) { if (note) note.textContent = ok ? "Скопировано" : "Не удалось скопировать: выделите текст и скопируйте вручную"; };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(ta.value).then(function () { done(true); }, function () { done(false); });
      } else {
        try { ta.select(); done(document.execCommand("copy")); } catch (e) { done(false); }
      }
    });
    if (/[?&]utm_medium=ai-task-paste(&|$)/.test(location.search || "")) {
      /* после загрузки: переход к #razbor-zapros браузер выполняет сам и снимает фокус, поэтому ставим его позже */
      var go = function () { setTimeout(function () { try { form.scrollIntoView({ block: "center" }); ta.focus({ preventScroll: true }); } catch (e) {} }, 0); };
      if (document.readyState === "complete") go(); else window.addEventListener("load", go);
    }
  }

  function run() {
    var p = document.getElementById("ai-task-paste");
    if (p) initPaste(p);
    var f = document.getElementById("task-intake");
    if (f) initIntake(f);
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", run); else run();
})();
