# -*- coding: utf-8 -*-
"""Каждая отдаваемая страница (кроме hub/404) должна считаться в GoatCounter."""
import os, subprocess, sys
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
files = subprocess.check_output(["git", "ls-files", "*.html"], cwd=HERE, text=True).split()
bad = [f for f in files
       if not f.startswith(("src/", "hub/")) and f != "404.html"
       and "stats.podlevskikh.com/count" not in open(os.path.join(HERE, f), encoding="utf-8").read()]
if bad:
    print("нет счётчика:", bad); sys.exit(1)
print("ok", len(files))
