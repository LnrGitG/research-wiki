#!/usr/bin/env python3
"""Сквозная проверка контекстного слоя: как профиль найдёт показатель."""
import sys
sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import query

print("1. Разговорный термин -> показатель")
for term in ("инфляция", "базовая инфляция", "розница", "СМР", "промпроизводство",
             "безработица", "зарплата", "инвестиции"):
    r = query("SELECT metric_code, left(name_ru,34), topic, match_kind "
              "FROM catalog.resolve_metric(%s,1)", (term,))
    if r:
        print(f"   «{term}» -> {r[0][0]} | {r[0][1]} | тема {r[0][2]}")
    else:
        print(f"   «{term}» -> не найдено")

print("\n2. Тема + регион + период -> готовый набор")
for topic, region in (("inflation", "RU"), ("labour", "RU"), ("output", None)):
    rows = query("SELECT metric_code, unit, frequency, freshness, last_value "
                 "FROM ops.context_bundle(%s,%s,36)", (topic, region))
    print(f"   {topic:10s} / {region or 'все регионы':12s} -> {len(rows)} показателей")
    for x in rows[:3]:
        print(f"      {x[0]:12s} {x[1] or '-':8s} {x[2]} {x[3]:9s} {x[4]}")

print("\n3. Доска свежести")
for r in query("SELECT freshness, count(*) FROM ops.freshness_snapshot "
               "GROUP BY 1 ORDER BY 2 DESC"):
    print(f"   {r[0]:10s} {r[1]}")

print("\n4. Объекты слоя")
for label, sql in (
    ("синонимы", "SELECT count(*) FROM catalog.metric_alias"),
    ("темы", "SELECT count(*) FROM catalog.topic"),
    ("связи с темами", "SELECT count(*) FROM catalog.metric_topic"),
    ("точки публикации", "SELECT count(*) FROM catalog.source_endpoint"),
    ("правила качества", "SELECT count(*) FROM ops.quality_rule"),
    ("показателей в контексте", "SELECT count(*) FROM derived.v_metric_context"),
):
    print(f"   {label:24s} {query(sql)[0][0]}")

print("\n5. Кто читает слой")
for r in query("""SELECT grantee, count(DISTINCT table_schema) AS схем, count(*) AS объектов
                  FROM information_schema.role_table_grants
                  WHERE grantee IN ('agent_ro','viewer','datalens_ro')
                    AND table_schema IN ('catalog','data','derived','ops','dkp','v2','core')
                  GROUP BY 1 ORDER BY 3 DESC"""):
    print(f"   {r[0]:14s} схем {r[1]}, объектов {r[2]}")