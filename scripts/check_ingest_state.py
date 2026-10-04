#!/usr/bin/env python3
"""Состояние контура автообновления."""
import sys
sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import query

print("=== прогоны разбора ===")
print("всего:", query("SELECT count(*) FROM ops.ingest_run")[0][0])
for r in query("""SELECT run_id, status, exit_code, left(coalesce(output_tail,''),70)
                  FROM ops.ingest_run ORDER BY run_id DESC LIMIT 8"""):
    print("  ", r)

print("\n=== очередь ===")
for r in query("SELECT status, count(*) FROM ops.ingest_queue GROUP BY 1 ORDER BY 2 DESC"):
    print("  ", r)

print("\n=== точки, проверенные за последние 10 минут ===")
rows = query("""SELECT s.source_code, e.last_checked_at
                FROM catalog.source_endpoint e
                JOIN catalog.source s ON s.source_id = e.source_id
                WHERE e.last_checked_at > now() - interval '10 minutes'
                ORDER BY 1""")
for r in rows:
    print("  ", r)
print("  всего:", len(rows))

print("\n=== доска ===")
for r in query("""SELECT source_code, в_очереди, разобрано, сбоев
                  FROM ops.v_ingest_board ORDER BY source_code"""):
    print("  ", r)