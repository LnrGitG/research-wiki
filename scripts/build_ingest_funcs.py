#!/usr/bin/env python3
"""Функции очереди загрузок. Подаются целиком: долларовые кавычки $$ не
переживают разбиение по ';', и тела функций превращаются в мусор."""
import sys
sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import execute, query

FUNCS = []

FUNCS.append(r"""
CREATE OR REPLACE FUNCTION ops.enqueue_release(
        p_endpoint_id int, p_hash text, p_published_hint text DEFAULT NULL,
        p_payload_ref text DEFAULT NULL)
RETURNS bigint LANGUAGE plpgsql AS $$
DECLARE v_queue bigint;
BEGIN
    INSERT INTO ops.release_seen (endpoint_id, content_hash, published_hint, payload_ref)
    VALUES (p_endpoint_id, p_hash, p_published_hint, p_payload_ref)
    ON CONFLICT (endpoint_id, content_hash) DO NOTHING;

    IF NOT FOUND THEN
        RETURN NULL;
    END IF;

    INSERT INTO ops.ingest_queue (endpoint_id, content_hash, parser_script)
    SELECT p_endpoint_id, p_hash, e.parser_script
    FROM catalog.source_endpoint e WHERE e.endpoint_id = p_endpoint_id
    ON CONFLICT (endpoint_id, content_hash) DO NOTHING
    RETURNING queue_id INTO v_queue;

    UPDATE catalog.source_endpoint
       SET last_checked_at = now(), last_hash = p_hash
     WHERE endpoint_id = p_endpoint_id;

    RETURN v_queue;
END $$
""")

FUNCS.append(r"""
CREATE OR REPLACE FUNCTION ops.claim_ingest(p_limit int DEFAULT 3)
RETURNS TABLE (queue_id bigint, endpoint_id int, url text, parser_script text,
               attempts int, content_hash text)
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
              q.parser_script, q.attempts, q.content_hash
$$;
""")

FUNCS.append(r"""
CREATE OR REPLACE FUNCTION ops.finish_ingest(
        p_queue_id bigint, p_status text, p_rows bigint DEFAULT NULL,
        p_exit int DEFAULT NULL, p_error text DEFAULT NULL, p_tail text DEFAULT NULL)
RETURNS void LANGUAGE plpgsql AS $$
BEGIN
    UPDATE ops.ingest_queue
       SET status = p_status, finished_at = now(), rows_written = p_rows,
           last_error = CASE WHEN p_status = 'failed'
                             THEN left(coalesce(p_error,''), 500) ELSE NULL END
     WHERE queue_id = p_queue_id;

    INSERT INTO ops.ingest_run (queue_id, endpoint_id, parser_script, finished_at,
                                status, rows_written, exit_code, output_tail)
    SELECT p_queue_id, q.endpoint_id, q.parser_script, now(),
           p_status, p_rows, p_exit, left(coalesce(p_tail,''), 2000)
    FROM ops.ingest_queue q WHERE q.queue_id = p_queue_id;
END $$
""")

for i, fn in enumerate(FUNCS, 1):
    name = fn.strip().split("ops.")[1].split("(")[0]
    try:
        execute(fn)
        print(f"OK  ops.{name}")
    except Exception as e:
        print(f"ERR ops.{name}: {str(e)[:250]}")

print("\n=== проверка наличия ===")
for r in query("""SELECT proname, pronargs FROM pg_proc
                  WHERE pronamespace = (SELECT oid FROM pg_namespace WHERE nspname='ops')
                    AND proname IN ('enqueue_release','claim_ingest','finish_ingest')
                  ORDER BY proname"""):
    print("  ", r)