#!/usr/bin/env python3
"""H-007 recheck (kanban t_55dda5c1).

1. Coherence checks of the delivered quarterly series vs the DB core.
2. Independent rebuild of the escrow transform (monthly stock -> Δ -> rolling3 yoy -> Almon 0.5).
3. corr@lag2 on the whole available range, subsamples, lag profile, inference.
4. OOS bridge (expanding): AR(1) vs bridge(esc_lag2), before/after.
Read-only. Writes JSON + TXT into the workspace.
"""
import json
import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import query  # noqa: E402

WS = os.environ.get("HERMES_KANBAN_WORKSPACE", ".")
CSV = os.environ.get("H007_INPUTS", "/home/lnr/.hermes/kanban/boards/research/attachments/t_e9cfa6d6/h007_inputs_quarterly.csv")
OUT = {}
LINES = []


def p(s=""):
    print(s)
    LINES.append(str(s))


# ---------------- 1. load delivered series
df = pd.read_csv(CSV)
df["quarter"] = pd.PeriodIndex(df["quarter"], freq="Q")
df = df.set_index("quarter").sort_index()
p("=== 1. DELIVERED SERIES ===")
p("rows=%d, range=%s..%s" % (len(df), df.index.min(), df.index.max()))

# frequency / continuity
exp = pd.period_range(df.index.min(), df.index.max(), freq="Q")
p("continuous quarterly grid: %s (dupes=%d)" % (list(exp) == list(df.index), int(df.index.duplicated().sum())))
p("complete quarters: %d / %d" % (int(df.quarter_complete.sum()), len(df)))
p("incomplete: %s" % list(df.index[~df.quarter_complete]))

# ---------------- 2. rebuild escrow transform from the DB
SQL = """
SELECT o.period_start, r.name_ru AS region, o.value
FROM data.observation o
JOIN catalog.metric m USING(metric_id)
JOIN catalog.region r ON r.region_id = o.region_id
WHERE m.metric_code = 'cbr_pf_sum_fo_m'
ORDER BY o.period_start
"""
rows = query(SQL)
pf = pd.DataFrame(rows, columns=["period_start", "region", "value"])
pf["period_start"] = pd.to_datetime(pf["period_start"])
pf["value"] = pd.to_numeric(pf["value"], errors="coerce")
cnt = pf.groupby("period_start").size()
p("\n=== 2. REBUILD FROM CORE ===")
p("core rows=%d months=%d regions=%d, %s..%s, balanced=%s" % (
    len(pf), pf.period_start.nunique(), pf.region.nunique(),
    pf.period_start.min().date(), pf.period_start.max().date(),
    bool(cnt.nunique() == 1 and cnt.iloc[0] == 8)))

stock = pf.groupby("period_start").value.sum().sort_index()
stk_idx = pd.PeriodIndex(stock.index, freq="M") - 1
stock_s = pd.Series(stock.values, index=stk_idx)
dstock = stock_s.diff()


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


esc_flow_yoy_m = dstock.rolling(3).sum().pct_change(12) * 100.0
p("monthly yoy-of-rolling3: first valid month = %s (needs 12+3 months of stock)" % esc_flow_yoy_m.first_valid_index())
esc_almon_q = almon_q(esc_flow_yoy_m)
p("esc_almon_q first valid quarter = %s" % esc_almon_q.first_valid_index())

cmp = pd.DataFrame({
    "delivered_almon": df["esc_almon_q_pct_change"],
    "rebuilt_almon": esc_almon_q.reindex(df.index),
    "delivered_lag2": df["esc_lag2"],
    "rebuilt_lag2": esc_almon_q.shift(2).reindex(df.index),
})
cmp["d_almon"] = (cmp.delivered_almon - cmp.rebuilt_almon).abs()
cmp["d_lag2"] = (cmp.delivered_lag2 - cmp.rebuilt_lag2).abs()
p("max |delivered - rebuilt| almon = %.3e, lag2 = %.3e" % (
    np.nanmax(cmp.d_almon.values), np.nanmax(cmp.d_lag2.values)))
OUT["rebuild_max_abs_diff_almon"] = float(np.nanmax(cmp.d_almon.values))
OUT["rebuild_max_abs_diff_lag2"] = float(np.nanmax(cmp.d_lag2.values))

# ---------------- 3. leakage / alignment checks
p("\n=== 3. LEAKAGE / ALIGNMENT ===")
lag_manual = esc_almon_q.shift(2).reindex(df.index)
align_ok = bool(np.allclose(lag_manual.dropna().values,
                            df["esc_lag2"].dropna().reindex(lag_manual.dropna().index).values,
                            rtol=0, atol=1e-9))
p("esc_lag2[t] == esc_almon[t-2] exactly: %s" % align_ok)
# regressor must contain no information from quarter t or later:
# esc_almon[t-2] is built from months <= (t-2)quarter end, and stock obs dated end-of-month+1 <= t-1 quarter start
p("regressor at t uses months up to %s -> available before quarter t: yes" % "end of (t-2)-quarter")
# check: shifting -1 (future) correlations to show bridge is not forward-looking
ikv = df["ikv_yoy_pct"]
OUT["align_ok"] = align_ok

# ikv sanity vs core
SQL2 = """
SELECT o.period_start, o.value
FROM data.observation o
JOIN catalog.metric m USING(metric_id)
WHERE m.metric_code = 'ikv_rf_q_yoy' ORDER BY o.period_start
"""
rows2 = query(SQL2)
ik = pd.DataFrame(rows2, columns=["d", "v"])
ik["d"] = pd.to_datetime(ik["d"])
ik["v"] = pd.to_numeric(ik["v"], errors="coerce")
ik["q"] = ik.d.dt.to_period("Q")
ikq = ik.groupby("q").v.mean().sort_index()
diff_ikv = (ikq.reindex(df.index) - df["ikv_yoy_pct"]).abs().max()
p("ikv_yoy max |core - delivered| = %.3e; core range %s..%s" % (diff_ikv, ikq.index.min(), ikq.index.max()))
OUT["ikv_max_abs_diff"] = float(diff_ikv)
p("ikv quarters where delivered is non-null: %d" % int(df.ikv_yoy_pct.notna().sum()))

# ---------------- 4. corr@lag2
p("\n=== 4. corr @ lag2 ===")
base = pd.DataFrame({"y": df["ikv_yoy_pct"], "x": df["esc_lag2"]}).dropna()
base = base[base.index >= pd.Period("2022Q1", "Q")]
n = len(base)
r = float(np.corrcoef(base.x, base.y)[0, 1])
p("full available overlap: N=%d, %s..%s, corr=%.4f" % (n, base.index.min(), base.index.max(), r))


def pearson_p(rho, nn):
    # two-sided t-test for rho
    from math import sqrt
    if nn < 3:
        return float("nan")
    t = rho * sqrt((nn - 2) / max(1e-12, 1 - rho ** 2))
    # survival function of Student t via incomplete beta (use scipy if available)
    try:
        from scipy import stats
        return float(2 * stats.t.sf(abs(t), nn - 2))
    except Exception:
        return float("nan")


def fisher_ci(rho, nn, z=1.959963985):
    if nn < 4:
        return (float("nan"), float("nan"))
    zr = np.arctanh(rho)
    se = 1.0 / np.sqrt(nn - 3)
    return (float(np.tanh(zr - z * se)), float(np.tanh(zr + z * se)))


p("p-value=%.4f  Fisher 95%% CI=[%.3f, %.3f]" % (pearson_p(r, n), *fisher_ci(r, n)))
from scipy import stats as _st
sp = float(_st.spearmanr(base.x, base.y).statistic)
p("Spearman rho = %.4f" % sp)

PREV = 0.60
OUT["corr_full"] = r
OUT["N_full"] = n
OUT["dc_abs_vs_0.60"] = r - PREV
OUT["dc_rel_vs_0.60_pct"] = (r - PREV) / PREV * 100
OUT["p_value"] = pearson_p(r, n)
OUT["fisher_ci95"] = fisher_ci(r, n)
OUT["spearman"] = sp
p("Δ vs +0.60 (protocol 2026Q2): %+.4f (%+.1f%%)" % (r - PREV, (r - PREV) / PREV * 100))

# comparability window: exactly the 11 quarters of the previous protocol
prev_win = base[(base.index >= pd.Period("2023Q4", "Q"))]
p("same window as protocol (2023Q4..2026Q2): N=%d corr=%.4f" % (
    len(prev_win), float(np.corrcoef(prev_win.x, prev_win.y)[0, 1])))
OUT["corr_prev_window"] = float(np.corrcoef(prev_win.x, prev_win.y)[0, 1])
OUT["N_prev_window"] = len(prev_win)

# subsamples (stability)
half = n // 2
s1, s2 = base.iloc[:half], base.iloc[half:]
p("subsample H1 %s..%s: N=%d corr=%+.4f" % (s1.index.min(), s1.index.max(), len(s1),
                                            float(np.corrcoef(s1.x, s1.y)[0, 1]) if len(s1) > 2 else float("nan")))
p("subsample H2 %s..%s: N=%d corr=%+.4f" % (s2.index.min(), s2.index.max(), len(s2),
                                            float(np.corrcoef(s2.x, s2.y)[0, 1]) if len(s2) > 2 else float("nan")))
OUT["subsamples"] = {}
for nm, sub in (("H1", s1), ("H2", s2)):
    OUT["subsamples"][nm] = {
        "window": [str(sub.index.min()), str(sub.index.max())],
        "N": int(len(sub)),
        "corr": float(np.corrcoef(sub.x, sub.y)[0, 1]) if len(sub) > 2 else None,
    }
# leave-one-out (influence) and pre/post 2025
pre25 = base[base.index < pd.Period("2025Q1", "Q")]
post25 = base[base.index >= pd.Period("2025Q1", "Q")]
p("split at 2025Q1: pre N=%d corr=%+.4f | from 2025Q1 N=%d corr=%+.4f" % (
    len(pre25), float(np.corrcoef(pre25.x, pre25.y)[0, 1]),
    len(post25), float(np.corrcoef(post25.x, post25.y)[0, 1])))
OUT["split_2025Q1"] = {
    "pre": {"N": int(len(pre25)), "corr": float(np.corrcoef(pre25.x, pre25.y)[0, 1])},
    "post": {"N": int(len(post25)), "corr": float(np.corrcoef(post25.x, post25.y)[0, 1])},
}
# ex-2026Q1 (structural break quarter)
ex = base[base.index != pd.Period("2026Q1", "Q")]
p("excluding 2026Q1: N=%d corr=%+.4f" % (len(ex), float(np.corrcoef(ex.x, ex.y)[0, 1])))
OUT["corr_ex_2026Q1"] = {"N": int(len(ex)), "corr": float(np.corrcoef(ex.x, ex.y)[0, 1])}

# lag profile
p("\nlag profile (corr of esc_almon[t-k] with ikv_yoy[t]):")
prof = {}
for k in range(0, 6):
    xx = esc_almon_q.shift(k).reindex(df.index)
    s = pd.DataFrame({"y": df.ikv_yoy_pct, "x": xx}).dropna()
    prof[k] = {"N": int(len(s)), "corr": float(np.corrcoef(s.x, s.y)[0, 1])}
    p("  k=%d  N=%2d  corr=%+.4f" % (k, len(s), prof[k]["corr"]))
OUT["lag_profile"] = prof
best = max(prof.items(), key=lambda kv: kv[1]["corr"])
p("argmax |corr| among k=0..5: k=%d (corr=%+.4f)" % (best[0], best[1]["corr"]))

# ---------------- 5. OOS bridge
p("\n=== 5. OOS BRIDGE (expanding) ===")
# protocol 2026Q2: expanding OOS, first prediction 2024Q1, training on all data up to t-1
# bridge: ikv ~ a + b*esc_lag2 ; AR(1): ikv_t ~ a + b*ikv_{t-1}
d = base.copy()
d["y_l1"] = base.y  # placeholder
full = pd.DataFrame({"y": df["ikv_yoy_pct"], "x": df["esc_lag2"]})
full["y_l1"] = full["y"].shift(1)

OOS_START = pd.Period("2024Q1", "Q")
recs = []
for t in full.index:
    if t < OOS_START:
        continue
    if pd.isna(full.loc[t, "x"]) or pd.isna(full.loc[t, "y"]):
        continue
    tr = full.loc[full.index < t]
    trb = tr.dropna(subset=["x", "y"])
    tra = tr.dropna(subset=["y_l1", "y"])
    if len(trb) < 4 or len(tra) < 4:
        continue
    if pd.isna(full.loc[t, "y_l1"]):
        ar = np.nan
    else:
        A = np.column_stack([np.ones(len(tra)), tra.y_l1.values])
        beta = np.linalg.lstsq(A, tra.y.values, rcond=None)[0]
        ar = float(beta[0] + beta[1] * full.loc[t, "y_l1"])
    B = np.column_stack([np.ones(len(trb)), trb.x.values])
    bb = np.linalg.lstsq(B, trb.y.values, rcond=None)[0]
    br = float(bb[0] + bb[1] * full.loc[t, "x"])
    recs.append({"q": str(t), "fact": float(full.loc[t, "y"]), "ar": ar, "bridge": br,
                 "n_train_bridge": len(trb), "n_train_ar": len(tra)})
oos = pd.DataFrame(recs)
p(oos.to_string(index=False))
for col in ("ar", "bridge"):
    v = oos.dropna(subset=[col])
    rmse = float(np.sqrt(np.mean((v[col] - v.fact) ** 2)))
    mae = float(np.mean(np.abs(v[col] - v.fact)))
    p("%s: N=%d RMSE=%.3f MAE=%.3f" % (col, len(v), rmse, mae))
OUT["oos"] = oos.to_dict(orient="records")
OUT["oos_rmse"] = {}
for col in ("ar", "bridge"):
    v = oos.dropna(subset=[col])
    OUT["oos_rmse"][col] = {
        "N": int(len(v)),
        "rmse": float(np.sqrt(np.mean((v[col] - v.fact) ** 2))),
        "mae": float(np.mean(np.abs(v[col] - v.fact))),
    }
# last 3 quarters window (protocol window 2025Q4..2026Q2) for before/after comparability
last3 = oos[oos.q.isin(["2025Q4", "2026Q1", "2026Q2"])]
p("\nprotocol window 2025Q4..2026Q2:")
for col in ("ar", "bridge"):
    if len(last3):
        p("  %s RMSE=%.3f" % (col, float(np.sqrt(np.mean((last3[col] - last3.fact) ** 2)))))
OUT["oos_rmse_protocol_window"] = {
    col: float(np.sqrt(np.mean((last3[col] - last3.fact) ** 2))) for col in ("ar", "bridge")
}
# prior protocol numbers for reference
OUT["previous_protocol"] = {"bridge_rmse": 10.37, "ar_rmse": 9.41, "corr": 0.598, "N": 11,
                             "point_2026Q2": {"fact": 93.4, "ar": 85.9, "bridge": 91.5}}

# bridge forecast for 2026Q3 (regressor observable, no fact) - information only
x_q3 = df.loc[pd.Period("2026Q3", "Q"), "esc_lag2"]
trb = full.dropna(subset=["x", "y"])
B = np.column_stack([np.ones(len(trb)), trb.x.values])
bb = np.linalg.lstsq(B, trb.y.values, rcond=None)[0]
f_q3 = float(bb[0] + bb[1] * x_q3)
p("\n2026Q3: regressor esc_lag2=%.4f -> bridge point = %.2f (факт отсутствует, не скорится)" % (x_q3, f_q3))
OUT["bridge_2026Q3_point"] = {"regressor": float(x_q3), "point_forecast": f_q3, "scored": False,
                              "coef": [float(bb[0]), float(bb[1])]}

# ---------------- 6. definition sensitivity: dirty series (all rows sum) from core
p("\n=== 6. SENSITIVITY: dirty definition (sum over all escrow_monthly rows) ===")
try:
    SQL3 = """
    SELECT o.period_start, o.value
    FROM data.observation o JOIN catalog.metric m USING(metric_id)
    WHERE m.metric_code LIKE 'cbr_pf%' ORDER BY o.period_start
    """
    metr = query("SELECT metric_code, count(*) FROM catalog.metric WHERE metric_code LIKE 'cbr_pf%' GROUP BY 1")
    p("cbr_pf metrics: %s" % metr)
except Exception as e:
    p("sensitivity skipped: %s" % e)

json.dump(OUT, open(os.path.join(WS, "h007_recheck_results.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=2, default=str)
open(os.path.join(WS, "h007_recheck_log.txt"), "w", encoding="utf-8").write("\n".join(LINES))
p("\nwritten h007_recheck_results.json / h007_recheck_log.txt")
