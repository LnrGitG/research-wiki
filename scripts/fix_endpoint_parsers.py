#!/usr/bin/env python3
"""Приведение точек публикации к фактическим именам скриптов на ВМ.

Первоначальное наполнение использовало имена из репозитория на рабочем VPS,
но на ВМ эти файлы лежат в клоне репозитория, и часть имён там другая.
Проверено листингом: есть kep_collect.py, fns_opendata_collect.py,
ingest_domrf.py; вместо load_cbr_keyrate.py — ingest_cbr.py,
вместо load_cbr_lending.py — cbr_lending_update.py,
вместо step2_ingest_all.py — emiss_loader.py.
"""
import sys
sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import execute, query

FIX = {
 "https://rosstat.gov.ru/compendium/document/50798": "kep_collect.py",
 "https://rosstat.gov.ru/storage/mediabank/": None,
 "https://www.fedstat.ru/indicator/31074": "emiss_loader.py",
 "https://www.cbr.ru/hd_base/KeyRate/": "ingest_cbr.py",
 "https://www.cbr.ru/statistics/": "cbr_lending_update.py",
 "https://www.nalog.gov.ru/opendata/": "fns_opendata_collect.py",
 "https://дом.рф/analytics/": "ingest_domrf.py",
 "https://rosreestr.gov.ru/opendata/": None,
}
print("=== правка скриптов разбора ===")
for url, script in FIX.items():
    try:
        n = execute("""UPDATE catalog.source_endpoint SET parser_script = %s WHERE url = %s""",
                    (script, url))
        print(f"   {'OK ' if n else 'нет'} {url[:46]:46s} -> {script}")
    except Exception as e:
        print(f"   ERR {url[:40]}: {str(e)[:120]}")

print("\n=== состояние точек ===")
for r in query("""SELECT s.source_code, e.parser_script, e.is_active
                  FROM catalog.source_endpoint e
                  JOIN catalog.source s ON s.source_id = e.source_id
                  ORDER BY s.source_code, e.endpoint_id"""):
    mark = "готов" if r[1] else "БЕЗ РАЗБОРА"
    print(f"   {r[0]:14s} {str(r[1]):24s} {mark}")

print("\n=== закрытие задач, оставшихся от ошибочных имён ===")
n = execute("""UPDATE ops.ingest_queue
                  SET status='skipped', finished_at=now(),
                      last_error='снято: имя скрипта исправлено'
                WHERE status='pending'
                  AND discovered_at < now() - interval '20 minutes'""")
print("   снято задач:", n)

print("\n=== очередь после правки ===")
for r in query("SELECT status, count(*) FROM ops.ingest_queue GROUP BY 1 ORDER BY 2 DESC"):
    print("  ", r)