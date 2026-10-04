#!/usr/bin/env python3
"""Сверка загруженного дневного ряда ключевой ставки с лестницей dkp.

Ряд в catalog/data и ступени в dkp.rate_level — независимые представления
одного процесса. Расхождение означает ошибку либо в загрузке ряда, либо в
ремонте лестницы, и должно быть видно, а не замолчано.
"""
import sys
sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import query

metric_id = query("SELECT metric_id FROM catalog.metric WHERE metric_code='cbr_key_rate'")[0][0]

print("=== 1. ступени ряда (из наблюдений) ===")
steps = query("""
    SELECT period_start, value FROM (
        SELECT period_start, value,
               lag(value) OVER (ORDER BY period_start) AS prev
        FROM data.observation WHERE metric_id = %s) t
    WHERE prev IS NULL OR value <> prev
    ORDER BY period_start""", (metric_id,))
print(f"   ступеней: {len(steps)}")

print("\n=== 2. ступени лестницы dkp ===")
ladder = query("""SELECT effective_from, value FROM dkp.rate_level
                  WHERE rate_code='key_rate' ORDER BY effective_from""")
print(f"   ступеней: {len(ladder)}")

print("\n=== 3. сверка по датам вступления ===")
d_steps = {r[0]: r[1] for r in steps}
d_ladder = {r[0]: r[1] for r in ladder}
only_row = sorted(set(d_steps) - set(d_ladder))
only_lad = sorted(set(d_ladder) - set(d_steps))
print(f"   только в ряду: {len(only_row)}")
for d in only_row[:8]:
    print(f"      {d} = {d_steps[d]}")
print(f"   только в лестнице: {len(only_lad)}")
for d in only_lad[:8]:
    print(f"      {d} = {d_ladder[d]}")

diff = [d for d in set(d_steps) & set(d_ladder) if d_steps[d] != d_ladder[d]]
print(f"   совпадающие даты с разным значением: {len(diff)}")
for d in sorted(diff)[:8]:
    print(f"      {d}: ряд {d_steps[d]} против лестницы {d_ladder[d]}")

print("\n=== 4. последние пять ступеней обеих сторон ===")
print("   ряд:")
for r in steps[-5:]:
    print("     ", r[0], r[1])
print("   лестница:")
for r in ladder[-5:]:
    print("     ", r[0], r[1])

print("\n=== 5. непрерывность ряда (пропуски календарных дней) ===")
gaps = query("""
    SELECT count(*) FROM (
        SELECT period_start,
               lag(period_start) OVER (ORDER BY period_start) AS prev
        FROM data.observation WHERE metric_id = %s) t
    WHERE prev IS NOT NULL AND period_start - prev > 5""", (metric_id,))[0][0]
print(f"   разрывов длиннее пяти дней: {gaps}")

print("\n=== 6. видимость в контекстном слое ===")
r = query("SELECT metric_code, name_ru, topic, freshness, observations "
          "FROM derived.v_metric_context WHERE metric_code='cbr_key_rate'")
for x in r:
    print("  ", x)
print("   resolve_metric('ключевая ставка'):")
for x in query("SELECT metric_code, match_kind, score FROM catalog.resolve_metric('ключевая ставка', 3)"):
    print("     ", x)