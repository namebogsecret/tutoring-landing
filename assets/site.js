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

  // PayLink checkout URL for the $55 trial lesson (multi-use link).
  var PAYLINK_TRIAL_URL = "https://payment.paylink.am?id=UjQzR1FCSDZpUTVSWDBlSURQNVFud3loaElrU1JCZ1d1Ky9zT2J4cUNoWWhvT0VZc1M5am1xWGY0OFQyNGp3TENLbXhaSEI4RkFQaEZRWEhrTXg2N0E9PQ";

  function wire() {
    document.querySelectorAll('[data-cta]').forEach(function (el) {
      var key = el.getAttribute('data-cta');
      if (key === 'email') {
        var subj = el.getAttribute('data-subject') || 'Tutoring enquiry';
        el.href = 'mailto:' + CONTACT.email + '?subject=' + encodeURIComponent(subj);
      } else if (key === 'paylink') {
        el.href = PAYLINK_TRIAL_URL;
        el.target = '_blank';
        el.rel = 'noopener';
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

/* analytics: неблокирующая */
window.addEventListener("load",function(){try{window.goatcounter=window.goatcounter||{};window.goatcounter.path=function(p){return location.host+(p==="/"?"/index":p)};var s=document.createElement("script");s.async=true;s.src="//gc.zgo.at/count.js";s.setAttribute("data-goatcounter","https://stats.podlevskikh.com/count");s.onerror=function(){};document.body.appendChild(s)}catch(e){}});

/* CTA-события: неблокирующий пиксель, не мешает переходу по ссылке */
document.addEventListener("click",function(ev){try{
  var a=ev.target.closest("a"); if(!a||!a.href) return;
  var href=a.href, name=null;
  if(/t\.me\/yerevan_afisha_bot/.test(href)) name="telegram-afisha";
  else if(/t\.me\/podlevskikh_consult_bot/.test(href)) name="telegram-consult";
  else if(/t\.me\/VladimirPodlevskikh/.test(href)) name="telegram-personal";
  else if(/calendly\.com/.test(href)) name="calendly";
  else if(/tutor\.podlevskikh\.com/.test(href) && location.host!=="tutor.podlevskikh.com") name="to-tutor";
  var path; if(name){path="/cta-"+name;}
  else if(a.hostname&&a.hostname!==location.hostname&&(a.protocol==="http:"||a.protocol==="https:")){path="/out-"+a.hostname;}
  else return;
  var p=location.host+path;
  var u="https://stats.podlevskikh.com/count?p="+encodeURIComponent(p)+"&e=true";
  if(navigator.sendBeacon){navigator.sendBeacon(u)}else{(new Image()).src=u}
}catch(e){}},true);
