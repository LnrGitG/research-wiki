#!/usr/bin/env python3
"""Панель регионов: опережают ли кредитно-спросовые индикаторы жилья выпуск (ВБВЭД).

Постановка. Панель «регион × месяц», 2022-01…2026-08. Зависимая переменная — ВБВЭД
(индекс выпуска по базовым видам экономической деятельности, «год к году», %).
Регрессоры интереса — выдачи ИЖК (объём и число) и число ДДУ, тоже «год к году»,
со сдвигом на 6 месяцев (гипотеза H-VB-2).

Две разные идентификации, и различие между ними — главный результат:

* S0 — только региональные фиксированные эффекты. Идентификация от общероссийской
  динамики: сравниваем регионы между собой в один и тот же месяц. Здесь ловится
  общий цикл, общий для выпуска и кредита.
* S1 — региональные И месячные фиксированные эффекты. Месячные эффекты забирают
  общероссийские шоки (ставка, льготные программы, сезонность), поэтому
  идентификация идёт от отклонения региона от среднемесячного профиля страны.

Оценка: альтернирующее демеанирование (FWL), OLS на преобразованных данных,
ошибки, кластеризованные по региону. Для S0 кластеризация по региону не учитывает
общие шоки, поэтому её t-статистики — верхняя граница точности, а не тест.

Запуск: python3 vbved_panel.py
"""
import os
import sys

import numpy as np
import pandas as pd
import statsmodels.api as sm

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from db_tunnel import query

START = '2021-01-01'      # запас 12 месяцев для расчёта «год к году»
FIGS = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'queries', 'figs')


def raw_series(code: str) -> pd.DataFrame:
    """Все регионы одним запросом; накопительные и «составные» подрезы отброшены."""
    rows = query("""
        select o.region_id, o.period_start, o.value
        from data.observation o join core.metric m using(metric_id)
        where m.metric_code = %s
          and o.period_start >= %s
          and (o.sub_dimension is null or
               (o.sub_dimension not like 'накопительно%%' and o.sub_dimension not like 'состав%%'))
          and o.value is not null
    """, (code, START))
    df = pd.DataFrame(rows, columns=['region', 'month', 'value'])
    df['month'] = pd.PeriodIndex(pd.to_datetime(df['month']), freq='M')
    df['value'] = pd.to_numeric(df['value'], errors='coerce')
    return df.dropna().drop_duplicates(subset=['region', 'month'], keep='last')


def to_yoy(df: pd.DataFrame) -> pd.DataFrame:
    df = df.sort_values(['region', 'month'])
    df['value'] = df.groupby('region')['value'].transform(lambda s: (s / s.shift(12) - 1) * 100)
    return df.dropna()


def load() -> pd.DataFrame:
    df = raw_series('vbved_reg_m').rename(columns={'value': 'vbved'})
    for code, name, kind in (('cbr_izhk_volume_m', 'izhk_vol', 'yoy'),
                             ('cbr_izhk_count_m', 'izhk_cnt', 'yoy'),
                             ('ddu_count_m', 'ddu', 'yoy'),
                             ('ippsm', 'ipp', 'as_is')):
        part = raw_series(code)
        if kind == 'yoy':
            part = to_yoy(part)
        df = df.merge(part.rename(columns={'value': name}), on=['region', 'month'], how='left')
    df = df[df['month'] >= pd.Period('2022-01', 'M')]
    return df.sort_values(['region', 'month']).reset_index(drop=True)


def add_lag(df: pd.DataFrame, col: str, k: int) -> pd.Series:
    return df.groupby('region')[col].shift(k)


def demean2(df: pd.DataFrame, cols: list, ent: str = 'region', tm: str = 'month',
            iters: int = 60) -> pd.DataFrame:
    """Двухстороннее демеанирование альтернирующими проекциями."""
    d = df[cols].astype(float).copy()
    for _ in range(iters):
        d = d - d.groupby(df[ent]).transform('mean')
        d = d - d.groupby(df[tm]).transform('mean')
    return d


def fe_fit(df: pd.DataFrame, ycol: str, xcols: list, time_fe: bool = True) -> dict:
    d = df.dropna(subset=[ycol] + xcols)
    if len(d) < 200:
        return {'n': len(d), 'регионов': int(d['region'].nunique())}
    if time_fe:
        dm = demean2(d, [ycol] + xcols)
    else:
        dm = d[[ycol] + xcols].astype(float)
        dm = dm - dm.groupby(d['region']).transform('mean')
    X = sm.add_constant(dm[xcols].values)
    res = sm.OLS(dm[ycol].values, X).fit(cov_type='cluster',
                                         cov_kwds={'groups': d['region'].values})
    out = {'n': int(len(d)), 'регионов': int(d['region'].nunique()),
           'within R2': float(res.rsquared)}
    for i, c in enumerate(['const'] + xcols):
        out['b:' + c] = float(res.params[i])
        out['t:' + c] = float(res.tvalues[i])
    return out


def report(name: str, r: dict, xs: list) -> None:
    line = '%-44s n=%-5d рег=%-3d R2=%.3f' % (name, r.get('n', 0), r.get('регионов', 0),
                                              r.get('within R2', float('nan')))
    for x in xs:
        line += ' | %s: %+.3f (t %+.2f)' % (x, r.get('b:' + x, float('nan')),
                                           r.get('t:' + x, float('nan')))
    print(line)


def main() -> int:
    df = load()
    print('панель: %d строк, %d регионов, %s — %s'
          % (len(df), df['region'].nunique(), df['month'].min(), df['month'].max()))
    print('покрытие: выдач ИЖК %d строк, ДДУ %d, промпроизводство %d (доступно с %s)'
          % (df.dropna(subset=['izhk_vol']).shape[0], df.dropna(subset=['ddu']).shape[0],
             df.dropna(subset=['ipp']).shape[0], df.dropna(subset=['ipp'])['month'].min()
             if df['ipp'].notna().any() else '—'))

    for c in ('izhk_vol', 'izhk_cnt', 'ddu', 'ipp'):
        df['L6_' + c] = add_lag(df, c, 6)

    print('\n--- S0: только региональные FE (общий цикл) ---')
    report('объём выдач ИЖК, лаг 6', fe_fit(df, 'vbved', ['L6_izhk_vol'], time_fe=False),
           ['L6_izhk_vol'])
    report('число кредитов ИЖК, лаг 6', fe_fit(df, 'vbved', ['L6_izhk_cnt'], time_fe=False),
           ['L6_izhk_cnt'])
    report('число ДДУ, лаг 6', fe_fit(df, 'vbved', ['L6_ddu'], time_fe=False), ['L6_ddu'])

    print('\n--- S1: региональные И месячные FE (идиосинкратическая вариация) ---')
    report('объём выдач ИЖК, лаг 6', fe_fit(df, 'vbved', ['L6_izhk_vol']), ['L6_izhk_vol'])
    report('число кредитов ИЖК, лаг 6', fe_fit(df, 'vbved', ['L6_izhk_cnt']), ['L6_izhk_cnt'])
    report('число ДДУ, лаг 6', fe_fit(df, 'vbved', ['L6_ddu']), ['L6_ddu'])
    report('объём ИЖК: лаг 0 и лаг 6', fe_fit(df, 'vbved', ['izhk_vol', 'L6_izhk_vol']),
           ['izhk_vol', 'L6_izhk_vol'])
    report('объём ИЖК + промпроизводство, лаг 6',
           fe_fit(df, 'vbved', ['L6_izhk_vol', 'L6_ipp']), ['L6_izhk_vol', 'L6_ipp'])

    sub = df[df['month'] >= pd.Period('2023-01', 'M')]
    report('2023+, объём ИЖК лаг 6', fe_fit(sub, 'vbved', ['L6_izhk_vol']), ['L6_izhk_vol'])

    sweep = []
    for k in range(0, 13):
        df['tmp'] = add_lag(df, 'izhk_vol', k)
        for label, tf in (('S0', False), ('S1', True)):
            r = fe_fit(df, 'vbved', ['tmp'], time_fe=tf)
            sweep.append({'lag': k, 'spec': label, 'b': r.get('b:tmp'),
                          't': r.get('t:tmp'), 'n': r.get('n')})
    sw = pd.DataFrame(sweep)

    print('\nпрофиль по лагам (объём выдач ИЖК, отдельная регрессия на каждый лаг):')
    for label in ('S0', 'S1'):
        g = sw[sw['spec'] == label]
        print('  %s: ' % label + '  '.join('%d:%+.2f(t%+.1f)'
                                           % (row['lag'], row['b'], row['t'])
                                           for _, row in g.iterrows()))

    # тренд региона как контроль
    d = df.dropna(subset=['vbved', 'L6_izhk_vol']).copy()
    d['trend'] = d.groupby('region').cumcount()
    dm = demean2(d, ['vbved', 'L6_izhk_vol'])
    X = sm.add_constant(np.column_stack([dm['L6_izhk_vol'].values, d['trend'].values]))
    res = sm.OLS(dm['vbved'].values, X).fit(cov_type='cluster',
                                            cov_kwds={'groups': d['region'].values})
    print('\nс линейным трендом региона (двусторонние FE): b=%+.3f (t %+.2f)'
          % (res.params[1], res.tvalues[1]))


    # межрегиональное сечение: средние за период уровни
    g = (df.dropna(subset=['vbved', 'izhk_vol'])
           .groupby('region')[['vbved', 'izhk_vol', 'izhk_cnt']].mean())
    print('\n--- между регионами (средние за 2022-01…2026-08, n=%d) ---' % len(g))
    print('  corr(ВБВЭД, объём выдач ИЖК) = %+.2f; corr(ВБВЭД, число кредитов) = %+.2f'
          % (g['vbved'].corr(g['izhk_vol']), g['vbved'].corr(g['izhk_cnt'])))
    bb = sm.OLS(g['vbved'], sm.add_constant(g['izhk_vol'])).fit(cov_type='HC1')
    print('  наклон %.3f (t %+.2f), R2 %.2f'
          % (bb.params.iloc[1], bb.tvalues.iloc[1], bb.rsquared))

    os.makedirs(FIGS, exist_ok=True)
    sw.to_csv(os.path.join(FIGS, 'vbved_panel_lags.csv'), index=False, encoding='utf-8-sig')

    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(8.4, 4.4))
    for label, color, name in (('S0', '#c05621', 'только региональные FE (общий цикл)'),
                               ('S1', '#2b6cb0', 'региональные и месячные FE (идиосинкразия)')):
        g = sw[sw['spec'] == label]
        ax.plot(g['lag'], g['b'], 'o-', color=color, label=name)
        se = (g['b'] / g['t']).abs()
        ax.fill_between(g['lag'], g['b'] - 2 * se, g['b'] + 2 * se, color=color, alpha=0.12)
    ax.axhline(0, color='black', lw=0.8)
    ax.set_xlabel('лаг выдач ИЖК, месяцев (k — насколько кредит опережает выпуск)')
    ax.set_ylabel('коэффициент при yoy выдач ИЖК, п.п. ВБВЭД')
    ax.set_title('Панель регионов РФ: ВБВЭД и выдачи ИЖК, 2022-01…2026-08')
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8)
    fig.tight_layout()
    png = os.path.join(FIGS, 'vbved_panel_lags.png')
    fig.savefig(png, dpi=150)
    print('график: %s' % os.path.abspath(png))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
