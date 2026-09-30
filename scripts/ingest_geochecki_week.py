#!/usr/bin/env python3
"""Инжест еженедельного CSV геочек ФНС в БД v2 (АФ-агрегаты РФ).

Вход /home/lnr/research-wiki-private/data/geochecki_week_YYYYWNN.csv
Выход: наблюдения в core.observation_v2 для метрик gchk_*_rf_w.
Идемпотентен: ON CONFLICT DO NOTHING.
"""
import csv
import json
import os
import sys
from statistics import mean

sys.path.insert(0, '/home/lnr/research-wiki-private/scripts')
from db_tunnel import execute, query

CSV_PATH = sys.argv[1] if len(sys.argv) > 1 else None

def parse_num(v):
    if v in (None, '', 'null'):
        return None
    try:
        return float(v)
    except Exception:
        return None

def main():
    path = CSV_PATH
    if not path or not os.path.exists(path):
        print("no csv path"); sys.exit(1)
    rows = list(csv.DictReader(open(path)))
    if not rows:
        print("empty"); sys.exit(1)
    period_start = rows[0]['period_start'][:10]
    period_end = rows[0]['period_end'][:10]
    # метрики
    m = {}
    for code, _, _ in query("SELECT metric_code, 1, 1 FROM core.metric WHERE metric_code LIKE 'gchk%'"):
        rid = query("SELECT metric_id FROM core.metric WHERE metric_code=%s", (code,))
        m[code] = rid[0][0]
    need = {
        'gchk_revenue_int_rf_w': [], 'gchk_receipts_int_rf_w': [],
        'gchk_avg_bill_rf_w': [], 'gchk_hex_active_rf_w': [],
    }
    for r in rows:
        if not r['hex_centroid'] or ',' not in r['hex_centroid']:
            continue
        lng_s, lat_s = r['hex_centroid'].split(',')
        lng, lat = float(lng_s), float(lat_s)
        # РФ bbox: 27-180 lng (Калининград 19.5+), 41-80 lat; исключение: вне РФ территории (Казахстан и др. по centroid не отличить — прим. bbox)
        if not (27.5 <= lng <= 180 and 41 <= lat <= 80):
            continue
        # RevenueIntensity / Intensity NumberBills — целые
        if r['revenue_intensity'] not in ('', 'null', None):
            need['gchk_revenue_int_rf_w'].append(float(r['revenue_intensity']))
        if r['bills_intensity'] not in ('', 'null', None):
            need['gchk_receipts_int_rf_w'].append(float(r['bills_intensity']))
        if r['average_bill'] and r['average_bill'].startswith('['):
            try:
                need['gchk_avg_bill_rf_w'].append(float(json.loads(r['average_bill'])[0]))
            except Exception:
                pass
    need['gchk_hex_active_rf_w'] = [float(len(need['gchk_revenue_int_rf_w']))]  # 1 значение
    # Средние
    values = {
        'gchk_revenue_int_rf_w': mean(need['gchk_revenue_int_rf_w']),
        'gchk_receipts_int_rf_w': mean(need['gchk_receipts_int_rf_w']),
        'gchk_avg_bill_rf_w': mean(need['gchk_avg_bill_rf_w']),
        'gchk_hex_active_rf_w': need['gchk_hex_active_rf_w'][0],
    }
    print("aggregates:", {k: round(v, 3) for k, v in values.items()})
    release_id = query("SELECT max(release_id) FROM core.release")[0][0]
    inserted = 0
    for code, val in values.items():
        mid = m.get(code)
        if mid is None:
            continue
        execute("""INSERT INTO core.observation_v2 (metric_id, region_id, frequency_id, period_start, period_end, value,
        observation_status, assessment_type, source_id, release_id)
        SELECT %s, 1, %s, %s, %s, %s, 'validated', 'final', 9, %s
        WHERE NOT EXISTS (SELECT 1 FROM core.observation_v2 WHERE metric_id=%s AND period_start=%s)""",
        (mid, 15, period_start, period_end, val, release_id, mid, period_start))
        inserted += 1
    print("inserted metrics:", inserted)
    # верификация
    for code in need:
        q = query("""SELECT o.period_start, o.value FROM core.observation_v2 o
        JOIN core.metric m ON m.metric_id=o.metric_id WHERE m.metric_code=%s ORDER BY period_start DESC LIMIT 2""", (code,))
        print(code, q)

if __name__ == '__main__':
    main()