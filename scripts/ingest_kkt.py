#!/usr/bin/env python3
"""Инжест ККТ-статистики ФНС (geochecki) в БД v2.

Источник: презентационная аналитика ФНС (geochecki-vpd.nalog.gov.ru).
Входы: data/kkt_summary.csv (68 строк), data/kkt_regions/*.json (68 файлов),
data/kkt_dynamics/*.json (6 файлов).
Метрики:
- kkt_revenue_m (млн руб, помесячная выручка по всем ККТ РФ)
- kkt_count_m (шт, парк ККТ на конец месяца)
- kkt_bills_m (шт, число чеков за месяц)
Региональная разбивка count-by-regions хранится как две метрики по регионам:
- kkt_count_ip_m, kkt_count_ul_m (шт, парк ККТ ИП / ЮЛ на конец месяца)
"""
import csv
import json
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import db_tunnel  # noqa: E402

BASE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SOURCE_ID = 9  # fns

# ФНС-код (первые 2 цифры) -> okato первой цифры региона из core.region
FNS_TO_OKATO_HINT = {
    '31': '14', '32': '15', '33': '17', '36': '20', '34': '19', '35': '22',
}


def period_to_db(per: str):
    y, m = per.split('-')
    return f"{y}-{int(m):02d}-01"


def ensure_release(cur):
    cur.execute("SELECT release_id FROM core.release WHERE release_label=%s",
                ('fns_kkt_geochecki_2026-09',))
    r = cur.fetchone()
    if r:
        return r[0]
    cur.execute("""INSERT INTO core.release (source_id, release_label, published_at, status, notes)
        VALUES (%s, %s, '2026-09-25', 'loaded', 'ККТ помесячно 2021-01..2026-08: summary РФ + разбивка по регионам ИП/ЮЛ') RETURNING release_id""",
                (SOURCE_ID, 'fns_kkt_geochecki_2026-09'))
    return cur.fetchone()[0]


def ensure_metric(cur, code, name, freq_id, unit_id, description=''):
    cur.execute("SELECT metric_id FROM core.metric WHERE metric_code=%s", (code,))
    r = cur.fetchone()
    if r:
        return r[0]
    cur.execute("""INSERT INTO core.metric
        (metric_code, name_ru, description, frequency_id, unit_id, metric_type, is_derived, status)
        VALUES (%s, %s, %s, %s, %s, 'primary', FALSE, 'active') RETURNING metric_id""",
        (code, name, description, freq_id, unit_id))
    return cur.fetchone()[0]


def insert_obs(cur, metric_id, region_id, period_yyyy_mm, value, release_id):
    per = period_to_db(period_yyyy_mm)
    if value is None:
        return 0
    cur.execute("""SELECT 1 FROM core.observation_v2
        WHERE metric_id=%s AND region_id=%s AND frequency_id=5
          AND period_start=%s AND sub_dimension='' LIMIT 1""",
        (metric_id, region_id, per))
    if cur.fetchone():
        return 0
    cur.execute("""INSERT INTO core.observation_v2
        (metric_id, region_id, frequency_id, period_start, period_end, value,
         assessment_type, observation_status, source_id, release_id, sub_dimension)
        VALUES (%s, %s, 5, %s, %s, %s, 'final', 'validated', %s, %s, '')""",
        (metric_id, region_id, per, per, value, SOURCE_ID, release_id))
    return 1


def month_sort(per):
    y, m = per.split('-')
    return (int(y), int(m))


def main():
    conn = db_tunnel.connect()
    if conn is None:
        raise RuntimeError("db_tunnel.connect() не вернул соединение")
    cur = conn.cursor()
    release_id = ensure_release(cur)

    # Полный маппинг ФНС-код (2 цифры) -> region_code в core.region
    FNS_TO_CODE = {
        '01': 'adygea', '02': 'bashkortostan', '03': 'buryatia', '04': 'altai_rep',
        '05': 'dagestan', '06': 'ingushetia', '07': 'kabardino', '08': 'kalmykia',
        '09': 'karachaevo', '10': 'karelia', '11': 'komi', '12': 'marij_el',
        '13': 'mordovia', '14': 'sakha', '15': 'north_ossetia', '16': 'tatarstan',
        '17': 'tuva', '18': 'udmurtia', '19': 'khakasia', '21': 'chuvashia',
        '22': 'altai_terr', '23': 'krasnodar', '24': 'krasnoyarsk', '25': 'primorsky',
        '26': 'stavropol', '27': 'khabarovsk', '28': 'amur', '29': 'arkhangelsk',
        '30': 'astrakhan', '31': 'belgorod', '32': 'bryansk', '33': 'vladimir',
        '34': 'volgograd', '35': 'vologda', '36': 'voronezh', '37': 'ivanovo',
        '38': 'irkutsk', '39': 'kaliningrad', '40': 'kaluga', '41': 'kamchatka',
        '42': 'kemerovo', '43': 'kirov', '44': 'kostroma', '45': 'kurgan',
        '46': 'kursk', '47': 'leningrad', '48': 'lipetsk', '49': 'magadan',
        '50': 'moscow_obl', '51': 'murmansk', '52': 'nizhni', '53': 'novgorod',
        '54': 'novosibirsk', '55': 'omsk', '56': 'orenburg', '57': 'oryol',
        '58': 'penza', '59': 'perm', '60': 'pskov', '61': 'rostov', '62': 'ryazan',
        '63': 'samara', '64': 'saratov', '65': 'sakhalin', '66': 'sverdlovsk',
        '67': 'smolensk', '68': 'tambov', '69': 'tver', '70': 'tomsk', '71': 'tula',
        '72': 'tyumen', '73': 'ulyanovsk', '75': 'zabaikalsk', '76': 'yaroslavl',
        '77': 'moscow', '78': 'spb', '79': 'jewish_ao', '83': 'nenets_ao',
        '86': 'khanty', '87': 'chukotka', '89': 'yamal', '91': 'crimea',
        '92': 'sevastopol', '20': 'chechnya', '74': 'chelyabinsk',
        '90': 'zaporozhye', '93': 'dnr', '94': 'lnr', '95': 'kherson',
    }

    # 1) РФ-сводные метрики
    m_rev = ensure_metric(cur, 'kkt_revenue_m', 'Выручка по ККТ, млн руб в месяц',
                          5, 11, 'Суммарная выручка по всем чекам ККТ РФ (geochecki ФНС)')
    m_cnt = ensure_metric(cur, 'kkt_count_m', 'Парк ККТ на конец месяца, шт',
                          5, 29, 'Число зарегистрированных ККТ')
    m_bill = ensure_metric(cur, 'kkt_bills_m', 'Число чеков ККТ за месяц, млн шт',
                           5, 29, 'Количество чеков по всем ККТ РФ')

    n = 0
    batch = []
    with open(os.path.join(BASE, 'data', 'kkt_summary.csv'), newline='') as f:
        for row in csv.DictReader(f):
            per = row['period']
            p = period_to_db(per)
            if row['revenue_rub']:
                batch.append((m_rev, 1, p, p, round(float(row['revenue_rub']) / 1e6, 2), SOURCE_ID, release_id))
            if row['kkt_count']:
                batch.append((m_cnt, 1, p, p, float(row['kkt_count']), SOURCE_ID, release_id))
            if row['bills']:
                batch.append((m_bill, 1, p, p, float(row['bills']), SOURCE_ID, release_id))
    print('РФ-батч:', len(batch))
    # дедуп: выбираем существующие
    existing = set()
    for mid, rid in ((m_rev, 1), (m_cnt, 1), (m_bill, 1)):
        cur.execute("SELECT period_start FROM core.observation_v2 WHERE metric_id=%s AND region_id=1 AND frequency_id=5", (mid,))
        existing.update((mid, r[0].strftime('%Y-%m-%d')) for r in cur.fetchall())
    batch = [r for r in batch if (r[0], r[2]) not in existing]
    if batch:
        args = ','.join(db_tunnel.psycopg.sql and "(%s,%s,5,%s,%s,%s,'final','validated',%s,%s,'')" for b in batch)
        cur.executemany("INSERT INTO core.observation_v2 (metric_id, region_id, frequency_id, period_start, period_end, value, assessment_type, observation_status, source_id, release_id, sub_dimension) VALUES (%s,%s,5,%s,%s,%s,'final','validated',%s,%s,'')", batch)
    print('РФ-точек вставлено:', len(batch))

    # 2) Региональная разбивка
    # строим маппинг ФНС-код (2 цифры) -> region_id
    # реальный маппинг: region_code -> region_id
    cur.execute("SELECT region_id, region_code FROM core.region")
    rid_by_code = {r[1]: r[0] for r in cur.fetchall()}
    code_map = {fns: rid_by_code[c] for fns, c in FNS_TO_CODE.items() if c in rid_by_code}

    nreg = 0
    unmapped = set()
    # ensure metrics до цикла
    m_ip = ensure_metric(cur, 'kkt_count_ip_m', 'Парк ККТ ИП на конец месяца, шт',
                         5, 29, 'Разбивка парка ККТ по регионам: ИП')
    m_ul = ensure_metric(cur, 'kkt_count_ul_m', 'Парк ККТ ЮЛ на конец месяца, шт',
                         5, 29, 'Разбивка парка ККТ по регионам: ЮЛ')
    existing_reg = set()
    for mid in (m_ip, m_ul):
        cur.execute("SELECT metric_id, region_id, period_start FROM core.observation_v2 WHERE metric_id=%s AND frequency_id=5", (mid,))
        existing_reg.update((r[0], r[1], r[2].strftime('%Y-%m-%d')) for r in cur.fetchall())
    reg_batch = []
    for fp in sorted(glob.glob(os.path.join(BASE, 'data', 'kkt_regions', '*.json')),
                     key=lambda p: month_sort(re.search(r'(\d{4}-\d{1,2})', p).group(1))):
        per = re.search(r'(\d{4}-\d{1,2})', fp).group(1)
        p = period_to_db(per)
        d = json.load(open(fp))
        for it in d['items']:
            m = re.match(r'^(\d{2})-', it['region'])
            if not m:
                continue
            fns = m.group(1)
            rid = code_map.get(fns)
            if rid is None:
                unmapped.add(it['region'])
                continue
            if it.get('entrepreneur') is not None:
                reg_batch.append((m_ip, rid, p, p, it['entrepreneur'], SOURCE_ID, release_id))
            if it.get('legalEntity') is not None:
                reg_batch.append((m_ul, rid, p, p, it['legalEntity'], SOURCE_ID, release_id))
    reg_batch = [r for r in reg_batch if (r[0], r[1], r[2]) not in existing_reg]
    print('Региональный батч:', len(reg_batch))
    for i in range(0, len(reg_batch), 500):
        chunk = reg_batch[i:i + 500]
        cur.executemany("INSERT INTO core.observation_v2 (metric_id, region_id, frequency_id, period_start, period_end, value, assessment_type, observation_status, source_id, release_id, sub_dimension) VALUES (%s,%s,5,%s,%s,%s,'final','validated',%s,%s,'') ON CONFLICT DO NOTHING", chunk)
        conn.commit()
    print('Региональных точек вставлено:', len(reg_batch))
    if unmapped:
        print('Не смэппированы ФНС-коды:', sorted(unmapped)[:10])

    conn.commit()
    print('Релиз:', release_id, '— готово')


if __name__ == '__main__':
    main()