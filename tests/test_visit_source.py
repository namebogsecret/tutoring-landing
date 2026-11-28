# -*- coding: utf-8 -*-
"""Источник визита (first-touch) в CTA-скриптах: cookie pdl_ft, &r=<источник> только у /cta-*.
Контракт: ~/воронка-репетитор/components/site-analytics-ft. Прогон кода через node (vm)."""
import json, os, shutil, subprocess, unittest
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = ["index.html", "quiz.html", "quiz-ru.html", "assets/site.js"]

RUNNER = r'''
const vm=require("vm"),fs=require("fs");
const [file,href,referrer,jar0]=process.argv.slice(2);
let s=fs.readFileSync(file,"utf8");
if(file.endsWith(".html")){const m=[...s.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(x=>x[1]).filter(x=>x.includes('"/cta-"')&&x.includes("__pdlSrc"));s=m.join("\n");}
else{const i=s.indexOf("/* CTA-события");const j=s.indexOf("/* AI-рефереры");s=s.slice(i,j);}
const jar=JSON.parse(jar0),beacons=[];let h;const u=new URL(href);
const document={referrer,cookie:null,addEventListener:(t,f)=>{h=f}};
Object.defineProperty(document,"cookie",{get:()=>Object.entries(jar).map(([k,v])=>k+"="+v).join("; "),set:(c)=>{const kv=c.split(";")[0],i=kv.indexOf("=");jar[kv.slice(0,i)]=kv.slice(i+1);}});
const ctx={window:{sessionStorage:{getItem:()=>null,setItem(){}}},document,Image:function(){},navigator:{sendBeacon:(x)=>{beacons.push(x);return true}},
 location:{host:u.host,hostname:u.hostname,pathname:u.pathname,search:u.search,protocol:u.protocol}};
vm.runInNewContext(s,ctx);
const click=(href)=>{const a={href,hostname:new URL(href).hostname,protocol:new URL(href).protocol,hasAttribute:()=>false,getAttribute:()=>null};h({target:{closest:()=>a}})};
click("https://calendly.com/x");click("https://example.org/");
console.log(JSON.stringify({beacons,jar}));
'''

def run(f, href, referrer="", jar=None):
    r = subprocess.check_output(["node", "-e", RUNNER, "x", os.path.join(HERE, f), href, referrer, json.dumps(jar or {})], text=True)
    return json.loads(r)

@unittest.skipUnless(shutil.which("node"), "node нужен")
class VisitSource(unittest.TestCase):
    def test_all(self):
        for f in FILES:
            with self.subTest(f=f):
                # utm_source → r=utm (lowercase), cta получает r, /out- — нет; cookie пишется
                d = run(f, "https://tutor.podlevskikh.com/?utm_source=ChatGPT.com")
                cta, out = d["beacons"]
                self.assertIn("&r=chatgpt.com", cta); self.assertIn("cta-calendly", cta)
                self.assertNotIn("&r=", out); self.assertIn("out-example.org", out)
                self.assertEqual(d["jar"]["pdl_ft"], "chatgpt.com")
                # внешний реферер → origin+path
                d = run(f, "https://tutor.podlevskikh.com/", "https://www.google.com/search?q=x")
                self.assertIn("&r=" + "https%3A%2F%2Fwww.google.com%2Fsearch", d["beacons"][0])
                # внутренний реферер сети и прямой заход → без r
                d = run(f, "https://tutor.podlevskikh.com/", "https://physics.podlevskikh.com/a")
                self.assertNotIn("&r=", d["beacons"][0]); self.assertEqual(d["jar"]["pdl_ft"], "")
                # cookie уже есть (другой сайт сети) → читаем, не перезаписываем
                d = run(f, "https://tutor.podlevskikh.com/?utm_source=bing", "", {"pdl_ft": "habr"})
                self.assertIn("&r=habr", d["beacons"][0]); self.assertEqual(d["jar"]["pdl_ft"], "habr")

if __name__ == "__main__":
    unittest.main()
