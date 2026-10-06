#!/usr/bin/env python3
"""Сбор данных hh.ru (HeadHunter) — каноническая схема, OAuth2 client_credentials.

Источник: api.hh.ru (HeadHunter API v1.0.0), OpenAPI spec:
  https://api.hh.ru/openapi/specification/public

Авторизация: OAuth2, flow client_credentials (app-level, без участия пользователя).
  1. Зарегистрировать приложение на https://dev.hh.ru/admin
  2. Получить client_id и client_secret
  3. Добавить HH_CLIENT_ID и HH_CLIENT_SECRET в .env
  4. Скрипт получает access_token через POST https://api.hh.ru/token

Эндпоинты (требуют OAuth2):
  GET /vacancies — поиск вакансий (пагинация: page, per_page)
    Параметры: text, area, industry, professional_role, only_with_salary,
    date_from, date_to, period, per_page (max 100), page
    Ответ: {found, per_page, pages, page, items: [{id, name, salary, area, employer, ...}]}
    found = общее количество вакансий по фильтру — ключевой показатель

  GET /salary_statistics/paid/salary_evaluation/{area_id} — оценка ЗП
    Параметры: position_name, industry, employee_level, speciality
    Ответ: {salary: {from, to, currency}, ...} (платный, может быть forbidden)

Справочники (доступны без авторизации):
  GET /areas — дерево регионов (Россия → ФО → субъекты → города)
  GET /industries — отрасли компаний
  GET /professional_roles — профессиональные роли
  GET /dictionaries — справочники полей (experience, employment, schedule)
  GET /salary_statistics/dictionaries/salary_areas — регионы для ЗП-статистики
  GET /salary_statistics/dictionaries/professional_areas — профобласти
  GET /salary_statistics/dictionaries/employee_levels — уровни компетенций
  GET /salary_statistics/dictionaries/salary_industries — отрасли

Метрики (каноническая схема, catalog.metric + data.observation):
  hh_vacancies_count_m  — количество вакансий (по фильтру), freq=5 (M), unit=29 (count)
  hh_resumes_count_m   — количество резюме (по фильтру), freq=5 (M), unit=29
  hh_avg_salary_m      — средняя предлагаемая ЗП, freq=5 (M), unit=38 (rub)
  hh_hhi_index_m       — HH-индекс (вакансии/резюме), freq=5 (M), unit=37 (ratio)

Параметры сбора для housing research:
  text: "строительство" / "строитель" / "монтаж" / "СМР"
  professional_role: 156 (Строительство) — из /professional_roles
  industry: 23 (Строительство) — из /industries
  area: по регионам из /areas (id=113 → Россия, id=1 → Москва, и т.д.)
  period: 30 (за последние 30 дней)
  only_with_salary: true (для расчёта средней ЗП)

Сопоставление регионов hh.ru → catalog.region:
  hh area_id → name → norm_name → catalog.region.region_id
  (через справочник /areas, загружается один раз и кэшируется)
"""
import json
import os
import re
import sys
import datetime
import urllib.request
import urllib.parse
import ssl
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import db_tunnel  # noqa: E402

BASE_URL = 'https://api.hh.ru'
SOURCE_CODE = 'hh'
FREQ_ID = 5  # месячная
USER_AGENT = 'research-wiki/1.0 (lnr@research)'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Сопоставление имён регионов hh.ru → catalog.region (аналогично iminfin)
ALIAS = {
    'республика татарстан (татарстан)': 'республика татарстан',
    'республика адыгея (адыгея)': 'республика адыгея',
    'чувашская республика - чувашия': 'чувашская республика',
    'чувашская республика-чувашия': 'чувашская республика',
    'санкт-петербург': 'санкт-петербург',
    'москва': 'москва',
    'севастополь': 'севастополь',
    'республика северная осетия - алания': 'республика северная осетия — алания',
    'кемеровская область - кузбасс': 'кемеровская область — кузбасс',
    'кемеровская область': 'кемеровская область — кузбасс',
}


def norm_name(s):
    s = re.sub(r'\s+', ' ', str(s)).strip().lower()
    return ALIAS.get(s, s)


def fetch_json(url, headers=None, method='GET', data=None, timeout=15):
    """Fetch JSON from URL with retry on rate limit."""
    if headers is None:
        headers = {'User-Agent': USER_AGENT}
    if 'User-Agent' not in headers and 'HH-User-Agent' not in headers:
        headers['User-Agent'] = USER_AGENT

    for attempt in range(3):
        try:
            if data is not None:
                body = urllib.parse.urlencode(data).encode('utf-8')
                headers['Content-Type'] = 'application/x-www-form-urlencoded'
            else:
                body = None
            req = urllib.request.Request(url, headers=headers, data=body, method=method)
            resp = urllib.request.urlopen(req, context=ctx, timeout=timeout)
            return json.loads(resp.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            if e.code == 403:
                raise PermissionError(f'403 Forbidden: {url} — OAuth2 token required')
            if e.code == 429:
                wait = 2 ** attempt
                print(f'  Rate limited, waiting {wait}s...')
                time.sleep(wait)
                continue
            body = e.read().decode('utf-8', errors='replace')
            raise RuntimeError(f'HTTP {e.code}: {body[:200]}')
        except Exception as e:
            if attempt < 2:
                time.sleep(2)
                continue
            raise


def get_token(client_id, client_secret):
    """Получить OAuth2 access_token через client_credentials flow."""
    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
    }
    result = fetch_json(f'{BASE_URL}/token', method='POST', data=data)
    token = result.get('access_token')
    if not token:
        raise RuntimeError(f'No access_token in response: {result}')
    return token


def auth_headers(token):
    return {
        'User-Agent': USER_AGENT,
        'Authorization': f'Bearer {token}',
        'Accept': 'application/json',
    }


def load_hh_areas():
    """Загрузить справочник регионов hh.ru (без авторизации)."""
    areas = fetch_json(f'{BASE_URL}/areas')
    # Плоский словарь: area_id → name
    flat = {}

    def flatten(node, parent_id=None):
        aid = node.get('id')
        name = node.get('name')
        if aid and name:
            flat[aid] = name
        for child in node.get('areas', []):
            flatten(child, aid)

    for country in areas:
        flatten(country)
    return flat


def load_region_map(cur):
    """Загрузить справочник catalog.region → {norm_name: (region_id, level)}."""
    cur.execute("SELECT region_id, name_ru, level, is_active FROM catalog.region")
    rid_by_name = {}
    for rid, name, level, is_active in cur.fetchall():
        if not name or not is_active:
            continue
        rid_by_name[norm_name(name)] = (rid, level)
    return rid_by_name


def match_hh_area_to_region(hh_area_name, rid_by_name):
    """Сопоставить имя региона hh.ru с catalog.region."""
    key = norm_name(hh_area_name)
    return rid_by_name.get(key)


def ensure_source(cur):
    cur.execute("SELECT source_id FROM catalog.source WHERE source_code = %s", (SOURCE_CODE,))
    r = cur.fetchone()
    if r:
        return r[0]
    cur.execute("""
        INSERT INTO catalog.source (source_code, name_ru, publisher, url, reliability, is_active)
        VALUES (%s, 'HeadHunter (hh.ru)', 'HeadHunter',
                'https://api.hh.ru', 'official', TRUE)
        RETURNING source_id
    """, (SOURCE_CODE,))
    return cur.fetchone()[0]


def ensure_metric(cur, source_id, code, name, unit_id, description, metric_type='primary'):
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
    """, (code, name, description, FREQ_ID, unit_id, source_id, metric_type))
    return cur.fetchone()[0]


def ensure_release(cur, source_id, label, snap_date):
    cur.execute("SELECT release_id FROM catalog.release WHERE label = %s", (label,))
    r = cur.fetchone()
    if r:
        return r[0]
    cur.execute("""
        INSERT INTO catalog.release (source_id, label, published_at, status, notes)
        VALUES (%s, %s, %s, 'loaded', 'hh.ru API: вакансии по строительству')
        RETURNING release_id
    """, (source_id, label, snap_date))
    return cur.fetchone()[0]


def collect_vacancies(token, text, area_id=None, period=30, per_page=100):
    """Сбор вакансий с пагинацией. Возвращает (total_found, all_items)."""
    headers = auth_headers(token)
    params = {
        'text': text,
        'period': period,
        'per_page': per_page,
        'only_with_salary': 'true',
    }
    if area_id:
        params['area'] = area_id

    url = f'{BASE_URL}/vacancies?{urllib.parse.urlencode(params)}'
    data = fetch_json(url, headers=headers)

    total = data.get('found', 0)
    pages = data.get('pages', 0)
    items = data.get('items', [])

    print(f'  {text} area={area_id}: found={total} pages={pages}')

    # Собираем все страницы (ограничиваем до 20 страниц = 2000 вакансий)
    max_pages = min(pages, 20)
    for page in range(1, max_pages):
        params['page'] = page
        url = f'{BASE_URL}/vacancies?{urllib.parse.urlencode(params)}'
        page_data = fetch_json(url, headers=headers)
        items.extend(page_data.get('items', []))
        time.sleep(0.5)  # rate limit safety

    return total, items


def compute_salary_stats(items):
    """Вычислить статистику зарплат из списка вакансий."""
    salaries = []
    for v in items:
        s = v.get('salary')
        if s and s.get('currency') == 'RUR':
            s_from = s.get('from')
            s_to = s.get('to')
            if s_from and s_to:
                salaries.append((s_from + s_to) / 2)
            elif s_from:
                salaries.append(s_from)
            elif s_to:
                salaries.append(s_to)

    if not salaries:
        return None, None, 0

    avg = sum(salaries) / len(salaries)
    median = sorted(salaries)[len(salaries) // 2]
    return avg, median, len(salaries)


def main():
    # Проверить авторизацию
    client_id = os.environ.get('HH_CLIENT_ID', '')
    client_secret = os.environ.get('HH_CLIENT_SECRET', '')

    if not client_id or not client_secret:
        env_path = os.path.expanduser('~/research-wiki-private/.env')
        if os.path.exists(env_path):
            with open(env_path) as f:
                for line in f:
                    if line.startswith('HH_CLIENT_ID='):
                        client_id = line.split('=', 1)[1].strip().strip('"')
                    elif line.startswith('HH_CLIENT_SECRET='):
                        client_secret = line.split('=', 1)[1].strip().strip('"')

    if not client_id or not client_secret:
        print('⚠️  HH_CLIENT_ID и HH_CLIENT_SECRET не найдены.')
        print()
        print('Для сбора данных hh.ru:')
        print('1. Зарегистрируйтесь на https://dev.hh.ru/admin (создайте приложение)')
        print('2. Получите client_id и client_secret')
        print('3. Добавьте в ~/research-wiki-private/.env:')
        print('   HH_CLIENT_ID=...')
        print('   HH_CLIENT_SECRET=...')
        print('4. Запустите скрипт повторно')
        print()
        print('Справочники (areas, industries) доступны без авторизации.')
        print('Поиск вакансий, резюме и ЗП-статистика требуют OAuth2 token.')

        # Сохранить справочники без авторизации
        try:
            print('\\nЗагрузка справочника регионов hh.ru...')
            areas = load_hh_areas()
            print(f'  Регионов: {len(areas)}')
            # Сохранить в raw/
            raw_dir = os.path.expanduser('~/yc-wiki/raw/hh')
            os.makedirs(raw_dir, exist_ok=True)
            today = datetime.date.today().isoformat()
            with open(os.path.join(raw_dir, f'areas_{today}.json'), 'w', encoding='utf-8') as f:
                json.dump(areas, f, ensure_ascii=False, indent=2)
            print(f'  Сохранён: {raw_dir}/areas_{today}.json')

            # Также сохранить industries и professional_roles
            industries = fetch_json(f'{BASE_URL}/industries')
            with open(os.path.join(raw_dir, f'industries_{today}.json'), 'w', encoding='utf-8') as f:
                json.dump(industries, f, ensure_ascii=False, indent=2)
            print(f'  Отраслей: {len(industries)}')

            prof_roles = fetch_json(f'{BASE_URL}/professional_roles')
            with open(os.path.join(raw_dir, f'professional_roles_{today}.json'), 'w', encoding='utf-8') as f:
                json.dump(prof_roles, f, ensure_ascii=False, indent=2)
            print(f'  Профессиональных ролей: {len(prof_roles.get("categories", []))}')

        except Exception as e:
            print(f'Ошибка загрузки справочников: {e}')
        return

    # С авторизацией — полный сбор
    print('Получение OAuth2 token...')
    token = get_token(client_id, client_secret)
    print(f'  Token получен ({len(token)} символов)')

    conn = db_tunnel.connect()
    cur = conn.cursor()

    source_id = ensure_source(cur)
    conn.commit()

    # Метрики
    metrics = {
        'vacancies': ensure_metric(cur, source_id, 'hh_vacancies_count_m',
            'Количество вакансий на hh.ru (строительство)', 29,
            'HeadHunter API: /vacancies?text=строительство&period=30'),
        'avg_salary': ensure_metric(cur, source_id, 'hh_avg_salary_m',
            'Средняя предлагаемая ЗП на hh.ru (строительство)', 38,
            'HeadHunter API: средняя ЗП из вакансий со строительством, RUR'),
        'median_salary': ensure_metric(cur, source_id, 'hh_median_salary_m',
            'Медианная предлагаемая ЗП на hh.ru (строительство)', 38,
            'HeadHunter API: медиана ЗП из вакансий со строительством, RUR'),
        'vacancies_salary': ensure_metric(cur, source_id, 'hh_vacancies_with_salary_m',
            'Количество вакансий с указанием ЗП на hh.ru (строительство)', 29,
            'HeadHunter API: вакансии only_with_salary=true'),
    }
    conn.commit()

    # Регионы
    rid_by_name = load_region_map(cur)
    hh_areas = load_hh_areas()
    print(f'Регионов hh.ru: {len(hh_areas)}, catalog.region: {len(rid_by_name)}')

    today = datetime.date.today().isoformat()
    release_id = ensure_release(cur, source_id, f'hh_api_{today}', today)
    conn.commit()

    # Сбор: РФ + региональный разрез
    # 1. РФ total (area=113 — Россия)
    print(f'\\nСбор вакансий по строительству (РФ)...')
    total_rf, items_rf = collect_vacancies(token, 'строительство', area_id='113', period=30)
    avg_rf, med_rf, n_sal_rf = compute_salary_stats(items_rf)

    batch = []
    m_vac = metrics['vacancies']
    m_avg = metrics['avg_salary']
    m_med = metrics['median_salary']
    m_vsal = metrics['vacancies_salary']

    # РФ (region_id=1)
    rid_rf = rid_by_name.get(norm_name('Российская Федерация'), (1, 'country'))[0]
    batch.append((m_vac, rid_rf, today, total_rf, release_id))
    if avg_rf:
        batch.append((m_avg, rid_rf, today, avg_rf, release_id))
    if med_rf:
        batch.append((m_med, rid_rf, today, med_rf, release_id))
    batch.append((m_vsal, rid_rf, today, n_sal_rf, release_id))

    # 2. Региональный разрез — топ-20 регионов по строительству
    # Сопоставляем hh areas с catalog.region (level='region')
    matched = 0
    for hh_id, hh_name in hh_areas.items():
        m = match_hh_area_to_region(hh_name, rid_by_name)
        if m and m[1] == 'region':
            try:
                total, items = collect_vacancies(token, 'строительство', area_id=hh_id, period=30)
                avg, med, n_sal = compute_salary_stats(items)
                rid = m[0]
                batch.append((m_vac, rid, today, total, release_id))
                if avg:
                    batch.append((m_avg, rid, today, avg, release_id))
                if med:
                    batch.append((m_med, rid, today, med, release_id))
                batch.append((m_vsal, rid, today, n_sal, release_id))
                matched += 1
                time.sleep(0.5)  # rate limit
            except Exception as e:
                print(f'  Ошибка {hh_name}: {e}')

    print(f'\\nСопоставлено регионов: {matched}')
    print(f'Батч: {len(batch)} наблюдений')

    # Вставка
    inserted = 0
    for i in range(0, len(batch), 500):
        chunk = batch[i:i + 500]
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

    print(f'Вставлено: {inserted}')
    cur.close()
    conn.close()


if __name__ == '__main__':
    main()