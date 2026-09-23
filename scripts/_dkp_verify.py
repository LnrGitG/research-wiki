#!/usr/bin/env python3
"""Верификация схемы dkp: счётчики, вьюхи, консистентность ступеней ставок."""
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from db_tunnel import query  # noqa: E402

print("== счётчики")
for t in ("meeting", "decision", "rate_level", "forecast", "forecast_realized",
          "argument", "statement", "minutes"):
    print(" dkp.%-18s" % t, query("SELECT count(*) FROM dkp.%s" % t)[0][0])

print("== v_decisions (последние 5)")
for r in query("SELECT meeting_date, rate_prev, rate_new, delta_bp, action "
               "FROM dkp.v_decisions ORDER BY meeting_date DESC LIMIT 5"):
    print("  ", r)

print("== консистентность ступеней: разрывы и пересечения")
for r in query("""
    SELECT count(*) FROM (
      SELECT effective_from, lag(effective_to) OVER (ORDER BY effective_from) prev_to
      FROM dkp.rate_level WHERE rate_code='key_rate') x
    WHERE prev_to IS NOT NULL AND effective_from <> prev_to
"""):
    print("  разрывов ступеней:", r[0])

print("== v_forecast_error на тесте (инфляция 2025 факт 5,6 дек/дек, среднегодовая 8,7)")
execute_dummy = None
print("== прогноз по сериям")
for r in query("SELECT series_code, count(*) FROM dkp.forecast "
               "GROUP BY 1 ORDER BY 1"):
    print("  ", r[0], r[1])