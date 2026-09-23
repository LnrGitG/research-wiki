#!/usr/bin/env python3
"""Создание dataset-карточки dkp_forecast и регистрация load_run (v2.load_run требует dataset_id)."""
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from db_tunnel import execute, query  # noqa: E402

# dataset: source_id 2 = cbr (v2.source)
have = query("SELECT dataset_id FROM v2.dataset WHERE dataset_code='dkp-forecast'")
if not have:
    execute(
        "INSERT INTO v2.dataset (source_id, dataset_code, name_ru, "
        "release_url, schedule, is_active) "
        "VALUES (2, 'dkp-forecast', 'Среднесрочные прогнозы ЦБ РФ к опорным заседаниям', "
        "'https://www.cbr.ru/dkp/mp_dec/', 'после опорных заседаний (4/год) + после решений (8/год)', true)")
    print("created dataset dkp-forecast")
ds_id = query("SELECT dataset_id FROM v2.dataset WHERE dataset_code='dkp-forecast'")[0][0]
print("dataset_id:", ds_id)