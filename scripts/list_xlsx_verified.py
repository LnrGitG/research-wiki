#!/usr/bin/env python3
"""Скрипты, у которых в отчёте есть хотя бы одна файловая сверка."""
import json
import sys

d = json.load(open(sys.argv[1], encoding="utf-8"))
ent = d.get("scripts") if isinstance(d, dict) and "scripts" in d else d
if isinstance(ent, dict):
    ent = list(ent.values())
with_files = [e for e in ent if (e.get("files") or [])]
print("со сверками:", len(with_files), "| без сырья:", len(ent) - len(with_files))
for e in with_files:
    fl = e.get("files") or []
    bad = [f.get("file") for f in fl if not f.get("ok")]
    print(f"  {e.get('script')}: {len(fl) - len(bad)}/{len(fl)}" + (f"  РАСХОД: {bad}" if bad else ""))
