# A/B Plan: Quiz vs Static CTA — tutor.podlevskikh.com

**Date drafted:** 2026-06-14
**Objective:** Confirm whether adding the quiz entry point above the existing hero CTA raises the contact/booking rate.

---

## 1. Baseline

| Metric | Value | Source |
|---|---|---|
| Landing page conversion (contact / unique visit) | ~4.9% | Unbounce tutoring benchmark (Coaching/Courses vertical) |
| Current primary CTA | "Book a free 20-min diagnostic" → Calendly | `index.html` #book section |
| Tracking | Calendly confirmation emails to `vladimir@podlevskikh.com` + `armenia.mail.vladimir@gmail.com` |
| Period to establish baseline | 2 weeks before the quiz is deployed (count Calendly bookings vs estimated visitors) |

Visitor count proxy (no GA yet): Calendly's own visit counter on the event page, or use a free Cloudflare web analytics snippet on index.html (zero-JS tracking, no cookie consent needed, free tier).

---

## 2. Variant

**Quiz embed inserted in the hero section of `index.html`** (see embed snippet in this repo) — a clear secondary CTA that routes visitors to `quiz.html` before they see the Calendly widget directly.

The quiz result screens all link to the same Calendly URL with UTM appended:
```
https://calendly.com/vladimir-podlevskikh/30min?utm_source=quiz&utm_medium=result&utm_campaign=<result_slug>
```

This means bookings originating from the quiz show `utm_source=quiz` in the Calendly confirmation email subject/body (Calendly passes UTMs through to the confirmation).

---

## 3. What to track

**Primary signal:** Calendly bookings per week.

- Bookings **with** `utm_source=quiz` in the confirmation email = quiz-driven conversions.
- Bookings **without** that tag = direct/organic.

**Secondary signal:** Quiz completion rate.
- Count: how many people reach the result screen vs how many click "Start the diagnostic".
- Proxy: if you add a single `<img src="https://plausible.io/...">` or a Cloudflare Worker logging pixel on the result screen — zero-setup, zero-JS-library. Or simply check manually by counting quiz-tagged Calendly emails.

---

## 4. Sample size and decision criteria

**Minimum before declaring a winner:** 200 visitors per variant (400 total). At current 4.9% baseline and expected quiz lift to ~10%, a 200-visitor sample per arm gives ~80% power to detect that delta (two-proportion z-test, α = 0.05).

At typical cold-traffic volumes for a tutoring landing (estimate 30–60 organic visits/week), this takes **4–8 weeks**. If you're running any paid traffic, it compresses to 2–3 weeks.

**Decision rules:**

| Outcome | Action |
|---|---|
| Quiz-sourced bookings ≥ 2× baseline rate for 2 consecutive weeks | Make quiz the primary above-fold CTA, demote "Book a free 20-min diagnostic" button to secondary |
| Quiz-sourced bookings within 20% of baseline (no lift) | Keep static CTA primary; use quiz as a nurture tool for visitors who don't book immediately |
| Quiz completion < 40% (people abandon mid-quiz) | Shorten quiz to 5 questions — remove Q7 and Q8 as they are latest-order and highest-dropout risk |
| Zero bookings from quiz after 4 weeks | Investigate: is the quiz CTA visible on mobile? Check that `quiz.html` loads in < 2s |

---

## 5. Tracking hook — no analytics setup required

The embed block adds `?source=quiz_embed` to the quiz link:
```html
<a href="quiz.html?source=quiz_embed" class="btn-quiz">Take the 5-minute diagnostic →</a>
```

Inside `quiz.html`, the Calendly links carry:
```
?utm_source=quiz&utm_medium=result&utm_campaign=strong|gap|risk
```

Calendly includes the full booking URL (with UTM params) in the notification email it sends to `vladimir@podlevskikh.com`. So the entire funnel is trackable through your existing email inbox — no analytics account needed.

To count: run a quick grep on the inbox each Sunday:
- Subject contains "New Event" + body contains `utm_source=quiz` → quiz-sourced booking.
- Subject contains "New Event" + no quiz tag → direct.

---

## 6. Deploy checklist (pending Vladimir confirmation)

- [ ] Review `quiz.html` locally: `python3 -m http.server 8900 --directory ~/money/landing-page/`
- [ ] Insert embed snippet from below into `index.html` hero section
- [ ] Run `~/money/landing-page/deploy.sh` to push to GitHub Pages (namebogsecret/tutoring-landing)
- [ ] Confirm `https://tutor.podlevskikh.com/quiz.html` resolves
- [ ] Book a test Calendly slot from the quiz result screen and verify the UTM appears in the notification email
- [ ] Note the week-0 Calendly booking count as baseline

---

## Embed snippet for `index.html`

Insert this block **inside the `.hero-copy` div, immediately before the `.hero-actions` div** (line ~511 in current index.html):

```html
<!-- QUIZ EMBED: insert inside .hero-copy, before .hero-actions -->
<div class="quiz-cta" style="
  margin-bottom: 18px;
  padding: 18px 22px;
  background: var(--accent-soft);
  border: 1px solid var(--accent-line);
  border-radius: var(--radius-lg);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  flex-wrap: wrap;
">
  <div>
    <p style="font-size:13px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--accent);margin-bottom:4px;">Free 5-minute quiz</p>
    <p style="font-size:15.5px;color:var(--ink-soft);margin:0;max-width:38ch;">Find out exactly where your child stands before the IB, AP or SAT exam.</p>
  </div>
  <a href="quiz.html?source=quiz_embed" style="
    display:inline-flex;align-items:center;gap:8px;
    padding:12px 22px;border-radius:var(--radius);
    font-size:14.5px;font-weight:600;font-family:var(--font-body);
    background:var(--accent);color:var(--accent-ink);
    white-space:nowrap;text-decoration:none;
    transition:background .2s,transform .2s;
  " onmouseover="this.style.background='var(--accent-bright)';this.style.transform='translateY(-1px)'"
     onmouseout="this.style.background='var(--accent)';this.style.transform='none'">
    Take the diagnostic →
  </a>
</div>
```
