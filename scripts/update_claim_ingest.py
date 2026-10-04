#!/usr/bin/env python3
"""claim_ingest возвращает аргументы и подготовительный скрипт точки."""
import sys
sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import execute, query

FN = r"""
CREATE OR REPLACE FUNCTION ops.claim_ingest(p_limit int DEFAULT 3)
RETURNS TABLE (queue_id bigint, endpoint_id int, url text, parser_script text,
               parser_args text, parser_pre text, attempts int, content_hash text)
LANGUAGE sql AS $$
    WITH claimed AS (
        SELECT q.queue_id FROM ops.ingest_queue q
        WHERE q.status = 'pending' AND q.attempts < q.max_attempts
        ORDER BY q.priority, q.discovered_at
        LIMIT p_limit
        FOR UPDATE SKIP LOCKED
    )
    UPDATE ops.ingest_queue q
       SET status = 'running', started_at = now(), attempts = q.attempts + 1
      FROM claimed c
     WHERE q.queue_id = c.queue_id
    RETURNING q.queue_id, q.endpoint_id,
              (SELECT e.url FROM catalog.source_endpoint e WHERE e.endpoint_id = q.endpoint_id),
              q.parser_script,
              (SELECT e.parser_args FROM catalog.source_endpoint e WHERE e.endpoint_id = q.endpoint_id),
              (SELECT e.parser_pre  FROM catalog.source_endpoint e WHERE e.endpoint_id = q.endpoint_id),
              q.attempts, q.content_hash
$$;
"""
try:
    execute("DROP FUNCTION IF EXISTS ops.claim_ingest(int)")
    execute(FN)
    print("OK  claim_ingest обновлена")
except Exception as e:
    print("ERR:", str(e)[:300])

print("колонок в возврате:", query("""SELECT count(*) FROM pg_get_function_result(
        'ops.claim_ingest(int)'::regprocedure) t WHERE t LIKE '%'""")[0][0] if False else "—")
r = query("SELECT * FROM ops.claim_ingest(0)")
print("проверка вызова (пустая выборка):", len(r), "строк")