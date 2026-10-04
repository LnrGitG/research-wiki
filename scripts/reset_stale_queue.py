#!/usr/bin/env python3
"""Снять задачи со старыми именами скриптов и вернуть сбойные в очередь.

Задачи 9 и 10 были поставлены до переименования (step2_ingest_all.py,
load_cbr_keyrate.py) — такие файлы на ВМ не существуют и существовать не
будут, повторять их бессмысленно.
"""
import sys
sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import execute, query

STALE = ("step2_ingest_all.py", "load_cbr_keyrate.py", "load_cbr_lending.py")
for name in STALE:
    n = execute("""UPDATE ops.ingest_queue
                      SET status='skipped', finished_at=now(),
                          last_error='снято: имя скрипта заменено на фактическое'
                    WHERE parser_script = %s AND status IN ('pending','failed')""",
                (name,))
    print(f"   снято по {name}: {n}")

# проставить фактическое имя там, где точка его уже сменила
fixed = execute("""UPDATE ops.ingest_queue q
                      SET parser_script = e.parser_script, status='pending',
                          attempts=0, last_error=NULL
                     FROM catalog.source_endpoint e
                    WHERE e.endpoint_id = q.endpoint_id
                      AND q.status = 'failed'
                      AND q.parser_script IS DISTINCT FROM e.parser_script
                      AND e.parser_script IS NOT NULL""")
print("   исправлено имён у сбойных:", fixed)

back = execute("""UPDATE ops.ingest_queue
                     SET status='pending', attempts=0, last_error=NULL
                   WHERE status='failed'""")
print("   возвращено в очередь:", back)

print()
for r in query("SELECT status, count(*) FROM ops.ingest_queue GROUP BY 1 ORDER BY 2 DESC"):
    print("  ", r)
print()
print("=== готовы к разбору ===")
for r in query("""SELECT q.queue_id, s.source_code, q.parser_script
                  FROM ops.ingest_queue q
                  JOIN catalog.source_endpoint e ON e.endpoint_id=q.endpoint_id
                  JOIN catalog.source s ON s.source_id=e.source_id
                  WHERE q.status='pending' ORDER BY q.queue_id"""):
    print("  ", r)