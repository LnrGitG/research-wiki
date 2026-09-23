#!/usr/bin/env python3
"""Загрузка среднесрочного прогноза к решению 24.07.2026 (dkp.forecast).

Источник: raw/forecast_260724.txt в ~/macroeconomist (извлечён и закоммичен
82ebf32). Диапазоны «a–b» -> low/high; точки -> value_point.
"""
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from db_tunnel import execute, query  # noqa: E402

MEETING_DATE = "2026-07-24"
RUN_LABEL = "dkp_forecast_20260724"


def main() -> None:
    rows = query(
        "SELECT meeting_id FROM dkp.meeting WHERE meeting_date=%s",
        (MEETING_DATE,))
    if not rows:
        raise RuntimeError("нет заседания %s" % MEETING_DATE)
    mid = rows[0][0]

    if query("SELECT count(*) FROM dkp.forecast WHERE meeting_id=%s", (mid,))[0][0]:
        print("SKIP: forecast для %s уже загружен" % MEETING_DATE)
        return

    # 1) load_run для происхождения (dataset_id 10 = dkp-forecast)
    execute(
        "INSERT INTO v2.load_run (dataset_id, loaded_at, source_file, "
        "file_sha256, parser_version, status, rows_parsed, rows_inserted, notes) "
        "VALUES (10, now(), 'macroeconomist/raw/forecast_260724.txt', "
        "'82ebf32-source', 'dkp_forecast_v1', 'verified', 68, 68, "
        "'среднесрочный прогноз к решению 24.07.2026')")
    run_id = query("SELECT max(run_id) FROM v2.load_run")[0][0]

    # 2) серии: (series_code, unit, {(year): (low, high, point)})
    def rng(low, high):
        return (low, high, None)

    def pt(x):
        return (None, None, x)

    DATA = {
        "inflation_dec": ("pct_yoy", {2025: pt(5.6), 2026: rng(6.0, 7.0),
                                      2027: pt(4.0), 2028: pt(4.0), 2029: pt(4.0)}),
        "inflation_avg": ("pct_yoy", {2025: pt(8.7), 2026: rng(5.9, 6.2),
                                      2027: rng(4.3, 5.2), 2028: pt(4.0),
                                      2029: pt(4.0)}),
        "key_rate_avg": ("pct_avg", {2025: pt(19.2), 2026: rng(14.5, 14.6),
                                     2027: rng(10.5, 12.5), 2028: rng(8.0, 9.0),
                                     2029: rng(7.5, 8.5)}),
        "gdp_yoy": ("pct_yoy", {2025: pt(1.0), 2026: rng(0.0, 1.0),
                                2027: rng(1.5, 2.5), 2028: rng(1.5, 2.5),
                                2029: rng(1.5, 2.5)}),
        "gdp_q4q4": ("pct_yoy", {2025: pt(1.0), 2026: rng(0.0, 1.5),
                                 2027: rng(1.5, 2.5), 2028: rng(1.5, 2.5),
                                 2029: rng(1.5, 2.5)}),
        "cons_total": ("pct_yoy", {2025: pt(2.9), 2026: rng(1.5, 2.5),
                                   2027: rng(1.0, 2.0), 2028: rng(1.0, 2.0),
                                   2029: rng(1.5, 2.5)}),
        "cons_hh": ("pct_yoy", {2025: pt(3.6), 2026: rng(1.5, 2.5),
                                2027: rng(1.0, 2.0), 2028: rng(1.0, 2.0),
                                2029: rng(1.5, 2.5)}),
        "gross_saving": ("pct_yoy", {2025: pt(-4.9), 2026: rng(-3.5, -1.5),
                                     2027: rng(2.0, 4.0), 2028: rng(1.5, 3.5),
                                     2029: rng(1.0, 3.0)}),
        "gross_capital": ("pct_yoy", {2025: pt(-0.4), 2026: rng(-1.5, 0.5),
                                      2027: rng(2.0, 4.0), 2028: rng(1.5, 3.5),
                                      2029: rng(1.0, 3.0)}),
        "export_goods": ("pct_yoy", {2026: rng(0.0, 2.0), 2027: rng(0.0, 2.0),
                                     2028: rng(1.0, 3.0), 2029: rng(1.0, 3.0)}),
        "import_goods": ("pct_yoy", {2026: rng(1.0, 3.0), 2027: rng(0.0, 2.0),
                                     2028: rng(1.0, 3.0), 2029: rng(1.0, 3.0)}),
        "m2n": ("pct_yoy", {2025: pt(10.6), 2026: rng(7.0, 12.0),
                            2027: rng(6.0, 11.0), 2028: rng(7.0, 12.0),
                            2029: rng(7.0, 12.0)}),
        "claims_total": ("pct_yoy", {2025: pt(9.5), 2026: rng(6.0, 10.0),
                                     2027: rng(6.0, 11.0), 2028: rng(8.0, 13.0),
                                     2029: rng(8.0, 13.0)}),
        "claims_firms": ("pct_yoy", {2025: pt(11.9), 2026: rng(7.0, 11.0),
                                     2027: rng(7.0, 12.0), 2028: rng(8.0, 13.0),
                                     2029: rng(8.0, 13.0)}),
        "claims_hh": ("pct_yoy", {2025: pt(2.8), 2026: rng(5.0, 9.0),
                                  2027: rng(5.0, 10.0), 2028: rng(8.0, 13.0),
                                  2029: rng(8.0, 13.0)}),
        "claims_mortgage": ("pct_yoy", {2025: pt(7.8), 2026: rng(6.0, 10.0),
                                        2027: rng(7.0, 12.0), 2028: rng(10.0, 15.0),
                                        2029: rng(10.0, 15.0)}),
        # платёжный баланс, млрд долл.
        "ca_balance": ("usd_bn", {2025: pt(39), 2026: pt(48), 2027: pt(25),
                                  2028: pt(15), 2029: pt(10)}),
        "trade_balance": ("usd_bn", {2025: pt(113), 2026: pt(119), 2027: pt(99),
                                     2028: pt(92), 2029: pt(88)}),
        "export_bp": ("usd_bn", {2025: pt(420), 2026: pt(458), 2027: pt(446),
                                 2028: pt(454), 2029: pt(465)}),
        "import_bp": ("usd_bn", {2025: pt(306), 2026: pt(339), 2027: pt(347),
                                 2028: pt(362), 2029: pt(377)}),
        "services_balance": ("usd_bn", {2025: pt(-49), 2026: pt(-50),
                                        2027: pt(-51), 2028: pt(-52), 2029: pt(-52)}),
        "income_balance": ("usd_bn", {2025: pt(-26), 2026: pt(-22),
                                      2027: pt(-23), 2028: pt(-25), 2029: pt(-26)}),
        "oil_price_tax": ("usd_barrel", {2025: pt(56), 2026: pt(60),
                                         2027: pt(50), 2028: pt(50), 2029: pt(50)}),
    }

    n = 0
    for series, (unit, by_year) in DATA.items():
        for year, (low, high, point) in by_year.items():
            execute(
                "INSERT INTO dkp.forecast (meeting_id, scenario, series_code, "
                "horizon_year, value_low, value_high, value_point, unit_code, run_id) "
                "VALUES (%s, 'base', %s, %s, %s, %s, %s, %s, %s)",
                (mid, series, year, low, high, point, unit, run_id))
            n += 1

    total = query("SELECT count(*) FROM dkp.forecast")[0][0]
    print("inserted:", n, "total forecast rows:", total, "run_id:", run_id)


if __name__ == "__main__":
    main()