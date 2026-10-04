#!/usr/bin/env python3
"""Долги: страховочное обновление витрины в pg_cron и права читающих ролей."""
import sys
sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import execute, query

print("=== 1. задание pg_cron (страховка от потерянных уведомлений) ===")
try:
    rows = query("SELECT jobid, schedule, command, active FROM cron.job ORDER BY jobid")
    print("   текущих заданий:", len(rows))
    for r in rows:
        print("   ", r)
except Exception as e:
    print("   нет доступа к cron.job:", str(e)[:150])

try:
    execute("""SELECT cron.schedule('refresh-metric-card', '*/30 * * * *',
               'REFRESH MATERIALIZED VIEW CONCURRENTLY derived.metric_card')""")
    print("   OK задание создано (каждые 30 минут)")
except Exception as e:
    print("   ERR создания:", str(e)[:250])

print("\n=== 2. права читающих ролей на catalog и data ===")
GRANTS = [
    ("USAGE на catalog", "GRANT USAGE ON SCHEMA catalog TO viewer, datalens_ro"),
    ("SELECT на catalog", "GRANT SELECT ON ALL TABLES IN SCHEMA catalog TO viewer, datalens_ro"),
    ("USAGE на data", "GRANT USAGE ON SCHEMA data TO viewer, datalens_ro"),
    ("SELECT на data", "GRANT SELECT ON ALL TABLES IN SCHEMA data TO viewer, datalens_ro"),
    ("SELECT на derived", "GRANT SELECT ON ALL TABLES IN SCHEMA derived TO viewer, datalens_ro"),
    ("USAGE на derived", "GRANT USAGE ON SCHEMA derived TO viewer, datalens_ro"),
]
for label, sql in GRANTS:
    try:
        execute(sql)
        print(f"   OK {label}")
    except Exception as e:
        print(f"   ERR {label}: {str(e)[:160]}")

print("\n=== 3. роль agent_ro для профилей агентов ===")
try:
    exists = query("SELECT 1 FROM pg_roles WHERE rolname='agent_ro'")
    if not exists:
        execute("CREATE ROLE agent_ro LOGIN")
        print("   роль создана")
    else:
        print("   роль уже есть")
except Exception as e:
    print("   ERR создания роли:", str(e)[:200])

for label, sql in [
    ("USAGE catalog", "GRANT USAGE ON SCHEMA catalog TO agent_ro"),
    ("SELECT catalog", "GRANT SELECT ON ALL TABLES IN SCHEMA catalog TO agent_ro"),
    ("USAGE data", "GRANT USAGE ON SCHEMA data TO agent_ro"),
    ("SELECT data", "GRANT SELECT ON ALL TABLES IN SCHEMA data TO agent_ro"),
    ("USAGE derived", "GRANT USAGE ON SCHEMA derived TO agent_ro"),
    ("SELECT derived", "GRANT SELECT ON ALL TABLES IN SCHEMA derived TO agent_ro"),
    ("USAGE dkp", "GRANT USAGE ON SCHEMA dkp TO agent_ro"),
    ("SELECT dkp", "GRANT SELECT ON ALL TABLES IN SCHEMA dkp TO agent_ro"),
    ("USAGE v2", "GRANT USAGE ON SCHEMA v2 TO agent_ro"),
    ("SELECT v2", "GRANT SELECT ON ALL TABLES IN SCHEMA v2 TO agent_ro"),
    ("USAGE core", "GRANT USAGE ON SCHEMA core TO agent_ro"),
    ("SELECT core", "GRANT SELECT ON ALL TABLES IN SCHEMA core TO agent_ro"),
]:
    try:
        execute(sql)
        print(f"   OK {label}")
    except Exception as e:
        print(f"   ERR {label}: {str(e)[:150]}")

print("\n=== контроль ===")
for r in query("""SELECT grantee, table_schema, count(*) AS объектов
                  FROM information_schema.role_table_grants
                  WHERE table_schema IN ('catalog','data','derived')
                    AND grantee IN ('viewer','datalens_ro','agent_ro')
                  GROUP BY 1,2 ORDER BY 1,2"""):
    print(f"   {r[0]:14s} {r[1]:10s} {r[2]}")