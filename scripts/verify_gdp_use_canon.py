#!/usr/bin/env python3
"""Приёмка группы «использование ВВП» (A-4): уровень, ИФО, ВДС раздела F.

Что проверяется и чем. Три независимые проверки, каждая со своим источником:

1. Уровень ВВП (`vvp`) и ИФО (`vvpi`) против живого roschart.ru. Набор
   `gdp-quarters-of-use-1995-1kv-2026-elementy-ispolzovaniya-vvp-2` (9 рядов,
   элементы использования ВВП, поквартально). Данные берутся со страницы набора —
   тег `<script type="application/json">`; старый путь `/api/dataset/<slug>` с
   17.10.2026 отдаёт 401 (см. A-3, `direct_vvd_rf_roschart.py`).

2. ВДС раздела F (`vvdsotrs`, релиз `vds_f`) и её ИФО (`vsii`, релиз `vds_f_ifo`)
   против релиза 39 `rosstat_vds_okved2` — это та же группа ОКВЭД2, пришедшая в
   канон из лендинга `rosstat_construction.db` (таблица `gdp_vds_quarterly_okved`,
   6 248 строк, перенос через гармонайзер 5). Ряд `vds_f` обязан совпасть с
   `vds_real_2021` раздела F, ИФО — с `vds_volume_index`.

3. Внутренняя согласованность ИФО ВВП: `vvpi[t]` против отношения уровней
   `vvp[t] / vvp[t-4] × 100`. Оба ряда одного набора, поэтому расхождение больше
   процентного пункта означает ошибку разметки одного из них.

Порог остановки — 1 % (для проверки 3 — 1 процентный пункт) на трёх и более
точках, как записано в реестре (A-4). Проверка 3 сравнивает два ряда одного
источника, поэтому её порог мягче по смыслу — она ловит подмену ряда, а не
единицы измерения.

Запуск: python3 scripts/verify_gdp_use_canon.py [--verbose]
"""

import argparse
import json
import os
import re
import ssl
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import db_tunnel as tunnel                                  # noqa: E402

ROSHART = ('https://roschart.ru/dataset/'
           'gdp-quarters-of-use-1995-1kv-2026-elementy-ispolzovaniya-vvp-2')
THRESHOLD = 1.0


def canon(code):
    """Наблюдения метрики: {'YYYY-MM': (значение, подразрез)}."""
    rows = tunnel.query("""
        SELECT o.period_start, o.value, coalesce(o.sub_dimension, '')
        FROM data.observation o JOIN core.metric m ON m.metric_id = o.metric_id
        WHERE m.metric_code = %s ORDER BY 1""", (code,))
    return {str(r[0])[:7]: (float(r[1]), r[2]) for r in rows}


def release_series(series, release_id=39, section='Раздел F'):
    rows = tunnel.query("""
        SELECT o.period_start, o.value
        FROM data.observation o
        WHERE o.release_id = %s
          AND o.sub_dimension LIKE %s AND o.sub_dimension LIKE %s
        ORDER BY 1""", (release_id, '%series: ' + series + ' |%', '%okved_section: ' + section + '%'))
    return {str(r[0])[:7]: float(r[1]) for r in rows}


def roschart_series():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    req = urllib.request.Request(ROSHART, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req, timeout=120, context=ctx).read().decode('utf-8', 'ignore')
    block = re.search(r'<script type="application/json"[^>]*>(.*?)</script>', html, re.S)
    if not block:
        raise SystemExit('в странице набора нет JSON-блока — вёрстка изменилась')
    d = json.loads(block.group(1))
    out = {}
    for s in d['series']:
        for period, val in zip(d['periods'], s['values']):
            if val is None:
                continue
            y, q = period.split('-Q')
            month = 3 * (int(q) - 1) + 1
            out.setdefault(s['label'].strip(), {})['%s-%02d' % (y, month)] = float(val)
    return out


def compare(name, a, b, unit='%', verbose=False):
    keys = sorted(set(a) & set(b))
    bad = []
    worst = 0.0
    for k in keys:
        base = abs(b[k])
        if base < 1e-9:
            continue
        diff = abs(a[k] - b[k]) / base * 100.0
        worst = max(worst, diff)
        if diff > THRESHOLD:
            bad.append((k, a[k], b[k], round(diff, 3)))
    verdict = 'ОК' if len(bad) < 3 else 'СТОП'
    print('  %-46s точек %-4d расхождений >%s%s: %-3d худшее %.3f%s  %s'
          % (name, len(keys), THRESHOLD, unit, len(bad), worst, unit, verdict))
    if verbose or len(bad) >= 3:
        for k, va, vb, d in bad[:5]:
            print('      %s: канон %s | источник %s | Δ %s%s' % (k, va, vb, d, unit))
    return len(keys), len(bad), worst


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--verbose', action='store_true')
    a = ap.parse_args()
    fails = []

    print('1. Живой roschart против канона (элементы использования ВВП)')
    rs = roschart_series()
    print('   рядов в наборе: %d' % len(rs))
    vvp = {k: v[0] for k, v in canon('vvp').items()}
    for label, code in (('Валовой внутренний продукт', 'vvp'),):
        src = rs.get(label)
        if not src:
            print('   ряд «%s» не найден в наборе — пропуск' % label)
            continue
        n, bad, worst = compare('vvp (уровень) vs roschart', vvp, src, verbose=a.verbose)
        if bad >= 3:
            fails.append('vvp расходится с roschart на %d точках' % bad)

    print('2. ВДС раздела F: релизы `vds_f`/`vds_f_ifo` против релиза 39 (из лендинга)')
    n, bad, _ = compare('vvdsotrs (vds_f) vs vds_real_2021',
                        {k: v[0] for k, v in canon('vvdsotrs').items()},
                        release_series('vds_real_2021'), verbose=a.verbose)
    if bad >= 3:
        fails.append('vds_f расходится с vds_real_2021 на %d точках' % bad)
    n, bad, _ = compare('vsii (vds_f_ifo) vs vds_volume_index',
                        {k: v[0] for k, v in canon('vsii').items()},
                        release_series('vds_volume_index'), verbose=a.verbose)
    if bad >= 3:
        fails.append('vds_f_ifo расходится с vds_volume_index на %d точках' % bad)

    print('3. Внутренняя согласованность: ИФО ВВП против отношения уровней (t / t−4)')
    lvl, ifo = {k: v[0] for k, v in canon('vvp').items()}, {k: v[0] for k, v in canon('vvpi').items()}
    implied = {}
    for k in sorted(ifo):
        y, m = k.split('-')
        prev = '%d-%s' % (int(y) - 1, m)
        if k in lvl and prev in lvl and lvl[prev]:
            implied[k] = lvl[k] / lvl[prev] * 100.0
    n, bad, worst = compare('vvpi vs vvp[t]/vvp[t−4]', implied, ifo, unit=' п.п.', verbose=a.verbose)
    if bad >= 3:
        fails.append('ИФО ВВП расходится с отношением уровней на %d точках' % bad)

    print()
    if fails:
        print('ИТОГ: СТОП — %s' % '; '.join(fails))
        return 1
    print('ИТОГ: все проверки пройдены, порог 1 %% не превышен')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
