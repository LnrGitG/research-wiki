#!/usr/bin/env python3
"""Аргументы запуска у точки публикации.

Живые прогоны показали, что парсеры не однородны: одни запускаются без
аргументов, другим нужен идентификатор источника, третьим — подготовительный
шаг (fns_opendata_collect.py читает /tmp/fns_scan.json, который готовит
отдельный скрипт разведки). Держать это в коде планировщика нельзя — знание
о конкретном источнике принадлежит каталогу.

Добавляется catalog.source_endpoint.parser_args (строка аргументов) и
parser_pre (подготовительный скрипт).
"""
import sys
sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import execute, query

DDL = [
 ("колонка parser_args",
  "ALTER TABLE catalog.source_endpoint ADD COLUMN IF NOT EXISTS parser_args text"),
 ("колонка parser_pre",
  "ALTER TABLE catalog.source_endpoint ADD COLUMN IF NOT EXISTS parser_pre text"),
 ("пояснение к args",
  "COMMENT ON COLUMN catalog.source_endpoint.parser_args IS "
  "'аргументы командной строки, передаваемые скрипту разбора'"),
 ("пояснение к pre",
  "COMMENT ON COLUMN catalog.source_endpoint.parser_pre IS "
  "'скрипт, который надо выполнить перед основным разбором'"),
]
for label, sql in DDL:
    try:
        execute(sql); print(f"OK  {label}")
    except Exception as e:
        print(f"ERR {label}: {str(e)[:150]}")

print("\n=== уточнение точек по фактам прогонов ===")
UPD = [
 # ДОМ.РФ: разбор требует идентификатор источника; берём жилищное строительство
 ("https://дом.рф/analytics/", "domrf_construction",
  "Разбор принимает идентификатор источника. Доступны также "
  "domrf_housing_starts, domrf_apartment_sales, domrf_prices, "
  "domrf_price_index_regions — остальные подключать по мере надобности."),
 # ФНС: разбору нужен файл разведки, который готовит отдельный шаг
 ("https://www.nalog.gov.ru/opendata/", None,
  "Разбор требует /tmp/fns_scan.json — его готовит отдельный скрипт разведки "
  "(fns_scan). Без подготовительного шага разбор падает; подключить, когда "
  "шаг разведки будет описан в parser_pre."),
]
for url, args, note in UPD:
    try:
        n = execute("""UPDATE catalog.source_endpoint
                          SET parser_args = %s, note = coalesce(note,'') || ' | ' || %s
                        WHERE url = %s""", (args, note, url))
        print(f"   {'OK ' if n else 'нет'} {url[:40]:40s} args={args}")
    except Exception as e:
        print(f"   ERR {url[:30]}: {str(e)[:120]}")

print("\n=== итог по точкам ===")
for r in query("""SELECT s.source_code, e.parser_script, e.parser_args, e.parser_pre
                  FROM catalog.source_endpoint e
                  JOIN catalog.source s ON s.source_id = e.source_id
                  ORDER BY s.source_code"""):
    state = "готов" if r[1] else "без разбора"
    print(f"   {r[0]:14s} {str(r[1]):24s} args={str(r[2]):18s} pre={r[3]}  [{state}]")