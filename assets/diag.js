/* Диагностика за 10 минут (блок .diag-block на страницах-ответах): 5 вопросов, подсчёт в браузере.
   Без запросов наружу и без хранения данных: ответы живут только в DOM страницы. Событие клика к репетитору
   шлёт общий обработчик в site.js (по data-tutor-src="diag-<slug>"). Без JS блок остаётся скрытым (hidden). */
(function () {
  "use strict";
  function init(box) {
    var qs = box.querySelectorAll(".diag-q");
    var result = box.querySelector(".diag-result");
    var hint = box.querySelector(".diag-hint");
    if (!qs.length || !result) return;
    box.hidden = false;
    function finish() {
      var n = 0, i, q, picked, ok, mark;
      for (i = 0; i < qs.length; i++) {
        q = qs[i];
        picked = q.querySelector("input:checked");
        if (!picked) return;                          /* ещё есть неотвеченные */
      }
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
      result.querySelector(".diag-score").textContent = box.getAttribute("data-score").replace("{n}", String(n));
      Array.prototype.forEach.call(result.querySelectorAll(".diag-level"), function (p) {
        p.hidden = p.getAttribute("data-levels") !== String(level);
      });
      result.hidden = false;
      if (hint) hint.hidden = true;
    }
    box.addEventListener("change", finish);
  }
  function run() {
    var boxes = document.querySelectorAll(".diag-block[data-diag]");
    for (var i = 0; i < boxes.length; i++) init(boxes[i]);
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", run); else run();
})();
