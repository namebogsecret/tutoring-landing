# -*- coding: utf-8 -*-
"""Проверки AI-дискавери: llms.txt, JSON-LD (Course/FAQPage), блок «страница репетитора».
Запуск: python3 tests/test_ai_discovery.py  (после python3 build.py)"""
import json, os, re, sys, subprocess
H = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://tutor.podlevskikh.com"
FORBID = re.compile(r"nyberg|кипр|лимасс|cyprus|limassol|cyprus|ереван|yerevan|gmt\+4|\$\s?\d|4\.88|\b127\b|\b214\b|20\+ призёров|\+30–60", re.I)
fails = []
def check(c, m):
    if not c: fails.append(m)
def rd(p): return open(os.path.join(H, p), encoding="utf-8").read()

page = rd("exam-prep-online/index.html")
llms = rd("llms.txt")
ld = [json.loads(x) for x in re.findall(r'<script type="application/ld\+json">\n(.*?)\n</script>', page, re.S)]
types = [d["@type"] for d in ld]
check("Course" in types and "FAQPage" in types and "BreadcrumbList" in types, f"JSON-LD типы: {types}")
faq = next(d for d in ld if d["@type"] == "FAQPage")
vis = len(re.findall(r'class="faq-item"', page))
check(len(faq["mainEntity"]) == vis >= 6, f"FAQ: ld={len(faq['mainEntity'])} видимых={vis}")
check(all(q["acceptedAnswer"]["text"] for q in faq["mainEntity"]), "пустой ответ в FAQPage")
check('rel="canonical" href="%s/exam-prep-online/"' % BASE in page, "canonical")
check(page.count("<h1") == 1, "ровно один h1")

# запрещённое — в видимом тексте новой страницы и в llms.txt (JSON-LD входит в страницу целиком)
for name, txt in (("exam-prep-online", page), ("llms.txt", llms)):
    m = FORBID.search(txt)
    check(not m, f"{name}: запрещённое «{m.group(0) if m else ''}»")
for w in ("Nyberg", "Кипр", "Лимассол", "Cyprus", "Limassol"):
    for p in ("exam-prep-online/index.html", "llms.txt", "src/exam-prep-online.html"):
        check(w.lower() not in rd(p).lower(), f"{p}: {w}")

# блок на других страницах и ссылка в sitemap/llms
for p in ("ege-physics", "ib-physics-tutor", "olympiad-physics", "blog/kinematics-grafiki"):
    h = rd(p + "/index.html")
    check('data-cta="tutor-page" href="/exam-prep-online/"' in h, f"{p}: нет блока")
check(BASE + "/exam-prep-online/" in rd("sitemap.xml"), "sitemap")
check(BASE + "/exam-prep-online/" in llms, "llms.txt ссылка")
check('data-cta="tutor-page"' not in page, "блок не должен быть на самой странице")

# все ссылки llms.txt ведут на существующие страницы
for u in re.findall(r"\]\((%s/[^)]*)\)" % re.escape(BASE), llms):
    path = u[len(BASE):].strip("/")
    check(os.path.exists(os.path.join(H, path, "index.html")) if path else True, f"llms ссылка без файла: {u}")

# site.js: события tutor-page и ai-ref
js = rd("assets/site.js")
check('name="tutor-page"' in js and "/ai-ref-" in js, "site.js события")
r = subprocess.run(["node", "-e", """
const src=require('fs').readFileSync(process.argv[1],'utf8');
const m=src.match(/\\(function\\(\\)\\{try\\{\\s*var src=null[\\s\\S]*?\\}catch\\(e\\)\\{\\}\\}\\)\\(\\);/);
if(!m) {console.log('NOBLOCK');process.exit(0)}
function run(ref,search){let sent=[];
 global.document={referrer:ref}; global.location={host:'tutor.podlevskikh.com',search};
 Object.defineProperty(global,'navigator',{value:{sendBeacon:u=>sent.push(decodeURIComponent(u))},configurable:true,writable:true});
 let loads=[];global.window={addEventListener:(e,f)=>{if(e==='load')loads.push(f)}};
 eval(m[0]); loads.forEach(f=>f()); return sent.join('|')}
console.log(JSON.stringify([run('https://chatgpt.com/',''),run('https://claude.ai/chat/x',''),run('https://google.com/','?utm_source=chatgpt.com'),run('https://google.com/','')]));
""", os.path.join(H, "assets/site.js")], capture_output=True, text=True)
try:
    o = json.loads(r.stdout.strip())
    check("ai-ref-chatgpt" in o[0] and "ai-ref-claude" in o[1] and "ai-ref-chatgpt" in o[2] and o[3] == "", f"ai-ref поведение: {o}")
except Exception:
    check(False, f"node-проверка: {r.stdout} {r.stderr}")

def test_ai_discovery():  # pytest/dev-gate: проверки выше выполняются при импорте
    assert not fails, "\n".join(fails)


if __name__ == "__main__":
    print("FAIL:\n" + "\n".join(fails) if fails else "OK: все проверки зелёные")
    sys.exit(1 if fails else 0)
