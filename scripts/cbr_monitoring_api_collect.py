#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Сбор данных мониторинга предприятий ЦБ (ИБК) из универсального API ЦБ в SQLite.

Датировка API: date = отчётный период + 2 мес (dt = месяц опроса).
Идемпотентен: DROP + CREATE + полная перезагрузка.
"""
import urllib.request, ssl, json, sqlite3, os

BASE = 'https://www.cbr.ru/dataservice/data'
DB = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                  'data', 'rosstat_construction.db')
MEASURES = [(118, 'Исходные данные'), (119, 'Сезонно скорректированные данные')]
SOURCE = 'cbr_api_monitoring_v2'


def get_json(url):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    return json.loads(urllib.request.urlopen(req, timeout=90, context=ctx).read().decode('utf-8', 'ignore'))


def shift_minus_2(iso):
    y, m = int(iso[:4]), int(iso[5:7])
    m2, y2 = (m - 2, y) if m > 2 else (m + 10, y - 1)
    return '%s-%02d-01' % (y2, m2)


def main():
    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.execute('DROP TABLE IF EXISTS cbr_monitoring_construction')
    cur.execute('CREATE TABLE cbr_monitoring_construction ('
                'question TEXT, adjustment TEXT, unit TEXT, date TEXT, value REAL, source TEXT)')
    total = 0
    for mid, adj in MEASURES:
        d = get_json('%s?y1=2002&y2=2026&datasetId=68&publicationId=25&measureId=%d' % (BASE, mid))
        hdr = {h['id']: h['elname'] for h in d['headerData']}
        units = {u['id']: u['val'] for u in d['units']}
        rows = [(hdr.get(r['element_id'], str(r['element_id'])), adj,
                 units.get(r['unit_id'], ''), shift_minus_2(r['date'][:10]),
                 r['obs_val'], SOURCE) for r in d['RawData']]
        cur.executemany('INSERT INTO cbr_monitoring_construction VALUES (?,?,?,?,?,?)', rows)
        print('measureId=%d (%s): %d строк' % (mid, adj, len(rows)))
        total += len(rows)
    con.commit()
    print('итого:', total)
    for r in cur.execute('SELECT adjustment, COUNT(*), MIN(date), MAX(date) '
                         'FROM cbr_monitoring_construction GROUP BY adjustment'):
        print(r)
    con.close()


if __name__ == '__main__':
    main()