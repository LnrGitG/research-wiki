# -*- coding: utf-8 -*-
"""Применение kb_ddl.sql транзакционно."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from db_tunnel import execute, query

ddl = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "kb_ddl.sql"),
           encoding="utf-8").read()

# db_tunnel.execute() — по одному стейтменту; разобьём по ';' на верхнем уровне
# (в DDL нет процедур с точками с запятой внутри тел)
stmts = [s.strip() for s in ddl.split(";") if s.strip() and not s.strip().startswith("--")]

ok = 0
for s in stmts:
    # убираем возможные комментарии в начале стейтмента
    lines = [ln for ln in s.splitlines() if not ln.strip().startswith("--")]
    body = "\n".join(lines).strip()
    if not body:
        continue
    try:
        rc = execute(body)
        ok += 1
    except Exception as e:
        print("FAIL:", str(e)[:300])
        print("  statement:", body[:120].replace("\n", " "))
        sys.exit(1)

print(f"applied {ok} statements")
r = query("SELECT table_name FROM information_schema.tables WHERE table_schema='kb' ORDER BY 1")
print("tables:", [x[0] for x in r])
r = query("SELECT indexname FROM pg_indexes WHERE schemaname='kb' ORDER BY 1")
print("indexes:", [x[0] for x in r])