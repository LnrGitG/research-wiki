#!/usr/bin/env python3
"""Демо v_decision_context: контекст для следующего решения (октябрь 2026)."""
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from db_tunnel import query  # noqa: E402

print("== текущие уровни ставок")
for r in query(
        "SELECT rate_code, value, effective_from "
        "FROM dkp.rate_level WHERE effective_to IS NULL"):
    print("  ", r)

print("== последний среднесрочный прогноз (по сериям, 2026-2029)")
for r in query("""
    SELECT series_code,
           string_agg(horizon_year::text, ',' ORDER BY horizon_year) AS years
    FROM dkp.forecast f JOIN dkp.meeting m USING (meeting_id)
    WHERE m.meeting_date = '2026-07-24' AND scenario='base'
    GROUP BY series_code ORDER BY series_code LIMIT 8
"""):
    print("  ", r)

print("== хронология 2025-2026 (v_decisions)")
for r in query(
        "SELECT meeting_date, rate_prev, rate_new, delta_bp, action "
        "FROM dkp.v_decisions WHERE meeting_date >= '2025-01-01' "
        "ORDER BY meeting_date"):
    print("  ", r)

print("== дневная траектория ставки 2024-2026 (развёртка ступеней, годовые границы)")
for r in query("""
    WITH d AS (
      SELECT gs::date AS day,
             (SELECT value FROM dkp.rate_level rl
              WHERE rl.rate_code='key_rate'
                AND rl.effective_from <= gs::date
                AND (rl.effective_to IS NULL OR rl.effective_to > gs::date)
              LIMIT 1) AS rate
      FROM generate_series('2024-01-01'::date, '2026-09-23'::date, '1 day') gs)
    SELECT extract(year from day)::int AS yr, min(rate), max(rate),
           count(DISTINCT rate) AS n_levels, count(*) AS n_days
    FROM d WHERE rate IS NOT NULL GROUP BY 1 ORDER BY 1
"""):
    print("  ", r)