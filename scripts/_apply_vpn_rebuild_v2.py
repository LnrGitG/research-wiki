#!/usr/bin/env python3
"""Регистрация пересборки демографического слоя ВПН-2020 (85 субъектов) в v2.

Обновляет карточку v2.metric 139 (определение экспозиции), добавляет метрику 140
(невзвешенная доля семей, чьё положение хуже) и версионную запись v2.load_run 66.
Идемпотентно (ON CONFLICT DO NOTHING / UPDATE).

Запуск: ~/.hermes/hermes-agent/venv/bin/python3 _apply_vpn_rebuild_v2.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from db_tunnel import execute, query  # noqa: E402

STEPS = [
    # 1) версионная запись о пересборке
    ("INSERT INTO v2.load_run (run_id, dataset_id, loaded_at, source_file, parser_version, status, rows_parsed, rows_inserted, notes) "
     "VALUES (66, 16, now(), 'public.vpn_households_children + public.rosstat_children_06 + public.did_exposure_reform2026', "
     "'research-load-vpn-85', 'ok', 85, 86, "
     "'Пересборка на 85 субъектов (ВПН-2020 Том 8 Табл.4 + Chisl_polvozr 01-01-2022). "
     "Экспозиция: три маржи M1/M2/M4, допущение независимости возрастов детей, "
     "веса = рост ставки п.п. (M1 +4/+6, M2 +2/+4, M4 6). РФ-агрегат = сумма 85 субъектов. "
     "Тюменская взята без АО (ХМАО и ЯНАО отдельными строками).') "
     "ON CONFLICT (run_id) DO NOTHING"),
    # 2) уточнение карточки метрики 139
    ("UPDATE v2.metric SET "
     "name_ru='Экспозиция реформы семейной ипотеки 01.10.2026 (маржи M1/M2/M4, взвешенная по росту ставки)', "
     "definition_ru='Сумма долей семей с 1 ребёнком (M1) и с 2 детьми (M2), имеющих ребёнка младше 7 лет, "
     "и семей с 2+ детьми без ребёнка младше 7 лет (M4), взвешенных ростом субсидируемой ставки в п.п.; "
     "нормирована на 6 п.п. Допущение: возрасты детей независимы.' "
     "WHERE metric_id=139"),
    # 3) метрика 140: невзвешенная доля
    ("INSERT INTO v2.metric (metric_id, metric_code, name_ru, name_en, definition_ru, domain_id, unit_id, frequency_id, is_aggregate, priority) "
     "VALUES (140, 'exposure_family_mortgage_2026_share', "
     "'Экспозиция реформы 01.10.2026: доля семей, чьё положение ухудшается (без весов)', "
     "'Share of families with children whose position worsens under the 01.10.2026 reform (unweighted)', "
     "'s1+s2+s4: доля семей с детьми, теряющих или получающих худшие условия; без весов по величине роста ставки.', "
     "9, 9, 4, false, 'extended') ON CONFLICT (metric_id) DO NOTHING"),
    ("INSERT INTO v2.metric_dataset_map (metric_id, dataset_id, native_code, scale_factor) "
     "VALUES (140, 16, 'did_exposure_reform2026:exposure_share', 1.0) ON CONFLICT DO NOTHING"),
]

for sql in STEPS:
    execute(sql)
    print('ok:', sql.split('(')[0].strip()[:60])

print('--- контроль ---')
for r in query("SELECT run_id, dataset_id, status, left(notes,60) FROM v2.load_run WHERE run_id=66"):
    print('  load_run', r)
for r in query("SELECT metric_id, metric_code, left(name_ru,50) FROM v2.metric WHERE metric_id IN (139,140)"):
    print('  metric', r)