/* Диагностика за 10 минут (блок .diag-block на страницах-ответах): 5 вопросов, подсчёт в браузере; ответы можно менять, результат по кнопке.
   Без запросов наружу и без хранения данных: ответы живут только в DOM страницы. Событие клика к репетитору
   шлёт общий обработчик в site.js (по data-tutor-src="diag-<slug>"). Без JS блок остаётся скрытым (hidden). */
(function () {
  "use strict";
  function init(box) {
    var qs = box.querySelectorAll(".diag-q");
    var result = box.querySelector(".diag-result");
    var hint = box.querySelector(".diag-hint");
    if (!qs.length || !result) return;
    var btn = box.querySelector(".diag-show");
    var cta = result.querySelector(".diag-cta");
    if (!btn) return;
    box.hidden = false;
    function allAnswered() {
      for (var i = 0; i < qs.length; i++) if (!qs[i].querySelector("input:checked")) return false;
      return true;
    }
    function show() {
      if (btn.disabled || !allAnswered()) return;
      var n = 0, i, q, picked, ok, mark;
      for (i = 0; i < qs.length; i++) {
        q = qs[i];
        picked = q.querySelector("input:checked");
        ok = picked.value === q.getAttribute("data-correct");
        if (ok) n++;
        q.className = "diag-q " + (ok ? "diag-ok" : "diag-bad");
        mark = q.querySelector(".diag-mark");
        mark.textContent = ok ? box.getAttribute("data-right") : box.getAttribute("data-wrong");
        mark.hidden = false;
        Array.prototype.forEach.call(q.querySelectorAll("input"), function (inp) { inp.disabled = true; });
      }
      var level = n <= 1 ? 0 : (n <= 3 ? 1 : 2);
      Array.prototype.forEach.call(result.querySelectorAll(".diag-level"), function (p) {
        p.hidden = p.getAttribute("data-levels") !== String(level);
      });
      if (cta) cta.hidden = false;
      btn.disabled = true;
      btn.hidden = true;
      if (hint) hint.hidden = true;
      /* aria-live стоит на .diag-result, видимом с самого начала: текст вставляется в уже существующую live-область */
      result.querySelector(".diag-score").textContent = box.getAttribute("data-score").replace("{n}", String(n));
    }
    box.addEventListener("change", function () { btn.disabled = !allAnswered(); });
    btn.addEventListener("click", show);
  }
  function run() {
    var boxes = document.querySelectorAll(".diag-block[data-diag]");
    for (var i = 0; i < boxes.length; i++) init(boxes[i]);
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", run); else run();
})();
