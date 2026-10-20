#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Достройка derived.catalog_facets для активных метрик, у которых фасета нет.

Зачем: фасеты собирались старым конвейером и покрывают 2 462 метрики против
17 336 в каталоге. Из-за этого у большинства строк derived.v_catalog_active
пусты measure/domain/unit_canonical — то есть фильтры витрины «не видят»
метрику, хотя ряд в базе есть. Класс отказа: «ряд записан, но не находится».

Что делает: только ДОБАВЛЯЕТ строки для метрик без фасета. Существующие
строки не трогает — у них эвристика старого конвейера (например, домен
'construction' по тегу rosstat_observations), которую нельзя воспроизвести
без риска ухудшить разметку.

Правила вывода (документированы, чтобы их можно было оспорить):
  unit_canonical     — catalog.unit.unit_code
  measure            — 'growth_rate' при теге роста, 'index' при индексной
                       единице или index_base, иначе 'level'
  domain             — по тегам и источнику, словарь DOMAIN_RULES; иначе 'other'
  is_aggregate       — is_derived, metric_type='derived' или тег aggregate
  seasonally_adjusted— true только при явном теге сезонной корректировки
  freshness          — из derived.v_metric_context (канон свежести)
  last_obs_at/depth  — max(period_end) и count(*) по data.observation

Все вставленные строки помечаются run_id, поэтому откат — один DELETE:
  DELETE FROM derived.catalog_facets WHERE run_id = '<значение>';

Запуск:
  python3 scripts/rebuild_catalog_facets.py --check     # сколько и как
  python3 scripts/rebuild_catalog_facets.py --apply     # вставка
"""
import argparse
import datetime as dt
import os
import sys
import uuid

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import db_tunnel  # noqa: E402

GROWTH_TAGS = {'growth', 'growth_rate', 'temp', 'yoy', 'mom'}
INDEX_TAGS = {'index', 'indices', 'deflator'}
SA_TAGS = {'sa', 'seasonal_adjusted', 'sa_adj'}
AGG_TAGS = {'aggregate', 'total', 'all_rf'}

# Порядок важен: первое совпадение выигрывает.
DOMAIN_RULES = [
    ({'kep'}, 'macro'),
    ({'cbr_survey'}, 'macro'),
    ({'cbr_mortgage', 'mortgage', 'ihk'}, 'credit'),
    ({'domrf_stock', 'domrf_flow', 'housing', 'zhil_fond'}, 'housing'),
    ({'rosstat_panel', 'rosstat_observations', 'emiss'}, 'construction'),
    ({'cbr_escrow', 'cbr_corporate'}, 'credit'),
    ({'fns', 'firms', 'rfsd'}, 'firms'),
    ({'budget', 'minfin'}, 'budget'),
    ({'demography', 'population'}, 'demography'),
    ({'labor', 'unemployment', 'wage'}, 'labor'),
    ({'prices', 'cpi', 'deflator'}, 'prices'),
]

SELECT_TARGETS = """
WITH obs AS (
    SELECT metric_id,
           max(period_end)      AS last_obs_at,
           count(*)             AS depth_obs
      FROM data.observation
     GROUP BY metric_id
)
SELECT m.metric_id, m.metric_code, m.unit_id, m.source_id, m.frequency_id,
       m.metric_type, m.is_derived, m.tags, m.index_base,
       u.unit_code,
       COALESCE(o.last_obs_at, NULL) AS last_obs_at,
       COALESCE(o.depth_obs, 0)      AS depth_obs,
       vc.freshness
  FROM catalog.metric m
  LEFT JOIN catalog.unit u        ON u.unit_id = m.unit_id
  LEFT JOIN obs o                 ON o.metric_id = m.metric_id
  LEFT JOIN derived.v_metric_context vc ON vc.metric_id = m.metric_id
 WHERE m.is_active
   AND NOT EXISTS (SELECT 1 FROM derived.catalog_facets f WHERE f.metric_id = m.metric_id)
 ORDER BY m.metric_id
"""


def derive_measure(unit_code, index_base, tags):
    t = {x.lower() for x in (tags or [])}
    if t & GROWTH_TAGS or 'temp' in (unit_code or ''):
        return 'growth_rate'
    if (unit_code or '').lower().startswith('index') or index_base is not None or (t & INDEX_TAGS):
        return 'index'
    return 'level'


SELECT_LEARNED = """
SELECT split_part(m.metric_code, '_', 1) AS prefix, f.domain, count(*) AS n
  FROM derived.catalog_facets f
  JOIN catalog.metric m USING (metric_id)
 WHERE f.domain IS NOT NULL
 GROUP BY 1, 2
"""


def learn_domain_prefixes(cur, min_n=3):
    """Перенос разметки домена по префиксу кода.

    Старый конвейер размечал домен по тегам; теги у новых семейств
    (`stage6`, `stage7`, `cbr_survey`) домен не несут. Поэтому берём модальный
    домен среди УЖЕ размеченных метрик с тем же префиксом кода (`kep1`,
    `cbrmon`, `emiss`, ...) — это перенос имеющегося решения, а не догадка.
    """
    cur.execute(SELECT_LEARNED)
    by_prefix = {}
    for prefix, domain, n in cur.fetchall():
        if not prefix:
            continue
        by_prefix.setdefault(prefix, []).append((n, domain))
    learned = {}
    for prefix, lst in by_prefix.items():
        total = sum(n for n, _ in lst)
        n, domain = max(lst)
        if total >= min_n and n * 2 > total:   # модальный домен — строго больше половины
            learned[prefix] = domain
    return learned


def derive_domain(tags, learned=None, code=None):
    t = {x.lower() for x in (tags or [])}
    for keys, domain in DOMAIN_RULES:
        if t & keys:
            return domain
    if learned and code:
        prefix = code.split('_')[0]
        if prefix in learned:
            return learned[prefix]
    return 'other'


def derive_row(row, run_id, learned=None):
    (metric_id, code, unit_id, source_id, freq_id, mtype, is_derived,
     tags, index_base, unit_code, last_obs_at, depth_obs, freshness) = row
    t = {x.lower() for x in (tags or [])}
    return (
        metric_id,
        derive_measure(unit_code, index_base, tags),
        unit_code,
        True if (t & SA_TAGS) else None,
        derive_domain(tags, learned, code),
        freshness,
        last_obs_at,
        depth_obs,
        bool(is_derived) or (mtype == 'derived') or bool(t & AGG_TAGS),
        run_id,
        dt.datetime.now(dt.timezone.utc),
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true', help='вставить строки')
    ap.add_argument('--check', action='store_true', help='только показать план')
    ap.add_argument('--run-id', default=None, help='метка прогона для отката')
    args = ap.parse_args()
    if not (args.apply or args.check):
        ap.error('нужен --check или --apply')

    run_id = args.run_id or ('fill-missing-' + dt.date.today().isoformat())
    with db_tunnel.connect() as conn, conn.cursor() as cur:
        cur.execute(SELECT_TARGETS)
        rows = cur.fetchall()
        print('метрик без фасета: %d' % len(rows))
        if not rows:
            return 0
        learned = learn_domain_prefixes(cur)
        print('префиксов с переносимой разметкой домена: %d' % len(learned))
        prepared = [derive_row(r, run_id, learned) for r in rows]
        from collections import Counter
        print('  measure:', dict(Counter(p[1] for p in prepared)))
        print('  domain :', dict(Counter(p[4] for p in prepared)))
        print('  без единицы:', sum(1 for p in prepared if p[2] is None))
        print('  без свежести:', sum(1 for p in prepared if p[5] is None))
        if args.check:
            print('проверочный режим: ничего не записано')
            return 0
        cur.executemany("""
            INSERT INTO derived.catalog_facets
                (metric_id, measure, unit_canonical, seasonally_adjusted, domain,
                 freshness, last_obs_at, depth_obs, is_aggregate, run_id, created_at)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            ON CONFLICT (metric_id) DO NOTHING
        """, prepared)
        conn.commit()
        cur.execute('SELECT count(*) FROM derived.catalog_facets WHERE run_id=%s', (run_id,))
        print('вставлено строк: %d (run_id=%s)' % (cur.fetchone()[0], run_id))
        cur.execute('SELECT count(*) FROM derived.catalog_facets')
        print('всего фасетов: %d' % cur.fetchone()[0])
        cur.execute("""
            SELECT count(*) FILTER (WHERE measure IS NULL),
                   count(*) FILTER (WHERE unit_canonical IS NULL)
              FROM derived.v_catalog_active
        """)
        empty = cur.fetchone()
        print('в v_catalog_active пустых measure: %d, unit: %d' % (empty[0], empty[1]))
    return 0


if __name__ == '__main__':
    sys.exit(main())
