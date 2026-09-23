#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Универсальный сбор данных мониторинга предприятий ЦБ из API в SQLite.

Покрывает:
- pub25 (Данные мониторинга всего): все сектора, ежемес. + квартальные (ИА,
  загрузка мощностей, персонал, ожидания) — datasetId 58-79, 140;
- pub28/29/30 (мониторинг по группам предприятий: крупные/средние/малые):
  14 метрик каждая — datasetId 80-121.

Датировка (проверена сверкой с XLSX 135603):
- месячные ряды: API date = отчётный период + 2 мес -> в БД date - 2 мес;
- квартальные ряды: dt = 'N квартал YYYY' — отчётный квартал напрямую
  (date = первый месяц следующего квартала), в БД 'YYYYQn'.

Идемпотентен: DROP + CREATE + полная перезагрузка.
"""
import urllib.request, ssl, json, sqlite3, os, re

BASE = 'https://www.cbr.ru/dataservice'
DB = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                  'data', 'rosstat_construction.db')
SOURCE = 'cbr_api_monitoring_v2'
SCOPE = [
    (25, list(range(58, 80)) + [140]),          # весь мониторинг по секторам
    (28, [80, 83, 86, 89, 92, 95, 98, 101, 104, 107, 110, 113, 116, 119]),  # крупные
    (29, [81, 84, 87, 90, 93, 96, 99, 102, 105, 108, 111, 114, 117, 120]),  # средние
    (30, [82, 85, 88, 91, 94, 97, 100, 103, 106, 109, 112, 115, 118, 121]), # малые и микро
]
MEASURES = [(118, 'Исходные данные'), (119, 'Сезонно скорректированные данные')]
GROUP_NAME = {28: 'Крупные', 29: 'Средние', 30: 'Малые и микро'}
QUART_RE = re.compile(r'(I{1,3}|IV)\s+квартал\s+(\d{4})')
QUART_NUM = {'I': 1, 'II': 2, 'III': 3, 'IV': 4}


def get_json(url):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    return json.loads(urllib.request.urlopen(req, timeout=90, context=ctx).read().decode('utf-8', 'ignore'))


def norm_date_monthly(iso):
    """API date - 2 месяца -> YYYY-MM-01."""
    y, m = int(iso[:4]), int(iso[5:7])
    m2, y2 = (m - 2, y) if m > 2 else (m + 10, y - 1)
    return '%s-%02d-01' % (y2, m2)


def norm_period(r):
    """Единый период: месячные -> YYYY-MM-01 (сдвиг -2), квартальные -> YYYYQn (по dt)."""
    dt = (r.get('dt') or '').strip()
    mq = QUART_RE.match(dt)
    if mq:
        return '%sQ%d' % (mq.group(2), QUART_NUM[mq.group(1)])
    return norm_date_monthly(r['date'][:10])


def main():
    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.execute('DROP TABLE IF EXISTS cbr_monitoring_api')
    cur.execute('CREATE TABLE cbr_monitoring_api ('
                'dataset TEXT, size_group TEXT, adjustment TEXT, question TEXT, '
                'unit TEXT, period TEXT, value REAL, source TEXT)')
    total = 0
    for pub_id, ds_ids in SCOPE:
        for ds_id in ds_ids:
            try:
                dsn = get_json(f'{BASE}/datasets?publicationId={pub_id}')
                items = dsn if isinstance(dsn, list) else dsn.get('dataset', [])
                ds_name = next((d.get('dataset_name') or d.get('name')
                                for d in items if d.get('id') == ds_id), str(ds_id))
            except Exception:
                ds_name = str(ds_id)
            for mid, adj in MEASURES:
                try:
                    d = get_json(f'{BASE}/data?y1=2002&y2=2026&datasetId={ds_id}'
                                 f'&publicationId={pub_id}&measureId={mid}')
                except Exception as e:
                    if getattr(e, 'code', None) == 501:
                        continue
                    raise
                rows = d.get('RawData', [])
                if not rows:
                    continue
                hdr = {h['id']: h['elname'] for h in d.get('headerData', [])}
                units = {u['id']: u['val'] for u in d.get('units', [])}
                group = GROUP_NAME.get(pub_id, 'Экономика всего')
                out = [(ds_name, group, adj,
                        hdr.get(r['element_id'], str(r['element_id'])),
                        units.get(r['unit_id'], ''),
                        norm_period(r), r['obs_val'], SOURCE) for r in rows]
                cur.executemany('INSERT INTO cbr_monitoring_api VALUES (?,?,?,?,?,?,?,?)', out)
                total += len(out)
            print(f'pub{pub_id} ds{ds_id} ({ds_name[:30]}): накоплено {total}')
    con.commit()
    print('ИТОГО строк:', total)
    for r in cur.execute('SELECT size_group, COUNT(DISTINCT question), COUNT(*), MIN(period), MAX(period) '
                         'FROM cbr_monitoring_api GROUP BY size_group'):
        print(r)
    # контрольные точки строительства
    for adj, dsname, per, q, exp in [('Исходные данные', 'Строительство', '2026-04-01', 'Индикатор бизнес-климата Банка России', 11.1019),
                          ('Сезонно скорректированные данные', 'Строительство', '2026-08-01', 'Индикатор бизнес-климата Банка России', -3.1102),
                          ('Исходные данные', 'Инвестиционная активность', '2026Q2', 'Экономика всего*', 2.3904)]:
        v = cur.execute("SELECT value FROM cbr_monitoring_api WHERE dataset=? "
                        "AND size_group='Экономика всего' AND adjustment=? AND period=? "
                        "AND question LIKE ?", (dsname, adj, per, q + '%')).fetchall()
        ok = any(x and abs(x[0] - exp) < 0.01 for x in v)
        print(f'контроль {dsname} {adj[:4]} {per}={exp}:', 'OK' if ok else f'FAIL {v}')
    con.close()


if __name__ == '__main__':
    main()