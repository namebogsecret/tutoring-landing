/* =========================================================================
   site.js — shared wiring for the content layer.
   Usage on links: <a data-cta="calendly">…</a>  (also: telegram, whatsapp,
   email, preply, linkedin, mainsite, video_physics, video_intro, book).
   Any element with [data-year] gets the current year. Elements with class
   .reveal fade in on scroll.
   ========================================================================= */
(function () {
  var CONTACT = {
    calendly:  "https://calendly.com/vladimir-podlevskikh/30min",
    telegram:  "https://t.me/VladimirPodlevskikh",
    whatsapp:  "https://wa.me/37455873402",
    email:     "vladimir@podlevskikh.com",
    linkedin:  "https://linkedin.com/in/vladimir-podlevskikh",
    preply:    "https://preply.in/VLADIMIR6EN2958527510",
    mainsite:  "https://podlevskikh.com",
    book:      "/#book",
    video_physics: "https://youtu.be/5ESCbijUaT4",
    video_intro:   "https://youtu.be/8dLVHqqmSD8"
  };

  function wire() {
    document.querySelectorAll('[data-cta]').forEach(function (el) {
      var key = el.getAttribute('data-cta');
      if (key === 'email') {
        var subj = el.getAttribute('data-subject') || 'Tutoring enquiry';
        el.href = 'mailto:' + CONTACT.email + '?subject=' + encodeURIComponent(subj);
      } else if (CONTACT[key]) {
        el.href = CONTACT[key];
        if (key !== 'book' && /^https?:/.test(CONTACT[key])) { el.target = '_blank'; el.rel = 'noopener'; }
      }
    });
    document.querySelectorAll('[data-year]').forEach(function (el) {
      el.textContent = new Date().getFullYear();
    });
  }

  function reveal() {
    if (!('IntersectionObserver' in window)) {
      document.querySelectorAll('.reveal').forEach(function (el) { el.classList.add('in'); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
    document.querySelectorAll('.reveal').forEach(function (el) { io.observe(el); });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () { wire(); reveal(); });
  } else { wire(); reveal(); }
})();
