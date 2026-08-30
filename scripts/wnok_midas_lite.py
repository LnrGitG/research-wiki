#!/usr/bin/env python3
"""(c-final) MIDAS-lite на приращениях темпа ВНОК. Чистая версия."""
import sqlite3, pandas as pd, numpy as np

con = sqlite3.connect('data/rosreestr_deals.db')
con2 = sqlite3.connect('data/rosstat_construction.db')

y = pd.read_sql("""SELECT period, ifo FROM gdp_use_ifo_quarterly
                   WHERE series LIKE '%аловое накопление%'""", con)
y['period'] = y.period.str.replace('-Q', 'Q', regex=False)
y = y.rename(columns={'ifo': 'y'}).drop_duplicates('period')
y = y.set_index(pd.PeriodIndex(y.period, freq='Q')).y

cem = pd.read_sql("SELECT year, month, value FROM building_materials_monthly WHERE product='Цемент (все гидравлические)' AND year>=2011", con2)
cem = cem.dropna(subset=['year', 'month']).drop_duplicates(subset=['year', 'month'], keep='first')
cem['dt'] = pd.to_datetime(dict(year=cem.year.astype(int), month=cem.month.astype(int), day=1))
cem_m = cem.set_index(cem.dt).value
cem_yoy = (cem_m.pct_change(12) * 100)

dmnd = pd.read_sql("""SELECT date, value FROM cbr_monitoring_construction
                      WHERE question LIKE 'Как изменился спрос%' ORDER BY date""", con2)
dmnd['dt'] = pd.to_datetime(dmnd.date)
dmnd_m = dmnd.set_index(dmnd.dt).value

def almon_q(monthly_q_end_values, decay=0.5, n_lag=6):
    # на входе — месячный ряд; на выходе — квартальная серия с алмон-весами по 6 предыдущим месяцам после конца квартала
    s = pd.Series(monthly_q_end_values).copy()
    s.index = pd.PeriodIndex(s.index, freq='M')
    d = s.to_dict()
    out = {}
    for t in s.index:
        num = 0.0; den = 0.0
        for k in range(n_lag):
            v = d.get(t - k)
            if v is None or (isinstance(v, float) and np.isnan(v)):
                continue
            w = decay ** k
            num += w * float(v); den += w
        out[t] = num / den if den > 0 else np.nan
    out = pd.Series(out)
    # квартальное среднее (взвешенный агрегат по 3 мес квартала)
    q = out.resample('Q').mean()
    q.index = pd.PeriodIndex(q.index, freq='Q')
    return q

df = pd.DataFrame({
    'y': y,
    'cem_almon': almon_q(cem_yoy).reindex(y.index),
    'dem_almon': almon_q(dmnd_m).reindex(y.index),
})
df['dy'] = df.y.diff()
df['dy_l1'] = df.dy.shift(1)
df['cem_l1'] = df.cem_almon.shift(1)
df['dem_l1'] = df.dem_almon.shift(1)

test_start = pd.Period('2023Q1', 'Q')

def run(cols, label):
    d = df[['dy'] + cols].dropna()
    tr, te = d[d.index < test_start], d[d.index >= test_start]
    if len(te) < 4 or len(tr) < 10:
        print(f'{label}: мало данных (tr={len(tr)}, te={len(te)})'); return
    Ztr = np.column_stack([np.ones(len(tr))] + [tr[c].values for c in cols])
    b, *_ = np.linalg.lstsq(Ztr, tr.dy.values, rcond=None)
    Zte = np.column_stack([np.ones(len(te))] + [te[c].values for c in cols])
    pred = Zte @ b
    r = float(np.sqrt(((te.dy.values - pred) ** 2).mean()))
    print(f'{label:38s} RMSE={r:.2f}  n_tr={len(tr)} n_te={len(te)}')

print('=== walk-forward, Δ(ИФО ВНОК), тест 2023Q1-2026Q1 ===')
run(['dy_l1'], 'AR(1)')
run(['cem_l1'], 'MIDAS-lite цемент')
run(['dem_l1'], 'MIDAS-lite спрос ЦБ')
run(['cem_l1', 'dem_l1'], 'MIDAS-lite цемент + спрос')
run(['dy_l1', 'cem_l1'], 'AR + цемент')
run(['dy_l1', 'dem_l1'], 'AR + спрос')
run(['dy_l1', 'cem_l1', 'dem_l1'], 'AR + цемент + спрос')

d = df[['dy', 'dy_l1', 'cem_l1', 'dem_l1']].dropna()
Z = np.column_stack([np.ones(len(d))] + [d[c].values for c in ['dy_l1', 'cem_l1', 'dem_l1']])
b, *_ = np.linalg.lstsq(Z, d.dy.values, rcond=None)
r2 = 1 - ((d.dy.values - Z @ b) ** 2).sum() / ((d.dy.values - d.dy.mean()) ** 2).sum()
print(f'\nПолная выборка dy ~ AR + cem + dem: R2={r2:.3f}, n={len(d)}, коэфф: AR={b[1]:.3f} cem={b[2]:.3f} dem={b[3]:.3f}')