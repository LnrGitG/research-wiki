#!/usr/bin/env python3
"""Показать окрестности мест чтения xlsx из отчёта scan_xlsx_sites.py.

Запуск: python3 scripts/show_xlsx_sites.py /tmp/xlsx_sites.json convert
"""
import json
import sys
from collections import defaultdict

path = sys.argv[1] if len(sys.argv) > 1 else "/tmp/xlsx_sites.json"
want = sys.argv[2] if len(sys.argv) > 2 else "convert"
sites = json.load(open(path, encoding="utf-8"))
d = defaultdict(list)
for s in sites:
    if s["verdict"] == want:
        d[s["file"]].append(s["line"])
for f, lines in d.items():
    text = open(f, encoding="utf-8", errors="replace").read().splitlines()
    print("=" * 20, f, lines)
    for ln in lines:
        lo, hi = max(0, ln - 3), min(len(text), ln + 20)
        print("\n".join(f"{i+1:5d}| {text[i]}" for i in range(lo, hi)))
        print("---")
