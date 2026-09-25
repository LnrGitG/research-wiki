# -*- coding: utf-8 -*-
"""Фаза 1, верификация: reconcile новой цепочки dkp.decision против лестницы.

Критерии приёмки A1/A2 (queries/dkp-backfill-audit-2026.md):
- A1: 0 hold_wrong_level / wrong_level для 2022-2026;
- A2: число решений = 107;
- лестница 66 ступеней, 0 перекрытий, 61 с FK-решением + 4 фазовых
  (2015-05, 2017-06, 2019-12, 2022-05-04 — пропущенные решения, фаза 2);
- цепочка rate_prev->rate_new непрерывна (prev[i] == new[i-1]).
"""
import sys, os, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from db_tunnel import connect

conn = connect()
cur = conn.cursor()

# Лестница из дневного ряда
ladder = []
with open("/tmp/keyrate_ladder.txt", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split(";")
        to = parts[1] if len(parts) > 1 and parts[1] else None
        ladder.append((parts[0], to, float(parts[2])))

cur.execute("""SELECT d.decision_id, m.meeting_date::text, d.rate_prev::float, d.rate_new::float,
d.delta_bp, d.action FROM dkp.decision d JOIN dkp.meeting m ON m.meeting_id=d.meeting_id
ORDER BY m.meeting_date""")
dec = cur.fetchall()
conn.commit()

errors = []

# A2
if len(dec) != 107:
    errors.append("A2 FAIL: решений %d вместо 107" % len(dec))

# Цепочка непрерывна: prev[i] == new[i-1]
prev_new = None
for did, md, rprev, rnew, dbp, act in dec:
    if prev_new is not None and abs(rprev - prev_new) > 1e-9:
        errors.append("chain break at %s (decision %d): prev=%.2f != prev.new=%.2f" % (md, did, rprev, prev_new))
    prev_new = rnew

# Reconcile против лестницы: для каждой ступени — было ли объявление на заседании 0-4 дней назад
ladder_by_date = {l[0]: l[2] for l in ladder}
ok = 0
problems = []
for did, md, rprev, rnew, dbp, act in dec:
    d = datetime.date.fromisoformat(md)
    # ступень, вступившая в окно 0-4 дней после заседания
    matched = None
    for frm, to, val in ladder:
        lag = (datetime.date.fromisoformat(frm) - d).days
        if 0 <= lag <= 4:
            matched = (frm, val, lag)
    if matched is None:
        problems.append((md, did, "no ladder step within 0-4d", "%.2f->%.2f %s" % (rprev, rnew, act)))
        continue
    frm, val, lag = matched
    # expected action/value
    if abs(rnew - val) < 1e-9:
        if abs(rnew - rprev) < 1e-9 and act != 'hold':
            problems.append((md, did, "hold level but action=%s" % act, ""))
        else:
            ok += 1
    else:
        problems.append((md, did, "level mismatch: db %.2f vs ladder %.2f (eff %s)" % (rnew, val, frm), ""))

print("=== Reconcile: OK %d / problems %d (из %d решений) ===" % (ok, len(problems), len(dec)))
for p in problems:
    print("  PROBLEM:", p)

# A1: проблемы только вне 2022-2026?
a1_fail = [p for p in problems if p[0] >= "2022-01-01"]
print("A1 (0 проблем 2022-2026):", "PASS" if not a1_fail else "FAIL %d" % len(a1_fail))
for p in a1_fail:
    print("  A1:", p)

# Перекрытия ступеней
cur.execute("""SELECT count(*) FROM dkp.rate_level a JOIN dkp.rate_level b
ON a.effective_from < b.effective_from AND COALESCE(a.effective_to,'2999-12-31'::date) >= b.effective_from""")
print("перекрытий ступеней:", cur.fetchone()[0])
conn.commit()

# FK-статус лестницы
cur.execute("SELECT count(*) FROM dkp.rate_level WHERE decision_id IS NULL")
null_fk = cur.fetchone()[0]
cur.execute("SELECT count(*) FROM dkp.rate_level")
total_levels = cur.fetchone()[0]
conn.commit()
print("лестница: %d ступеней, decision_id NULL: %d" % (total_levels, null_fk))

# Специальные проверки фазы 1
print()
print("=== Спец-проверки фазы 1 ===")
cur.execute("""SELECT d.decision_id, m.meeting_date::text, d.rate_prev::float, d.rate_new::float, d.delta_bp, d.action
FROM dkp.decision d JOIN dkp.meeting m USING (meeting_id)
WHERE m.meeting_date IN ('2025-12-19','2026-02-13','2026-03-20','2026-04-24','2026-06-19','2026-07-24','2026-09-11',
'2014-12-12','2022-02-14','2022-02-18','2022-02-28','2022-05-26','2023-08-15','2025-04-25','2025-06-06','2022-09-16','2022-10-28')
ORDER BY m.meeting_date""")
for r in cur.fetchall():
    conn.commit()
    print(" ", r)

# Граф-узлы решений синхронизированы?
cur.execute("""SELECT count(*) FROM graph.node WHERE node_type='cbr_decision'""")
g_nodes = cur.fetchone()[0]
conn.commit()
print()
print("graph cbr_decision узлов: %d (ожидается 107 после rebuild)" % g_nodes)

if errors:
    print()
    print("ОШИБКИ:")
    for e in errors:
        print(" -", e)
else:
    print()
    print("Цепочка непрерывна; решение-счёт 107: PASS" if len(dec) == 107 else "")

conn.close()