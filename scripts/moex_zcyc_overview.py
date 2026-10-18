#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Обзор загруженной кривой ОФЗ: покрытие по годам, уровни, спреды к ключевой ставке.

Читает канон (moex__zcyc__yield, cbr_key_rate) и печатает:
  * число торговых дней с кривой по годам (и пропуски);
  * средние уровни по срокам на конец периода;
  * наклон 10y−1y, кривизну 2·5y−1y−10y и спред 10y к ключевой ставке;
  * корреляцию наклона с ключевой ставкой и с её изменением.

Запуск: python3 scripts/moex_zcyc_overview.py [--since 2014-01-06]
"""
import argparse
import statistics as st
import sys

sys.path.insert(0, '/home/lnr/research-wiki-private/scripts')
import db_tunnel as dt

TENORS = ['0.25y', '0.5y', '0.75y', '1y', '2y', '3y', '5y', '7y', '10y', '15y', '20y']


def load(since):
    rows = dt.query("""
        SELECT o.period_start, o.sub_dimension, o.value
        FROM data.observation o JOIN catalog.metric m ON m.metric_id = o.metric_id
        WHERE m.metric_code = 'moex__zcyc__yield' AND o.period_start >= %s
        ORDER BY o.period_start""", (since,))
    curve = {}
    for d, sub, v in rows:
        curve.setdefault(d, {})[sub] = float(v)
    kr = dict(dt.query("""
        SELECT o.period_start, o.value FROM data.observation o
        JOIN catalog.metric m ON m.metric_id = o.metric_id
        WHERE m.metric_code = 'cbr_key_rate' AND o.period_start >= %s""", (since,)))
    kr = {d: float(v) for d, v in kr.items()}
    return curve, kr


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--since', default='2014-01-06')
    a = ap.parse_args()
    curve, kr = load(a.since)
    days = sorted(curve)
    print('дней с кривой: %d | с %s по %s' % (len(days), days[0], days[-1]))

    print('\nпокрытие по годам (торговых дней с кривой):')
    per_year = {}
    for d in days:
        per_year.setdefault(d.year, 0)
        per_year[d.year] += 1
    for y in sorted(per_year):
        bar = '#' * (per_year[y] // 5)
        print('  %d: %3d  %s' % (y, per_year[y], bar))

    last = days[-1]
    print('\nкривая на %s:' % last)
    for t in TENORS:
        v = curve[last].get(t)
        print('  %5s %s' % (t, ('%.2f' % v) if v is not None else '—'))

    def series(fn):
        out = []
        for d in days:
            c = curve[d]
            v = fn(c)
            if v is not None:
                out.append((d, v))
        return out

    slope = series(lambda c: None if ('10y' not in c or '1y' not in c) else c['10y'] - c['1y'])
    curve_t = series(lambda c: None if not all(k in c for k in ('5y', '1y', '10y'))
                     else 2 * c['5y'] - c['1y'] - c['10y'])
    spread = [(d, c['10y'] - kr[d]) for d, c in ((d, curve[d]) for d in days)
              if '10y' in curve[d] and d in kr]
    print('\nсредние за период:')
    for name, s in (('10y−1y (наклон)', slope), ('2·5y−1y−10y (кривизна)', curve_t),
                    ('10y − ключевая ставка', spread)):
        vs = [v for _, v in s]
        print('  %-24s %5.2f п.п. | мин %5.2f | макс %5.2f | n=%d'
              % (name, st.mean(vs), min(vs), max(vs), len(vs)))
    if spread:
        d, v = spread[-1]
        print('  на %s: 10y %.2f, ключевая %.2f → спред %.2f п.п.' % (d, curve[d]['10y'], kr[d], v))

    # связь наклона и ставки
    common = [(d, s, kr[d]) for d, s in slope if d in kr]
    if len(common) > 30:
        xs = [c[2] for c in common]
        ys = [c[1] for c in common]
        mx, my = st.mean(xs), st.mean(ys)
        cov = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
        r = cov / (sum((x - mx) ** 2 for x in xs) ** 0.5 * sum((y - my) ** 2 for y in ys) ** 0.5)
        print('\ncorr(наклон 10y−1y, ключевая ставка) = %+.2f (n=%d)' % (r, len(common)))


if __name__ == '__main__':
    main()
