#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Рисунок к записке по кривой ОФЗ: уровни по срокам, наклон и спред к ключевой ставке."""
import os
import sys

import matplotlib
matplotlib.use('Agg')
import matplotlib.dates as mdates  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import db_tunnel as dt  # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'moex_zcyc_overview.png')

rows = dt.query("""SELECT o.period_start, o.sub_dimension, o.value
    FROM data.observation o JOIN catalog.metric m ON m.metric_id=o.metric_id
    WHERE m.metric_code='moex__zcyc__yield' ORDER BY o.period_start""")
curve = {}
for d, sub, v in rows:
    curve.setdefault(d, {})[sub] = float(v)
kr = {d: float(v) for d, v in dt.query("""SELECT o.period_start, o.value FROM data.observation o
    JOIN catalog.metric m ON m.metric_id=o.metric_id WHERE m.metric_code='cbr_key_rate'""")}
days = sorted(curve)

fig, ax = plt.subplots(2, 1, figsize=(13, 9), sharex=True,
                       gridspec_kw={'height_ratios': [3, 2]})
for t, c, lw in (('1y', '#1f77b4', 1.0), ('5y', '#ff7f0e', 1.0), ('10y', '#d62728', 1.4)):
    xs = [d for d in days if t in curve[d]]
    ys = [curve[d][t] for d in xs]
    ax[0].plot(xs, ys, c, lw=lw, label='ОФЗ, срок %s' % t.replace('y', ' лет').replace('1 лет', '1 год'))
kxs = sorted(d for d in days if d in kr)
ax[0].plot(kxs, [kr[d] for d in kxs], 'k--', lw=1.1, label='ключевая ставка')
ax[0].set_ylabel('% годовых')
ax[0].legend(loc='upper right', fontsize=9)
ax[0].grid(alpha=0.3)
ax[0].set_title('Кривая бескупонной доходности ОФЗ (Мосбиржа, NSS) и ключевая ставка, 2014–2026')

sx = [d for d in days if '10y' in curve[d] and '1y' in curve[d]]
ax[1].plot(sx, [curve[d]['10y'] - curve[d]['1y'] for d in sx], '#2ca02c', lw=1.0, label='наклон 10y − 1y')
px = [d for d in days if '10y' in curve[d] and d in kr]
ax[1].plot(px, [curve[d]['10y'] - kr[d] for d in px], '#9467bd', lw=1.0, label='10y − ключевая ставка')
ax[1].axhline(0, color='grey', lw=0.8)
ax[1].set_ylabel('п.п.')
ax[1].legend(loc='upper right', fontsize=9)
ax[1].grid(alpha=0.3)
ax[1].xaxis.set_major_locator(mdates.YearLocator(1))
ax[1].xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

os.makedirs(os.path.dirname(OUT), exist_ok=True)
fig.tight_layout()
fig.savefig(OUT, dpi=150)
print('записано:', OUT)
