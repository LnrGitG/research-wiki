#!/usr/bin/env python3
"""FAVAR-MIDAS MVP v2: quarterly net-DDU-flow (Dom.RF declarations delta)
explained by weekly Wordstat demand factors via exponential Almon polynomial.
Clean functional version. OOS = expanding window, 1-step-ahead with known lag.
"""
import csv, sqlite3, math
import numpy as np
from scipy.optimize import minimize

BASE = '/home/lnr/research-wiki'

# ---------- target ----------
con = sqlite3.connect(f'{BASE}/data/rosstat_construction.db')
rows = con.execute("""SELECT date, SUM(value) FROM domrf_indicators
 WHERE indicator_name LIKE 'Количество действующих договоров участия в долевом строительстве согласно%'
 GROUP BY date ORDER BY date""").fetchall()
months = sorted(d[:7] for d, _ in rows)
stock = {d[:7]: v for d, v in rows}
qy = {}
for i in range(1, len(months)):
    ym = months[i]
    q = f"{ym[:4]}Q{(int(ym[5:7])-1)//3+1}"
    qy[q] = qy.get(q, 0.0) + (stock[ym] - stock[months[i-1]])

# ---------- weekly regressors (z-scored full-sample) ----------
wrows = list(csv.DictReader(open(f'{BASE}/data/wordstat_demand_indices_weekly.csv')))
COLS = ['A_invest', 'B_rent', 'C_panic', 'rii_B']
XW = {}
for col in COLS:
    vals = np.array([float(r[col]) for r in wrows])
    mu, sd = vals.mean(), vals.std()
    XW[col] = {r['date']: (float(r[col]) - mu) / sd for r in wrows}

def wk2q(d): return f"{d[:4]}Q{(int(d[5:7])-1)//3+1}"
wk_by_q = {}
for d in sorted(next(iter(XW.values()))):
    wk_by_q.setdefault(wk2q(d), []).append(d)

K = 12
def xvec(col, q):
    ds = wk_by_q.get(q, [])[-K:]
    v = np.array([XW[col][d] for d in ds])
    if len(v) == 0: return None
    if len(v) < K:
        v = np.concatenate([np.full(K - len(v), v[0]), v])
    return v

def almon(th1, th2, K=K):
    k = np.arange(K)
    e = np.exp(np.clip(th1 * k + th2 * k**2, -500, 500))
    return e / e.sum()

def design(quarters_list, th1, th2, xcols):
    w = almon(th1, th2)
    cols = []
    for c in xcols:
        M = np.stack([xvec(c, q) for q in quarters_list])
        cols.append(M @ w)
    return np.column_stack(cols)

def fit_midas(qs, y, ylag, xcols):
    mask = ~np.isnan(ylag)
    qs_m, y_m, yl_m = [q for q, m in zip(qs, mask) if m], y[mask], ylag[mask]
    def sse(p):
        th1, th2, a, b = p[0], p[1], p[2], p[3]
        g = p[4:]
        X = design(qs_m, th1, th2, xcols)
        r = y_m - (a + b * yl_m + X @ g)
        return float(r @ r)
    best = None
    for t1 in (-3, 0, 3):
        for t2 in (-1.5, 0, 1.5):
            res = minimize(sse, [t1, t2, 0, 0.8] + [0.0]*len(xcols),
                           method='Nelder-Mead',
                           options={'maxiter': 3000, 'fatol': 1e-1})
            if best is None or res.fun < best.fun: best = res
    th1, th2, a, b, g = best.x[0], best.x[1], best.x[2], best.x[3], best.x[4:]
    yhat_full = a + b * ylag + design(qs, th1, th2, xcols) @ g
    ss_res = np.nansum((y - yhat_full)**2)
    ss_tot = np.nansum((y - np.nanmean(y))**2)
    return dict(yhat=yhat_full, r2=1 - ss_res/ss_tot,
                params=(a, b, g, th1, th2), weights=almon(th1, th2))

def ar_fit_fit(y):
    yl = np.roll(y, 1); yl[0] = np.nan
    m = ~np.isnan(yl)
    A = np.column_stack([np.ones(m.sum()), yl[m]])
    coef, *_ = np.linalg.lstsq(A, y[m], rcond=None)
    yhat = np.full(len(y), np.nan)
    yhat[1:] = coef[0] + coef[1]*yl[1:]
    ss_res = np.nansum((y-yhat)**2); ss_tot = np.nansum((y-np.nanmean(y))**2)
    return coef, yhat, 1 - ss_res/ss_tot

# ---------- run ----------
quarters = sorted(q for q in qy if q >= '2021Q2' and wk_by_q.get(q))
y = np.array([qy[q] for q in quarters])
print(f"Sample: {quarters[0]}..{quarters[-1]} (n={len(quarters)})")
print(f"Net DDU flow/quarter: mean={np.nanmean(y):,.0f}  min={np.nanmin(y):,.0f} "
      f"({quarters[int(np.nanargmin(y))]})  max={np.nanmax(y):,.0f} ({quarters[int(np.nanargmax(y))]})")

SPEC = {'AR(1)': [],
        'AR+A': ['A_invest'], 'AR+B': ['B_rent'], 'AR+C': ['C_panic'],
        'AR+B+C': ['B_rent', 'C_panic']}

# ---- in-sample ----
ylag = np.roll(y, 1); ylag[0] = np.nan
coef_ar, ar_hat, r2_ar = ar_fit_fit(y)
print(f"\n=== In-sample ===\n{'AR(1)':10s} R2={r2_ar:.3f}  coef={coef_ar.round(3)}")
fits = {}
for name, xc in SPEC.items():
    if not xc: continue
    f = fit_midas(quarters, y, ylag, xc)
    fits[name] = f
    a, b, g, t1, t2 = f['params']
    print(f"{name:10s} R2={f['r2']:.3f}  beta_AR={b:+.2f} gamma={np.round(g,2)} theta=({t1:.2f},{t2:.2f})")
    print(f"{'':10s} weights new->old: {' '.join(f'{v:.3f}' for v in f['weights'][::-1])}")

# ---- OOS expanding window, last H quarters ----
H = 6
oos = {n: [] for n in SPEC}; acts = []
for i in range(len(quarters)-H, len(quarters)):
    qs_tr, y_tr = quarters[:i], y[:i].copy()
    c_ar, _, _ = ar_fit_fit(y_tr)
    pred_ar = c_ar[0] + c_ar[1]*y[i-1]
    oos['AR(1)'].append(pred_ar - y[i]); acts.append(y[i])
    for name, xc in SPEC.items():
        if not xc: continue
        ylag_tr = np.roll(y_tr, 1); ylag_tr[0] = np.nan
        f = fit_midas(qs_tr, y_tr, ylag_tr, xc)
        a, b, g, t1, t2 = f['params']
        pred = a + b*y[i-1] + almon(t1, t2) @ (np.stack([xvec(c, quarters[i]) for c in xc]).T @ g) \
               if False else a + b*y[i-1] + sum(almon(t1,t2) @ xvec(c, quarters[i]) * gg for c, gg in zip(xc, g))
        oos[name].append(pred - y[i])

print(f"\n=== OOS RMSE / MAE (last {H}q, 1-step ahead) ===")
base = math.sqrt(np.mean(np.array(oos['AR(1)'])**2))
for name in SPEC:
    e = np.array(oos[name])
    rm = math.sqrt(np.mean(e**2)); ma = np.mean(np.abs(e))
    print(f"{name:10s} RMSE={rm:>9,.0f} rel={rm/base:+.2f}  MAE={ma:>9,.0f}")
print('actuals:', [f'{v/1000:.0f}k' for v in acts])

# ---- save dataset ----
with open(f'{BASE}/data/ddu_flow_quarterly_with_weekly_x.csv', 'w', newline='') as fo:
    wr = csv.writer(fo)
    head = ['quarter','ddu_net_flow','ar_hat'] + [f'fit_{n}' for n in fits]
    wr.writerow(head)
    for j, q in enumerate(quarters):
        wr.writerow([q, int(y[j]), int(ar_hat[j])] + [int(fits[n]['yhat'][j]) for n in fits])
print("\nSaved data/ddu_flow_quarterly_with_weekly_x.csv")
