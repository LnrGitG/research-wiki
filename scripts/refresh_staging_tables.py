#!/usr/bin/env python3
"""Точечное зеркалирование таблиц SQLite → PostgreSQL staging.<db>__<table>.

Полное зеркало делает scripts/mirror_to_staging.py (читает SQLite из бакета
agent-vm-exchange). Этот скрипт нужен для инкрементального обновления: после
дописывания свежих строк в локальную SQLite достаточно перелить одну-две
таблицы, а затем прогнать соответствующий рубеж гармонизации.

Запуск:
  python3 scripts/refresh_staging_tables.py rosreestr_deals.db:rosstat_ind_prod_saar \
      rosstat_construction.db:prom_products_monthly
  python3 scripts/refresh_staging_tables.py --list          # что лежит в staging
"""
import argparse
import os
import re
import sqlite3
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, 'scripts'))
import db_tunnel  # noqa: E402
from yc_sync import ensure_db  # noqa: E402

TYPE_MAP = {
    'INTEGER': 'bigint', 'INT': 'bigint', 'BIGINT': 'bigint', 'SMALLINT': 'smallint',
    'REAL': 'double precision', 'FLOAT': 'double precision', 'DOUBLE': 'double precision',
    'NUMERIC': 'numeric', 'DECIMAL': 'numeric', 'TEXT': 'text', 'VARCHAR': 'text',
    'DATE': 'date', 'TIMESTAMP': 'timestamptz', 'DATETIME': 'timestamptz', 'BLOB': 'bytea',
    'BOOLEAN': 'boolean',
}


def pg_type(decl):
    base = re.sub(r'\(.*\)', '', (decl or 'TEXT')).strip().upper()
    return TYPE_MAP.get(base, 'text')


def mirror(db_file, table):
    con = sqlite3.connect(str(ensure_db(db_file)))
    cols = con.execute(f'PRAGMA table_info({table})').fetchall()
    if not cols:
        print(f'  {table}: нет такой таблицы в {db_file}')
        return 0
    names = [c[1] for c in cols]
    types = [pg_type(c[2]) for c in cols]
    rows = con.execute(f'SELECT * FROM {table}').fetchall()
    con.close()

    schema, tname = 'staging', f'{re.sub(r"[^a-z0-9_]", "_", db_file.replace(".db", "").lower())}__{table}'
    conn = db_tunnel.connect()
    with conn.cursor() as cur:
        cur.execute(f'DROP TABLE IF EXISTS {schema}.{tname}')
        ddl = ', '.join(f'"{n}" {t}' for n, t in zip(names, types))
        cur.execute(f'CREATE TABLE {schema}.{tname} ({ddl})')
        if rows:
            placeholders = ','.join(['%s'] * len(names))
            cur.executemany(
                f'INSERT INTO {schema}.{tname} ({",".join(chr(34)+n+chr(34) for n in names)}) VALUES ({placeholders})',
                rows)
        cur.execute(f'SELECT count(*) FROM {schema}.{tname}')
        n = cur.fetchone()[0]
    conn.commit()
    print(f'  {schema}.{tname}: строк в SQLite {len(rows)}, в staging {n}')
    return n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('pairs', nargs='*', help='db_file:table')
    ap.add_argument('--list', action='store_true')
    args = ap.parse_args()

    db_tunnel.connect()
    if args.list or not args.pairs:
        for r in db_tunnel.query("""SELECT table_name FROM information_schema.tables
            WHERE table_schema='staging' ORDER BY 1"""):
            print(' ', r[0])
        return 0
    for pair in args.pairs:
        if ':' not in pair:
            print('ожидается db_file:table, получено', pair)
            continue
        db_file, table = pair.split(':', 1)
        print(f'{db_file} → staging :: {table}')
        mirror(db_file, table)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())