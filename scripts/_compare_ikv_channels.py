#!/usr/bin/env python3
"""Три канала РФ-ИКВ: сопоставление значений по кварталам."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import db_tunnel as t  # noqa: E402

LEVEL = ('iokmro', 'ikv_rf_q_bln', 'kep1_63')
YOY = ('iokspo', 'ikv_rf_q_yoy', 'kep1_6_y3')


def series(codes):
    out = {}
    for code in codes:
        out[code] = {p: v for p, v in t.query(
            "SELECT o.period_start, o.value FROM data.observation o "
            "JOIN core.metric m USING(metric_id) WHERE m.metric_code=%s", (code,))}
    return out


def table(codes, title):
    print('\n=== %s ===' % title)
    s = series(codes)
    periods = sorted(set().union(*[set(v) for v in s.values()]))
    hdr = '%-12s' % 'квартал' + ''.join('%14s' % c for c in codes)
    print(hdr)
    for p in periods:
        row = '%-12s' % p.strftime('%Y-%m-%d')
        vals = []
        for c in codes:
            v = s[c].get(p)
            vals.append('—' if v is None else ('%.2f' % v))
            row += '%14s' % vals[-1]
        flag = ''
        nums = [float(x) for x in vals if x != '—']
        if len(nums) > 1 and (max(nums) - min(nums)) > 1e-6:
            flag = '   <-- расхождение %.2f' % (max(nums) - min(nums))
        print(row + flag)


table(LEVEL, 'уровень, млрд руб.')
table(YOY, 'в % к соответствующему периоду')

print('\n=== число периодов и статусы ===')
for code in LEVEL + YOY:
    st = t.query("""SELECT m.status, count(o.*), min(o.period_start), max(o.period_start),
          min(o.release_id), max(o.release_id)
        FROM core.metric m JOIN data.observation o USING(metric_id)
        WHERE m.metric_code=%s GROUP BY 1""", (code,))
    print('%-12s %s' % (code, st))
print('\n=== статус релизов КЭП ===')
for r in t.query("SELECT release_id, label, status FROM catalog.release WHERE release_id IN (70,84,134,187)"):
    print(r)
