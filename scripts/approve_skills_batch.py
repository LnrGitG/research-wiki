#!/usr/bin/env python3
"""Пакетная обработка staged-навыков: применение годного, отклонение устаревшего.

Логика:
  1. Патчи, чей old_string ещё находится в файле -> применить.
  2. Патчи, чей new_string уже в файле -> признать применёнными, убрать из очереди.
  3. Патчи, где ни old, ни new не найдены -> устарели (файл менялся curator'ом
     за 5 дней ожидания) -> отклонить с фиксацией причины.
  4. create: сократить description до SKILL_PROMPT_DESC_LIMIT (иначе гейт
     отвергает), затем применить.
  5. write_file к навыку, созданному на шаге 4 -> применить.

Отклонение = файл уходит в rejected/ с записью причины, а не удаляется молча.
"""
import glob
import json
import os
import re
import shutil
import sys
import time

sys.path.insert(0, os.path.expanduser("~/.hermes/hermes-agent"))

from tools import write_approval as wa  # noqa: E402
from tools.skill_manager_tool import apply_skill_pending  # noqa: E402
from agent.skill_utils import SKILL_PROMPT_DESC_LIMIT  # noqa: E402

SK = os.path.expanduser("~/.hermes/skills")
REJECTED = os.path.expanduser("~/.hermes/pending/skills/rejected")
APPLY = os.environ.get("APPLY") == "1"


def find_skill(name):
    for pat in (f"{SK}/*/{name}/SKILL.md", f"{SK}/{name}/SKILL.md",
                f"{SK}/*/*/{name}/SKILL.md", f"{SK}/*/*/*/{name}/SKILL.md"):
        hits = glob.glob(pat)
        if hits:
            return hits[0]
    return None


def shorten_description(content, limit):
    """Сжать description до лимита, сохранив триггер в начале."""
    m = re.match(r"^---\n(.*?)\n---\n", content, re.S)
    if not m:
        return content, None
    fm = m.group(1)
    dm = re.search(r'^description:\s*(.*)$', fm, re.M)
    if not dm:
        return content, None
    raw = dm.group(1).strip().strip('"').strip("'")
    if len(raw) <= limit:
        return content, None
    # берём первое предложение, при необходимости обрезаем по границе слова
    first = re.split(r"(?<=[.;])\s+", raw)[0]
    if len(first) > limit:
        cut = raw[:limit].rsplit(" ", 1)[0].rstrip(",;:")
        first = cut if cut.endswith(".") else cut + "."
    new_fm = fm[:dm.start(1)] + f'"{first}"' + fm[dm.end(1):]
    return content[:m.start(1)] + new_fm + content[m.end(1):], (len(raw), len(first))


def reject(rec, reason):
    os.makedirs(REJECTED, exist_ok=True)
    rec = dict(rec)
    rec["rejected_at"] = time.time()
    rec["rejected_reason"] = reason
    path = os.path.join(REJECTED, f'{rec["id"]}.json')
    with open(path, "w", encoding="utf-8") as f:
        json.dump(rec, f, ensure_ascii=False, indent=1)
    wa.discard_pending("skills", rec["id"])


def main():
    records = sorted(wa.list_pending("skills"), key=lambda r: r.get("created_at") or 0)
    print("Записей: %d | режим: %s | лимит description: %d"
          % (len(records), "ПРИМЕНЕНИЕ" if APPLY else "сухой прогон", SKILL_PROMPT_DESC_LIMIT))
    print()

    applied, done_already, rejected, deferred = [], [], [], []
    made_skills = set()

    # --- проход 1: патчи ---
    for rec in records:
        ops = (rec.get("payload") or {}).get("operations") or []
        if not ops or ops[0].get("action") != "patch":
            continue
        o = ops[0]
        name, rid = o.get("name"), rec["id"]
        path = find_skill(name)
        if not path:
            rejected.append((rid, name, "навык не найден")); continue
        cur = open(path, encoding="utf-8").read()
        if (o.get("new_string") or "") and o["new_string"] in cur:
            if APPLY: wa.discard_pending("skills", rid)
            done_already.append((rid, name)); continue
        if (o.get("old_string") or "") and o["old_string"] in cur:
            if APPLY:
                res = json.loads(apply_skill_pending(rec["payload"]))
                if res.get("success"):
                    wa.discard_pending("skills", rid); applied.append((rid, name))
                else:
                    rejected.append((rid, name, (res.get("error") or "")[:90]))
            else:
                applied.append((rid, name))
            continue
        rejected.append((rid, name, "устарел: ни old, ни new не найдены (файл менялся после постановки)"))

    # --- проход 2: create (с сокращением description) ---
    for rec in records:
        ops = (rec.get("payload") or {}).get("operations") or []
        if not ops or ops[0].get("action") != "create":
            continue
        o = ops[0]
        name, rid = o.get("name"), rec["id"]
        if find_skill(name):
            if APPLY: wa.discard_pending("skills", rid)
            done_already.append((rid, name + " (уже существует)"))
            made_skills.add(name)
            continue
        content = o.get("content") or ""
        fixed, delta = shorten_description(content, SKILL_PROMPT_DESC_LIMIT)
        if delta:
            print("  description: %d -> %d симв. (%s)" % (delta[0], delta[1], name))
            o["content"] = fixed
        if APPLY:
            res = json.loads(apply_skill_pending(rec["payload"]))
            if res.get("success"):
                wa.discard_pending("skills", rid); applied.append((rid, name)); made_skills.add(name)
            else:
                rejected.append((rid, name, (res.get("error") or "")[:90]))
        else:
            applied.append((rid, name)); made_skills.add(name)

    # --- проход 3: write_file к созданным ---
    for rec in records:
        ops = (rec.get("payload") or {}).get("operations") or []
        if not ops or ops[0].get("action") != "write_file":
            continue
        o = ops[0]
        name, rid = o.get("name"), rec["id"]
        if not find_skill(name):
            deferred.append((rid, name, "навык-владелец не создан")); continue
        if APPLY:
            res = json.loads(apply_skill_pending(rec["payload"]))
            if res.get("success"):
                wa.discard_pending("skills", rid); applied.append((rid, name))
            else:
                rejected.append((rid, name, (res.get("error") or "")[:90]))
        else:
            applied.append((rid, name))

    # --- отчёт ---
    if APPLY:
        for rid, name, reason in rejected:
            rec = wa.get_pending("skills", rid)
            if rec: reject(rec, reason)
        for rid, name, reason in deferred:
            rec = wa.get_pending("skills", rid)
            if rec: reject(rec, reason)

    print()
    print("Применено/применимо: %d" % len(applied))
    for r, n in applied: print("   + %-9s %s" % (r, n))
    print()
    print("Уже применено ранее: %d" % len(done_already))
    for r, n in done_already: print("   = %-9s %s" % (r, n))
    print()
    print("Отклонено: %d" % len(rejected))
    for r, n, why in rejected[:45]: print("   - %-9s %-34s %s" % (r, n, why))
    print()
    if APPLY:
        print("Осталось в очереди: %d" % len(wa.list_pending("skills")))
        print("Отклонённые: %s" % REJECTED)
    return 0


if __name__ == "__main__":
    sys.exit(main())
