#!/usr/bin/env python3
import sys
sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import query

TARGETS = ["core.observation_v2", "core.metric", "core.source",
           "core.release", "core.region", "core.unit", "core.frequency"]

print("=== зависимые представления (схема.имя -> что читает) ===")
for r in query("""
    SELECT DISTINCT
           dn.nspname || '.' || dc.relname AS dependent,
           sn.nspname || '.' || sc.relname AS source,
           dc.relkind
    FROM pg_depend d
    JOIN pg_rewrite rw ON rw.oid = d.objid
    JOIN pg_class dc ON dc.oid = rw.ev_class
    JOIN pg_namespace dn ON dn.oid = dc.relnamespace
    JOIN pg_class sc ON sc.oid = d.refobjid
    JOIN pg_namespace sn ON sn.oid = sc.relnamespace
    WHERE sn.nspname = 'core'
      AND sc.relname IN ('observation_v2','metric','source','release','region','unit','frequency')
      AND dc.relname <> sc.relname
    ORDER BY 1, 2"""):
    kind = {"v": "view", "m": "matview", "r": "table"}.get(r[2], r[2])
    print(f"   {r[0]} ({kind}) <- {r[1]}")

print("\n=== представления в core ===")
for r in query("""SELECT c.relname, c.relkind FROM pg_class c
                  JOIN pg_namespace n ON n.oid=c.relnamespace
                  WHERE n.nspname='core' AND c.relkind IN ('v','m')
                  ORDER BY 1"""):
    print(f"   {r[0]} ({r[1]})")