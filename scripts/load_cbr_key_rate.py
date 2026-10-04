#!/usr/bin/env python3
"""Загрузка дневного ряда ключевой ставки в catalog/data.

Закрывает пробел, зафиксированный в разборе паспортов метрик: ключевой ставки
в каталоге не было вовсе, хотя для ДКП это первостепенный ряд.

Что делает:
  1. регистрирует метрику cbr_key_rate в catalog.metric (дневная частота,
     источник cbr, единица pct);
  2. регистрирует релиз для провенанса;
  3. заливает наблюдения в data.observation идемпотентно.

Ключ наблюдения включает sub_dimension и release_id; NULL в уникальном
индексе считается отличным от NULL, поэтому ON CONFLICT с NULL не сработает —
sub_dimension пишется пустой строкой, release_id настоящий.
"""
import json
import os
import sys

sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import execute, query

SRC = "/home/lnr/research-wiki-private/data/cbr_key_rate_daily.json"
METRIC_CODE = "cbr_key_rate"
NAME = "Ключевая ставка Банка России"
RELEASE_LABEL = "Ключевая ставка (дневной ряд), выгрузка 2026-10-04"

if not os.path.exists(SRC):
    print("нет файла ряда:", SRC)
    sys.exit(1)

with open(SRC, encoding="utf-8") as f:
    data = json.load(f)
daily = data["daily"]
print("точек в файле:", len(daily))

# ---------- 1. метрика ----------
src_id = query("SELECT source_id FROM catalog.source WHERE source_code='cbr'")[0][0]
freq_id = query("SELECT frequency_id FROM catalog.frequency WHERE freq_code='D'")[0][0]
unit_id = query("SELECT unit_id FROM catalog.unit WHERE unit_code='pct'")[0][0]
print(f"справочники: source={src_id} frequency={freq_id} unit={unit_id}")

have = query("SELECT metric_id FROM catalog.metric WHERE metric_code=%s", (METRIC_CODE,))
if have:
    metric_id = have[0][0]
    print("метрика уже есть, id:", metric_id)
else:
    metric_id = query("""INSERT INTO catalog.metric
        (metric_code, name_ru, short_name_ru, description, unit_id, source_id,
         frequency_id, metric_type, is_active)
        VALUES (%s, %s, %s, %s, %s, %s, %s, 'primary', true)
        RETURNING metric_id""",
        (METRIC_CODE, NAME, "Ключевая ставка",
         "Дневной ряд ключевой ставки Банка России. Источник: cbr.ru/hd_base/KeyRate "
         "(POST UniDbQuery). Ряд отражает действующее значение на дату; решения "
         "принимаются на заседаниях, значение вступает в силу со следующего дня "
         "или через 1-3 дня после объявления.",
         unit_id, src_id, freq_id))[0][0]
    print("метрика создана, id:", metric_id)

# ---------- 2. релиз ----------
rel = query("SELECT release_id FROM catalog.release WHERE source_id=%s AND label=%s",
            (src_id, RELEASE_LABEL))
if rel:
    release_id = rel[0][0]
    print("релиз уже есть, id:", release_id)
else:
    release_id = query("""INSERT INTO catalog.release
        (source_id, label, published_at, status, url)
        VALUES (%s, %s, %s, 'loaded', %s) RETURNING release_id""",
        (src_id, RELEASE_LABEL, "2026-10-04",
         "https://www.cbr.ru/hd_base/KeyRate/"))[0][0]
    print("релиз создан, id:", release_id)

# ---------- 3. наблюдения ----------
region_id = query("SELECT region_id FROM catalog.region WHERE region_code='ru'")[0][0]
print("регион:", region_id)

rows = sorted(daily.items())
print("к загрузке:", len(rows))

inserted = 0
failed = 0
SQL = """INSERT INTO data.observation
           (metric_id, region_id, period_start, frequency_id, value,
            assessment_type, observation_status, source_id, release_id,
            sub_dimension, notes)
         VALUES (%s, %s, %s::date, %s, %s, 'final', 'validated', %s, %s, '', %s)
         ON CONFLICT (metric_id, region_id, period_start, frequency_id,
                      assessment_type, sub_dimension, release_id) DO NOTHING"""
for iso, val in rows:
    try:
        n = execute(SQL, (metric_id, region_id, iso, freq_id, val,
                          src_id, release_id, "cbr.ru/hd_base/KeyRate"))
        inserted += n
    except Exception as e:
        failed += 1
        if failed <= 3:
            print("   ошибка на", iso, str(e)[:120])

print(f"\nвставлено: {inserted}, ошибок: {failed}")

# ---------- 4. контроль ----------
print("\n=== контроль в базе ===")
got = query("""SELECT count(*), min(period_start), max(period_start)
               FROM data.observation WHERE metric_id=%s""", (metric_id,))[0]
print(f"   наблюдений: {got[0]}, диапазон: {got[1]} .. {got[2]}")
print("   последние значения:")
for r in query("""SELECT period_start, value FROM data.observation
                  WHERE metric_id=%s ORDER BY period_start DESC LIMIT 4""", (metric_id,)):
    print("     ", r)

# ---------- 5. соответствия ----------
print("\n=== привязка к теме и синонимы ===")
for a in ("ключевая ставка", "ставка ЦБ", "ставка Банка России", "key rate"):
    try:
        execute("""INSERT INTO catalog.metric_alias (metric_id, alias, alias_type)
                   VALUES (%s, %s, 'synonym')""", (metric_id, a))
        print("   синоним:", a)
    except Exception as e:
        print("   ERR", a, str(e)[:80])
try:
    execute("""INSERT INTO catalog.metric_topic (metric_id, topic_id, weight)
               SELECT %s, topic_id, 1 FROM catalog.topic WHERE topic_code='dku'
               ON CONFLICT DO NOTHING""", (metric_id,))
    print("   тема: dku")
except Exception as e:
    print("   ERR темы:", str(e)[:80])