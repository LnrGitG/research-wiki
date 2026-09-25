# -*- coding: utf-8 -*-
"""Шаг 3 v2: сверка решений против ступеней с учётом вступления на след. день.

Конвенция rate_level: effective_from = день вступления ставки в действие
(обычно заседание + 1 день). Решение 19.06.2026 → ступень с 20.06.2026.
Проверяем: level_at(meeting_date + 1) == rate_new; level_at(meeting_date) == rate_prev.
"""
import datetime
import sys

sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import query

levels = query("""
    SELECT effective_from, effective_to, value, level_id, decision_id FROM dkp.rate_level
    WHERE rate_code='key_rate' ORDER BY effective_from""")

def level_at(d):
    for frm, to, pct, lid, did in levels:
        if frm <= d and (to is None or d < to):
            return float(pct), lid, did
    return None

print("== Лестница 2025-2026 (контекст проблемы):")
for frm, to, pct, lid, did in levels:
    if frm >= datetime.date(2025, 1, 1):
        print(f"  level {lid} (decision {did}): {pct} с {frm} по {to}")

print("\n== Решения 2026 против пресс-релизов:")
for mid in (100, 101, 102, 103):
    r = query("SELECT meeting_date::text FROM dkp.meeting WHERE meeting_id=%s" % mid)
    md = r[0][0]
    d = query("SELECT rate_prev, rate_new, delta_bp, action FROM dkp.decision WHERE meeting_id=%s" % mid)[0]
    pr = query("SELECT url, substr(body, 1, 600) FROM dkp.statement WHERE meeting_id=%s AND kind='press_release'" % mid)
    print(f"\n--- meeting {mid} ({md}): decision prev={d[0]} new={d[1]} delta={d[2]} action={d[3]}")
    if pr:
        body = pr[0][1].replace("\n", " ")
        import re
        m = re.search(r"(?:снизить|повысить|сохранить)[^.]*?ставку[^.]*?(\d+[,.]\d+|\d+)", body)
        m2 = re.search(r"(?:до|на уровне)\s*(\d+[,.]\d+)\s*%", body)
        print(f"  URL: {pr[0][0]}")
        print(f"  regex 'до X%': {m2.group(1) if m2 else '—'}")
        print(f"  фрагмент: ...{body[:400]}...")

print("\n== Полная сверка всех 103 решений (правило +1 день):")
rows = query("""
    SELECT d.decision_id, m.meeting_date, d.rate_prev, d.rate_new, d.delta_bp, d.action
    FROM dkp.decision d JOIN dkp.meeting m USING (meeting_id)
    ORDER BY m.meeting_date""")
issues = []
for did, md, prev, new, delta, action in rows:
    dd = md if isinstance(md, datetime.date) else datetime.date.fromisoformat(str(md)[:10])
    lv_next = level_at(dd + datetime.timedelta(days=1))
    lv_now = level_at(dd)
    new_f = float(new) if new is not None else None
    prev_f = float(prev) if prev is not None else None
    ok_new = lv_next and new_f == lv_next[0]
    ok_prev = lv_now and prev_f == lv_now[0]
    if not (ok_new and ok_prev):
        issues.append((str(dd), did, prev_f, new_f, lv_now[0] if lv_now else None,
                       lv_next[0] if lv_next else None, lv_next[2] if lv_next else None))
print(f"проблемных: {len(issues)} из {len(rows)}")
for it in issues:
    print(f"  {it[0]} decision {it[1]}: prev={it[2]} new={it[3]}; лестница: на дату={it[4]} на след.день={it[5]} (level {it[6]})")