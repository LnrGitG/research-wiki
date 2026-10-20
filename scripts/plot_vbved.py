#!/usr/bin/env python3
"""График ВБВЭД (vbved_reg_m) по региону из канона.

Запуск: python3 plot_vbved.py [имя региона] [--out путь]

Читает только месячные наблюдения (sub_dimension IS NULL) — накопительные
периоды источника («январь-август») на график не попадают.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from db_tunnel import query  # noqa: E402

import matplotlib  # noqa: E402
matplotlib.use('Agg')
import matplotlib.pyplot as plt  # noqa: E402

METRIC = 'vbved_reg_m'


def series(region='Республика Башкортостан'):
    rows = query("""SELECT r.name_ru, o.period_start, o.value
        FROM data.observation o
        JOIN catalog.metric m ON m.metric_id = o.metric_id
        JOIN catalog.region r ON r.region_id = o.region_id
        WHERE m.metric_code = %s AND r.name_ru = %s
          AND o.sub_dimension IS NULL
          AND o.observation_status <> 'rejected'
        ORDER BY o.period_start""", (METRIC, region))
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('region', nargs='?', default='Республика Башкортостан')
    ap.add_argument('--out', default=None)
    a = ap.parse_args()
    rows = series(a.region)
    if not rows:
        print('нет данных по региону %s' % a.region)
        return 1
    dates = [r[1] for r in rows]
    vals = [float(r[2]) for r in rows]

    fig, ax = plt.subplots(figsize=(11, 5.2), dpi=170)
    ax.plot(dates, vals, marker='o', ms=3.6, lw=1.8, color='#1f5fa8')
    ax.axhline(100, color='#555', lw=1, ls='--')
    ax.fill_between(dates, 100, vals, where=[v < 100 for v in vals],
                    color='#b03a2e', alpha=.15)
    ax.set_title('Индекс выпуска по базовым видам экономической деятельности:\n'
                 '%s, %% к соответствующему периоду предыдущего года (канон: %s)'
                 % (a.region, METRIC), fontsize=11)
    ax.set_ylabel('% к соотв. периоду предыдущего года')
    ax.grid(alpha=.25)
    ax.set_ylim(min(vals + [100]) - 3, max(vals + [100]) + 3)
    for d, v in zip(dates, vals):
        ax.annotate('%.1f' % v, (d, v), textcoords='offset points', xytext=(0, 6),
                    ha='center', fontsize=7, color='#333')
    out = a.out or os.path.expanduser(
        '~/research-wiki-private/queries/figs/vbved_bashkortostan_canon.png')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    fig.tight_layout()
    fig.savefig(out)
    print('точек %d, %s - %s, среднее %.2f' %
          (len(vals), dates[0], dates[-1], sum(vals) / len(vals)))
    print('png:', out)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
