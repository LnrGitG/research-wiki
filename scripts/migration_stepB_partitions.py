#!/usr/bin/env python3
"""Этап B: партиции на весь диапазон данных.

Схема нарезки: годовые партиции 1970-2014 (там данные редкие — десятки строк
в год), месячные 2015-01 .. 2031-02 (плотная часть). Диапазоны стыкуются без
разрывов и перекрытий, DEFAULT-партиции нет — значит будущие месяцы можно
добавлять свободно.

Идемпотентно: IF NOT EXISTS, уже созданные месяцы пропускаются.
"""
import sys
sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import execute, query

DDL = """CREATE TABLE IF NOT EXISTS data.observation_%s
         PARTITION OF data.observation
         FOR VALUES FROM (%s) TO (%s)"""

made = skipped = failed = 0

# 1) годовые 1970..2014
for y in range(1970, 2015):
    name = f"{y}"
    lo, hi = f"{y}-01-01", f"{y+1}-01-01"
    try:
        execute(DDL % (name, f"'{lo}'", f"'{hi}'"))
        made += 1
    except Exception as e:
        msg = str(e)[:80]
        if "already exists" in msg or "overlap" in msg:
            skipped += 1
        else:
            failed += 1
            print("ERR", name, msg)

print(f"годовые 1970-2014: создано {made}, пропущено {skipped}, ошибок {failed}")

# 2) месячные 2015-01 .. 2031-02
made2 = skipped2 = failed2 = 0
for y in range(2015, 2032):
    for m in range(1, 13):
        if y == 2031 and m > 2:
            break
        name = f"{y}{m:02d}"
        lo = f"{y}-{m:02d}-01"
        hi = f"{y+1}-01-01" if m == 12 else f"{y}-{m+1:02d}-01"
        try:
            execute(DDL % (name, f"'{lo}'", f"'{hi}'"))
            made2 += 1
        except Exception as e:
            msg = str(e)[:80]
            if "already exists" in msg or "overlap" in msg:
                skipped2 += 1
            else:
                failed2 += 1
                if failed2 <= 3:
                    print("ERR", name, msg)

print(f"месячные 2015-2031: создано {made2}, пропущено {skipped2}, ошибок {failed2}")

# 3) контроль покрытия
print("\n=== покрытие ===")
r = query("""SELECT count(*) FILTER (WHERE pg_get_expr(c.relpartbound, c.oid)
                                     LIKE 'FOR VALUES%') AS n_part,
                    min(pg_get_expr(c.relpartbound, c.oid)) AS lo,
                    max(pg_get_expr(c.relpartbound, c.oid)) AS hi
             FROM pg_class c JOIN pg_namespace n ON n.oid=c.relnamespace
             WHERE n.nspname='data' AND c.relispartition""")[0]
print(f"   партиций: {r[0]}")
print(f"   первая: {r[1]}")
print(f"   последняя: {r[2]}")

# 4) проверка: попадает ли каждая дата из источника в какую-то партицию
print("\n=== проверка: месяцы источника, не покрытые партициями ===")
rows = query("""
    WITH m AS (
      SELECT DISTINCT date_trunc('month', period_start)::date AS ms
      FROM core.observation_v2
    )
    SELECT ms FROM m
    WHERE NOT EXISTS (
      SELECT 1 FROM pg_class c JOIN pg_namespace n ON n.oid=c.relnamespace
      WHERE n.nspname='data' AND c.relispartition
        AND pg_get_expr(c.relpartbound, c.oid) LIKE 'FOR VALUES%'
        AND ms >= (regexp_match(pg_get_expr(c.relpartbound, c.oid),
                                'FROM \\(''([0-9-]+)''\\)'))[1]::date
        AND ms <  (regexp_match(pg_get_expr(c.relpartbound, c.oid),
                                'TO \\(''([0-9-]+)''\\)'))[1]::date
    )
    ORDER BY 1""")
print("   непокрытых месяцев:", len(rows))
for r in rows[:10]:
    print("    ", r[0])