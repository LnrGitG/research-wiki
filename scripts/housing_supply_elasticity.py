#!/usr/bin/env python3
"""(a-final) Эластичность предложения: within-OLS с кластерными SE."""
import sqlite3, pandas as pd, numpy as np

con = sqlite3.connect('data/rosreestr_deals.db')
con2 = sqlite3.connect('data/rosstat_construction.db')

hin = pd.read_sql("""SELECT region, year, value FROM housing_input_annual
                     WHERE source='roschart_pril_invest_2025_7_5' AND region != 'Российская Федерация'""", con)
pr = pd.read_sql("""SELECT region_name, year, market, AVG(price_per_sqm) p FROM housing_prices_quarterly
                    GROUP BY region_name, year, market""", con2)

def run(pr_subset, label):
    q = pr_subset.rename(columns={'region_name': 'region', 'p': 'price'})
    pan = hin.merge(q, on=['region', 'year'], how='inner').dropna().sort_values(['region', 'year'])
    if len(pan) < 100:
        print(label, 'too few rows:', len(pan)); return
    pan['din'] = pan.groupby('region').value.transform(lambda x: np.log(x).diff())
    pan['dp'] = pan.groupby('region').price.transform(lambda x: np.log(x).diff())
    pan['dp_l1'] = pan.groupby('region').dp.shift(1)
    pan['dp2'] = pan.groupby('region').dp.shift(1) + pan.groupby('region').dp.shift(2)
    pan = pan.dropna(subset=['din', 'dp'])

    def within_ols(d, y, x):
        d = d[[y, x, 'region']].dropna().copy()
        for v in (y, x):
            d[v + '_w'] = d[v] - d.groupby('region')[v].transform('mean')
        X = np.column_stack([np.ones(len(d)), d[x + '_w'].values]); Y = d[y + '_w'].values
        beta, *_ = np.linalg.lstsq(X, Y, rcond=None)
        resid = Y - X @ beta
        d = d.assign(resid=resid)
        n, k = X.shape; G = d.region.nunique()
        dfc = n / (n - k) * (G / (G - 1))
        meat = np.zeros((k, k))
        for _, g in d.groupby('region'):
            Xg = np.column_stack([np.ones(len(g)), g[x + '_w'].values])
            XTu = Xg.T @ g.resid.values; meat += np.outer(XTu, XTu)
        V = np.linalg.inv(X.T @ X) @ meat @ np.linalg.inv(X.T @ X) * dfc
        se = np.sqrt(np.diag(V))
        return f"beta={beta[1]:+.4f} (se {se[1]:.4f}) t={beta[1]/se[1]:+.2f} n={len(d)} regs={G}"

    print(f'-- {label} --')
    print(' E_t:   ', within_ols(pan, 'din', 'dp'))
    print(' E_lag1:', within_ols(pan, 'din', 'dp_l1'))
    print(' E_2yr: ', within_ols(pan.dropna(subset=['dp2']), 'din', 'dp2'))
    # уровень: log input ~ log price (level - heterog)
    pan['lin'] = np.log(pan.value); pan['lp'] = np.log(pan.price)
    print(' levels:', within_ols(pan, 'lin', 'lp'))

run(pr[pr.market == 'primary'], 'цены первичный рынок')
run(pr[pr.market == 'secondary'], 'цены вторички')