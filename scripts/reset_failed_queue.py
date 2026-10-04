#!/usr/bin/env python3
"""Вернуть сбойные задачи в очередь: причина сбоя устранена (интерпретатор)."""
import sys
sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import execute, query

n = execute("""UPDATE ops.ingest_queue
                  SET status='pending', attempts=0, last_error=NULL
                WHERE status='failed'""")
print("возвращено в очередь:", n)
for r in query("SELECT status, count(*) FROM ops.ingest_queue GROUP BY 1 ORDER BY 2 DESC"):
    print("  ", r)