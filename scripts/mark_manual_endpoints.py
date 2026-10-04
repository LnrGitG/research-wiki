#!/usr/bin/env python3
"""Честные пометки по точкам, которые автообновлению не поддаются как есть.

Живые прогоны показали:
  - ДОМ.РФ: разбор ищет выгрузки в data/raw/domrf и просит положить CSV,
    скачанные с сайта вручную. Публичной ленты с файлами нет — автоопрос
    такую точку обслужить не может, пока выгрузки кладут руками.
  - ФНС: разбору нужен /tmp/fns_scan.json, который готовит отдельный шаг
    разведки. Двухступенчатый разбор надо описывать явно (parser_pre),
    иначе задача падает на отсутствии файла.
"""
import sys
sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import execute, query

UPD = [
 ("https://дом.рф/analytics/", None,
  "Автоопрос не обслуживает: разбор ищет выгрузки в data/raw/domrf, а "
  "публичной ленты с файлами нет — выгрузки кладут руками. Точку держать "
  "как напоминание о ручном шаге, а не как задачу автообновления."),
 ("https://www.nalog.gov.ru/opendata/", None,
  "Двухступенчатый разбор: нужен подготовительный шаг разведки, готовящий "
  "/tmp/fns_scan.json. Пока parser_pre не описан, задача падает — это и "
  "видно в журнале прогонов."),
]
for url, args, note in UPD:
    n = execute("""UPDATE catalog.source_endpoint
                      SET parser_script = %s,
                          note = coalesce(note,'') || ' || ' || %s
                    WHERE url = %s""", (args, note, url))
    print(f"   {'OK ' if n else 'нет'} {url[:40]}")

print("\n=== итоговая картина по точкам ===")
for r in query("""SELECT s.source_code,
                         coalesce(e.parser_script, '—') AS скрипт,
                         coalesce(e.parser_args, '—')   AS аргументы,
                         CASE WHEN e.parser_script IS NULL THEN 'ручной/не подключён'
                              ELSE 'авто' END AS режим
                  FROM catalog.source_endpoint e
                  JOIN catalog.source s ON s.source_id = e.source_id
                  ORDER BY 2, 1"""):
    print(f"   {r[0]:14s} {r[1]:26s} {r[2]:20s} {r[3]}")

print("\n=== итог разбора ===")
print("успешно загружено выпусков:",
      query("SELECT count(*) FROM ops.ingest_run WHERE status='done'")[0][0])
print("прогонов всего:", query("SELECT count(*) FROM ops.ingest_run")[0][0])
print("точек в авторежиме:",
      query("SELECT count(*) FROM catalog.source_endpoint WHERE parser_script IS NOT NULL")[0][0])