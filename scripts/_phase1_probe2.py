# -*- coding: utf-8 -*-
"""Зонд 2 фазы 1: таблицы dkp, флаг needs_source_check, sequence, rate_level/FK."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from db_tunnel import connect

conn = connect()
cur = conn.cursor()

print("=== tables in dkp ===")
cur.execute("""SELECT table_name FROM information_schema.tables
WHERE table_schema='dkp' ORDER BY table_name""")
tables = [r[0] for r in cur.fetchall()]
print(" ", tables)

print("=== columns with check/flag/verify anywhere ===")
cur.execute("""SELECT table_name, column_name FROM information_schema.columns
WHERE table_schema='dkp' AND (column_name ILIKE '%check%' OR column_name ILIKE '%flag%'
OR column_name ILIKE '%verif%' OR column_name ILIKE '%confid%')""")
for r in cur.fetchall():
    print(" ", r)

print("=== decision.source_id null profile ===")
cur.execute("""SELECT (source_id IS NULL) AS no_src, COUNT(*) FROM dkp.decision
GROUP BY 1 ORDER BY 1""")
for r in cur.fetchall():
    print("  source_id is null:", r[0], "count:", r[1])

print("=== decision source_id distribution by year ===")
cur.execute("""SELECT EXTRACT(YEAR FROM m.meeting_date)::int, COUNT(*),
SUM((d.source_id IS NULL)::int) AS null_src
FROM dkp.decision d JOIN dkp.meeting m ON m.meeting_id=d.meeting_id
GROUP BY 1 ORDER BY 1""")
for r in cur.fetchall():
    print("  year:", r[0], "decisions:", r[1], "source_id null:", r[2])

print("=== meeting.notes samples (any 'проверк'/'source') ===")
cur.execute("""SELECT meeting_id, meeting_date::text, left(coalesce(notes,''),80)
FROM dkp.meeting WHERE notes IS NOT NULL AND (notes ILIKE '%проверк%' OR notes ILIKE '%source%')
ORDER BY meeting_id LIMIT 10""")
for r in cur.fetchall():
    print(" ", r)

print("=== max ids ===")
cur.execute("SELECT max(decision_id) FROM dkp.decision")
print("  max decision_id:", cur.fetchall()[0][0])
cur.execute("SELECT max(meeting_id) FROM dkp.meeting")
print("  max meeting_id:", cur.fetchall()[0][0])
cur.execute("SELECT max(level_id) FROM dkp.rate_level")
print("  max level_id:", cur.fetchall()[0][0])

print("=== rate_level current rows (all) ===")
cur.execute("""SELECT r.level_id, r.decision_id, r.rate_code, r.value, r.annualized,
r.effective_from::text, r.effective_to::text, r.source_id
FROM dkp.rate_level r ORDER BY r.effective_from""")
for r in cur.fetchall():
    print(" ", r)

print("=== broken FK check (rate_level -> decision) ===")
cur.execute("""SELECT r.level_id, r.decision_id FROM dkp.rate_level r
LEFT JOIN dkp.decision d ON d.decision_id=r.decision_id
WHERE d.decision_id IS NULL""")
for r in cur.fetchall():
    print("  orphan level:", r)

print("=== decision table constraints/sequences ===")
cur.execute("""SELECT pg_get_serial_sequence('dkp.decision','decision_id')""")
print("  decision seq:", cur.fetchall()[0][0])
cur.execute("""SELECT pg_get_serial_sequence('dkp.meeting','meeting_id')""")
print("  meeting seq:", cur.fetchall()[0][0])
cur.execute("""SELECT pg_get_serial_sequence('dkp.rate_level','level_id')""")
print("  level seq:", cur.fetchall()[0][0])

conn.close()