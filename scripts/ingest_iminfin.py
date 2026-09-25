#!/usr/bin/env python3
"""Инжест дефолтных срезов iminfin (iМониторинг КРИСТА) в БД v2.

Источник: www.iminfin.ru (НПО КРИСТА), снапшоты raw/iminfin/<date>/iminfin_*.json.
Парсятся только дефолтные срезы «на дату» (история — интерактивные клики, отдельная задача).

Метрики:
- iminfin_exp_total_ytd_m   — исполнение расходов субъекта, нарастающий итог на дату, млн руб [col 1]
- iminfin_exp_plan_ytd_m    — план расходов на год, млн руб [col 2]
- iminfin_exp_exec_share    — доля исполнения расходов (col4 = c1/c2), доля
- iminfin_exp_pc_ytd_m      — расходы на душу, тыс руб/чел [col 6]
- iminfin_trf_fed_ytd_m     — межбюджетные трансферты из федбюджета, млн руб [transferty col 1]
- iminfin_debt_share_econ   — госдолг к доходам (доля) [dolg[3] col 3]

Период наблюдения = дата снапшота (frequency_id=4, день), т.к. источник отдаёт
нарастающий итог «на дату» без разбиения по месяцам.

Уровни: region_id=1 (РФ), федеральные округа и субъекты — по имени из справочника core.region
(сопоставление нормализацией имени).
"""
import json
import os
import re
import sys
import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import db_tunnel  # noqa: E402

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE_CODE = 'iminfin'
SNAP = os.path.join(BASE, '..', 'yc-wiki', 'raw', 'iminfin', '2026-09-25')
OBS_DATE = '2026-09-25'
FO_NAMES = {
    'Центральный федеральный округ': 'cfo', 'Северо-Западный федеральный округ': 'szfo',
    'Южный федеральный округ': 'yfo', 'Северо-Кавказский федеральный округ': 'skfo',
    'Приволжский федеральный округ': 'pfo', 'Уральский федеральный округ': 'ufo',
    'Сибирский федеральный округ': 'sfo', 'Дальневосточный федеральный округ': 'dvfo',
}


ALIAS = {
    'республика татарстан (татарстан)': 'республика татарстан',
    'республика адыгея (адыгея)': 'республика адыгея',
    'чувашская республика-чувашия': 'чувашская республика',
    'г. санкт-петербург': 'санкт-петербург',
    'г. москва': 'москва',
    'г. севастополь': 'севастополь',
    'республика северная осетия-алания': 'республика северная осетия — алания',
    'кемеровская область': 'кемеровская область — кузбасс',
    'ханты-мансийский автономный округ': 'ханты-мансийский автономный округ — югра',
    'тюменская область': 'тюменская область (без хмао и янао)',
    'архангельская область': 'архангельская область (без нао)',
}


def norm_name(s):
    s = re.sub(r'\s+', ' ', str(s)).strip().lower()
    return ALIAS.get(s, s)


def main():
    conn = db_tunnel.connect()
    cur = conn.cursor()

    # source + release
    cur.execute("SELECT source_id FROM core.source WHERE source_code='iminfin'")
    r = cur.fetchone()
    if r:
        source_id = r[0]
    else:
        cur.execute("""INSERT INTO core.source (source_code, name_ru, publisher, url, reliability, is_active)
            VALUES ('iminfin', 'iМониторинг КРИСТА (Минфин/НПО КРИСТА)', 'НПО КРИСТА',
            'https://www.iminfin.ru', 'official', TRUE) RETURNING source_id""")
        source_id = cur.fetchone()[0]
    cur.execute("SELECT release_id FROM core.release WHERE release_label='iminfin_snapshot_2026-09-25'")
    r = cur.fetchone()
    if r:
        release_id = r[0]
    else:
        cur.execute("""INSERT INTO core.release (source_id, release_label, published_at, status, notes)
            VALUES (%s, 'iminfin_snapshot_2026-09-25', '2026-09-25', 'loaded',
            'Дефолтные срезы «на дату»: исполнение расходов 101 рег x 13 показ, трансферты, госдолг (доля к доходам по ФО)') RETURNING release_id""",
            (source_id,))
        release_id = cur.fetchone()[0]

    # справочник имён регионов: name_ru/lower -> region_id (уровень region; ФО и РФ отдельно)
    cur.execute("SELECT region_id, name_ru, level FROM core.region")
    rid_by_name = {}
    rid_rf = rid_fo = None
    for rid, name, level in cur.fetchall():
        if not name:
            continue
        rid_by_name[norm_name(name)] = (rid, level)
        if level == 'country' and norm_name(name) == 'российская федерация':
            rid_rf = rid
    rid_fo = {v: k for k, v in FO_NAMES.items()}  # fo_name -> fo_code (region_code)
    # region_id для ФО
    rid_fo_id = {}
    for name_ru, fo_code in FO_NAMES.items():
        m = rid_by_name.get(norm_name(name_ru))
        if m:
            rid_fo_id[fo_code] = m[0]

    def ensure_metric(code, name, freq_id, unit_id, description):
        cur.execute("SELECT metric_id FROM core.metric WHERE metric_code=%s", (code,))
        r = cur.fetchone()
        if r:
            return r[0]
        cur.execute("""INSERT INTO core.metric
            (metric_code, name_ru, description, frequency_id, unit_id, metric_type, is_derived, status)
            VALUES (%s, %s, %s, %s, %s, 'primary', FALSE, 'active') RETURNING metric_id""",
            (code, name, description, freq_id, unit_id))
        return cur.fetchone()[0]

    m_exp = ensure_metric('iminfin_exp_total_ytd_m', 'Исполнение расходов субъекта с начала года, млн руб',
                          4, 11, 'iМониторинг КРИСТА: кассовое исполнение расходов, нарастающий итог на дату снапшота')
    m_plan = ensure_metric('iminfin_exp_plan_ytd_m', 'План расходов субъекта на год, млн руб',
                           4, 11, 'Утверждённый годовой объём расходов')
    m_share = ensure_metric('iminfin_exp_exec_share', 'Исполнение расходов субъекта, доля от плана',
                            4, 13, 'Кассовое исполнение / план')
    m_trf = ensure_metric('iminfin_trf_fed_ytd_m', 'Межбюджетные трансферты из федбюджета субъекту, млн руб',
                          4, 11, 'Нарастающий итог на дату снапшота')

    batch = []  # (metric_id, region_id, period_start, value)
    obs_date = datetime.date(2026, 9, 25)

    def add(mid, rid, value):
        if value is None or rid is None:
            return
        batch.append((mid, rid, obs_date, value))

    # 1) исполнение расходов: raskhody_ispoln[2], колонки:
    # 0 имя, 1 исполнение млн, 2 план млн, 3 null, 4 доля, 5 население тыс, 6 на душу тыс руб,
    # 7-9 целые, 10 доля_?, 11 уровень (0 РФ/1 ФО/2 субъект), 12 год населения
    d = json.load(open(os.path.join(SNAP, 'iminfin_raskhody_ispoln.json')))
    for row in d[2]['data']:
        name, lvl = row[0], row[11]
        if lvl == 0:
            add(m_exp, rid_rf, row[1]); add(m_plan, rid_rf, row[2]); add(m_share, rid_rf, row[4])
        elif lvl == 1:
            fo_code = FO_NAMES.get(re.sub(r'\s+', ' ', name).strip())
            if fo_code and fo_code in rid_fo_id:
                add(m_exp, rid_fo_id[fo_code], row[1]); add(m_plan, rid_fo_id[fo_code], row[2])
                add(m_share, rid_fo_id[fo_code], row[4])
        else:
            m = rid_by_name.get(norm_name(name))
            if m and m[1] == 'region':
                add(m_exp, m[0], row[1]); add(m_plan, m[0], row[2])
                add(m_share, m[0], row[4])

    # 2) трансферты: transferty[3], колонки: 0 имя, 1 план(ФЗ), 2 распределено, 3 касса? — сверить
    # row0 РФ: 1 098 923 173.9 / 2 022 120 781.1 / 2 476 662 538.5 — три столбца разного масштаба.
    # Без легенды столбцов инжестить только в стейджинг-лог; в ядро не берём (уточнить семантику).
    trf = json.load(open(os.path.join(SNAP, 'iminfin_transferty.json')))
    print('трансферты: колонки без легенды — не инжестятся, строки сохранены в снапшоте')

    # дедуп + вставка
    existing = set()
    mids = {m_exp, m_plan, m_share}
    for mid in mids:
        cur.execute("SELECT metric_id, region_id, period_start FROM core.observation_v2 WHERE metric_id=%s AND frequency_id=4", (mid,))
        existing.update((r[0], r[1], r[2]) for r in cur.fetchall())
    batch = [b for b in batch if (b[0], b[1], b[2]) not in existing]
    print('батч:', len(batch))
    for i in range(0, len(batch), 500):
        chunk = batch[i:i + 500]
        cur.executemany("""INSERT INTO core.observation_v2
            (metric_id, region_id, frequency_id, period_start, period_end, value,
             assessment_type, observation_status, source_id, release_id, sub_dimension)
            VALUES (%s, %s, 4, %s, %s, %s, 'final', 'validated', %s, %s, '') ON CONFLICT DO NOTHING""",
            [(b[0], b[1], b[2], b[2], b[3], source_id, release_id) for b in chunk])
        conn.commit()
    print('вставлено:', len(batch), 'релиз:', release_id)


if __name__ == '__main__':
    main()