#!/usr/bin/env python3
"""
Loader: stats.hh.ru → research-wiki PostgreSQL (data.observation).

Source:  GET https://stats.hh.ru/api/v1/data/RU  (~21 MB JSON, no auth)
Schema:  catalog.metric + catalog.release + data.observation
         profarea → sub_dimension (e.g. 'profarea:all', 'profarea:11')
         region:  hh.ru area ID → catalog.region via mapping table

Usage:
    python3 scripts/load_hh_stats.py              # full load
    python3 scripts/load_hh_stats.py --dry-run     # preview, no writes
    python3 scripts/load_hh_stats.py --metrics salary,index   # subset
"""

import sys, os, json, hashlib, subprocess, argparse, datetime
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from db_tunnel import query, execute, execute_many

# ── Constants ──────────────────────────────────────────────────────────────

SOURCE_ID = 32  # catalog.source 'HeadHunter (hh.ru)'
FREQUENCY_ID = 5  # месячная

# Metric mapping: stats.hh.ru category → (metric_code, name_ru, unit_id, sub_type)
# sub_type: 'abs' = absolute values, 'yoy' = year-over-year %, 'mom' = month-over-month %
METRIC_DEFS = {
    'averageCompensation': {
        'metric_code': 'hh_avg_salary_m',
        'name_ru': 'Средняя предлагаемая ЗП на hh.ru (медиана)',
        'unit_id': 38,  # руб
        'sub_type': 'abs',
    },
    'averageExpected': {
        'metric_code': 'hh_avg_expected_salary_m',
        'name_ru': 'Средняя ожидаемая ЗП на hh.ru (медиана, по резюме)',
        'unit_id': 38,  # руб
        'sub_type': 'abs',
    },
    'hhindex': {
        'metric_code': 'hh_hhi_index_m',
        'name_ru': 'HH-индекс (соотношение резюме к вакансиям)',
        'unit_id': 37,  # коэф
        'sub_type': 'abs',
    },
    'numberVacancies': {
        'metric_code': 'hh_vacancies_count_m',
        'name_ru': 'Количество вакансий на hh.ru',
        'unit_id': 29,  # шт
        'sub_type': 'abs',
    },
    'numberResumes': {
        'metric_code': 'hh_resumes_count_m',
        'name_ru': 'Количество резюме на hh.ru',
        'unit_id': 29,  # шт
        'sub_type': 'abs',
    },
    'vacancies': {
        'metric_code': 'hh_vacancies_yoy_m',
        'name_ru': 'Динамика вакансий на hh.ru (YoY, %)',
        'unit_id': 12,  # %
        'sub_type': 'yoy_mom',  # has 'year' and 'month' sub-keys
    },
    'resumes': {
        'metric_code': 'hh_resumes_yoy_m',
        'name_ru': 'Динамика резюме на hh.ru (YoY, %)',
        'unit_id': 12,  # %
        'sub_type': 'yoy_mom',
    },
}

# Profarea ID → name (from api.hh.ru/professional_roles)
PROFAREA_NAMES = {
    'all': 'Все профобласти',
    '1':  'Продажи, обслуживание клиентов',
    '2':  'Розничная торговля',
    '3':  'Финансы, бухгалтерия',
    '4':  'Стратегия, инвестиции, консалтинг',
    '5':  'Административный персонал',
    '6':  'Маркетинг, реклама, PR',
    '7':  'Производство, сервисное обслуживание',
    '8':  'Добыча сырья',
    '9':  'Сельское хозяйство',
    '10': 'Транспорт, логистика, перевозки',
    '11': 'Информационные технологии',
    '12': 'Управление персоналом, тренинги',
    '13': 'Юристы',
    '14': 'Закупки',
    '15': 'Безопасность',
    '16': 'Домашний, обслуживающий персонал',
    '17': 'Рабочий персонал',
    '18': 'Строительство, недвижимость',
    '19': 'Автомобильный бизнес',
    '20': 'Туризм, гостиницы, рестораны',
    '21': 'Спортивные клубы, фитнес, салоны красоты',
    '22': 'Страхование',
    '23': 'Медицина, фармацевтика',
    '24': 'Искусство, развлечения, массмедиа',
    '25': 'Наука, образование',
    '26': 'Высший и средний менеджмент',
    '27': 'Другое',
}

# Manual region mapping overrides (hh_id → db region_id)
# For cities whose parent region has a non-trivial name match
REGION_OVERRIDES = {
    '113':  1,    # Россия → РФ
    '1342': 200,  # Тюменская область → Тюменская область (с ХМАО и ЯНАО)
    '95':   200,  # Тюмень (city) → Тюменская область (с ХМАО и ЯНАО)
    '1229': 80,   # Кемеровская область → Кемеровская область — Кузбасс
    '1475': 51,   # РСО-Алания → Республика Северная Осетия — Алания
    '1008': 199,  # Архангельская область → Архангельская область (с НАО)
    '1368': 71,   # ХМАО — Югра
    '1414': 72,   # ЯНАО
    '1941': 93,   # Еврейская АО
    '1982': 94,   # Чукотский АО
    '1985': 31,   # Ненецкий АО
}

API_URL = 'https://stats.hh.ru/api/v1/data/RU'
AREAS_URL = 'https://api.hh.ru/areas'
UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'


# ── Functions ──────────────────────────────────────────────────────────────

def fetch_stats_data():
    """Fetch stats.hh.ru JSON data."""
    print('[1/6] Загрузка данных stats.hh.ru…', flush=True)
    result = subprocess.run(
        ['curl', '-s', '-H', f'User-Agent: {UA}', '-H', 'Referer: https://stats.hh.ru/',
         API_URL],
        capture_output=True, text=True, timeout=120
    )
    data = json.loads(result.stdout)
    print(f'      Регионов в выдаче: {len(data)} ({len(result.stdout)} байт)', flush=True)
    return data


def build_region_mapping(stats_data):
    """Build hh_id → db region_id mapping using api.hh.ru/areas + overrides."""
    print('[2/6] Построение маппинга регионов…', flush=True)

    # Fetch hh.ru areas
    result = subprocess.run(['curl', '-s', AREAS_URL], capture_output=True, text=True, timeout=30)
    areas_raw = json.loads(result.stdout)

    # Flatten
    hh_areas = {}
    def flatten(items, parent=""):
        for a in items:
            hh_areas[str(a['id'])] = {'name': a['name'], 'parent': parent}
            if a.get('areas'):
                flatten(a['areas'], a['name'])
    flatten(areas_raw)

    # Get DB regions
    db_regions = query("SELECT region_id, name_ru FROM catalog.region WHERE is_active = true")
    db_by_name = {r[1].lower(): r[0] for r in db_regions}

    def norm(s):
        s = s.lower().strip()
        for suf in [' область', ' край']:
            s = s.replace(suf, '')
        if s.startswith('республика '):
            s = s[11:]
        return s.strip()

    db_norm = {norm(r[1]): r[0] for r in db_regions}

    hh_to_db = {}
    skipped = []

    for hh_id in stats_data.keys():
        if hh_id in REGION_OVERRIDES:
            hh_to_db[hh_id] = REGION_OVERRIDES[hh_id]
            continue

        if hh_id.startswith('700'):
            skipped.append((hh_id, 'internal stats ID, no hh.ru area match'))
            continue

        info = hh_areas.get(hh_id, {})
        name = info.get('name', '')
        parent = info.get('parent', '')

        db_id = None
        if name.lower() in db_by_name:
            db_id = db_by_name[name.lower()]
        elif norm(name) in db_norm:
            db_id = db_norm[norm(name)]
        elif parent and norm(parent) in db_norm:
            db_id = db_norm[norm(parent)]
        elif parent and parent.lower() in db_by_name:
            db_id = db_by_name[parent.lower()]

        if db_id:
            hh_to_db[hh_id] = db_id
        else:
            skipped.append((hh_id, f'{name} (parent: {parent})'))

    print(f'      Смэтчено: {len(hh_to_db)}/{len(stats_data)}', flush=True)
    if skipped:
        print(f'      Пропущено: {len(skipped)} → {[s[0] for s in skipped]}', flush=True)

    return hh_to_db


def ensure_metrics():
    """Create missing metrics in catalog.metric. Returns metric_code → metric_id."""
    print('[3/6] Регистрация метрик в catalog.metric…', flush=True)

    metric_ids = {}
    for cat, mdef in METRIC_DEFS.items():
        code = mdef['metric_code']
        existing = query("SELECT metric_id FROM catalog.metric WHERE metric_code = %s", (code,))
        if existing:
            metric_ids[code] = existing[0][0]
        else:
            execute(
                "INSERT INTO catalog.metric (metric_code, name_ru, unit_id, source_id, frequency_id, status, is_active) "
                "VALUES (%s, %s, %s, %s, %s, 'active', true) ON CONFLICT (metric_code) DO NOTHING",
                (code, mdef['name_ru'], mdef['unit_id'], SOURCE_ID, FREQUENCY_ID)
            )
            row = query("SELECT metric_id FROM catalog.metric WHERE metric_code = %s", (code,))
            metric_ids[code] = row[0][0]
            print(f'      + {code} → metric_id={metric_ids[code]}', flush=True)

    print(f'      Всего метрик: {len(metric_ids)}', flush=True)
    return metric_ids


def create_release(payload_bytes):
    """Create a release record with content hash. Returns release_id."""
    print('[4/6] Создание релиза…', flush=True)
    content_hash = hashlib.sha256(payload_bytes).hexdigest()
    label = f'stats.hh.ru/data/RU {datetime.date.today().isoformat()}'

    existing = query(
        "SELECT release_id FROM catalog.release WHERE content_hash = %s AND source_id = %s",
        (content_hash, SOURCE_ID)
    )
    if existing:
        print(f'      Релиз уже существует: release_id={existing[0][0]}', flush=True)
        return existing[0][0]

    execute(
        "INSERT INTO catalog.release (source_id, label, content_hash, status, ingested_at) "
        "VALUES (%s, %s, %s, 'active', now()) ON CONFLICT DO NOTHING",
        (SOURCE_ID, label, content_hash)
    )
    row = query(
        "SELECT release_id FROM catalog.release WHERE content_hash = %s AND source_id = %s",
        (content_hash, SOURCE_ID)
    )
    release_id = row[0][0]
    print(f'      release_id={release_id}', flush=True)
    return release_id


def build_observations(stats_data, hh_to_db, metric_ids, release_id, payload_bytes):
    """Parse stats JSON → list of observation tuples for execute_many."""
    print('[5/6] Подготовка наблюдений…', flush=True)

    obs_rows = []
    skipped_no_region = 0
    months = ['january','february','march','april','may','june',
              'july','august','september','october','november','december']

    for hh_region_id, region_data in stats_data.items():
        db_region_id = hh_to_db.get(hh_region_id)
        if not db_region_id:
            skipped_no_region += 1
            continue

        for cat, mdef in METRIC_DEFS.items():
            if cat not in region_data:
                continue

            metric_id = metric_ids[mdef['metric_code']]
            cat_data = region_data[cat]

            if mdef['sub_type'] == 'yoy_mom':
                # Format: {"year": {profarea: matrix}, "month": {profarea: matrix}}
                for sub_key, sub_suffix in [('year', 'yoy'), ('month', 'mom')]:
                    if sub_key not in cat_data:
                        continue
                    for prof_id, matrix in cat_data[sub_key].items():
                        if not isinstance(matrix, list) or len(matrix) < 2:
                            continue
                        header = matrix[0]
                        years = [str(h) for h in header[1:]]
                        sub_dim = f'profarea:{prof_id}|{sub_suffix}'
                        for row_idx in range(1, len(matrix)):
                            row = matrix[row_idx]
                            month_idx = row[0]
                            for yi, year in enumerate(years):
                                val = row[1 + yi] if 1 + yi < len(row) else None
                                if val is not None and val != '':
                                    period_start = datetime.date(int(year), month_idx + 1, 1)
                                    if month_idx + 1 == 12:
                                        period_end = datetime.date(int(year), 12, 31)
                                    else:
                                        period_end = (datetime.date(int(year), month_idx + 2, 1) - datetime.timedelta(days=1))
                                    obs_rows.append((
                                        metric_id, db_region_id, period_start, period_end,
                                        float(val), SOURCE_ID, release_id,
                                        'validated', 'final', FREQUENCY_ID, sub_dim
                                    ))
            else:
                # Format: {profarea: matrix}
                if not isinstance(cat_data, dict):
                    continue
                for prof_id, matrix in cat_data.items():
                    if not isinstance(matrix, list) or len(matrix) < 2:
                        continue
                    header = matrix[0]
                    years = [str(h) for h in header[1:]]
                    sub_dim = f'profarea:{prof_id}'
                    for row_idx in range(1, len(matrix)):
                        row = matrix[row_idx]
                        month_idx = row[0]
                        for yi, year in enumerate(years):
                            val = row[1 + yi] if 1 + yi < len(row) else None
                            if val is not None and val != '':
                                period_start = datetime.date(int(year), month_idx + 1, 1)
                                if month_idx + 1 == 12:
                                    period_end = datetime.date(int(year), 12, 31)
                                else:
                                    period_end = (datetime.date(int(year), month_idx + 2, 1) - datetime.timedelta(days=1))
                                obs_rows.append((
                                    metric_id, db_region_id, period_start, period_end,
                                    float(val), SOURCE_ID, release_id,
                                    'validated', 'final', FREQUENCY_ID, sub_dim
                                ))

    print(f'      Регионов без маппинга (пропущено): {skipped_no_region}', flush=True)
    print(f'      Наблюдений к записи: {len(obs_rows)}', flush=True)
    return obs_rows


def insert_observations(obs_rows, dry_run=False):
    """Batch insert observations into data.observation."""
    if dry_run:
        print('[6/6] DRY RUN — запись пропущена', flush=True)
        # Print sample
        print('      Пример (первые 5):', flush=True)
        for r in obs_rows[:5]:
            print(f'      metric_id={r[0]}, region_id={r[1]}, period={r[2]}, val={r[4]}, sub_dim={r[10]}')
        return 0

    print(f'[6/6] Запись {len(obs_rows)} наблюдений в data.observation…', flush=True)

    insert_sql = """
        INSERT INTO data.observation
            (metric_id, region_id, period_start, period_end, value,
             source_id, release_id, observation_status, assessment_type,
             frequency_id, sub_dimension)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (metric_id, region_id, period_start, frequency_id,
                     assessment_type, sub_dimension, release_id)
        DO NOTHING
    """

    BATCH = 500
    total_inserted = 0
    for i in range(0, len(obs_rows), BATCH):
        batch = obs_rows[i:i + BATCH]
        execute_many(insert_sql, batch)
        total_inserted += len(batch)
        if (i // BATCH) % 20 == 0:
            print(f'      …{total_inserted}/{len(obs_rows)}', flush=True)

    print(f'      Записано: {total_inserted}', flush=True)
    return total_inserted


def verify(source_id=SOURCE_ID):
    """Post-load verification."""
    print('\n=== Проверка ===', flush=True)
    rows = query(
        "SELECT m.metric_code, count(o.*) as cnt, "
        "min(o.period_start) as min_period, max(o.period_start) as max_period, "
        "count(DISTINCT o.region_id) as regions, "
        "count(DISTINCT o.sub_dimension) as sub_dims "
        "FROM data.observation o "
        "JOIN catalog.metric m ON m.metric_id = o.metric_id "
        "WHERE o.source_id = %s "
        "GROUP BY m.metric_code ORDER BY m.metric_code",
        (source_id,)
    )
    print(f'{"metric_code":35s} {"count":>8s} {"period":20s} {"regions":>8s} {"sub_dims":>8s}')
    for r in rows:
        period = f'{r[2]} — {r[3]}'
        print(f'{r[0]:35s} {r[1]:>8d} {period:20s} {r[4]:>8d} {r[5]:>8d}')

    total = sum(r[1] for r in rows)
    print(f'\nИтого: {total} наблюдений')
    return total


# ── Main ───────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description='Load stats.hh.ru data into PostgreSQL')
    parser.add_argument('--dry-run', action='store_true', help='Preview without writing')
    parser.add_argument('--metrics', type=str, default=None,
                        help='Comma-separated metric keys to load (default: all)')
    args = parser.parse_args()

    # Filter metrics if requested
    global METRIC_DEFS
    if args.metrics:
        allowed = set(args.metrics.split(','))
        METRIC_DEFS = {k: v for k, v in METRIC_DEFS.items()
                       if k in allowed or v['metric_code'] in allowed}

    # Fetch
    stats_data = fetch_stats_data()

    # Save raw payload for hash
    payload_bytes = json.dumps(stats_data, ensure_ascii=False).encode('utf-8')

    # Region mapping
    hh_to_db = build_region_mapping(stats_data)

    # Ensure metrics exist
    metric_ids = ensure_metrics()

    # Create release
    if args.dry_run:
        release_id = 0
        print('[4/6] DRY RUN — релиз не создан', flush=True)
    else:
        release_id = create_release(payload_bytes)

    # Build observations
    obs_rows = build_observations(stats_data, hh_to_db, metric_ids, release_id, payload_bytes)

    # Insert
    insert_observations(obs_rows, dry_run=args.dry_run)

    # Verify
    if not args.dry_run:
        verify()


if __name__ == '__main__':
    main()