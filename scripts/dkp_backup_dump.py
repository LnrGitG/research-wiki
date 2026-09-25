# -*- coding: utf-8 -*-
"""Точка возврата перед исправлением лестницы: дамп схемы dkp (DDL+данные)."""
import os
import subprocess
import sys

OUT = "/home/lnr/research-wiki-private/backups/dkp_pre_ladder_fix_20260925.sql"
os.makedirs(os.path.dirname(OUT), exist_ok=True)

# pg_dump через тоннель (~/.pgpass содержит запись для 15432)
cmd = ["pg_dump", "-h", "127.0.0.1", "-p", "15432", "-U", "wiki",
       "-d", "research_wiki", "-n", "dkp", "-f", OUT]
try:
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    if r.returncode != 0:
        raise RuntimeError(r.stderr[:500])
    size = os.path.getsize(OUT)
    print(f"pg_dump OK: {OUT} ({size} bytes)")
except Exception as e:
    print(f"pg_dump failed: {e} → python-фолбэк")
    sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
    from db_tunnel import query

    lines = []
    tables = query("""SELECT table_name FROM information_schema.tables
                      WHERE table_schema='dkp' AND table_type='BASE TABLE'""")
    for (t,) in tables:
        rows = query(f"SELECT * FROM dkp.{t}")
        cols = query("""SELECT column_name FROM information_schema.columns
                        WHERE table_schema='dkp' AND table_name='%s'
                        ORDER BY ordinal_position""" % t)
        names = ",".join(c[0] for c in cols)
        lines.append(f"-- dkp.{t}: {len(rows)} rows")
        for row in rows:
            vals = []
            for v in row:
                if v is None:
                    vals.append("NULL")
                elif isinstance(v, str):
                    vals.append("'" + v.replace("'", "''") + "'")
                else:
                    vals.append(str(v))
            lines.append(f"INSERT INTO dkp.{t} ({names}) VALUES ({','.join(vals)});")
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"python-дамп OK: {OUT} ({os.path.getsize(OUT)} bytes)")