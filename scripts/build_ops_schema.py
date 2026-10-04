#!/usr/bin/env python3
"""Схема ops — эксплуатационный слой: свежесть, качество, алерты.

Разделение обязанностей: правила считает база (это арифметика), делегат на ВМ
читает результат и формулирует короткий дайджест. Модель не должна считать то,
что считается запросом.

ops.freshness_snapshot — снимок свежести на момент времени
ops.quality_rule       — декларативные правила проверки
ops.quality_result     — результаты прогонов правил
ops.alert              — поднятые сигналы с отметкой о доставке
ops.check_freshness()  — снять снимок и поднять алерты
"""
import sys
sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import execute, query

DDL = [
 ("схема", "CREATE SCHEMA IF NOT EXISTS ops AUTHORIZATION wiki"),
 ("ops.freshness_snapshot", """CREATE TABLE IF NOT EXISTS ops.freshness_snapshot (
        snapshot_at timestamptz NOT NULL DEFAULT now(),
        metric_id int NOT NULL,
        metric_code text,
        frequency text,
        freshness text NOT NULL,
        last_observation date,
        observations bigint,
        days_stale int,
        PRIMARY KEY (snapshot_at, metric_id))"""),
 ("ops.quality_rule", """CREATE TABLE IF NOT EXISTS ops.quality_rule (
        rule_id serial PRIMARY KEY,
        rule_code text UNIQUE NOT NULL,
        name_ru text NOT NULL,
        kind text NOT NULL,
        target_topic text,
        params jsonb DEFAULT '{}',
        severity text DEFAULT 'warning',
        is_active boolean DEFAULT true,
        note text)"""),
 ("ops.quality_result", """CREATE TABLE IF NOT EXISTS ops.quality_result (
        result_id bigserial PRIMARY KEY,
        rule_code text NOT NULL,
        checked_at timestamptz NOT NULL DEFAULT now(),
        metric_id int,
        passed boolean NOT NULL,
        detail text,
        value numeric)"""),
 ("ops.alert", """CREATE TABLE IF NOT EXISTS ops.alert (
        alert_id bigserial PRIMARY KEY,
        raised_at timestamptz NOT NULL DEFAULT now(),
        severity text NOT NULL,
        kind text NOT NULL,
        subject text NOT NULL,
        message text,
        metric_id int,
        delivered_at timestamptz,
        acknowledged_at timestamptz)"""),
 ("индекс по свежести", "CREATE INDEX IF NOT EXISTS ix_freshness_snap_at ON ops.freshness_snapshot (snapshot_at DESC)"),
 ("индекс по недоставленным", "CREATE INDEX IF NOT EXISTS ix_alert_undelivered ON ops.alert (delivered_at) WHERE delivered_at IS NULL"),
]
for label, sql in DDL:
    try:
        execute(sql); print(f"OK  {label}")
    except Exception as e:
        print(f"ERR {label}: {str(e)[:200]}")

# ---------- правила качества ----------
RULES = [
 ("null_values",   "Доля пустых значений выше порога", "row_level", None, '{"max_share": 0.2}', "warning"),
 ("dup_periods",   "Дубли периодов по показателю и региону", "row_level", None, '{}', "error"),
 ("gap_periods",   "Разрыв в ряду длиннее ожидаемого", "series", None, '{"max_gap_periods": 3}', "warning"),
 ("jump_values",   "Скачок значения относительно предыдущего", "series", None, '{"max_ratio": 10}', "warning"),
 ("unit_missing",  "У показателя не указана единица измерения", "meta", None, '{}', "info"),
 ("topic_missing", "Показатель не привязан ни к одной теме", "meta", None, '{}', "info"),
 ("freshness_sla", "Нарушен срок свежести по частоте", "series", None, '{}', "warning"),
]
print("\n--- правила качества ---")
for code, name, kind, topic, params, sev in RULES:
    try:
        execute("""INSERT INTO ops.quality_rule (rule_code, name_ru, kind, target_topic, params, severity)
                   VALUES (%s,%s,%s,%s,%s::jsonb,%s) ON CONFLICT (rule_code) DO NOTHING""",
                (code, name, kind, topic, params, sev))
    except Exception as e:
        print("  ERR", code, str(e)[:120])
print("   правил:", query("SELECT count(*) FROM ops.quality_rule")[0][0])

# ---------- снимок свежести ----------
CHECK = """
CREATE OR REPLACE FUNCTION ops.check_freshness()
RETURNS int LANGUAGE plpgsql AS $$
DECLARE n int;
BEGIN
    INSERT INTO ops.freshness_snapshot
        (metric_id, metric_code, frequency, freshness, last_observation, observations, days_stale)
    SELECT metric_id, metric_code, frequency, freshness, last_observation, observations,
           CASE WHEN last_observation IS NULL THEN NULL
                ELSE (now()::date - last_observation) END
    FROM derived.v_metric_context;
    GET DIAGNOSTICS n = ROW_COUNT;

    -- алерты по ухудшению: то, что раньше было свежим, стало устаревшим
    INSERT INTO ops.alert (severity, kind, subject, message, metric_id)
    SELECT 'warning', 'freshness', c.metric_code,
           format('показатель перешёл в «%s»; последнее наблюдение %s (%s дн. назад)',
                  c.freshness, c.last_observation, (now()::date - c.last_observation)),
           c.metric_id
    FROM derived.v_metric_context c
    JOIN LATERAL (
        SELECT freshness FROM ops.freshness_snapshot s
        WHERE s.metric_id = c.metric_id AND s.snapshot_at < now() - interval '1 hour'
        ORDER BY s.snapshot_at DESC LIMIT 1
    ) prev ON true
    WHERE c.freshness IN ('устарели','отстают')
      AND prev.freshness = 'свежие'
      AND NOT EXISTS (SELECT 1 FROM ops.alert a
                      WHERE a.metric_id = c.metric_id AND a.kind='freshness'
                        AND a.raised_at > now() - interval '3 days');
    RETURN n;
END $$;
"""
try:
    execute(CHECK); print("\nOK  ops.check_freshness() создана")
except Exception as e:
    print("\nERR:", str(e)[:250])

# ---------- витрины ----------
BOARD = """
CREATE OR REPLACE VIEW ops.v_freshness_board AS
SELECT frequency, freshness, count(*) AS показателей,
       round(100.0*count(*)/sum(count(*)) OVER (PARTITION BY frequency), 1) AS доля_pct
FROM derived.v_metric_context GROUP BY 1,2 ORDER BY 1,3 DESC
"""
QLIST = """
CREATE OR REPLACE VIEW ops.v_quality_board AS
SELECT r.rule_code, r.name_ru, r.severity,
       count(*) FILTER (WHERE NOT q.passed) AS нарушений,
       max(q.checked_at) AS последняя_проверка
FROM ops.quality_rule r
LEFT JOIN ops.quality_result q ON q.rule_code = r.rule_code
GROUP BY 1,2,3 ORDER BY 4 DESC NULLS LAST
"""
for label, sql in (("ops.v_freshness_board", BOARD), ("ops.v_quality_board", QLIST)):
    try:
        execute(sql); print(f"OK  {label}")
    except Exception as e:
        print(f"ERR {label}: {str(e)[:200]}")

try:
    execute("GRANT USAGE ON SCHEMA ops TO viewer, datalens_ro, agent_ro")
    execute("GRANT SELECT ON ALL TABLES IN SCHEMA ops TO viewer, datalens_ro, agent_ro")
    print("OK  права на ops")
except Exception as e:
    print("ERR прав:", str(e)[:150])

print("\n=== прогон check_freshness ===")
try:
    n = query("SELECT ops.check_freshness()")[0][0]
    print("   снято строк снимка:", n)
    print("   поднято алертов:", query("SELECT count(*) FROM ops.alert")[0][0])
except Exception as e:
    print("   ERR:", str(e)[:200])