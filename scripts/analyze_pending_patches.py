#!/usr/bin/env python3
"""Разбор неприменённых staged-патчей: полные тексты вместо фрагментов диффа.

Для каждой отклонённой записи берёт new_string каждой операции и сравнивает
с текущим текстом навыка: что уже есть, что ново, что конфликтует.
"""
import difflib
import glob
import json
import os
import sys

SK = os.path.expanduser("~/.hermes/skills")
REJ = os.path.expanduser("~/.hermes/pending/skills/rejected")
OUT = os.path.expanduser("~/pending-recovered/_full")
os.makedirs(OUT, exist_ok=True)


def find(name):
    for pat in (f"{SK}/*/{name}/SKILL.md", f"{SK}/{name}/SKILL.md",
                f"{SK}/*/*/{name}/SKILL.md", f"{SK}/*/*/*/{name}/SKILL.md",
                f"{SK}/_disabled/{name}/SKILL.md"):
        h = glob.glob(pat)
        if h:
            return h[0]
    return None


def norm(s):
    """Нормализация для сравнения: пробелы и пунктуация не важны."""
    return " ".join(s.split()).lower()


report = []
for f in sorted(glob.glob(f"{REJ}/*.json")):
    d = json.load(open(f, encoding="utf-8"))
    rid = os.path.basename(f)[:-5]
    ops = (d.get("payload") or {}).get("operations") or []
    for i, o in enumerate(ops):
        if not isinstance(o, dict) or o.get("action") != "patch":
            continue
        name = o.get("name")
        ns = o.get("new_string") or ""
        os_ = o.get("old_string") or ""
        path = find(name)
        cur = open(path, encoding="utf-8").read() if path else ""
        nc = norm(cur)

        # блоки new_string, которых нет в навыке (по абзацам)
        blocks = [b.strip() for b in ns.split("\n\n") if b.strip()]
        novel, known = [], []
        for b in blocks:
            (known if norm(b) in nc else novel).append(b)

        if not novel:
            continue
        report.append({"id": rid, "name": name, "path": path,
                       "novel": novel, "known": len(known), "op": i})

report.sort(key=lambda r: -sum(len(b) for b in r["novel"]))
print("Записей с новым контентом: %d" % len(report))
print()
tot = 0
for r in report:
    size = sum(len(b) for b in r["novel"])
    tot += size
    print("  %-9s %-32s новое: %5d симв. в %d блоках (уже есть: %d)"
          % (r["id"], r["name"], size, len(r["novel"]), r["known"]))
print()
print("Итого нового контента: %d символов" % tot)

# сохранить полные тексты
for r in report:
    p = os.path.join(OUT, f'{r["name"]}__{r["id"]}.md')
    with open(p, "w", encoding="utf-8") as g:
        g.write("\n\n".join(r["novel"]))
print("Полные тексты: %s" % OUT)
