#!/usr/bin/env python3
"""H-007: inference and trend/spuriousness diagnostics for corr@lag2."""
import json
import sys

import numpy as np
import pandas as pd
from scipy import stats

CSV = os.environ.get("H007_INPUTS", "/home/lnr/.hermes/kanban/boards/research/attachments/t_e9cfa6d6/h007_inputs_quarterly.csv")
df = pd.read_csv(CSV)
df["quarter"] = pd.PeriodIndex(df["quarter"], freq="Q")
df = df.set_index("quarter").sort_index()

# precise alignment check (CSV is rounded to 6 dp)
al = pd.DataFrame({"a": df.esc_almon_q_pct_change, "l": df.esc_lag2})
maxd = (al.a.shift(2) - al.l).abs().max()
print("max |esc_lag2[t] - esc_almon[t-2]| = %.3e" % maxd)

base = pd.DataFrame({"y": df.ikv_yoy_pct, "x": df.esc_lag2}).dropna()
print("\nfull overlap N=%d: %s..%s" % (len(base), base.index.min(), base.index.max()))
for name, b in (("full N=12", base), ("window 2023Q4..2026Q2 (N=11)", base[base.index >= pd.Period("2023Q4", "Q")])):
    n = len(b)
    r = float(np.corrcoef(b.x, b.y)[0, 1])
    t = r * np.sqrt((n - 2) / (1 - r ** 2))
    p = float(2 * stats.t.sf(abs(t), n - 2))
    zr = np.arctanh(r)
    se = 1 / np.sqrt(n - 3)
    ci = (float(np.tanh(zr - 1.96 * se)), float(np.tanh(zr + 1.96 * se)))
    sp = float(stats.spearmanr(b.x, b.y).statistic)
    print("  %-30s r=%+.4f  p=%.3f  CI95=[%+.3f, %+.3f]  spearman=%+.4f  R2=%.3f" % (name, r, p, ci[0], ci[1], sp, r * r))
    print("    Δ vs 0.60 = %+.4f (%+.1f%%)" % (r - 0.60, (r - 0.60) / 0.60 * 100))

print("\n=== spuriousness diagnostics (full N=12) ===")
b = base.copy()
b["t"] = np.arange(len(b), dtype=float)
# residuals from a linear time trend
for col in ("x", "y"):
    sl, ic, *_ = stats.linregress(b.t, b[col])
    b[col + "_detr"] = b[col] - (ic + sl * b.t)
    print("  trend %s: slope=%+.3f per quarter (%.1f%% of sd), p=%.3f" % (
        col, sl, 100 * abs(sl) * b.t.max() / b[col].std(), stats.linregress(b.t, b[col]).pvalue))
r_detr = float(np.corrcoef(b.x_detr, b.y_detr)[0, 1])
print("  corr of detrended series = %+.4f (was %+.4f)" % (r_detr, float(np.corrcoef(b.x, b.y)[0, 1])))
dx, dy = b.x.diff().dropna(), b.y.diff().dropna()
r_diff = float(np.corrcoef(dx, dy)[0, 1])
n_diff = len(dx)
t_d = r_diff * np.sqrt((n_diff - 2) / (1 - r_diff ** 2))
print("  corr of first differences = %+.4f (N=%d, p=%.3f)" % (r_diff, n_diff, float(2 * stats.t.sf(abs(t_d), n_diff - 2))))

# multiple regression y ~ x + t
X = np.column_stack([np.ones(len(b)), b.x.values, b.t.values])
coef, res, *_ = np.linalg.lstsq(X, b.y.values, rcond=None)
resid = b.y.values - X @ coef
s2 = resid @ resid / (len(b) - 3)
cov = s2 * np.linalg.inv(X.T @ X)
se = np.sqrt(np.diag(cov))
tvals = coef / se
pv = [float(2 * stats.t.sf(abs(tv), len(b) - 3)) for tv in tvals]
print("  y = a + b*x + c*t :  b(x)=%+.4f (se %.4f, p=%.3f)  c(t)=%+.3f (se %.3f, p=%.3f)" % (
    coef[1], se[1], pv[1], coef[2], se[2], pv[2]))

# within-subsample (demeaned by half) correlation
half = len(b) // 2
b["g"] = (b.index >= b.index[half]).astype(int)
xd = b.x - b.groupby("g").x.transform("mean")
yd = b.y - b.groupby("g").y.transform("mean")
r_within = float(np.corrcoef(xd, yd)[0, 1])
print("  within-half (group-demeaned) corr = %+.4f" % r_within)
print("  group means: x %.2f -> %.2f ; y %.2f -> %.2f" % (
    b.groupby("g").x.mean()[0], b.groupby("g").x.mean()[1],
    b.groupby("g").y.mean()[0], b.groupby("g").y.mean()[1]))

print("\n=== bootstrap 95%% CI of corr@lag2 (block bootstrap, 5000 draws, N=12) ===")
rng = np.random.default_rng(20261028)
rs = []
for _ in range(5000):
    i = rng.integers(0, len(b), len(b))
    xs, ys = b.x.values[i], b.y.values[i]
    if xs.std() == 0:
        continue
    rs.append(float(np.corrcoef(xs, ys)[0, 1]))
rs = np.array(rs)
print("  mean=%+.3f  CI2.5=%.3f CI97.5=%.3f  share r>0.7 = %.3f  share r<0 = %.3f" % (
    rs.mean(), np.percentile(rs, 2.5), np.percentile(rs, 97.5), (rs > 0.7).mean(), (rs < 0).mean()))

print("\n=== per-quarter table (full overlap) ===")
print(base.assign(quarter=[str(i) for i in base.index]).to_string(index=False))
json.dump({"max_align_diff": float(maxd), "corr_full": float(np.corrcoef(base.x, base.y)[0, 1])},
          open("h007_stats_extra.json", "w"), indent=2)
