#!/usr/bin/env python3
"""Этап 2: бенчмарки bridge/MIDAS для nowcasting ИКВ/ВНОК (H-007/H-008 подготовка).
Цель: yoy ИКВ (ikv_rf_quarter, 2020-2026Q1, n=25).
Регрессоры: эскроу-приток yoy (ЦБ, квартальный из месячного), цемент yoy (мес), зарплата стройки yoy (мес), wordstat S6a (мес).
Схемы: AR(1), bridge (кварт. агрегаты), MIDAS-Almon-lite (взвешенные месяцы квартала).
Pseudo-OOO: expanding window, тест с 2024Q1 (эскроу-эпоха). Метрика RMSE vs AR(1).
"""
import sqlite3, pandas as pd, numpy as np, csv
from collections import defaultdict

con = sqlite3.connect('data/rosreestr_deals.db')
con2 = sqlite3.connect('data/rosstat_construction.db')
con3 = sqlite3.connect('data/cbr_lending.db')

# --- Целевая: yoy ИКВ квартал ---
ikv = pd.read_sql("select year, q, yoy_pct from ikv_rf_quarter order by year, q", con)
ikv['p'] = pd.PeriodIndex(ikv.year.astype(str) + 'Q' + ikv.q.astype(str), freq='Q')
y = ikv.set_index('p').yoy_pct.rename('y')

# --- Эскроу: РФ агрегат, месячный приток (Δ активных ПФК), кв. yoy ---
esc = pd.read_sql("""select report_date, sum(value) v from escrow_monthly
    where indicator='Сумма действующих кредитных договоров'
    group by report_date order by report_date""", con3)
esc['dt'] = pd.to_datetime(esc.report_date)
esc = esc.set_index('dt').v.asfreq('MS')
esc_flow = esc.diff()
esc_yoy_m = esc_flow.rolling(3).sum().pct_change(12) * 100  # кв. приток yoy, мес.

# --- Цемент: мес yoy ---
cem = pd.read_sql("""select year, month, value from building_materials_monthly
    where product='Цемент (все гидравлические)' and year>=2011""", con2)
cem = cem.dropna(subset=['year','month']).drop_duplicates(subset=['year','month'], keep='first')
cem['dt'] = pd.to_datetime(dict(year=cem.year.astype(int), month=cem.month.astype(int), day=1))
cem_yoy_m = cem.set_index('dt').value.asfreq('MS').pct_change(12) * 100

# --- Зарплата стройки: мес yoy (rosstat_construction) ---
try:
    wag = pd.read_sql("""select year, month, wage_rub as value from average_wage_monthly_regional
        where region_name='Российская Федерация' order by year, month""", con2)
    wag['dt'] = pd.to_datetime(dict(year=wag.year.astype(int), month=wag.month.astype(int), day=1))
    wag_yoy_m = wag.set_index('dt').value.asfreq('MS').pct_change(12) * 100
except Exception:
    wag_yoy_m = pd.Series(dtype=float)

# --- Wordstat S6a: недели → мес. сумма → yoy ---
rows = list(csv.DictReader(open('data/wordstat_weekly_b2b_invest.csv', encoding='utf-8')))
wq = defaultdict(int)
for r in rows:
    if r['group'] == 'S6a_mach_buy':
        d = r['date']; wq[d[:7]] += int(r['count'])
ws = pd.Series(wq).sort_index(); ws.index = pd.PeriodIndex(ws.index, freq='M').to_timestamp()
ws_m = ws.asfreq('MS')
# yoy по месячным суммам
ws_yoy_m = ws_m.pct_change(12) * 100

def almon_q(m_series, decay=0.5, n_lag=6):
    s = m_series.copy(); s.index = pd.PeriodIndex(s.index, freq='M')
    d = s.to_dict(); out = {}
    for t in s.index:
        num = den = 0.0
        for k in range(n_lag):
            v = d.get(t - k)
            if v is None or (isinstance(v, float) and np.isnan(v)): continue
            w = decay ** k; num += w * float(v); den += w
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
    b, *_ = np.linalg.lstsq(Z, yy, rcond=None); return b

def rmse(a, b): return float(np.sqrt(((a - b) ** 2).mean()))

TEST_START = pd.Period('2024Q1', 'Q')   # эскроу-эпоха; min_train=8
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
print(f"=== Pseudo-OOO expanding, Δy/y ИКВ, тест с {TEST_START} ===")
res = {}
for label, cols in SPECS.items():
    d = pd.concat([y, X[cols]], axis=1).dropna()
    d_te = d[d.index >= TEST_START]
    if len(d_te) < 3: print(f'{label}: мало теста ({len(d_te)})'); continue
    preds = []
    for t in d_te.index:
        tr = d[d.index < t]
        if len(tr) < 6: continue
        Ztr = np.column_stack([np.ones(len(tr))] + [tr[c].values for c in cols])
        b = ols(Ztr, tr.y.values)
        zt = np.array([1.0] + [d.loc[t, c] for c in cols])
        preds.append((t, zt @ b))
    if not preds: continue
    idx = [p[0] for p in preds]; pv = np.array([p[1] for p in preds])
    act = y.reindex(idx).values
    r = rmse(act, pv)
    # AR-бенчмарк на тех же датах
    d_ar = pd.concat([y, X['dy_l1']], axis=1).dropna()
    ar_preds = []
    for t in idx:
        tr = d_ar[d_ar.index < t]
        Ztr = np.column_stack([np.ones(len(tr)), tr.dy_l1.values])
        b = ols(Ztr, tr.y.values)
        ar_preds.append(b[0] + b[1] * d_ar.loc[t, 'dy_l1'])
    ra = rmse(act, np.array(ar_preds))
    res[label] = (r, ra, len(idx))
    print(f'{label:26s} RMSE={r:6.2f}  (AR same-dates {ra:5.2f})  n={len(idx)}')

# Полная выборка OLS R2 для лучшей спецификации
d = pd.concat([y, X[['esc', 'cem', 'ws6']]], axis=1).dropna()
Z = np.column_stack([np.ones(len(d))] + [d[c].values for c in ['esc', 'cem', 'ws6']])
b = ols(Z, d.y.values)
r2 = 1 - ((d.y.values - Z @ b) ** 2).sum() / ((d.y.values - d.y.mean()) ** 2).sum()
print(f'\nПолная выборка: yoy ИКВ ~ esc+cem+ws6: R2={r2:.3f}, n={len(d)}, коэфф esc={b[1]:.3f} cem={b[2]:.3f} ws6={b[3]:.3f}')
# Результаты этапа 2 (2026-09-08): см. queries/ikv-nowcasting-pilot.md (обновление этапа 2)
# Прогноз 2026Q2 из 2026Q1-модели:
# (требует данных 2026Q2 — после релиза Росстата в сентябре)