# -*- coding: utf-8 -*-
"""Каждая отдаваемая страница (кроме hub/404) должна считаться в GoatCounter:
либо инлайн-сниппетом (главная, quiz), либо через /assets/site.js (собранные страницы).
Сниппет И site.js на одной странице = двойной счёт — тоже ошибка."""
import os, subprocess, sys
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
files = subprocess.check_output(["git", "ls-files", "*.html"], cwd=HERE, text=True).split()
bad = []
for f in files:
    if f.startswith(("src/", "hub/")) or f == "404.html":
        continue
    s = open(os.path.join(HERE, f), encoding="utf-8").read()
    inline = "stats.podlevskikh.com/count.js" in s
    shared = 'src="/assets/site.js"' in s
    if inline == shared:
        bad.append((f, "inline" if inline else "none"))
if bad:
    print("нет счётчика или двойной счёт:", bad); sys.exit(1)
print("ok", len(files))
