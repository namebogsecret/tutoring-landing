/* «Разобрать задачу из ИИ» (блок #ai-task-paste на страницах-ответах) и форма #task-intake на /exam-prep-online/.
   Страница-ответ: по клику на ссылку текст задачи кладётся в sessionStorage (ключ tutorTask, JSON {text, slug, ts});
   в адрес и в статистику он не попадает (событие шлёт site.js по data-tutor-src="paste-<slug>", без текста).
   Пустое поле переход не блокирует. Форма заявки: подхватывает текст из sessionStorage (и стирает ключ), готовит письмо
   (mailto) и копирование. Текст пользователя вставляется только через value/textContent. Без JS блок скрыт (hidden). */
(function () {
  "use strict";
  var KEY = "tutorTask", MAX = 2000;

  function store(text, slug) {
    try { sessionStorage.setItem(KEY, JSON.stringify({ text: text, slug: slug, ts: Date.now() })); } catch (e) {}
  }
  function take() {
    var raw = null, o = null;
    try { raw = sessionStorage.getItem(KEY); sessionStorage.removeItem(KEY); } catch (e) { return null; }
    if (!raw) return null;
    try { o = JSON.parse(raw); } catch (e) { return null; }
    if (!o || typeof o.text !== "string") return null;
    return { text: o.text.slice(0, MAX), slug: typeof o.slug === "string" ? o.slug.slice(0, 120) : "" };
  }

  function initPaste(box) {
    var ta = box.querySelector("textarea");
    var link = box.querySelector("a[data-tutor-src]");
    if (!ta || !link) return;
    box.hidden = false;
    link.addEventListener("click", function () {
      var text = ta.value.slice(0, MAX);
      if (text.replace(/\s+/g, "") !== "") store(text, box.getAttribute("data-slug") || "");
    });
  }

  function initIntake(form) {
    var ta = form.querySelector("textarea");
    var mail = form.querySelector("#task-mail");
    var copy = form.querySelector("#task-copy");
    var note = form.querySelector("#task-copied");
    if (!ta || !mail) return;
    var slug = "";
    var got = take();
    if (got) { ta.value = got.text; slug = got.slug; }
    var addr = form.getAttribute("data-mail") || "";
    function refresh() {
      var subj = "Задача из ИИ: " + (slug || "exam-prep");
      mail.setAttribute("href", "mailto:" + addr + "?subject=" + encodeURIComponent(subj) + "&body=" + encodeURIComponent(ta.value));
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
