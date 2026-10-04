#!/usr/bin/env python3
"""Замыкание автообновления: очередь загрузок, фиксация релизов, прогоны.

Логика разделена на две половины:
  - база знает, что пора (таблицы и функции ниже);
  - планировщик на ВМ умеет сходить в сеть и разобрать (ingest_watcher.py).

ops.release_seen   — какие версии содержимого точки публикации уже видели
                     (дедупликация по хэшу, а не по дате: точка может
                     отдавать ту же страницу со сменой служебной вёрстки)
ops.ingest_queue   — очередь задач на разбор
ops.ingest_run     — журнал прогонов
ops.claim_ingest() — взять пачку задач (FOR UPDATE SKIP LOCKED: два
                     планировщика не возьмут одну задачу)
ops.finish_ingest()— закрыть задачу и записать прогон
ops.enqueue_release() — заметить новую версию и поставить в очередь
"""
import sys
sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import execute, query

DDL = [
 ("ops.release_seen", """CREATE TABLE IF NOT EXISTS ops.release_seen (
        endpoint_id int NOT NULL REFERENCES catalog.source_endpoint(endpoint_id),
        content_hash text NOT NULL,
        first_seen_at timestamptz NOT NULL DEFAULT now(),
        published_hint text,
        payload_ref text,
        note text,
        PRIMARY KEY (endpoint_id, content_hash))"""),
 ("ops.ingest_queue", """CREATE TABLE IF NOT EXISTS ops.ingest_queue (
        queue_id bigserial PRIMARY KEY,
        endpoint_id int NOT NULL REFERENCES catalog.source_endpoint(endpoint_id),
        content_hash text,
        discovered_at timestamptz NOT NULL DEFAULT now(),
        status text NOT NULL DEFAULT 'pending',
        priority int NOT NULL DEFAULT 5,
        attempts int NOT NULL DEFAULT 0,
        max_attempts int NOT NULL DEFAULT 3,
        parser_script text,
        last_error text,
        started_at timestamptz,
        finished_at timestamptz,
        rows_written bigint,
        UNIQUE (endpoint_id, content_hash))"""),
 ("ограничение статуса очереди",
  """ALTER TABLE ops.ingest_queue ADD CONSTRAINT ck_queue_status
     CHECK (status IN ('pending','running','done','failed','skipped'))"""),
 ("ограничение статуса релиза",
  """ALTER TABLE ops.release_seen ADD CONSTRAINT ck_seen_status
     CHECK (true)"""),
 ("ops.ingest_run", """CREATE TABLE IF NOT EXISTS ops.ingest_run (
        run_id bigserial PRIMARY KEY,
        queue_id bigint REFERENCES ops.ingest_queue(queue_id),
        endpoint_id int,
        parser_script text,
        started_at timestamptz NOT NULL DEFAULT now(),
        finished_at timestamptz,
        status text,
        rows_written bigint,
        exit_code int,
        output_tail text)"""),
 ("индекс очереди", "CREATE INDEX IF NOT EXISTS ix_queue_pending ON ops.ingest_queue (status, priority, discovered_at)"),
 ("индекс прогонов", "CREATE INDEX IF NOT EXISTS ix_ingest_run_at ON ops.ingest_run (started_at DESC)"),
]
for label, sql in DDL:
    try:
        execute(sql); print(f"OK  {label}")
    except Exception as e:
        msg = str(e)[:120]
        if "уже существует" in msg or "already exists" in msg:
            print(f"--  {label}: уже есть")
        else:
            print(f"ERR {label}: {msg}")

FN = r"""
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
        RETURN NULL;   -- эта версия уже была
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
END $$;

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
              q.parser_script, q.attempts, q.content_hash;
$$;

CREATE OR REPLACE FUNCTION ops.finish_ingest(
        p_queue_id bigint, p_status text, p_rows bigint DEFAULT NULL,
        p_exit int DEFAULT NULL, p_error text DEFAULT NULL, p_tail text DEFAULT NULL)
RETURNS void LANGUAGE plpgsql AS $$
BEGIN
    UPDATE ops.ingest_queue
       SET status = p_status, finished_at = now(), rows_written = p_rows,
           last_error = CASE WHEN p_status = 'failed' THEN left(coalesce(p_error,''), 500)
                             ELSE NULL END
     WHERE queue_id = p_queue_id;

    INSERT INTO ops.ingest_run (queue_id, endpoint_id, parser_script, finished_at,
                                status, rows_written, exit_code, output_tail)
    SELECT p_queue_id, q.endpoint_id, q.parser_script, now(),
           p_status, p_rows, p_exit, left(coalesce(p_tail,''), 2000)
    FROM ops.ingest_queue q WHERE q.queue_id = p_queue_id;
END $$;
"""
for stmt in [s for s in FN.split(";\n") if s.strip()]:
    try:
        execute(stmt)
    except Exception as e:
        print("ERR функции:", str(e)[:160])
print("OK  функции очереди")

BOARD = """
CREATE OR REPLACE VIEW ops.v_ingest_board AS
SELECT s.source_code,
       e.url,
       e.poll_cron,
       e.parser_script,
       e.is_active,
       count(*) FILTER (WHERE q.status='pending') AS в_очереди,
       count(*) FILTER (WHERE q.status='running') AS в_работе,
       count(*) FILTER (WHERE q.status='done')    AS разобрано,
       count(*) FILTER (WHERE q.status='failed')  AS сбоев,
       max(q.finished_at) AS последний_разбор,
       e.last_checked_at  AS последняя_проверка
FROM catalog.source_endpoint e
JOIN catalog.source s ON s.source_id = e.source_id
LEFT JOIN ops.ingest_queue q ON q.endpoint_id = e.endpoint_id
GROUP BY 1,2,3,4,5,11
"""
try:
    execute(BOARD); print("OK  ops.v_ingest_board")
except Exception as e:
    print("ERR витрины:", str(e)[:160])

try:
    execute("GRANT SELECT ON ALL TABLES IN SCHEMA ops TO viewer, datalens_ro, agent_ro")
    print("OK  права")
except Exception as e:
    print("ERR прав:", str(e)[:150])

print("\n=== контроль ===")
for label, sql in (
    ("точек публикации", "SELECT count(*) FROM catalog.source_endpoint"),
    ("увиденных релизов", "SELECT count(*) FROM ops.release_seen"),
    ("задач в очереди", "SELECT count(*) FROM ops.ingest_queue"),
):
    print(f"   {label:20s} {query(sql)[0][0]}")