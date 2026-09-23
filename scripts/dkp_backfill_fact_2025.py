#!/usr/bin/env python3
"""Тест вьюхи v_forecast_error: подставляем факт-2025 (инфляция, ставка, ВВП).

Факт-2025 из среднесрочного прогноза 24.07.2026 (колонка «факт»):
inflation_dec 5,6; inflation_avg 8,7; key_rate_avg 19,2; gdp_yoy 1,0.
Это витринный тест: as_of = 2026-07-24 (дата публикации прогноза).
"""
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from db_tunnel import execute, query  # noqa: E402

# load_run для факта (dataset 10, dkp-forecast)
if not query("SELECT count(*) FROM v2.load_run WHERE run_id=58"):
    execute(
        "INSERT INTO v2.load_run (dataset_id, loaded_at, source_file, "
        "file_sha256, parser_version, status, rows_parsed, rows_inserted, notes) "
        "VALUES (10, now(), 'macroeconomist/raw/forecast_260724.txt', "
        "'82ebf32-fact', 'dkp_fact_v1', 'verified', 4, 4, "
        "'факт-2025 из колонки «факт» прогноза 24.07.2026')")

FACTS = [
    ("inflation_dec", 2025, 5.6, "pct_yoy"),
    ("inflation_avg", 2025, 8.7, "pct_yoy"),
    ("key_rate_avg", 2025, 19.2, "pct_avg"),
    ("gdp_yoy", 2025, 1.0, "pct_yoy"),
    ("gdp_q4q4", 2025, 1.0, "pct_yoy"),
    ("cons_total", 2025, 2.9, "pct_yoy"),
    ("cons_hh", 2025, 3.6, "pct_yoy"),
    ("gross_saving", 2025, -4.9, "pct_yoy"),
    ("gross_capital", 2025, -0.4, "pct_yoy"),
    ("m2n", 2025, 10.6, "pct_yoy"),
    ("claims_total", 2025, 9.5, "pct_yoy"),
    ("claims_firms", 2025, 11.9, "pct_yoy"),
    ("claims_hh", 2025, 2.8, "pct_yoy"),
    ("claims_mortgage", 2025, 7.8, "pct_yoy"),
    ("ca_balance", 2025, 39, "usd_bn"),
    ("trade_balance", 2025, 113, "usd_bn"),
    ("export_bp", 2025, 420, "usd_bn"),
    ("import_bp", 2025, 306, "usd_bn"),
    ("services_balance", 2025, -49, "usd_bn"),
    ("income_balance", 2025, -26, "usd_bn"),
    ("oil_price_tax", 2025, 56, "usd_barrel"),
]

n = query("SELECT count(*) FROM dkp.forecast_realized")[0][0]
if n == 0:
    for series, year, value, unit in FACTS:
        execute(
            "INSERT INTO dkp.forecast_realized (series_code, period_year, "
            "value_point, unit_code, as_of, source_id) "
            "VALUES (%s, %s, %s, %s, %s, 2)",
            (series, year, value, unit, "2026-07-24"))
    print("inserted facts:", len(FACTS))
else:
    print("facts already:", n)

print("== v_forecast_error (оценка диапазона и точек для 2025)")
for r in query(
        "SELECT series_code, forecast_point, actual, err_point, hit_range "
        "FROM dkp.v_forecast_error "
        "WHERE horizon_year=2025 AND scenario='base' ORDER BY series_code"):
    print("  ", r)