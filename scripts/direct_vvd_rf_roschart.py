#!/usr/bin/env python3
"""Ввод жилых домов по Российской Федерации, год — таблица 1.33 Росстата через roschart.

Источник: страница датасета `stroi-133-2025-vvod-v-deystvie-zhilyh-domov-
organizaciyami-r` на roschart.ru. Прежний путь (`/api/dataset/<slug>`) с
17.10.2026 отдаёт 401 Unauthorized; данные по-прежнему открыты и лежат в самой
странице — в теге `<script type="application/json">` как объект
`{periods, series[{slot,label,values}]}`. Разбор идёт по странице, API не
используется.

Что в таблице (18 лет: 2000, 2005, 2010–2025, ряды по slot):
  1 — всего, млн м²;  2 — удельный вес «всего» (100 %);
  3 — населением за счёт собственных и привлечённых средств, млн м²;
  4 — то же, удельный вес %;  5 — частная, удельный вес %;
  6 — частная, млн м²;  7 — смешанная, удельный вес % (источник пуст).

Две метрики, потому что единица измерения должна быть однозначной:
`vvdzh_rf` — площади в млн м², `vvdzh_rf_doli` — удельные веса в процентах.
Годы пишутся как есть (period = 1 января года данных); сверка с уже
загруженными годовыми рядами Росстата (`y477110016` — всего, `y477110015` —
населением, тыс. м²) печатается как приёмка: расхождение должно быть нулевым
с точностью до округления источника до 0,1 млн м². Новое здесь — 2025 год.

Запуск: python3 scripts/direct_vvd_rf_roschart.py [APPLY=1] [PRUNE=period]
"""

import csv
import gzip
import json
import os
import re
import ssl
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import db_tunnel as tunnel                                  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
URL = ('https://roschart.ru/dataset/'
       'stroi-133-2025-vvod-v-deystvie-zhilyh-domov-organizaciyami-r')
RELEASE = 'Stroit_1.33_2025 (roschart)'
SOURCE = 'rosstat'
M_ABS = 'Ввод в действие жилых домов по Российской Федерации (Росстат 1.33, через roschart), млн м2'
M_SHARE = 'Удельный вес категорий ввода жилых домов по Российской Федерации (Росстат 1.33), проценты'
DUMP = os.path.join(REPO, 'attic', 'vvd_rf_roschart_before.csv.gz')

# slot → (подразрез, единица канона, метрика)
SLOTS = {
    1: ('категория: всего | ед.: млн м2', 'million_m2', M_ABS),
    2: ('категория: всего (удельный вес) | ед.: процентов', 'percent', M_SHARE),
    3: ('категория: населением за счёт собственных и привлечённых средств | ед.: млн м2',
        'million_m2', M_ABS),
    4: ('категория: населением за счёт собственных и привлечённых средств (удельный вес) | ед.: процентов',
        'percent', M_SHARE),
    5: ('категория: частная (удельный вес) | ед.: процентов', 'percent', M_SHARE),
    6: ('категория: частная | ед.: млн м2', 'million_m2', M_ABS),
    7: ('категория: смешанная (удельный вес) | ед.: процентов', 'percent', M_SHARE),
}
# сверка: метрика канона (тыс. м²) ↔ слот загрузчика
CROSS = (('y477110016', 1, 'всего'), ('y477110015', 3, 'населением'))


def fetch():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    req = urllib.request.Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req, timeout=120, context=ctx).read().decode('utf-8', 'ignore')
    block = re.search(r'<script type="application/json"[^>]*>(.*?)</script>', html, re.S)
    if not block:
        raise SystemExit('в странице нет блока application/json — вёрстка изменилась')
    return json.loads(block.group(1))


def parse(d):
    years = [int(str(p)[:4]) for p in d['periods']]
    recs, report = [], []
    for s in d['series']:
        slot = s.get('slot')
        if slot not in SLOTS:
            report.append('незнакомый ряд slot=%s: %s' % (slot, s['label'][:70]))
            continue
        sub, unit, metric = SLOTS[slot]
        n = 0
        for year, val in zip(years, s['values']):
            if val is None:
                continue
            recs.append(dict(metric_name=metric, value=float(val), ps=(year, 0),
                             region='Российская Федерация', sub=sub, freq='A',
                             source=SOURCE, unit=unit, release=RELEASE))
            n += 1
        if n == 0:
            report.append('ряд пуст целиком: slot=%s (%s)' % (slot, sub[:46]))
        else:
            report.append('%-64s %d значений' % (sub[:64], n))
    return recs, report


def cross_check(recs):
    """Приёмка: сверить с годовыми рядами Росстата, уже стоящими в каноне."""
    mine = {}
    for r in recs:
        if r['metric_name'] == M_ABS:
            mine[(r['sub'].split('|')[0].strip(), r['ps'][0])] = r['value']
    key = {1: 'категория: всего', 3: 'категория: населением за счёт собственных и привлечённых средств'}
    out, worst = [], 0.0
    for code, slot, human in CROSS:
        old = dict(tunnel.query("""
            SELECT EXTRACT(year FROM o.period_start)::int, o.value
            FROM data.observation o JOIN core.metric m USING(metric_id)
            WHERE m.metric_code = %s AND o.region_id = 1""", (code,)))
        for year, val in sorted(old.items()):
            new = mine.get((key[slot], year))
            if new is None:
                continue
            diff = abs(new * 1000.0 - float(val))
            worst = max(worst, diff)
            if diff > 60.0:                     # источник округляет до 0,1 млн м², то есть до 50 тыс. м²
                out.append('   РАСХОЖДЕНИЕ %s %d: roschart %.1f млн | канон %.1f тыс. (+%.1f тыс.)'
                           % (human, year, new, float(val), diff))
    out.append('   сверено с y477110016/y477110015, худшее расхождение: %.1f тыс. м²' % worst)
    return out


def main():
    d = fetch()
    recs, report = parse(d)
    print('периоды: %s' % d['periods'])
    for r in report:
        print('  ', r)
    print('разобрано записей: %d' % len(recs))
    for line in cross_check(recs):
        print(line)
    last = {y: v for y, v in
            ((r['ps'][0], r['value']) for r in recs
             if r['sub'].startswith('категория: всего |'))}
    if last:
        y = max(last)
        print('   точка обновления: всего %d — %.1f млн м²' % (y, last[y]))
    if os.environ.get('APPLY') != '1':
        print('СУХОЙ ПРОГОН (APPLY=1 для записи)')
        return 0
    with gzip.open(DUMP, 'wt', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['metric_code', 'region_id', 'period', 'sub_dimension', 'value'])
        for r in tunnel.query("""
                SELECT m.metric_code, o.region_id, o.period_start::text,
                       o.sub_dimension, o.value::text
                FROM data.observation o JOIN core.metric m USING(metric_id)
                WHERE m.name_ru IN (%s, %s)""", (M_ABS, M_SHARE)):
            w.writerow([str(x) if x is not None else '' for x in r])
    print('дамп прежнего состояния: %s' % DUMP)
    from direct_core import Writer                           # noqa: E402
    w = Writer(tag='direct_vvd_rf_roschart')
    for r in recs:
        rid, parts = w.resolve_region({'region': r.get('region')}, 'region', None)
        r['region'] = rid
        if parts:
            r['sub'] = '%s | %s' % (r['sub'], ' | '.join(parts))
    prep, ins, conf, new = w.ingest(recs, group='', prune=os.environ.get('PRUNE', ''))
    w.close()
    print('подготовлено %d | вставлено %d | конфликтов %d | новых метрик %d'
          % (prep, ins, conf, new))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
