#!/usr/bin/env python3
"""H-007: robustness of the regressor transform + diagnosis of the -95.89 value."""
import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import query  # noqa: E402

CSV = os.environ.get("H007_INPUTS", "/home/lnr/.hermes/kanban/boards/research/attachments/t_e9cfa6d6/h007_inputs_quarterly.csv")
df = pd.read_csv(CSV)
df["quarter"] = pd.PeriodIndex(df["quarter"], freq="Q")
df = df.set_index("quarter").sort_index()

rows = query("""
SELECT o.period_start, r.name_ru, o.value
FROM data.observation o JOIN catalog.metric m USING(metric_id)
JOIN catalog.region r ON r.region_id=o.region_id
WHERE m.metric_code='cbr_pf_sum_fo_m' ORDER BY 1""")
fo = pd.DataFrame(rows, columns=["d", "reg", "v"])
fo["d"] = pd.to_datetime(fo["d"])
fo["v"] = pd.to_numeric(fo["v"], errors="coerce")
stock = fo.groupby("d").v.sum().sort_index()
idx = pd.PeriodIndex(stock.index, freq="M") - 1
s = pd.Series(stock.values, index=idx).sort_index()
d = s.diff()

print("=== monthly inflow Δ (месяц покрытия), 2025-06..2026-09, млн руб ===")
for m, v in d.tail(16).items():
    yoy_roll = (d.rolling(3).sum() / d.rolling(3).sum().shift(12) - 1) * 100
    print("  %s  Δ=%12.1f   rolling3yoy=%s" % (m, v, ("%8.2f" % yoy_roll[m]) if yoy_roll[m] == yoy_roll[m] else "   n/a"))

print("\n=== quarterly inflow & yoy (from CSV) ===")
print(df[["pf_inflow_q_mln_rub", "pf_inflow_q_yoy_pct", "esc_almon_q_pct_change"]].tail(8).to_string())


def corr(x, y, a, b):
    t = pd.DataFrame({"y": y, "x": x}).dropna()
    t = t[(t.index >= pd.Period(a, "Q")) & (t.index <= pd.Period(b, "Q"))]
    if len(t) < 3:
        return len(t), float("nan")
    return len(t), float(np.corrcoef(t.x, t.y)[0, 1])


ikv = df["ikv_yoy_pct"]
specs = {
    "A almon-monthly (протокол)": df["esc_almon_q_pct_change"],
    "B квартальный yoy притока": df["pf_inflow_q_yoy_pct"],
    "C уровень притока, трлн": df["pf_inflow_q_mln_rub"] / 1e6,
    "D остаток ПФК, yoy %": (df["pf_stock_end_mln_rub"] / df["pf_stock_end_mln_rub"].shift(4) - 1) * 100,
}
print("\n=== corr @ lag2/lag3 по спецификациям регрессора (окно 2023Q4..2026Q2) ===")
print("%-32s %-22s %-22s" % ("spec", "lag2 (N, corr)", "lag3 (N, corr)"))
for name, x in specs.items():
    n2, r2 = corr(x.shift(2), ikv, "2023Q4", "2026Q2")
    n3, r3 = corr(x.shift(3), ikv, "2023Q4", "2026Q2")
    print("%-32s N=%2d corr=%+.4f      N=%2d corr=%+.4f" % (name, n2, r2, n3, r3))

print("\n=== full overlap (no window cut) ===")
for name, x in specs.items():
    n2, r2 = corr(x.shift(2), ikv, "1900Q1", "2100Q1")
    print("%-32s N=%2d corr=%+.4f" % (name, n2, r2))

print("\n=== esc_lag2 values used by the two competing protocols ===")
print("clean almon lag2:",
      {str(k): round(float(v), 2) for k, v in df["esc_lag2"].tail(5).items() if v == v})
print("quarterly yoy lag2:",
      {str(k): round(float(v), 2) for k, v in df["pf_inflow_q_yoy_pct"].shift(2).tail(5).items()
       if v == v})

# partial-window artefact at the start of the almon series
print("\n=== граничный артефакт: первые месяцы ряда rolling3yoy ===")
r3 = d.rolling(3).sum() / d.rolling(3).sum().shift(12) - 1
first = r3.dropna().head(4)
for m, v in first.items():
    print("  %s  %+.2f%%  (в окне %d месяца)" % (m, v * 100, min(3, (m.ordinal - pd.Period('2022-01', 'M').ordinal) + 1)))
print("=> первое полное значение quarter 2023Q2; 2023Q1 собран из одного месяца (март).")
