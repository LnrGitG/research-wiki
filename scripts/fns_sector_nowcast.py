#!/usr/bin/env python3
"""
fns_sector_nowcast.py — ФНС-сектор (ОКВЭД F) nowcast ВДС-F/ВНОК ИФО.

Методы:
  1. Годовой агрегат ФНС → квартальная интерполяция (Denton-Cholette)
  2. Bridge-модель с цементом + эскроу (Almon-взвешенные)
  3. Walk-forward OOS тест 2024Q4–2026Q1

H-008 (narrowed): секторный агрегат F + квартализация через СМР
даёт nowcast ВДС-F ИФО с RMSE < AR(1).

Источники:
  - fns_tochno_sectors.db (firms_F_{year}: line_2110 = выручка, тыс.руб)
  - rosstat_construction.db (gdp_vds_quarterly_okved, building_materials_monthly,
    cbr_escrow_monthly, construction_volume_monthly_rf)
"""

import sqlite3
import sys
from pathlib import Path

import numpy as np
import pandas as pd

# ── Paths ────────────────────────────────────────────────────────────────────
WIKI = Path("~/research-wiki").expanduser()
DB_FNS = WIKI / "data" / "fns_tochno_sectors.db"
DB_ROS = WIKI / "data" / "rosstat_construction.db"
OUT_CSV = WIKI / "data" / "fns_sector_nowcast_results.csv"

# ── 1. Load ФНС sector F aggregate (annual) ─────────────────────────────────
def load_fns_annual() -> pd.DataFrame:
    """Year → sector F total revenue (bln rub), filed & line_2110>0."""
    db = sqlite3.connect(DB_FNS)
    rows = []
    for yr in range(2021, 2026):
        total, n = db.execute(
            f"SELECT SUM(line_2110), COUNT(*) "
            f"FROM firms_F_{yr} WHERE filed=1 AND line_2110>0"
        ).fetchone()
        rows.append({"year": yr, "revenue_ths": total, "n_firms": n})
    db.close()
    df = pd.DataFrame(rows)
    df["revenue_bln"] = df["revenue_ths"] / 1e6
    df["yoy_pct"] = df["revenue_bln"].pct_change() * 100
    return df


# ── 2. Load ВДС-F IFO (quarterly target) ───────────────────────────────────
def load_vds_f_ifo() -> pd.DataFrame:
    """Quarterly ВДС section F volume index (ИФО, % к пред. году)."""
    db = sqlite3.connect(DB_ROS)
    df = pd.read_sql(
        "SELECT year, quarter, value as ifo "
        "FROM gdp_vds_quarterly_okved "
        "WHERE okved_section='Раздел F' AND series='vds_volume_index' "
        "ORDER BY year, quarter",
        db,
    )
    db.close()
    # Clean quarter labels
    df["qnum"] = df["quarter"].str.extract(r"(\d+)").astype(int)
    df["period"] = df["year"].astype(str) + "Q" + df["qnum"].astype(str)
    df["period"] = pd.PeriodIndex(df["period"], freq="Q")
    df = df.set_index("period").sort_index()
    return df[["ifo"]]


# ── 3. Load monthly HF predictors ───────────────────────────────────────────
def load_cement_monthly() -> pd.DataFrame:
    """Cement production monthly (тыс.тонн) → yoy%."""
    db = sqlite3.connect(DB_ROS)
    df = pd.read_sql(
        "SELECT year, month, value "
        "FROM building_materials_monthly "
        "WHERE product LIKE '%емент%' AND unit='тыс.т' "
        "ORDER BY year, month",
        db,
    )
    db.close()
    df["year_int"] = df["year"].fillna(0).astype(int)
    df["month_int"] = df["month"].fillna(0).astype(int)
    df = df[(df["year_int"] > 0) & (df["month_int"] > 0)].copy()
    df["period_str"] = df["year_int"].astype(str) + "-" + df["month_int"].astype(str).str.zfill(2)
    df["period"] = pd.PeriodIndex(df["period_str"], freq="M")
    df = df.set_index("period").sort_index()
    df["cement_yoy"] = df["value"].pct_change(12) * 100
    return df[["value", "cement_yoy"]]


def load_escrow_monthly() -> pd.DataFrame:
    """CBR escrow inflows monthly (aggregated РФ from regional data)."""
    db = sqlite3.connect(DB_ROS)
    df = pd.read_sql(
        "SELECT report_date, SUM(value) as escrow_total "
        "FROM cbr_escrow_monthly "
        "WHERE indicator LIKE '%поступлен%' "
        "GROUP BY report_date ORDER BY report_date",
        db,
    )
    db.close()
    df["period_str"] = df["report_date"].str[:7]
    df["period"] = pd.PeriodIndex(df["period_str"], freq="M")
    df = df.set_index("period").sort_index()
    # Escrow inflow yoy (need level → diff for flow, then yoy)
    df["escrow_yoy"] = df["escrow_total"].pct_change(12) * 100
    return df[["escrow_total", "escrow_yoy"]]


def load_smr_monthly() -> pd.DataFrame:
    """СМР volume monthly (млрд руб, yoy%)."""
    db = sqlite3.connect(DB_ROS)
    df = pd.read_sql(
        "SELECT report_year, report_month, value_bln_rub, yoy_pct "
        "FROM construction_volume_monthly_rf "
        "WHERE report_month IS NOT NULL "
        "ORDER BY report_year, report_month",
        db,
    )
    db.close()
    df["period_str"] = df["report_year"].astype(str) + "-" + df["report_month"].astype(str).str.zfill(2)
    df["period"] = pd.PeriodIndex(df["period_str"], freq="M")
    df = df.set_index("period").sort_index()
    return df[["value_bln_rub", "yoy_pct"]].rename(columns={"yoy_pct": "smr_yoy"})


# ── 4. Denton-Cholette quarterly interpolation ───────────────────────────────
def denton_cholette(
    annual: pd.Series, quarterly_indicator: pd.Series, start_year: int = 2021
) -> pd.Series:
    """
    Proportional Denton-Cholette: distribute annual totals into quarters
    using a high-frequency indicator as distribution key.

    annual: Series indexed by year, values in levels.
    quarterly_indicator: Series indexed by Period('Q'), high-freq benchmark.
    Returns: quarterly Series with same index as indicator, preserving annual sums.
    """
    # Align indicator to quarters
    if quarterly_indicator.index.freq == "M":
        qi_q = quarterly_indicator.groupby(
            pd.PeriodIndex(quarterly_indicator.index, freq="Q")
        ).mean()
    else:
        qi_q = quarterly_indicator.copy()

    result = {}
    for yr in annual.index:
        if yr < start_year:
            continue
        yr_quarters = [pd.Period(year=yr, quarter=q, freq="Q") for q in range(1, 5)]
        weights = []
        for qp in yr_quarters:
            if qp in qi_q.index:
                weights.append(qi_q.loc[qp])
            else:
                weights.append(np.nan)

        weights = pd.Series(weights, index=yr_quarters)
        if weights.isna().all():
            # Equal distribution if no indicator
            for qp in yr_quarters:
                result[qp] = annual.loc[yr] / 4
        else:
            weights = weights.fillna(weights.mean())
            wsum = weights.sum()
            for qp in yr_quarters:
                if qp in weights.index:
                    result[qp] = annual.loc[yr] * weights.loc[qp] / wsum

    return pd.Series(result).sort_index()


# ── 5. Almon-weighted quarterly aggregation ──────────────────────────────────
def almon_aggregate(
    monthly: pd.Series, decay: float = 0.5, window: int = 6
) -> pd.Series:
    """
    Exponential Almon weights → weighted rolling mean → quarterly aggregation.
    monthly: PeriodIndex('M') Series.
    Returns: PeriodIndex('Q') Series.
    """
    weights = np.array([decay**i for i in range(window)])[::-1]
    weights = weights / weights.sum()
    rolled = monthly.rolling(window, min_periods=1).apply(
        lambda x: np.dot(x, weights[-len(x):]), raw=True
    )
    # Monthly → quarterly (mean)
    q_idx = pd.PeriodIndex(rolled.index, freq="Q")
    return rolled.groupby(q_idx).mean()


# ── 6. Walk-forward OOS test ────────────────────────────────────────────────
def walk_forward_ols(
    y: pd.Series, X: pd.DataFrame, min_train: int = 8
) -> pd.DataFrame:
    """
    Expanding window OLS walk-forward.
    y: quarterly target (PeriodIndex 'Q').
    X: quarterly predictors (same index).
    Returns: DataFrame with actual, forecast, error per test period.
    """
    from numpy.linalg import lstsq

    results = []
    start = min_train
    for i in range(start, len(y)):
        y_train = y.iloc[:i]
        X_train = X.iloc[:i]
        y_test = y.iloc[i]
        X_test = X.iloc[i]

        # OLS
        Xa = np.column_stack([np.ones(len(X_train)), X_train.values])
        try:
            beta, *_ = lstsq(Xa, y_train.values, rcond=None)
        except Exception:
            continue

        x_test = np.concatenate([[1], X_test.values])
        forecast = float(x_test @ beta)
        results.append(
            {
                "period": y.index[i],
                "actual": y_test,
                "forecast": forecast,
                "error": y_test - forecast,
            }
        )

    return pd.DataFrame(results).set_index("period")


# ── 7. Main pipeline ─────────────────────────────────────────────────────────
def main():
    print("=" * 70)
    print("ФНС сектор F → nowcast ВДС-F ИФО")
    print("=" * 70)

    # Load data
    fns = load_fns_annual()
    print("\n1. ФНС годовой агрегат (ОКВЭД F, filed, revenue>0):")
    print(fns[["year", "revenue_bln", "n_firms", "yoy_pct"]].to_string(index=False))

    target = load_vds_f_ifo()
    print(f"\n2. Целевая переменная ВДС-F ИФО: {len(target)} кварталов")
    print(target.tail(10).to_string())

    cement = load_cement_monthly()
    print(f"\n3. Цемент: {len(cement)} мес. наблюдений")
    print(cement.tail(5).to_string())

    escrow = load_escrow_monthly()
    print(f"\n4. Эскроу: {len(escrow)} мес. наблюдений")
    print(escrow.tail(5).to_string())

    smr = load_smr_monthly()
    print(f"\n5. СМР: {len(smr)} мес. наблюдений")
    print(smr.tail(5).to_string())

    # ── Denton-Cholette: annual FNS → quarterly ──────────────────────────
    # Use СМР yoy as distribution key (most correlated with investment cycle)
    smr_q = smr["smr_yoy"].dropna()
    smr_q_idx = pd.PeriodIndex(smr_q.index, freq="Q")
    smr_q_agg = smr_q.groupby(smr_q_idx).mean()

    fns_annual = fns.set_index("year")["revenue_bln"]
    fns_quarterly = denton_cholette(fns_annual, smr_q_agg, start_year=2021)
    fns_q_yoy = fns_quarterly.pct_change(4) * 100  # yoy

    print(f"\n6. ФНС квартальная (Denton-Cholette via СМР): {len(fns_q_yoy.dropna())} набл.")
    print(fns_q_yoy.dropna().to_string())

    # ── Almon aggregation for HF predictors ──────────────────────────────
    cement_almon = almon_aggregate(cement["cement_yoy"].dropna(), decay=0.5, window=6)
    print(f"\n7. Цемент Almon (decay=0.5, window=6): {len(cement_almon.dropna())} кварталов")

    # ── Merge to quarterly panel ───────────────────────────────────────────
    panel = target.copy()
    panel.columns = ["target_ifo"]
    panel["fns_yoy"] = fns_q_yoy
    panel["cement_almon"] = cement_almon

    # Add escrow (lag-2 for leading properties)
    esc_almon = almon_aggregate(escrow["escrow_yoy"].dropna(), decay=0.5, window=6)
    panel["escrow_almon"] = esc_almon
    panel["escrow_lag2"] = esc_almon.shift(2)

    # AR(1) term
    panel["ar1"] = panel["target_ifo"].shift(1)

    panel = panel.dropna()
    print(f"\n8. Панель (все предикторы, без NaN): {len(panel)} кварталов")
    print(panel.head(10).to_string())
    print(f"   Период: {panel.index[0]} — {panel.index[-1]}")

    # ── Walk-forward OOS tests ────────────────────────────────────────────
    print("\n" + "=" * 70)
    print("WALK-FORWARD OOS ТЕСТЫ (expanding window, min_train=8)")
    print("=" * 70)

    y = panel["target_ifo"]
    specs = {
        "AR(1)": panel[["ar1"]],
        "FNS only": panel[["fns_yoy"]],
        "Cement only": panel[["cement_almon"]],
        "Escrow lag2 only": panel[["escrow_lag2"]],
        "AR + Cement": panel[["ar1", "cement_almon"]],
        "AR + FNS": panel[["ar1", "fns_yoy"]],
        "AR + Cement + Esc lag2": panel[["ar1", "cement_almon", "escrow_lag2"]],
        "Full (AR+Cem+Esc+FNS)": panel[["ar1", "cement_almon", "escrow_lag2", "fns_yoy"]],
    }

    results_table = []
    for name, X in specs.items():
        common = y.index.intersection(X.index)
        if len(common) < 10:
            print(f"  {name}: insufficient data ({len(common)} quarters), skip")
            continue
        res = walk_forward_ols(y.loc[common], X.loc[common], min_train=8)
        if len(res) == 0:
            continue
        rmse = np.sqrt(np.mean(res["error"] ** 2))
        mae = np.mean(np.abs(res["error"]))
        sign_hit = np.mean(np.sign(res["forecast"] - res["actual"].shift(1).reindex(res.index)) == np.sign(res["actual"] - res["actual"].shift(1).reindex(res.index)))

        results_table.append(
            {"spec": name, "n_test": len(res), "RMSE": round(rmse, 2), "MAE": round(mae, 2), "sign_hit": round(sign_hit, 2) if not np.isnan(sign_hit) else "N/A"}
        )
        print(f"  {name:30s}  n_test={len(res):2d}  RMSE={rmse:6.2f}  MAE={mae:6.2f}")

    results_df = pd.DataFrame(results_table)
    print("\n" + "=" * 70)
    print("ИТОГИ (ранжирование по RMSE):")
    print("=" * 70)
    print(results_df.sort_values("RMSE").to_string(index=False))

    # ── Save ──────────────────────────────────────────────────────────────
    panel.to_csv(OUT_CSV, encoding="utf-8")
    print(f"\nПанель сохранена: {OUT_CSV}")
    print(f"Размер: {OUT_CSV.stat().st_size / 1024:.1f} КБ")

    # ── Correlations ──────────────────────────────────────────────────────
    print("\n" + "=" * 70)
    print("ПАРНЫЕ КОРРЕЛЯЦИИ с ВДС-F ИФО (yoy):")
    print("=" * 70)
    corr_cols = [c for c in panel.columns if c != "target_ifo"]
    for c in corr_cols:
        for lag in [0, 1, 2]:
            r = panel["target_ifo"].corr(panel[c].shift(lag))
            print(f"  {c:20s}  lag={lag}:  r={r:+.3f}")


if __name__ == "__main__":
    main()