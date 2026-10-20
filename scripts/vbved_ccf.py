#!/usr/bin/env python3
"""Кросс-корреляции ВБВЭД Башкортостана с жилищными и кредитными индикаторами.

Задача (гипотеза H-VB-2): опережает ли месячный ВБВЭД (vbved_reg_m) годовой ИФО ВРП
и жилищные ряды, и с каким лагом.

Метод. Все ряды сводятся к месячной сетке по региону 54 (Башкортостан). Уровневые ряды
переводятся в темп прироста к соответствующему месяцу прошлого года — иначе уровни
несопоставимы с ВБВЭД, который сам является индексом «год к году». Для каждой пары
считается кросс-корреляционная функция на лагах −12…+12; знак лага: k>0 означает, что
ВБВЭД опережает индикатор на k месяцев, k<0 — индикатор опережает ВБВЭД.

Ограничение, которое нельзя игнорировать: обе стороны — «год к году», то есть 12-месячные
скользящие суммы шоков, поэтому соседние наблюдения сильно автокоррелированы, а
номинальная значимость корреляции завышена. Поэтому к регрессии применяются
стандартные ошибки HAC (Newey-West, 12 лагов), а устойчивость проверяется сравнением
двух подвыборок и обнулением перекрытия (тест на полугодиях).

Запуск: python3 vbved_ccf.py [--region 54] [--out имя.png]
"""
import argparse
import os
import sys

import numpy as np
import pandas as pd
import statsmodels.api as sm

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from db_tunnel import query

TARGET_CODE = 'vbved_reg_m'

# (метка, код метрики, преобразование)
SERIES = [
    ('Цены новостроек, ДОМ.РФ', 'domrf_price_index_m', 'yoy'),
    ('Цена сделки, первичный рынок, Сбер', 'sber_deal_px_median_primary', 'yoy'),
    ('Число ДДУ, ДОМ.РФ', 'ddu_count_m', 'yoy'),
    ('Выдачи ИЖК, объём', 'cbr_izhk_volume_m', 'yoy'),
    ('Выдачи ИЖК, число кредитов', 'cbr_izhk_count_m', 'yoy'),
    ('Ставка ИЖК, п.п.', 'cbr_izhk_rate_m', 'level'),
    ('Разрешения на МКД, площадь', 'domrf_permits_flow_m2', 'yoy'),
    ('Реализация квартир, м²', 'domrf_sales_m2_level', 'yoy'),
    ('Строящиеся МКД, площадь', 'domrf_stock_bld_m2', 'yoy'),
]

LAGS = range(-12, 13)


def series(code: str, region: int) -> pd.Series:
    """Месячный ряд по региону.

    При дублях (пересмотры, повторные релизы) берём строку последнего релиза.
    Подразрез допускается, если он единственный и является провенансом
    («источник: …»), а не разбиением ряда.
    """
    subs = query("""select distinct o.sub_dimension from data.observation o
                    join core.metric m using(metric_id)
                    where m.metric_code = %s and o.region_id = %s""", (code, region))
    subs = [s for (s,) in subs]
    keep = [s for s in subs if s not in (None, '') and not s.startswith('накопительно')]
    if keep:
        if len(keep) > 1:
            return pd.Series(dtype=float)   # настоящее разбиение — не наш случай
        rows = query("""
            select distinct on (o.period_start) o.period_start, o.value
            from data.observation o join core.metric m using(metric_id)
            where m.metric_code = %s and o.region_id = %s and o.sub_dimension = %s
              and o.value is not null
            order by o.period_start, o.release_id desc
        """, (code, region, keep[0]))
    else:
        rows = query("""
            select distinct on (o.period_start) o.period_start, o.value
            from data.observation o join core.metric m using(metric_id)
            where m.metric_code = %s and o.region_id = %s
              and (o.sub_dimension is null or o.sub_dimension = '') and o.value is not null
            order by o.period_start, o.release_id desc
        """, (code, region))
    if not rows:
        return pd.Series(dtype=float)
    s = pd.Series({pd.Timestamp(p): float(v) for p, v in rows}).sort_index()
    s.index = s.index.to_period('M')
    return s


def to_yoy(s: pd.Series) -> pd.Series:
    return (s / s.shift(12) - 1.0) * 100.0


def hac_tstat(y: np.ndarray, x: np.ndarray, maxlags: int = 12):
    X = sm.add_constant(x)
    res = sm.OLS(y, X).fit(cov_type='HAC', cov_kwds={'maxlags': maxlags})
    return float(res.tvalues[1]), float(res.rsquared)


def cross_section() -> None:
    """Проверка H-VB-2 в разрезе регионов: годовой ВБВЭД против ИФО ВРП.

    Временной ряд по одному региону для этого теста бесполезен (ИФО ВРП — годовой,
    точек 3), поэтому сопоставление идёт по панели регионов: среднее ВБВЭД за год
    против ИФО ВРП того же года.
    """
    vb = query("""
        select o.region_id, extract(year from o.period_start)::int as y, avg(o.value)
        from data.observation o join core.metric m using(metric_id)
        where m.metric_code = 'vbved_reg_m'
          and (o.sub_dimension is null or o.sub_dimension not like 'накопительно%%')
        group by 1, 2
    """)
    ifo = query("""
        select o.region_id, extract(year from o.period_start)::int as y, o.value
        from data.observation o join core.metric m using(metric_id)
        where m.metric_code = 'grp_ifo' and o.value is not null
    """)
    df = (pd.DataFrame(vb, columns=['region', 'year', 'vbved'])
          .merge(pd.DataFrame(ifo, columns=['region', 'year', 'ifo']),
                 on=['region', 'year'], how='inner'))
    for c in ('vbved', 'ifo'):
        df[c] = pd.to_numeric(df[c], errors='coerce')
    df = df.dropna(subset=['vbved', 'ifo'])
    if df.empty:
        print('\nпоперечный тест H-VB-2: нет общих лет')
        return
    print('\nпоперечный тест H-VB-2 (среднее ВБВЭД за год против ИФО ВРП):')
    for y, g in df.groupby('year'):
        if len(g) >= 20:
            print('  %d: corr = %+.2f, n = %d, ИФО ВРП %.1f…%.1f, ВБВЭД %.1f…%.1f'
                  % (y, g['vbved'].corr(g['ifo']), len(g),
                     g['ifo'].min(), g['ifo'].max(), g['vbved'].min(), g['vbved'].max()))
    X = sm.add_constant(df['vbved'])
    pooled = sm.OLS(df['ifo'], X).fit(cov_type='cluster',
                                      cov_kwds={'groups': df['region']})
    print('  пул %d наблюдений: наклон %.2f (t = %.2f), R² = %.2f'
          % (len(df), pooled.params.iloc[1], pooled.tvalues.iloc[1], pooled.rsquared))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--region', type=int, default=54)
    ap.add_argument('--out', default='vbved_ccf.png')
    a = ap.parse_args()

    tgt = series(TARGET_CODE, a.region)
    if tgt.empty:
        print('ОСТАНОВ: нет ряда %s по региону %s' % (TARGET_CODE, a.region))
        return 2
    print('цель: %s, %d месяцев, %s — %s'
          % (TARGET_CODE, len(tgt), tgt.index.min(), tgt.index.max()))

    results, curves = [], {}
    for label, code, kind in SERIES:
        s = series(code, a.region)
        if s.empty:
            print('  %-38s нет данных' % label)
            continue
        x = to_yoy(s) if kind == 'yoy' else s
        df = pd.DataFrame({'y': tgt, 'x': x}).dropna()
        if len(df) < 30:
            print('  %-38s мало общих месяцев: %d' % (label, len(df)))
            continue
        curve = {}
        for k in LAGS:
            shifted = df['x'].shift(-k)
            pair = pd.DataFrame({'y': df['y'], 'x': shifted}).dropna()
            curve[k] = (pair['y'].corr(pair['x']), len(pair))
        best_k = max((k for k in curve if not np.isnan(curve[k][0])),
                     key=lambda k: abs(curve[k][0]))
        pair_best = pd.DataFrame({'y': df['y'], 'x': df['x'].shift(-best_k)}).dropna()
        t_best, _ = hac_tstat(pair_best['y'].values, pair_best['x'].values)
        c0 = df['y'].corr(df['x'])
        t0, r2 = hac_tstat(df['y'].values, df['x'].values)
        half = len(df) // 2
        c1 = df['y'].iloc[:half].corr(df['x'].iloc[:half])
        c2 = df['y'].iloc[half:].corr(df['x'].iloc[half:])
        d = df.diff().dropna()
        cdel = d['y'].corr(d['x'])
        cool = df[df.index >= pd.Period('2025-01', 'M')]
        c3 = cool['y'].corr(cool['x']) if len(cool) >= 8 else float('nan')
        results.append({'ряд': label, 'код': code, 'вид': kind,
                        'лучший лаг': best_k, 'corr(лаг*)': curve[best_k][0],
                        'HAC t(лаг*)': t_best,
                        'corr(0)': c0, 'HAC t(0)': t0, 'R2': r2, 'n': len(df),
                        'corr 1-я половина': c1, 'corr 2-я половина': c2,
                        'corr 2025+': c3, 'corr Δ(0)': cdel})
        curves[label] = curve

    res = pd.DataFrame(results).sort_values('corr(лаг*)', key=lambda s: s.abs(),
                                            ascending=False)
    pd.set_option('display.width', 200)
    pd.set_option('display.max_colwidth', 40)
    fmt = res.copy()
    for c in ('corr(лаг*)', 'corr(0)', 'corr 1-я половина', 'corr 2-я половина',
              'corr 2025+', 'corr Δ(0)'):
        fmt[c] = fmt[c].map(lambda v: '%.2f' % v if pd.notna(v) else '—')
    for c in ('HAC t(лаг*)', 'HAC t(0)', 'R2'):
        fmt[c] = fmt[c].map(lambda v: '%.2f' % v)
    print('\n' + fmt.to_string(index=False))

    csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..',
                            'queries', 'figs', os.path.splitext(a.out)[0] + '.csv')
    res.to_csv(csv_path, index=False, encoding='utf-8-sig')
    print('\nтаблица: %s' % csv_path)
    cross_section()

    if curves:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        wanted = ['Выдачи ИЖК, объём', 'Число ДДУ, ДОМ.РФ', 'Ставка ИЖК, п.п.',
                  'Цены новостроек, ДОМ.РФ']
        top = [lab for lab in wanted if lab in curves]
        fig, axes = plt.subplots(2, 2, figsize=(11, 7))
        for ax, label in zip(axes.ravel(), top):
            ks = sorted(curves[label])
            cs = [curves[label][k][0] for k in ks]
            ax.bar(ks, cs, color=['#2b6cb0' if k > 0 else '#c05621' for k in ks])
            ax.axhline(0, color='black', lw=0.8)
            band = 2.0 / np.sqrt(56)
            ax.axhspan(-band, band, color='grey', alpha=0.15,
                       label='ориентир ±2/√n (n=56)')
            ax.set_title(label, fontsize=9)
            ax.set_xlabel('лаг, мес (k>0 — ВБВЭД опережает)')
            ax.set_ylabel('corr')
            ax.grid(alpha=0.3)
        fig.suptitle('ВБВЭД Башкортостана: кросс-корреляции «год к году», 2022-01…2026-08')
        fig.tight_layout()
        png = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'queries', 'figs', a.out)
        fig.savefig(png, dpi=150)
        print('график: %s' % os.path.abspath(png))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
