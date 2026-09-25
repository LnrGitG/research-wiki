# -*- coding: utf-8 -*-
"""Зонд перед фазой 1: схемы таблиц, флаги, строки 2025-04/06, лестница 2025."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from db_tunnel import connect, query

conn = connect()
cur = conn.cursor()

print("=== dkp.meeting columns ===")
cur.execute("""SELECT column_name, data_type, is_nullable FROM information_schema.columns
WHERE table_schema='dkp' AND table_name='meeting' ORDER BY ordinal_position""")
for r in cur.fetchall():
    print(" ", r[0], "|", r[1], "|", r[2])

print("=== dkp.decision columns ===")
cur.execute("""SELECT column_name, data_type, is_nullable FROM information_schema.columns
WHERE table_schema='dkp' AND table_name='decision' ORDER BY ordinal_position""")
for r in cur.fetchall():
    print(" ", r[0], "|", r[1], "|", r[2])

print("=== needs_source_check location ===")
cur.execute("""SELECT table_name, column_name FROM information_schema.columns
WHERE table_schema='dkp' AND column_name LIKE '%source%' ORDER BY table_name""")
for r in cur.fetchall():
    print(" ", r)

print("=== dkp.rate_level columns ===")
cur.execute("""SELECT column_name, data_type FROM information_schema.columns
WHERE table_schema='dkp' AND table_name='rate_level' ORDER BY ordinal_position""")
for r in cur.fetchall():
    print(" ", r)

print("=== decisions 2025-02..2025-08 (current state) ===")
cur.execute("""SELECT decision_id, meeting_date::text, rate_prev, rate_new, delta_bp, action, signal_kind
FROM dkp.decision WHERE meeting_date BETWEEN '2025-01-01' AND '2025-12-31' ORDER BY meeting_date""")
for r in cur.fetchall():
    print(" ", r)

print("=== ladder 2025 (from daily series dump) ===")
p = "/tmp/keyrate_series.txt"
if os.path.exists(p):
    prev = None
    with open(p) as f:
        for line in f:
            parts = line.strip().split(";")
            if len(parts) != 2:
                continue
            d, v = parts[0], float(parts[1].replace(",", "."))
            if d >= "2025-01-01":
                if prev is not None and abs(v - prev[1]) > 1e-9:
                    print("  change: %s %.2f -> %s %.2f" % (prev[0], prev[1], d, v))
                prev = (d, v)
else:
    print("  /tmp/keyrate_series.txt отсутствует — нужен regenerate")

print("=== meetings near unplanned inserts (check duplicates) ===")
cur.execute("""SELECT meeting_id, meeting_date::text, decision_kind FROM dkp.meeting
WHERE meeting_date IN ('2014-12-11','2014-12-12','2022-02-14','2022-02-28','2022-05-26','2023-08-15') ORDER BY meeting_date""")
for r in cur.fetchall():
    print(" ", r)

print("=== decisions at those dates (current) ===")
cur.execute("""SELECT decision_id, meeting_date::text, rate_prev, rate_new, delta_bp, action
FROM dkp.decision WHERE meeting_date IN ('2014-12-11','2014-12-12','2022-02-14','2022-02-18','2022-02-28','2022-05-26','2023-08-15') ORDER BY meeting_date""")
for r in cur.fetchall():
    print(" ", r)

print("=== decisions 2022-09/10 (current) ===")
cur.execute("""SELECT decision_id, meeting_date::text, rate_prev, rate_new, delta_bp, action
FROM dkp.decision WHERE meeting_date BETWEEN '2022-09-01' AND '2022-11-01' ORDER BY meeting_date""")
for r in cur.fetchall():
    print(" ", r)

print("=== needs_source_check rows 2014-2026 (count by year) ===")
cur.execute("""SELECT COUNT(*) FROM dkp.decision WHERE needs_source_check IS TRUE""")
print("  count:", cur.fetchall()[0][0])

conn.close()