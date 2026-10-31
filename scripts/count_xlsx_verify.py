#!/usr/bin/env python3
"""Сводка по отчётам сверки: скрипты, файловые сверки, совпадения."""
import json
import sys

for p in sys.argv[1:]:
    d = json.load(open(p, encoding="utf-8"))
    ent = d.get("scripts") if isinstance(d, dict) and "scripts" in d else d
    if isinstance(ent, dict):
        ent = list(ent.values())
    files = sum(len(e.get("files") or []) for e in ent)
    ok = sum(1 for e in ent for f in (e.get("files") or []) if f.get("ok"))
    print(f"{p} | скриптов: {len(ent)} | сверок: {files} | совпало: {ok}")
