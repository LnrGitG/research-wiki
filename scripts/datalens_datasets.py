#!/usr/bin/env python3
"""Датасеты DataLens «Мониторинг региона и округа»: SQL-спеки + проверка (29.09.2026).

Четыре датасета из концепции queries/datalens-collection-concept-20260929.md.
Каждый SQL прогоняется против живой PG (тоннель), проверенные числа печатаются.
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
from db_tunnel import query  # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'datalens_datasets.yaml')

# Примечание: percentile_cont(...) WITHIN GROUP не поддерживает OVER в PG —
# медиана ФО считается коррелированным подзапросом (проверено 29.09).
DATASETS = {}

DATASETS['ds_region_monthly'] = {
    'description': 'Региональный срез: субъект × метрика × период (блоки A/B/C/E/F)',
    'sql': """
SELECT m.metric_code,
       left(m.name_ru, 60) AS metric_name,
       r.parent_id         AS fo_id,
       r.region_id,
       r.name_ru           AS region,
       o.frequency_id,
       o.period_start::date AS period,
       o.value
FROM core.observation_v2 o
JOIN core.metric m ON m.metric_id = o.metric_id
JOIN core.region r ON r.region_id = o.region_id
WHERE o.region_id > 9 AND o.sub_dimension = ''
  AND o.observation_status <> 'rejected'
  AND m.metric_code = ANY(ARRAY[
      'emiss_31074_cpi_prevm_m', 'emiss_57824_wage_m', 'emiss_43062_unemp_q',
      'zkf', 'zyi', 'vhdt', 'vmd', 'vhlvt', 'oipflrrivrsrf',
      'rosstat_housing_total_m', 'rosstat_housing_pop_m', 'snz'])
""",
    'columns': ['metric_code', 'metric_name', 'fo_id', 'region_id', 'region', 'freq', 'period', 'value'],
}

DATASETS['ds_region_rating'] = {
    'description': 'Рейтинги региона внутри ФО + медианы ФО и РФ (оконные функции)',
    'sql': """
SELECT fd.name_ru AS federal_district,
       r.name_ru  AS region,
       m.metric_code,
       m.name_ru  AS metric_name,
       o.period_start::date AS period,
       o.value,
       RANK() OVER (PARTITION BY fd.region_id, m.metric_id, o.period_start
                    ORDER BY o.value DESC) AS rank_in_fo,
       (SELECT percentile_cont(0.5) WITHIN GROUP (ORDER BY o2.value)
        FROM core.observation_v2 o2
        JOIN core.region r2 ON r2.region_id = o2.region_id
        WHERE r2.parent_id = fd.region_id AND o2.metric_id = m.metric_id
          AND o2.period_start = o.period_start) AS fo_median
FROM core.observation_v2 o
JOIN core.metric m ON m.metric_id = o.metric_id
JOIN core.region r ON r.region_id = o.region_id
JOIN core.region fd ON fd.region_id = r.parent_id
WHERE fd.level = 'federal_district' AND o.region_id > 9
  AND o.observation_status <> 'rejected'
  AND m.metric_code = ANY(ARRAY[
      'rosstat_housing_total_m', 'zkf', 'zyi', 'vmd',
      'emiss_31074_cpi_prevm_m', 'snz'])
""",
    'columns': ['federal_district', 'region', 'metric_code', 'metric_name', 'period', 'value', 'rank_in_fo', 'fo_median'],
}

DATASETS['ds_rf_trend'] = {
    'description': 'Федеральные агрегаты: КЭП (ВВП, ИКВ), ВРП годовой, ИПЦ РФ',
    'sql': """
SELECT m.metric_code, m.name_ru, o.period_start::date AS period, o.value,
       s.source_code
FROM core.observation_v2 o
JOIN core.metric m ON m.metric_id = o.metric_id
JOIN core.source s ON s.source_id = o.source_id
WHERE o.region_id = 1
  AND m.metric_code IN ('kep1_1', 'kep1_6', 'grp_level', 'grp_pys',
                        'vvp', 'emiss_31074_cpi_prevm_m')
  AND o.observation_status <> 'rejected'
""",
    'columns': ['metric_code', 'metric_name', 'period', 'value', 'source'],
}

DATASETS['db_health'] = {
    'description': 'Свежесть источников (пороги из queries/datalens-db-health-dashboard-20260928.md)',
    'sql': """
SELECT s.source_code,
       max(o.period_start)::date AS last_period,
       extract(epoch from now() - max(o.period_start)) / 86400 AS age_days,
       count(*) AS n_obs
FROM core.observation_v2 o
JOIN core.source s ON s.source_id = o.source_id
WHERE o.period_start < CURRENT_DATE
GROUP BY 1 ORDER BY 1
""",
    'columns': ['source', 'last_period', 'age_days', 'n_obs'],
}


def main():
    results = {}
    for name, spec in DATASETS.items():
        sql = spec['sql'].strip().rstrip(';')
        try:
            rows = __import__('db_tunnel').query(sql + ' LIMIT 20')
            results[name] = {'rows_sample': len(rows), 'status': 'ok',
                             'example': [str(x)[:40] for x in rows[0]] if rows else None}
            print(f'{name}: OK, пример: {rows[0] if rows else "пусто"}')
        except Exception as e:
            results[name] = {'status': 'fail', 'error': str(e)[:200]}
            print(f'{name}: FAIL — {str(e)[:200]}')
    # сохранить YAML
    with open(OUT, 'w', encoding='utf-8') as f:
        import yaml
        yaml.safe_dump({'datasets': {k: {'description': v['description'], 'sql': v['sql'].strip()} for k, v in DATASETS.items()},
                        'check_results': results}, f, allow_unicode=True, sort_keys=False)
    print('сохранено:', OUT)


if __name__ == '__main__':
    main()