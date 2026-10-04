#!/usr/bin/env python3
import sys
sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import query

print("=== текущий пользователь и его роли ===")
for r in query("SELECT current_user, session_user"):
    print("   current:", r[0], "| session:", r[1])
for r in query("""SELECT r.rolname, r.rolsuper, r.rolcreaterole, r.rolcreatedb,
                         pg_has_role(current_user, r.oid, 'MEMBER') AS is_member
                  FROM pg_roles r
                  WHERE r.rolname NOT LIKE 'pg_%'
                  ORDER BY 1"""):
    print(f"   роль {r[0]:20s} super={r[1]} createrole={r[2]} member={r[4]}")

print("\n=== владельцы таблиц ===")
for r in query("""SELECT n.nspname, c.relname, pg_get_userbyid(c.relowner) AS owner, c.relkind
                  FROM pg_class c JOIN pg_namespace n ON n.oid=c.relnamespace
                  WHERE n.nspname IN ('core','catalog','data','derived')
                    AND c.relkind IN ('r','v','m','p')
                    AND c.relname IN ('observation_v2','observation_v2_legacy','metric',
                                      'metric_legacy','source','release','region','unit',
                                      'frequency','observation')
                  ORDER BY 1,2"""):
    print(f"   {r[0]}.{r[1]:26s} owner={r[2]:15s} kind={r[3]}")

print("\n=== состояние core сейчас ===")
for r in query("""SELECT c.relname, c.relkind FROM pg_class c
                  JOIN pg_namespace n ON n.oid=c.relnamespace
                  WHERE n.nspname='core' AND c.relkind IN ('r','v','m','p')
                    AND c.relname IN ('observation_v2','observation_v2_legacy','metric',
                                      'source','release','region','unit','frequency')
                  ORDER BY 1"""):
    kind = {"r": "таблица", "v": "представление", "m": "matview", "p": "партиц.таблица"}
    print(f"   {r[0]:26s} {kind.get(r[1], r[1])}")