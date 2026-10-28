#!/usr/bin/env python3
"""Sensitivity: reconstruct the 'dirty' escrow series (double counting) and see whether
the old corr +0.598 / +0.572 replicate; also AR(1) with the full ikv history."""
import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import query  # noqa: E402

WS = os.environ.get("HERMES_KANBAN_WORKSPACE", ".")
CSV = os.environ.get("H007_INPUTS", "/home/lnr/.hermes/kanban/boards/research/attachments/t_e9cfa6d6/h007_inputs_quarterly.csv")

df = pd.read_csv(CSV)
df["quarter"] = pd.PeriodIndex(df["quarter"], freq="Q")
df = df.set_index("quarter").sort_index()


def almon_q(m_series, decay=0.5, n_lag=6):
    d = m_series.to_dict()
    out = {}
    for t in m_series.index:
        num = den = 0.0
        for k in range(n_lag):
            v = d.get(t - k)
            if v is None or (isinstance(v, float) and np.isnan(v)):
                continue
            w = decay ** k
            num += w * float(v)
            den += w
        out[t] = num / den if den > 0 else np.nan
    ms = pd.Series(out)
    q = ms.groupby(pd.PeriodIndex(ms.index, freq="Q")).mean()
    q.index = pd.PeriodIndex(q.index, freq="Q")
    return q


def build(monthly_stock):
    idx = pd.PeriodIndex(monthly_stock.index, freq="M") - 1
    s = pd.Series(monthly_stock.values, index=idx).sort_index()
    d = s.diff()
    yoy_m = d.rolling(3).sum().pct_change(12) * 100.0
    return almon_q(yoy_m)


print("=== meta of cbr_pf metrics ===")
for r in query("SELECT metric_code FROM catalog.metric WHERE metric_code LIKE 'cbr_pf%' ORDER BY 1"):
    print(" ", r[0])

# clean: 8 FO
rows = query("""
SELECT o.period_start, r.name_ru, o.value
FROM data.observation o JOIN catalog.metric m USING(metric_id)
JOIN catalog.region r ON r.region_id=o.region_id
WHERE m.metric_code='cbr_pf_sum_fo_m' ORDER BY 1""")
fo = pd.DataFrame(rows, columns=["d", "reg", "v"])
fo["d"] = pd.to_datetime(fo["d"]); fo["v"] = pd.to_numeric(fo["v"], errors="coerce")
clean_m = fo.groupby("d").v.sum().sort_index()

# regions (if present in core)
res = {}
try:
    rows2 = query("""
    SELECT o.period_start, r.name_ru, o.value
    FROM data.observation o JOIN catalog.metric m USING(metric_id)
    JOIN catalog.region r ON r.region_id=o.region_id
    WHERE m.metric_code='cbr_pf_debt_reg_m' ORDER BY 1""")
    rg = pd.DataFrame(rows2, columns=["d", "reg", "v"])
    rg["d"] = pd.to_datetime(rg["d"]); rg["v"] = pd.to_numeric(rg["v"], errors="coerce")
    print("\ncbr_pf_debt_reg_m: rows=%d months=%d regions=%d" % (len(rg), rg.d.nunique(), rg.reg.nunique()))
    print("sample region names:", sorted(rg.reg.unique())[:12])
    # which rows look like aggregates
    agg_mask = rg.reg.str.contains("ФО|Итого|РФ", regex=True, na=False)
    print("aggregate-like rows:", sorted(rg.reg[agg_mask].unique())[:15])
    res["reg"] = rg
except Exception as e:
    print("regions query failed:", e)

clean_q = build(clean_m)
clean_lag2 = clean_q.shift(2)

ik = df["ikv_yoy_pct"]


def corr_window(x, y, a="2023Q4", b="2026Q2"):
    s = pd.DataFrame({"y": y, "x": x}).dropna()
    s = s[(s.index >= pd.Period(a, "Q")) & (s.index <= pd.Period(b, "Q"))]
    return len(s), float(np.corrcoef(s.x, s.y)[0, 1])


print("\n=== clean series, corr by lag (window 2023Q4..2026Q2) ===")
for k in range(0, 5):
    n, r = corr_window(clean_q.shift(k), ik)
    print("  k=%d N=%2d corr=%+.4f" % (k, n, r))

# dirty variants
variants = {"clean_8FO": clean_m}
if "reg" in res:
    rg = res["reg"]
    regs_only = rg[~rg.reg.str.contains("ФО|Итого|РФ", regex=True, na=False)]
    print("\nregions-only rows: %d (months %d)" % (len(regs_only), regs_only.d.nunique()))
    variants["regions_only"] = regs_only.groupby("d").v.sum().sort_index()
    # dirty = FO aggregates + regions (FO rows counted twice if regions include them)
    allrows = rg.groupby("d").v.sum().sort_index()
    variants["reg_table_total"] = allrows
    joined = pd.concat([clean_m.rename("fo"), allrows.rename("allr")], axis=1)
    print("\nlevel ratio allrows/fo (describe):")
    print((joined.allr / joined.fo).describe().to_string())

print("\n=== level series (end of quarter), last 6 ===")
for name, m in variants.items():
    q = pd.Series(m.values, index=(pd.PeriodIndex(m.index, freq="M") - 1)).groupby(
        lambda i: i.asfreq("Q")).last()
    print(" ", name, {str(k): round(float(v) / 1e6, 2) for k, v in q.tail(6).items()}, "трлн руб.")

print("\n=== corr@lag2 by variant (window 2023Q4..2026Q2 and full overlap) ===")
for name, m in variants.items():
    q = build(m)
    l2 = q.shift(2)
    n1, r1 = corr_window(l2, ik, "2023Q4", "2026Q2")
    s = pd.DataFrame({"y": ik, "x": l2}).dropna()
    r2 = float(np.corrcoef(s.x, s.y)[0, 1])
    lag2_q3 = l2.get(pd.Period("2026Q3", "Q"))
    print("  %-16s window N=%2d corr=%+.4f | full N=%2d corr=%+.4f | esc_lag2@2026Q3=%s" % (
        name, n1, r1, len(s), r2,
        ("%.2f" % lag2_q3) if lag2_q3 == lag2_q3 else "n/a"))

# AR(1) with the FULL ikv history (2020Q1+ from core)
rows3 = query("""
SELECT o.period_start, o.value FROM data.observation o
JOIN catalog.metric m USING(metric_id)
WHERE m.metric_code='ikv_rf_q_yoy' ORDER BY 1""")
ikv_full = pd.DataFrame(rows3, columns=["d", "v"])
ikv_full["d"] = pd.to_datetime(ikv_full["d"])
ikv_full["q"] = ikv_full.d.dt.to_period("Q")
ikv_full = ikv_full.groupby("q").v.mean().sort_index().astype(float)

print("\n=== OOS: bridge on clean series vs AR(1) (full ikv history 2020Q1+) ===")
full = pd.DataFrame({"y": ikv_full})
full["x"] = clean_lag2.reindex(full.index)
full["y_l1"] = full.y.shift(1)
recs = []
for t in full.index:
    if t < pd.Period("2024Q1", "Q"):
        continue
    if pd.isna(full.loc[t, "x"]) or pd.isna(full.loc[t, "y"]):
        continue
    tr = full.loc[full.index < t]
    trb = tr.dropna(subset=["x", "y"])
    tra = tr.dropna(subset=["y_l1", "y"])
    if len(trb) < 4:
        continue
    A = np.column_stack([np.ones(len(tra)), tra.y_l1.values])
    ba = np.linalg.lstsq(A, tra.y.values, rcond=None)[0]
    ar = float(ba[0] + ba[1] * full.loc[t, "y_l1"]) if not pd.isna(full.loc[t, "y_l1"]) else np.nan
    B = np.column_stack([np.ones(len(trb)), trb.x.values])
    bb = np.linalg.lstsq(B, trb.y.values, rcond=None)[0]
    br = float(bb[0] + bb[1] * full.loc[t, "x"])
    recs.append({"q": str(t), "fact": float(full.loc[t, "y"]), "ar": ar, "bridge": br,
                 "n_tr_ar": len(tra), "n_tr_br": len(trb)})
oos = pd.DataFrame(recs)
print(oos.to_string(index=False))
for c in ("ar", "bridge"):
    v = oos.dropna(subset=[c])
    print("%s: N=%d RMSE=%.3f MAE=%.3f" % (c, len(v), float(np.sqrt(np.mean((v[c] - v.fact) ** 2))),
                                           float(np.mean(np.abs(v[c] - v.fact)))))
w = oos[oos.q.isin(["2025Q4", "2026Q1", "2026Q2"])]
for c in ("ar", "bridge"):
    print("  protocol window 25Q4-26Q2 %s RMSE=%.3f" % (c, float(np.sqrt(np.mean((w[c] - w.fact) ** 2)))))

# final model coefficients on all clean data
trb = full.dropna(subset=["x", "y"])
B = np.column_stack([np.ones(len(trb)), trb.x.values])
bb = np.linalg.lstsq(B, trb.y.values, rcond=None)[0]
resid = trb.y.values - B @ bb
print("\nfinal bridge: ikv = %.4f + %.4f * esc_lag2 ; N=%d ; resid sd=%.2f" % (
    bb[0], bb[1], len(trb), float(resid.std(ddof=2))))
print("esc_lag2 range: %.2f .. %.2f ; ikv range %.1f .. %.1f" % (
    trb.x.min(), trb.x.max(), trb.y.min(), trb.y.max()))
print("2026Q3 point: x=%.2f -> y=%.2f" % (
    clean_lag2.get(pd.Period("2026Q3", "Q")),
    bb[0] + bb[1] * clean_lag2.get(pd.Period("2026Q3", "Q"))))
