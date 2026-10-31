#!/usr/bin/env python3
"""Сводка сверки: по каждому скрипту — файлы, расхождения, разборный уровень."""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rep = json.load(open(os.path.join(ROOT, "findings/xlsx-migration-verify-20261031.json"),
                    encoding="utf-8"))
no_files, bad_files, bad_parse, good = [], [], [], []
for e in rep:
    s = e["script"]
    files = e.get("files", [])
    bads = [f["file"] for f in files if not f["ok"]]
    parse = e.get("parse")
    parse_ok = None if not parse else parse.get("ok")
    if not files and parse_ok is None:
        no_files.append(s)
    elif bads or parse_ok is False:
        bad_files.append((s, bads))
        if parse_ok is False:
            bad_parse.append(s)
    else:
        good.append((s, len(files), parse_ok))

print("=== ПОДТВЕРЖДЕНО (сверка пройдена) ===")
for s, n, p in good:
    print(f"  {s}: файлов {n}" + ("" if p is None else f", разбор {'ок' if p else 'РАСХОДИТСЯ'}"))
print("\n=== РАСХОЖДЕНИЯ -> остаются на openpyxl ===")
for s, b in bad_files:
    print(f"  {s}: {len(b)} файл(ов) " + ", ".join(os.path.basename(x) for x in b))
print("  разбор расходится: " + ", ".join(bad_parse))
print("\n=== СВЕРКА НЕ ВЫПОЛНЕНА (сырьё не найдено) -> остаются на openpyxl ===")
for s in no_files:
    print("  " + s)
print(f"\nитого скриптов {len(rep)}: подтверждено {len(good)}, расхождений {len(bad_files)},"
      f" без сверки {len(no_files)}")
