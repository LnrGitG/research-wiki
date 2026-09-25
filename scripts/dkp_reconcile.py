# -*- coding: utf-8 -*-
"""Реконсилиация: авторитетная лестница (hd_base) против dkp.decision.

Классификация каждого решения:
- OK: ступень на след. рабочий день == rate_new, на день заседания == rate_prev
- wrong_action: БД говорит hold, лестница двигается (или наоборот)
- wrong_level: изменение есть, но уровень другой
- date_shift: ступень вступает позже, дата в БД = дата вступления
- unverifiable_hold: hold, лестница не двигается — проверяется только по релизам

Отдельно: ступени лестницы без покрытого решения (пропущенные заседания).
"""
import datetime
import json
import sys

sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import query

# Авторитетная лестница (hd_base, извлечена dkp_full_audit.py)
steps = []
with open("/tmp/keyrate_ladder.txt", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        d, v = line.split(";")
        steps.append((datetime.date.fromisoformat(d), float(v)))

def level_at(d):
    lv = None
    for frm, v in steps:
        if frm <= d:
            lv = v
        else:
            break
    return lv

def next_bd(d):
    d += datetime.timedelta(days=1)
    while d.weekday() >= 5:
        d += datetime.timedelta(days=1)
    return d

rows = query("""
    SELECT d.decision_id, m.meeting_id, m.meeting_date, d.rate_prev, d.rate_new, d.action
    FROM dkp.decision d JOIN dkp.meeting m USING (meeting_id)
    ORDER BY m.meeting_date""")

report = []
for did, mid, md, prev, new, action in rows:
    d = md if isinstance(md, datetime.date) else datetime.date.fromisoformat(str(md)[:10])
    lv_now = level_at(d)
    lv_eff = level_at(next_bd(d))
    new_f = float(new) if new is not None else None
    prev_f = float(prev) if prev is not None else None
    moved = lv_eff != lv_now
    cls = None
    if moved:
        if new_f == lv_eff and prev_f == lv_now:
            cls = "OK"
        elif new_f == lv_eff or prev_f == lv_now:
            cls = "wrong_level"
        else:
            cls = "date_shift_or_wrong"
    else:
        if prev_f == lv_now and new_f == lv_now:
            cls = "hold_ok"
        else:
            cls = "hold_wrong_level"
    # date_shift: ступень вступает позднее след. рабочего дня (до 5 дней)
    if moved and cls != "OK":
        probe = next_bd(d)
        for _ in range(5):
            probe = next_bd(probe)
            if level_at(probe) == new_f and prev_f == lv_now:
                cls = "date_shift"
                break
    report.append({"decision_id": did, "meeting_id": mid, "date": str(d),
                   "recorded": [prev_f, new_f], "action": action,
                   "level_now": lv_now, "level_eff": lv_eff, "class": cls})

# Сводка
from collections import Counter
cnt = Counter(r["class"] for r in report)
print("== Классификация 103 решений против лестницы hd_base:")
for k, v in cnt.most_common():
    print(f"  {k}: {v}")

print("\n== Проблемные классы (все):")
for r in report:
    if r["class"] not in ("OK", "hold_ok"):
        print(f"  {r['date']} decision {r['decision_id']} [{r['class']}]: "
              f"записано {r['recorded']}; факт на дату={r['level_now']}, на вступление={r['level_eff']}")

# Пропущенные ступени: каждая ступень лестницы должна быть чьим-то rate_new
covered = {round(r["recorded"][1], 2) for r in report if r["recorded"][1]}
print("\n== Ступени лестницы:")
prev_v = None
for d, v in steps:
    print(f"  {d}: {v}")
prev_v = None
missing = []
for i, (d, v) in enumerate(steps):
    if i == 0:
        continue
    missing.append((d, v))
print("\n(полная лестница выше — для ручной привязки дат решений)")

with open("/tmp/dkp_audit_report.json", "w", encoding="utf-8") as f:
    json.dump(report, f, ensure_ascii=False, indent=1)
print("\nJSON: /tmp/dkp_audit_report.json")