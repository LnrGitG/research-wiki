#!/usr/bin/env python3
"""Этап 2: бенчмарки bridge/MIDAS для nowcasting ИКВ/ВНОК (H-007/H-008 подготовка).

Источник — ТОЛЬКО канон (`data.observation` + `catalog.metric`) через тоннель
`db_tunnel`; ни одного локального SQLite (пункт 1 аудита 16.10.2026).

Цель: yoy ИКВ РФ, квартал — метрика `ikv_rf_q_yoy` (2020Q1…2026Q2, n=26).
Регрессоры (месячные, квартальный агрегат Almon):
  esc — эскроу-приток: Δ активных ПФК, РФ-сумма по `sdkd` (Сумма действующих
        кредитных договоров, ЦБ), rolling(3).pct_change(12);
  cem — цемент: `ptvg` (Цемент (все гидравлические)), yoy;
  wag — зарплата: `snz` (среднемесячная начисленная зарплата, РФ), yoy;
  ws6 — Wordstat S6a из CSV-файла (вне канона, ряд поисковых лидов).
Схемы: AR(1), bridge, MIDAS-Almon-lite. Pseudo-OOO: expanding, тест с 2024Q1.
Метрика RMSE против AR(1).
"""
import csv
import os
import sys
from collections import defaultdict

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from db_tunnel import query  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORDSTAT = os.path.join(REPO, "data", "wordstat_weekly_b2b_invest.csv")


def canon_monthly(code, regions=None):
    """Месячный ряд канона → pd.Series с индексом PeriodIndex(M)."""
    if regions is None:
        rows = query("""SELECT o.period_start, avg(o.value) FROM data.observation o
            JOIN catalog.metric m ON m.metric_id=o.metric_id
            WHERE m.metric_code=%s GROUP BY 1 ORDER BY 1""", (code,))
    else:
        rows = query("""SELECT o.period_start, sum(o.value) FROM data.observation o
            JOIN catalog.metric m ON m.metric_id=o.metric_id
            WHERE m.metric_code=%s AND o.region_id = ANY(%s)
            GROUP BY 1 ORDER BY 1""", (code, regions))
    s = pd.Series({pd.Period(str(p), freq='M'): float(v) for p, v in rows})
    return s.sort_index()


# --- Целевая: yoy ИКВ квартал (канон) ---
rows = query("""SELECT o.period_start, o.value FROM data.observation o
    JOIN catalog.metric m ON m.metric_id=o.metric_id
    WHERE m.metric_code='ikv_rf_q_yoy' ORDER BY 1""")
y = pd.Series({pd.Period(str(p), freq='Q'): float(v) for p, v in rows}
              ).sort_index().rename('y')

# --- Эскроу: РФ-сумма по регионам, месячный приток (Δ активных ПФК), кв. yoy ---
_regs = [r[0] for r in query("SELECT DISTINCT o.region_id FROM data.observation o "
                             "JOIN catalog.metric m ON m.metric_id=o.metric_id "
                             "WHERE m.metric_code='sdkd'")]
esc = canon_monthly('sdkd', regions=_regs).asfreq('M')
esc_flow = esc.diff()
esc_yoy_m = esc_flow.rolling(3).sum().pct_change(12) * 100

# --- Цемент: мес yoy (канон `ptvg`) ---
cem = canon_monthly('ptvg').asfreq('M')
cem_yoy_m = cem.pct_change(12) * 100

# --- Зарплата: мес yoy, РФ (канон `snz`) ---
wag = canon_monthly('snz', regions=[1]).asfreq('M')
wag_yoy_m = wag.pct_change(12) * 100

# --- Wordstat S6a: недели → мес. сумма → yoy ---
if os.path.exists(WORDSTAT):
    rows = list(csv.DictReader(open(WORDSTAT, encoding='utf-8')))
    wq = defaultdict(int)
    for r in rows:
        if r['group'] == 'S6a_mach_buy':
            wq[r['date'][:7]] += int(r['count'])
    ws = pd.Series(wq).sort_index()
    ws.index = pd.PeriodIndex(ws.index, freq='M')
    ws_yoy_m = ws.sort_index().asfreq('M').pct_change(12) * 100
else:
    print('нет', WORDSTAT, '— wordstat-блок пропущен')
    ws_yoy_m = pd.Series(dtype=float)


def almon_q(m_series, decay=0.5, n_lag=6):
    s = m_series.copy()
    s.index = pd.PeriodIndex(s.index, freq='M')
    d = s.to_dict()
    out = {}
    for t in s.index:
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
    q = ms.groupby(pd.PeriodIndex(ms.index, freq='Q')).mean()
    q.index = pd.PeriodIndex(q.index, freq='Q')
    return q


X = pd.DataFrame({
    'esc': almon_q(esc_yoy_m).reindex(y.index),
    'cem': almon_q(cem_yoy_m).reindex(y.index),
    'wag': almon_q(wag_yoy_m).reindex(y.index),
    'ws6': almon_q(ws_yoy_m).reindex(y.index),
})
X['dy_l1'] = y.diff().shift(1)


def ols(Z, yy):
    b, *_ = np.linalg.lstsq(Z, yy, rcond=None)
    return b


def rmse(a, b):
    return float(np.sqrt(((a - b) ** 2).mean()))


TEST_START = pd.Period('2024Q1', 'Q')
SPECS = {
    'AR(1)': ['dy_l1'],
    'bridge_esc': ['esc'],
    'bridge_esc+cem': ['esc', 'cem'],
    'bridge_esc+cem+wag': ['esc', 'cem', 'wag'],
    'bridge_esc+ws6': ['esc', 'ws6'],
    'bridge_esc+cem+ws6': ['esc', 'cem', 'ws6'],
    'bridge_full': ['esc', 'cem', 'wag', 'ws6'],
    'AR+esc': ['dy_l1', 'esc'],
    'AR+esc+cem+ws6': ['dy_l1', 'esc', 'cem', 'ws6'],
}
print(f"=== Pseudo-OOO expanding, Δy/y ИКВ, тест с {TEST_START}; y: n={len(y)} "
      f"{y.index.min()}..{y.index.max()} ===")
for label, cols in SPECS.items():
    d = pd.concat([y, X[cols]], axis=1).dropna()
    d_te = d[d.index >= TEST_START]
    if len(d_te) < 3:
        print(f'{label}: мало теста ({len(d_te)})')
        continue
    preds = []
    for t in d_te.index:
        tr = d[d.index < t]
        if len(tr) < 6:
            continue
        Ztr = np.column_stack([np.ones(len(tr))] + [tr[c].values for c in cols])
        b = ols(Ztr, tr.y.values)
        zt = np.array([1.0] + [d.loc[t, c] for c in cols])
        preds.append((t, zt @ b))
    if not preds:
        continue
    idx = [p[0] for p in preds]
    pv = np.array([p[1] for p in preds])
    act = y.reindex(idx).values
    r = rmse(act, pv)
    d_ar = pd.concat([y, X['dy_l1']], axis=1).dropna()
    ar_preds = []
    for t in idx:
        tr = d_ar[d_ar.index < t]
        Ztr = np.column_stack([np.ones(len(tr)), tr.dy_l1.values])
        b = ols(Ztr, tr.y.values)
        ar_preds.append(b[0] + b[1] * d_ar.loc[t, 'dy_l1'])
    ra = rmse(act, np.array(ar_preds))
    print(f'{label:26s} RMSE={r:6.2f}  (AR same-dates {ra:5.2f})  n={len(idx)}')

d = pd.concat([y, X[['esc', 'cem', 'ws6']]], axis=1).dropna()
Z = np.column_stack([np.ones(len(d))] + [d[c].values for c in ['esc', 'cem', 'ws6']])
b = ols(Z, d.y.values)
r2 = 1 - ((d.y.values - Z @ b) ** 2).sum() / ((d.y.values - d.y.mean()) ** 2).sum()
print(f'\nПолная выборка: yoy ИКВ ~ esc+cem+ws6: R2={r2:.3f}, n={len(d)}, '
      f'коэфф esc={b[1]:.3f} cem={b[2]:.3f} ws6={b[3]:.3f}')
