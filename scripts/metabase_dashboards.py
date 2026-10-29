"""Сборка дашбордов research_wiki в Metabase через API.

Запуск: python3 scripts/metabase_dashboards.py [--dry-run]
Требует: METABASE_API_KEY в ~/.hermes/.env, тоннель на 127.0.0.1:13000.
Идемпотентно: коллекция, карточки и дашборд ищутся по имени и обновляются.
"""
import argparse
import json
import os
import sys

import requests

BASE = os.environ.get("METABASE_URL", "http://127.0.0.1:13000")
ENV = os.path.expanduser("~/.hermes/.env")
DB_ID = 2
COLLECTION = "Жильё, стройка и ипотека (research)"
DASHBOARD = "Research: жильё, стройка, ипотека"


def api_key():
    with open(ENV, encoding="utf-8") as f:
        for line in f:
            if line.startswith("METABASE_API_KEY="):
                return line.split("=", 1)[1].strip()
    raise SystemExit("METABASE_API_KEY не найден в .env")


S = requests.Session()
S.headers["x-api-key"] = api_key()
S.headers["Content-Type"] = "application/json"


def api(method, path, expect=(200, 201, 202), **payload):
    r = S.request(method, BASE + path, json=payload or None, timeout=300)
    if r.status_code not in expect:
        raise SystemExit(f"{method} {path} -> {r.status_code}: {r.text[:400]}")
    if not r.text:
        return None
    try:
        return r.json()
    except ValueError:
        return r.text


REGION_TAG = {
    "region": {
        "id": "region_tag",
        "name": "region",
        "display-name": "Регион (код)",
        "type": "text",
        "default": "",
    }
}

V = "derived.v_bi_observation"

# (name, display, sql, has_region_param, description)
CARDS = [
    (
        "KPI региона: текущие значения и год к году",
        "table",
        f"""
WITH src AS (
  SELECT * FROM {V}
  WHERE (%REG% = '' OR region_code = %REG%)
    AND metric_code IN ('orvdssmpg','orvdsningmr','vzszopmrvzs','01_01_06','01_03_06',
                        'cbr_izhk_rate_m','cbr_izhk_volume_m','cbr_izhk_debt_m',
                        'rkop_3','emiss_31074_cpi_prevm_m','emiss_43062_unemp_q')
    AND (metric_code <> 'rkop_3'
         OR sub_dimension = 'охват: регионы | статус: Всего')
),
base AS (
  SELECT DISTINCT ON (metric_code, period_start)
         metric_code, metric_name, unit_name, unit_code, freq_code, period_start, value
  FROM src
  ORDER BY metric_code, period_start, release_id DESC
),
last AS (
  SELECT DISTINCT ON (metric_code) metric_code, metric_name, unit_name, unit_code, freq_code,
         period_start AS last_period, value AS last_value
  FROM base
  ORDER BY metric_code, period_start DESC
),
prev AS (
  SELECT l.metric_code, b.value AS year_ago
  FROM last l
  JOIN base b ON b.metric_code = l.metric_code
             AND b.period_start = (l.last_period - INTERVAL '1 year')::date
)
SELECT l.metric_code, l.metric_name, l.unit_name AS unit, l.freq_code, l.last_period,
       l.last_value,
       p.year_ago,
       ROUND(100 * (l.last_value - p.year_ago) / NULLIF(abs(p.year_ago), 0), 1) AS chg_yoy_pct,
       ROUND(l.last_value - p.year_ago, 2) AS chg_yoy_pp
FROM last l LEFT JOIN prev p USING (metric_code)
ORDER BY l.metric_name
""",
        True,
        "Значения по последней доступной точке для выбранного региона; chg_yoy_pct — % г/г.",
    ),
    (
        "Объём работ «Строительство»: темп г/г",
        "line",
        f"""
SELECT period_start,
       CASE WHEN %REG% = '' THEN 'медиана по регионам' ELSE max(region_name) END AS series,
       PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY value) AS value
FROM {V}
WHERE metric_code = 'orvdssmpg'
  AND region_level = 'region'
  AND (region_code = %REG% OR %REG% = '')
  AND period_start >= DATE '2022-01-01'
GROUP BY period_start, (%REG% = '')
ORDER BY period_start
""",
        True,
        "ИФО объёма работ по ВЭД «Строительство», % к соответствующему месяцу. Без региона показана медиана по субъектам: среднее искажается выбросом по Ингушетии (январь 2026 — 53 336 %).",
    ),
    (
        "Строительство: накопительный объём работ",
        "line",
        f"""
SELECT period_start,
       CASE WHEN %REG% = '' THEN 'сумма по регионам' ELSE max(region_name) END AS series,
       SUM(value) AS value
FROM {V}
WHERE metric_code = 'orvdsningmr'
  AND region_level = 'region'
  AND (region_code = %REG% OR %REG% = '')
  AND period_start >= DATE '2024-01-01'
GROUP BY period_start, (%REG% = '')
ORDER BY period_start
""",
        True,
        "Накопительно с начала года; не суммировать повторно.",
    ),
    (
        "Ставка ИЖК: регион и РФ",
        "line",
        f"""
SELECT period_start, region_name, value
FROM {V}
WHERE metric_code = 'cbr_izhk_rate_m'
  AND (region_code = %REG% OR (%REG% = '' AND region_level = 'country'))
  AND period_start >= DATE '2022-01-01'
ORDER BY period_start
""",
        True,
        "Средневзвешенная ставка по ипотечным кредитам в рублях, % годовых.",
    ),
    (
        "Выдачи ИЖК по месяцам",
        "bar",
        f"""
SELECT period_start, value
FROM {V}
WHERE metric_code = 'cbr_izhk_volume_m'
  AND (region_code = %REG% OR (%REG% = '' AND region_level = 'country'))
  AND period_start >= DATE '2023-01-01'
ORDER BY period_start
""",
        True,
        "Объём выданных ипотечных кредитов, млн руб. за месяц.",
    ),
    (
        "Портфель: строящееся жильё и действующие ДДУ",
        "line",
        f"""
SELECT period_start, metric_name, value
FROM {V}
WHERE metric_code IN ('01_01_06','01_03_05')
  AND (region_code = %REG% OR (%REG% = '' AND region_level = 'country'))
  AND period_start >= DATE '2023-01-01'
ORDER BY period_start
""",
        True,
        "01_01_06 — площадь МКД, строящихся с привлечением средств граждан; 01_03_05 — площадь квартир по действующим ДДУ, м².",
    ),
    (
        "Карта: темп объёма работ по регионам (последний месяц)",
        "bar",
        f"""
WITH p AS (
  SELECT max(period_start) AS p FROM {V}
  WHERE metric_code = 'orvdssmpg' AND region_level = 'region'
    AND period_start >= CURRENT_DATE - INTERVAL '9 months'
)
SELECT region_name, value
FROM {V}, p
WHERE metric_code = 'orvdssmpg' AND region_level = 'region' AND period_start = p.p
ORDER BY value DESC
""",
        False,
        "Темп г/г по 87 субъектам за последний доступный месяц (сентябрь 2026).",
    ),
    (
        "Ввод жилых зданий по регионам (последний месяц)",
        "bar",
        f"""
WITH p AS (
  SELECT max(period_start) AS p FROM {V}
  WHERE metric_code = 'vzszopmrvzs' AND region_level = 'region'
    AND period_start >= CURRENT_DATE - INTERVAL '9 months'
)
SELECT region_name, value
FROM {V}, p
WHERE metric_code = 'vzszopmrvzs' AND region_level = 'region' AND period_start = p.p
  AND value IS NOT NULL
ORDER BY value DESC
LIMIT 40
""",
        False,
        "Общая площадь введённых жилых зданий, м², месяц (Росстат vv-zd-sub).",
    ),
    (
        "Ввод нежилых зданий по регионам (последний месяц)",
        "bar",
        f"""
WITH p AS (
  SELECT max(period_start) AS p FROM {V}
  WHERE metric_code = 'vzsnopmrvzs' AND region_level = 'region'
    AND period_start >= CURRENT_DATE - INTERVAL '9 months'
)
SELECT region_name, value
FROM {V}, p
WHERE metric_code = 'vzsnopmrvzs' AND region_level = 'region' AND period_start = p.p
  AND value IS NOT NULL
ORDER BY value DESC
LIMIT 40
""",
        False,
        "Общая площадь введённых нежилых зданий, м², месяц.",
    ),
    (
        "Ставка ИЖК по регионам (последний месяц)",
        "bar",
        f"""
WITH p AS (
  SELECT max(period_start) AS p FROM {V}
  WHERE metric_code = 'cbr_izhk_rate_m' AND region_level = 'region'
    AND period_start >= CURRENT_DATE - INTERVAL '9 months'
)
SELECT region_name, value
FROM {V}, p
WHERE metric_code = 'cbr_izhk_rate_m' AND region_level = 'region' AND period_start = p.p
  AND value IS NOT NULL
ORDER BY value DESC
LIMIT 40
""",
        False,
        "Средневзвешенная ставка ИЖК по субъектам, %; в базе 75 регионов.",
    ),
    (
        "Выдачи ИЖК по регионам (последний месяц)",
        "bar",
        f"""
WITH p AS (
  SELECT max(period_start) AS p FROM {V}
  WHERE metric_code = 'cbr_izhk_volume_m' AND region_level = 'region'
    AND period_start >= CURRENT_DATE - INTERVAL '9 months'
)
SELECT region_name, value
FROM {V}, p
WHERE metric_code = 'cbr_izhk_volume_m' AND region_level = 'region' AND period_start = p.p
  AND value IS NOT NULL
ORDER BY value DESC
LIMIT 40
""",
        False,
        "Объём выдач, млн руб. за месяц.",
    ),
    (
        "Задолженность по ИЖК по регионам (последний месяц)",
        "bar",
        f"""
WITH p AS (
  SELECT max(period_start) AS p FROM {V}
  WHERE metric_code = 'cbr_izhk_debt_m' AND region_level = 'region'
    AND period_start >= CURRENT_DATE - INTERVAL '9 months'
)
SELECT region_name, value
FROM {V}, p
WHERE metric_code = 'cbr_izhk_debt_m' AND region_level = 'region' AND period_start = p.p
  AND value IS NOT NULL
ORDER BY value DESC
LIMIT 40
""",
        False,
        "Портфель ипотеки, млн руб.; в базе 75 регионов.",
    ),
    (
        "Реализация квартир по регионам (последний месяц)",
        "bar",
        f"""
WITH p AS (
  SELECT max(period_start) AS p FROM {V}
  WHERE metric_code = 'rkop_3' AND region_level = 'region'
    AND sub_dimension = 'охват: регионы | статус: Всего'
    AND period_start >= CURRENT_DATE - INTERVAL '9 months'
)
SELECT region_name, value
FROM {V}, p
WHERE metric_code = 'rkop_3' AND region_level = 'region' AND period_start = p.p
  AND sub_dimension = 'охват: регионы | статус: Всего'
  AND value IS NOT NULL
ORDER BY value DESC
LIMIT 40
""",
        False,
        "Объём проданных площадей, м² (89 регионов).",
    ),
    (
        "Ставка и объём выдач: пузырьковая диаграмма по регионам",
        "scatter",
        f"""
WITH r AS (
  SELECT region_code, region_name, period_start, value
  FROM {V} WHERE metric_code = 'cbr_izhk_rate_m' AND region_level = 'region'
),
v AS (
  SELECT region_code, period_start, value
  FROM {V} WHERE metric_code = 'cbr_izhk_volume_m' AND region_level = 'region'
),
p AS (SELECT max(period_start) AS p FROM r)
SELECT r.region_name, r.value AS rate_pct, v.value AS volume_mln_rub
FROM r
JOIN v ON v.region_code = r.region_code AND v.period_start = r.period_start
JOIN p ON r.period_start = p.p
WHERE r.value IS NOT NULL AND v.value IS NOT NULL
""",
        False,
        "Цена кредита против объёма выдач в одном месяце: видно, где спрос держится дорогим кредитом.",
    ),
    (
        "Свежесть каталога по частотам",
        "table",
        """
SELECT frequency, freshness, count(*) AS metrics
FROM derived.v_metric_context
GROUP BY 1, 2
ORDER BY 1, 3 DESC
""",
        False,
        "Статусы по допускам пер-частотой (D=10, W=5, M=75, Q=160, A=550 дней).",
    ),
    (
        "Ряды с устаревшим краем (старше года)",
        "table",
        f"""
SELECT metric_code, name_ru, frequency, last_observation, observations, freshness
FROM derived.v_metric_context
WHERE last_observation < CURRENT_DATE - INTERVAL '365 days'
ORDER BY last_observation DESC NULLS LAST
LIMIT 40
""",
        False,
        "Сюда попадают годовые ряды и vztgr; на таких данных нельзя строить оперативные выводы.",
    ),
    (
        "Доля отклонённых наблюдений и сентинелов",
        "scalar",
        """
SELECT ROUND(100.0 * count(*) FILTER (WHERE observation_status = 'rejected') / count(*), 2)
       AS rejected_share_pct
FROM data.observation
""",
        False,
        "Доля строк, исключённых из витрины (сентинелы и дубли).",
    ),
]

TABS = ["Паспорт региона", "Строительство", "Ипотека и спрос", "Здоровье данных"]

LAYOUT = {
    "Паспорт региона": [(0, 0, 24, 8), (8, 0, 12, 8), (8, 12, 12, 8), (16, 0, 12, 8), (16, 12, 12, 8)],
    "Строительство": [(0, 0, 24, 8), (8, 0, 12, 8), (8, 12, 12, 8), (16, 0, 24, 8)],
    "Ипотека и спрос": [(0, 0, 12, 8), (0, 12, 12, 8), (8, 0, 12, 8), (8, 12, 12, 8), (16, 0, 24, 8)],
    "Здоровье данных": [(0, 0, 24, 8), (8, 0, 24, 8), (16, 0, 12, 4)],
}

# соответствие: вкладка -> имена карточек в порядке LAYOUT
TAB_CARDS = {
    "Паспорт региона": [
        "KPI региона: текущие значения и год к году",
        "Объём работ «Строительство»: темп г/г",
        "Ставка ИЖК: регион и РФ",
        "Выдачи ИЖК по месяцам",
        "Портфель: строящееся жильё и действующие ДДУ",
    ],
    "Строительство": [
        "Строительство: накопительный объём работ",
        "Карта: темп объёма работ по регионам (последний месяц)",
        "Ввод жилых зданий по регионам (последний месяц)",
        "Ввод нежилых зданий по регионам (последний месяц)",
    ],
    "Ипотека и спрос": [
        "Ставка ИЖК по регионам (последний месяц)",
        "Выдачи ИЖК по регионам (последний месяц)",
        "Задолженность по ИЖК по регионам (последний месяц)",
        "Реализация квартир по регионам (последний месяц)",
        "Ставка и объём выдач: пузырьковая диаграмма по регионам",
    ],
    "Здоровье данных": [
        "Свежесть каталога по частотам",
        "Ряды с устаревшим краем (старше года)",
        "Доля отклонённых наблюдений и сентинелов",
    ],
}


def ensure_collection():
    items = api("GET", "/api/collection")
    for c in items if isinstance(items, list) else []:
        if c.get("name") == COLLECTION:
            return c["id"]
    root = api("GET", "/api/collection/root/items?models=collection")
    return api("POST", "/api/collection", name=COLLECTION, parent_id=None)["id"]


def find_card(name, coll_id):
    items = api("GET", f"/api/collection/{coll_id}/items?models=card")
    for c in items.get("data", []):
        if c.get("name") == name:
            return c["id"]
    return None


def build_card(name, display, sql, has_region, desc, coll_id, dry):
    query = {
        "database": DB_ID,
        "type": "native",
        "native": {"query": sql.replace("%REG%", "{{region}}"), "template-tags": dict(REGION_TAG) if has_region else {}},
    }
    payload = {
        "name": name,
        "description": desc,
        "display": display,
        "dataset_query": query,
        "visualization_settings": {},
        "collection_id": coll_id,
    }
    if dry:
        print(f"[dry] card {name}")
        return None
    cid = find_card(name, coll_id)
    if cid:
        api("PUT", f"/api/card/{cid}", **payload)
    else:
        cid = api("POST", "/api/card", **payload)["id"]
    # проверка исполнения
    res = api("POST", f"/api/card/{cid}/query")
    data = res.get("data", {})
    rows = data.get("rows", [])
    cols = [c["name"] for c in data.get("cols", [])]
    status = res.get("status")
    print(f"card {cid:>4} {status:<8} rows={len(rows):<4} cols={cols[:4]} :: {name}")
    if not rows and name != "Доля отклонённых наблюдений и сентинелов":
        print("   !! пустой результат")
    return cid


def ensure_tabs(dash_id):
    dash = api("GET", f"/api/dashboard/{dash_id}")
    have = {t["name"]: t["id"] for t in dash.get("tabs", [])}
    tabs = []
    for name in TABS:
        tabs.append({"id": have.get(name, -1 - TABS.index(name)), "name": name})
    return tabs


def ensure_dashboard(coll_id, cards, dry):
    existing = api("GET", "/api/collection/root/items?models=dashboard")
    dash_id = None
    for d in api("GET", "/api/dashboard"):
        if d.get("name") == DASHBOARD:
            dash_id = d["id"]
    if dash_id is None:
        if dry:
            print("[dry] dashboard")
            return
        dash_id = api("POST", "/api/dashboard", name=DASHBOARD, collection_id=coll_id)["id"]

    tabs = ensure_tabs(dash_id)
    tab_ids = {t["name"]: t["id"] for t in tabs}
    region_cards = {n for n, _, _, h, _ in CARDS if h}
    cur = api("GET", f"/api/dashboard/{dash_id}")
    existing = {(d.get("card_id"), d.get("dashboard_tab_id")): d["id"]
                for d in cur.get("dashcards", [])}
    dashcards, idx = [], 0
    for tab in TABS:
        for (row, col, sx, sy), cname in zip(LAYOUT[tab], TAB_CARDS[tab]):
            cid = cards[cname]
            idx += 1
            mapping = []
            if cname in region_cards:
                mapping = [{"parameter_id": "region", "card_id": cid,
                            "target": ["template-tag", "region"]}]
            dashcards.append({
                "id": existing.get((cid, tab_ids[tab]), -idx),
                "card_id": cid,
                "row": row, "col": col, "size_x": sx, "size_y": sy,
                "dashboard_tab_id": tab_ids[tab],
                "parameter_mappings": mapping,
                "visualization_settings": {},
            })
    params = [{
        "id": "region", "name": "Регион (код)", "slug": "region",
        "type": "string/=", "sectionId": "string",
        "default": "bashkortostan",
    }]
    if dry:
        print(f"[dry] dashcards {len(dashcards)}")
        return
    api("PUT", f"/api/dashboard/{dash_id}", tabs=tabs, dashcards=dashcards, parameters=params)
    print(f"dashboard {dash_id}: вкладок {len(tabs)}, карточек {len(dashcards)}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    coll = ensure_collection()
    print("collection:", coll)
    cards = {}
    has_param = {n: h for n, _, _, h, _ in CARDS}
    for name, display, sql, h, desc in CARDS:
        cards[name] = build_card(name, display, sql, h, desc, coll, args.dry_run)
    ensure_dashboard(coll, {k: v for k, v in cards.items() if v or args.dry_run}, args.dry_run)
    return 0


if __name__ == "__main__":
    sys.exit(main())
