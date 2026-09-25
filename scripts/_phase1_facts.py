# -*- coding: utf-8 -*-
"""Фактура фазы 1: решения 97-103, окрестность 2022-02, потомки 62/63,
тексты релизов 2025-04/06, дек 2025, фев-мар 2026, needs_source_check."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from db_tunnel import connect, query

conn = connect()
cur = conn.cursor()

def show(title, sql):
    print("=== %s ===" % title)
    try:
        cur.execute(sql)
        rows = cur.fetchall()
        for r in rows:
            print(" ", r)
    except Exception as e:
        conn.rollback()
        print("  ERR:", e)
    print()

show("decisions mid 97-104", """
SELECT d.decision_id, d.meeting_id, m.meeting_date::text, d.rate_prev, d.rate_new,
d.delta_bp, d.action, d.signal_kind, d.headline_ru IS NOT NULL AS has_headline
FROM dkp.decision d JOIN dkp.meeting m ON m.meeting_id=d.meeting_id
WHERE d.meeting_id BETWEEN 97 AND 104 ORDER BY d.meeting_id""")

show("meetings 62-66 (2022-02..05) + their FK children", """
SELECT m.meeting_id, m.meeting_date::text, m.decision_kind, m.notes,
 (SELECT count(*) FROM dkp.statement s WHERE s.meeting_id=m.meeting_id) AS stmts,
 (SELECT count(*) FROM dkp.minutes mn WHERE mn.meeting_id=m.meeting_id) AS mins,
 (SELECT count(*) FROM dkp.argument a WHERE a.statement_id IN
   (SELECT statement_id FROM dkp.statement s2 WHERE s2.meeting_id=m.meeting_id)) AS args,
 (SELECT count(*) FROM dkp.forecast f WHERE f.meeting_id=m.meeting_id) AS fcts
FROM dkp.meeting m WHERE m.meeting_id IN (62,63,64,65,66) ORDER BY m.meeting_id""")

show("rate_level rows for decisions 61-64 (2022-02)", """
SELECT r.level_id, r.decision_id, r.value, r.effective_from::text, r.effective_to::text
FROM dkp.rate_level r WHERE r.decision_id BETWEEN 61 AND 64 ORDER BY r.effective_from""")

show("statement/minutes tables FK columns", """
SELECT table_name, column_name FROM information_schema.columns
WHERE table_schema='dkp' AND column_name IN ('meeting_id')
AND table_name IN ('statement','minutes','argument','forecast','forecast_realized','dissent','uncertainty_item','rate_level','decision')
ORDER BY table_name""")

show("release texts 2025-04-25 / 2025-06-06", """
SELECT s.statement_id, s.meeting_id, s.kind, s.event_date::text, left(s.text_raw, 220)
FROM dkp.statement s
WHERE (s.event_date IN ('2025-04-25','2025-06-06')
  OR (s.event_date IN ('2025-04-24','2025-06-05') AND s.kind='press_release'))
ORDER BY s.event_date""")

show("release texts dec 2025 / feb 2026 / mar 2026", """
SELECT s.statement_id, s.meeting_id, s.kind, s.event_date::text, left(s.text_raw, 200)
FROM dkp.statement s WHERE s.event_date IN ('2025-12-19','2026-02-13','2026-03-20')
ORDER BY s.event_date, s.kind""")

show("needs_source_check flags on meetings 2014-2026", """
SELECT string_agg(m.meeting_id::text, ',' ORDER BY m.meeting_id) AS mids
FROM dkp.meeting m WHERE m.notes ILIKE '%needs_source_check%'""")

show("decision source ids for 97-103", """
SELECT d.decision_id, d.source_id FROM dkp.decision d WHERE d.decision_id BETWEEN 97 AND 103 ORDER BY 1""")

show("dkp.dissent schema + rows near 2022", """
SELECT column_name FROM information_schema.columns WHERE table_schema='dkp' AND table_name='dissent'""")
cur.execute("SELECT count(*) FROM dkp.dissent")
print("  dissent rows:", cur.fetchall()[0][0])

show("decision 62/63 detail (rate_prev/new/sha/source)", """
SELECT decision_id, meeting_id, rate_prev, rate_new, delta_bp, action, sha256, source_id,
signal_kind, left(coalesce(headline_ru,''),100)
FROM dkp.decision WHERE decision_id IN (62,63)""")

conn.close()