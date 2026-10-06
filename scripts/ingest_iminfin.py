#!/usr/bin/env python3
"""Инжест дефолтных срезов iminfin (iМониторинг КРИСТА) в БД — каноническая схема.

Источник: www.iminfin.ru (НПО КРИСТА), снапшоты raw/iminfin/<date>/iminfin_*.json.
Парсятся только дефолтные срезы «на дату» (история — интерактивные клики, отдельная задача).

Каноническая схема: catalog.source, catalog.metric, catalog.release,
data.observation, catalog.region. Никаких compat-слоёв (core.*).

Метрики (6):
- iminfin_exp_total_ytd_m   — исполнение расходов субъекта, нарастающий итог на дату, млн руб [raskhody col 1]
- iminfin_exp_plan_ytd_m    — план расходов на год, млн руб [raskhody col 2]
- iminfin_exp_exec_share    — доля исполнения расходов (col4 = col1/col2), доля [raskhody col 4]
- iminfin_exp_pc_ytd_m      — расходы на душу, тыс руб/чел [raskhody col 6]
- iminfin_trf_fed_ytd_m     — межбюджетные трансферты из федбюджета, млн руб [transferty col 0 или col 1, /1e3]
- iminfin_debt_share_econ   — госдолг к доходам (доля) [dolg[3] col 2], только ФО

Единицы измерения:
- raskhody: raw в млн руб → пишем as-is (unit=11, mln_rub)
- exp_pc: raw в тыс руб/чел → пишем as-is (unit=15, ths_rub)
- transferty: raw в тыс руб → делим на 1e3 → млн руб (unit=11, mln_rub)
- debt_share: raw в долях → пишем as-is (unit=12, pct)
- exec_share: raw в долях → пишем as-is (unit=13, pct_pts)

Период наблюдения = дата снапшота (frequency_id=4, день), т.к. источник отдаёт
нарастающий итог «на дату» без разбиения по месяцам.

Уровни: region_id=1 (РФ), федеральные округа (8) и субъекты (91) — по имени
из catalog.region (сопоставление нормализацией имени).

Трансферты: col0 (план по ФЗ) — предпочтительный; при None → col1 (распределено).
27 регионов (Москва, СПб, Татарстан и др.) имеют None в col0, но данные в col1.

Исправления (06.10.2026):
- Переписано с core.* на catalog.*/data.* (каноническая схема)
- exp_pc: col6 (на душу) вместо col5 (население) — баг предыдущей версии
- transferty: /1e3 вместо /1e6 — raw в тыс. руб, не рублях
- transferty: загрузка регионов с None col0 через col1 (распределено)
- Цикл по всем снапшотам в raw/iminfin/, не один захардкоженный
"""
import json
import os
import re
import sys
import datetime
import glob

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import db_tunnel  # noqa: E402

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_BASE = os.path.join(BASE, '..', 'yc-wiki', 'raw', 'iminfin')
SOURCE_CODE = 'iminfin'
FREQ_ID = 4  # дневная (дата снапшота)

FO_NAMES = {
    'Центральный федеральный округ': 'cfo', 'Северо-Западный федеральный округ': 'szfo',
    'Южный федеральный округ': 'yfo', 'Северо-Кавказский федеральный округ': 'skfo',
    'Приволжский федеральный округ': 'pfo', 'Уральский федеральный округ': 'ufo',
    'Сибирский федеральный округ': 'sfo', 'Дальневосточный федеральный округ': 'dvfo',
}

# Нормализация имён регионов iminfin → catalog.region
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


def load_regions(cur):
    """Загружает справочник регионов из catalog.region."""
    cur.execute("SELECT region_id, name_ru, level, is_active FROM catalog.region")
    rid_by_name = {}
    rid_rf = None
    rid_fo = {}  # fo_name → region_id
    for rid, name, level, is_active in cur.fetchall():
        if not name or not is_active:
            continue
        key = norm_name(name)
        rid_by_name[key] = (rid, level)
        if level == 'country' and key == 'российская федерация':
            rid_rf = rid
    for fo_name in FO_NAMES:
        m = rid_by_name.get(norm_name(fo_name))
        if m:
            rid_fo[fo_name] = m[0]
    return rid_by_name, rid_rf, rid_fo


def ensure_source(cur):
    """Возвращает source_id для iminfin из catalog.source."""
    cur.execute("SELECT source_id FROM catalog.source WHERE source_code = %s", (SOURCE_CODE,))
    r = cur.fetchone()
    if r:
        return r[0]
    cur.execute("""
        INSERT INTO catalog.source (source_code, name_ru, publisher, url, reliability, is_active)
        VALUES (%s, 'iМониторинг КРИСТА (Минфин/НПО КРИСТА)', 'НПО КРИСТА',
                'https://www.iminfin.ru', 'official', TRUE)
        RETURNING source_id
    """, (SOURCE_CODE,))
    return cur.fetchone()[0]


def ensure_release(cur, source_id, snap_date):
    """Создаёт или возвращает release_id для снапшота."""
    label = f'iminfin_snapshot_{snap_date}'
    cur.execute("SELECT release_id FROM catalog.release WHERE label = %s", (label,))
    r = cur.fetchone()
    if r:
        return r[0]
    cur.execute("""
        INSERT INTO catalog.release (source_id, label, published_at, status, notes)
        VALUES (%s, %s, %s, 'loaded',
                'Дефолтные срезы «на дату»: исполнение расходов 101 рег x 13 показ, трансферты, госдолг (доля к доходам по ФО)')
        RETURNING release_id
    """, (source_id, label, snap_date))
    return cur.fetchone()[0]


def ensure_metric(cur, code, name, freq_id, unit_id, description, metric_type='primary'):
    """Создаёт или возвращает metric_id из catalog.metric."""
    cur.execute("SELECT metric_id FROM catalog.metric WHERE metric_code = %s", (code,))
    r = cur.fetchone()
    if r:
        return r[0]
    cur.execute("""
        INSERT INTO catalog.metric
            (metric_code, name_ru, description, frequency_id, unit_id, source_id,
             metric_type, is_derived, status, is_active)
        VALUES (%s, %s, %s, %s, %s, %s, %s, FALSE, 'active', TRUE)
        RETURNING metric_id
    """, (code, name, description, freq_id, unit_id, ensure_metric._source_id, metric_type))
    return cur.fetchone()[0]


def ingest_snapshot(snap_dir, snap_date_str, conn, cur, source_id, metric_ids, rid_by_name, rid_rf, rid_fo):
    """Инжест одного снапшота."""
    snap_date = datetime.date.fromisoformat(snap_date_str)
    release_id = ensure_release(cur, source_id, snap_date_str)

    m_exp, m_plan, m_share, m_pc, m_trf, m_debt = (
        metric_ids['exp_total'], metric_ids['exp_plan'], metric_ids['exec_share'],
        metric_ids['exp_pc'], metric_ids['trf_fed'], metric_ids['debt_share'],
    )

    batch = []  # (metric_id, region_id, period_start, value, release_id)

    def add(mid, rid, value):
        if value is None or rid is None:
            return
        batch.append((mid, rid, snap_date, value, release_id))

    # 1) raskhody_ispoln[2]: исполнение расходов
    #    col 0=имя, 1=исполнение(млн), 2=план(млн), 3=null, 4=доля, 5=население(тыс),
    #    6=на_душу(тыс руб/чел), 7-9=целые, 10=доля_?, 11=уровень(0=РФ/1=ФО/2=субъект), 12=год
    rask_path = os.path.join(snap_dir, 'iminfin_raskhody_ispoln.json')
    if os.path.exists(rask_path):
        d = json.load(open(rask_path))
        for row in d[2]['data']:
            name, lvl = row[0], row[11]
            if lvl == 0:
                add(m_exp, rid_rf, row[1])
                add(m_plan, rid_rf, row[2])
                add(m_share, rid_rf, row[4])
                add(m_pc, rid_rf, row[6])  # col 6 — на душу, НЕ col 5 (население)
            elif lvl == 1:
                fo_rid = rid_fo.get(re.sub(r'\s+', ' ', name).strip())
                if fo_rid:
                    add(m_exp, fo_rid, row[1])
                    add(m_plan, fo_rid, row[2])
                    add(m_share, fo_rid, row[4])
                    add(m_pc, fo_rid, row[6])
            else:
                m = rid_by_name.get(norm_name(name))
                if m and m[1] == 'region':
                    add(m_exp, m[0], row[1])
                    add(m_plan, m[0], row[2])
                    add(m_share, m[0], row[4])
                    add(m_pc, m[0], row[6])  # col 6 — на душу

    # 2) transferty[3]: межбюджетные трансферты
    #    col 0=имя, 1=план(ФЗ, тыс руб), 2=распределено(тыс руб), 3=касса(тыс руб)
    #    27 регионов имеют None в col0 → используем col1 (распределено)
    #    Конвертация: тыс руб → млн руб = /1e3
    trf_path = os.path.join(snap_dir, 'iminfin_transferty.json')
    if os.path.exists(trf_path):
        trf = json.load(open(trf_path))
        for row in trf[3]['data']:
            name = row[0]
            # Prefer col0 (plan), fallback to col1 (raspredeleno)
            raw_val = row[1] if row[1] is not None else row[2]
            if raw_val is None:
                continue
            val_mln = raw_val / 1e3  # тыс → млн

            # Determine region level
            if 'Российская' in name and 'Федерация' in name:
                add(m_trf, rid_rf, val_mln)
            elif 'федеральный округ' in name.lower():
                fo_rid = rid_fo.get(re.sub(r'\s+', ' ', name).strip())
                if fo_rid:
                    add(m_trf, fo_rid, val_mln)
            else:
                m = rid_by_name.get(norm_name(name))
                if m:
                    add(m_trf, m[0], val_mln)

    # 3) dolg[3]: госдолг к доходам (доля) — только по федеральным округам
    #    col 0=имяФО, 1=код, 2=доля
    dolg_path = os.path.join(snap_dir, 'iminfin_dolg.json')
    if os.path.exists(dolg_path):
        dolg = json.load(open(dolg_path))
        for row in dolg[3]['data']:
            name = row[0]
            val = row[2]
            if 'федеральный округ' in name.lower():
                fo_rid = rid_fo.get(re.sub(r'\s+', ' ', name).strip())
                if fo_rid:
                    add(m_debt, fo_rid, val)

    # Дедупликация: убираем записи, уже существующие в БД
    existing = set()
    all_mids = list(set(b[0] for b in batch))
    for mid in all_mids:
        cur.execute(
            "SELECT metric_id, region_id, period_start FROM data.observation "
            "WHERE metric_id = %s AND period_start = %s",
            (mid, snap_date),
        )
        existing.update((r[0], r[1], r[2]) for r in cur.fetchall())
    new_batch = [b for b in batch if (b[0], b[1], b[2]) not in existing]
    skipped = len(batch) - len(new_batch)

    # Вставка
    # Уникальный индекс ux_observation: (metric_id, region_id, period_start,
    # frequency_id, assessment_type, sub_dimension, release_id)
    inserted = 0
    for i in range(0, len(new_batch), 500):
        chunk = new_batch[i:i + 500]
        cur.executemany("""
            INSERT INTO data.observation
                (metric_id, region_id, period_start, period_end, value,
                 assessment_type, observation_status, source_id, release_id,
                 frequency_id, sub_dimension)
            VALUES (%s, %s, %s, %s, %s, 'final', 'validated', %s, %s, %s, '')
            ON CONFLICT (metric_id, region_id, period_start, frequency_id,
                         assessment_type, sub_dimension, release_id)
            DO NOTHING
        """, [(b[0], b[1], b[2], b[2], b[3], source_id, b[4], FREQ_ID) for b in chunk])
        inserted += cur.rowcount
        conn.commit()

    print(f"  {snap_date_str}: batch={len(batch)} new={len(new_batch)} inserted={inserted} skipped={skipped}")
    return inserted, skipped


def main():
    conn = db_tunnel.connect()
    cur = conn.cursor()

    # Source
    source_id = ensure_source(cur)
    ensure_metric._source_id = source_id
    conn.commit()

    # Regions
    rid_by_name, rid_rf, rid_fo = load_regions(cur)
    print(f"Regions: РФ={rid_rf}, ФО={len(rid_fo)}, всего={len(rid_by_name)}")

    # Metrics (каноническая схема)
    metric_ids = {
        'exp_total': ensure_metric(cur, 'iminfin_exp_total_ytd_m',
            'Исполнение расходов субъекта с начала года, млн руб',
            FREQ_ID, 11, 'iМониторинг КРИСТА: кассовое исполнение расходов, нарастающий итог на дату снапшота'),
        'exp_plan': ensure_metric(cur, 'iminfin_exp_plan_ytd_m',
            'План расходов субъекта на год, млн руб',
            FREQ_ID, 11, 'Утверждённый годовой объём расходов'),
        'exec_share': ensure_metric(cur, 'iminfin_exp_exec_share',
            'Исполнение расходов субъекта, доля от плана',
            FREQ_ID, 13, 'Кассовое исполнение / план', 'ratio'),
        'exp_pc': ensure_metric(cur, 'iminfin_exp_pc_ytd_m',
            'Расходы субъекта на душу населения, руб./чел',
            FREQ_ID, 38, 'Отношение кассового исполнения расходов к численности населения', 'level'),
        'trf_fed': ensure_metric(cur, 'iminfin_trf_fed_ytd_m',
            'Межбюджетные трансферты из федбюджета субъекту, млн руб',
            FREQ_ID, 11, 'Нарастающий итог на дату снапшота. План по ФЗ при наличии, иначе распределено. Конвертация тыс→млн.'),
        'debt_share': ensure_metric(cur, 'iminfin_debt_share_econ',
            'Госдолг субъекта к доходам, доля',
            FREQ_ID, 12, 'Отношение госдолга субъекта к доходам бюджета, по федеральным округам', 'ratio'),
    }
    conn.commit()
    print(f"Metrics: {metric_ids}")

    # Найти все снапшоты
    snap_dirs = sorted(glob.glob(os.path.join(RAW_BASE, '*')))
    snap_dirs = [d for d in snap_dirs if os.path.isdir(d) and re.match(r'\d{4}-\d{2}-\d{2}', os.path.basename(d))]

    if not snap_dirs:
        print(f"Нет снапшотов в {RAW_BASE}")
        return

    print(f"Найдено {len(snap_dirs)} снапшотов: {[os.path.basename(d) for d in snap_dirs]}")

    total_inserted = 0
    total_skipped = 0
    for snap_dir in snap_dirs:
        snap_date = os.path.basename(snap_dir)
        try:
            ins, skip = ingest_snapshot(
                snap_dir, snap_date, conn, cur, source_id,
                metric_ids, rid_by_name, rid_rf, rid_fo,
            )
            total_inserted += ins
            total_skipped += skip
        except Exception as e:
            print(f"  ОШИБКА {snap_date}: {e}")
            conn.rollback()

    print(f"\nИтого: вставлено={total_inserted} пропущено={total_skipped}")
    cur.close()
    conn.close()


if __name__ == '__main__':
    main()