#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Точечный снимок таблиц канона в JSON и обратная заливка.

Зачем: на VPS нет ни `pg_dump`, ни `psql` (проверено 20.10.2026), а перед правкой
схемы нужна точка возврата. Полный дамп базы делать нельзя — векторный слой
раздувает его до гигабайтов, — поэтому снимаются только затрагиваемые таблицы.

Формат: на каждую таблицу — `<schema>.<table>.json` с колонками и строками;
типы, которых нет в JSON (date/datetime, Decimal, массивы, jsonb), приводятся
к строкам/спискам при снимке и восстанавливаются адаптацией драйвера по типу
колонки. DDL в снимок не входит: меняются данные, а не структура таблиц;
определения представлений сохраняются отдельными `.sql` файлами.

Использование:

    python3 scripts/db_snapshot_tables.py snapshot \
        --tables catalog.source_endpoint,ops.ingest_endpoint \
        --out attic/db-snapshot-20261020

    python3 scripts/db_snapshot_tables.py restore \
        --dir attic/db-snapshot-20261020 [--apply]

Без `--apply` restore только печатает, что будет сделано.
"""
import argparse
import base64
import datetime as dt
import json
import os
import sys
from decimal import Decimal

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from db_tunnel import connect  # noqa: E402


def _cols(cur, schema, table):
    cur.execute(
        """SELECT column_name, data_type FROM information_schema.columns
           WHERE table_schema=%s AND table_name=%s ORDER BY ordinal_position""",
        (schema, table),
    )
    return cur.fetchall()


def _enc(v):
    if isinstance(v, (dt.date, dt.datetime)):
        return v.isoformat()
    if isinstance(v, Decimal):
        return str(v)
    if isinstance(v, (bytes, bytearray, memoryview)):
        return {'__b64__': base64.b64encode(bytes(v)).decode()}
    if isinstance(v, dict):
        return {'__json__': v}
    if isinstance(v, list):
        return {'__array__': [_enc(x) for x in v]}
    return v


def _dec(v, dtype):
    if isinstance(v, dict):
        if '__b64__' in v:
            return base64.b64decode(v['__b64__'])
        if '__json__' in v:
            return json.dumps(v['__json__'])
        if '__array__' in v:
            return [_dec(x, dtype) for x in v['__array__']]
        return json.dumps(v)
    if isinstance(v, list):
        return [_dec(x, dtype) for x in v]
    return v


def snapshot(tables, outdir):
    os.makedirs(outdir, exist_ok=True)
    meta = {'created_at': dt.datetime.now(dt.timezone.utc).isoformat(), 'tables': []}
    with connect() as c, c.cursor() as cur:
        for t in tables:
            schema, table = t.split('.')
            cols = _cols(cur, schema, table)
            names = [x[0] for x in cols]
            cur.execute('SELECT %s FROM %s.%s' % (
                ', '.join('"%s"' % n for n in names), schema, table))
            rows = [[_enc(v) for v in r] for r in cur.fetchall()]
            path = os.path.join(outdir, '%s.%s.json' % (schema, table))
            with open(path, 'w', encoding='utf-8') as fh:
                json.dump({'table': t, 'columns': names,
                           'types': [x[1] for x in cols], 'rows': rows},
                          fh, ensure_ascii=False, indent=1)
            meta['tables'].append({'table': t, 'rows': len(rows),
                                   'file': os.path.basename(path)})
            print('%-40s %6d строк -> %s' % (t, len(rows), path))
        # определения представлений, если они есть среди запрошенных
        cur.execute("""SELECT schemaname, viewname, definition FROM pg_views
                       WHERE (schemaname || '.' || viewname) = ANY(%s)""", (tables,))
        for schema, name, ddl in cur.fetchall():
            p = os.path.join(outdir, '%s.%s.sql' % (schema, name))
            with open(p, 'w', encoding='utf-8') as fh:
                fh.write('CREATE OR REPLACE VIEW %s.%s AS\n%s;\n' % (schema, name, ddl.strip()))
            print('%-40s DDL -> %s' % ('%s.%s' % (schema, name), p))
    with open(os.path.join(outdir, '_meta.json'), 'w', encoding='utf-8') as fh:
        json.dump(meta, fh, ensure_ascii=False, indent=1)
    return meta


def restore(outdir, apply):
    meta = json.load(open(os.path.join(outdir, '_meta.json'), encoding='utf-8'))
    total = 0
    with connect() as c, c.cursor() as cur:
        for item in meta['tables']:
            data = json.load(open(os.path.join(outdir, item['file']), encoding='utf-8'))
            table, names, types = data['table'], data['columns'], data['types']
            schema, tbl = table.split('.')
            cur.execute("""SELECT a.attname FROM pg_index i
                           JOIN pg_attribute a ON a.attrelid=i.indrelid AND a.attnum=ANY(i.indkey)
                           WHERE i.indrelid=%s::regclass AND i.indisprimary""", (table,))
            pk = [r[0] for r in cur.fetchall()]
            cols = ', '.join('"%s"' % n for n in names)
            sql = 'INSERT INTO %s (%s) VALUES (%s)' % (table, cols, ', '.join(['%s'] * len(names)))
            if pk:
                upd = ', '.join('"%s"=EXCLUDED."%s"' % (n, n) for n in names if n not in pk)
                sql += ' ON CONFLICT (%s) DO UPDATE SET %s' % (
                    ', '.join('"%s"' % n for n in pk), upd or '"%s"=EXCLUDED."%s"' % (pk[0], pk[0]))
            else:
                sql += ' ON CONFLICT DO NOTHING'
            rows = [[_dec(v, t) for v, t in zip(r, types)] for r in data['rows']]
            print('%s: %d строк%s' % (table, len(rows), '' if apply else ' (пробный прогон)'))
            if apply and rows:
                cur.executemany(sql, rows)
                total += len(rows)
        if apply:
            c.commit()
    print('вставлено/обновлено:', total if apply else 'ничего (нужен --apply)')


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest='cmd', required=True)
    s = sub.add_parser('snapshot')
    s.add_argument('--tables', required=True)
    s.add_argument('--out', required=True)
    r = sub.add_parser('restore')
    r.add_argument('--dir', required=True)
    r.add_argument('--apply', action='store_true')
    a = ap.parse_args()
    if a.cmd == 'snapshot':
        snapshot([t.strip() for t in a.tables.split(',') if t.strip()], a.out)
    else:
        restore(a.dir, a.apply)


if __name__ == '__main__':
    main()
