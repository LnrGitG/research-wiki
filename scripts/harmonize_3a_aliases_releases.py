#!/usr/bin/env python3
"""
Гармонизация: рубеж 3а — алиасы регионов и релизы.

1. Загружает data/region_aliases.csv в meta.region_alias.
2. Создаёт core.release — по одному релизу на источник (текущий срез данных).

Идемпотентно. Запуск: python3 harmonize_3a_aliases_releases.py [--dry-run]
"""
import os, sys, csv, re, hashlib
from collections import Counter

os.environ.setdefault("PGPASSFILE", os.path.expanduser("~/.pgpass"))
import psycopg

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DSN = os.environ.get("PGDSN", "host=127.0.0.1 port=15432 dbname=research_wiki user=wiki")

# релизы: код источника → метка версии
RELEASES = {
    'rosstat':   ('Срез Росстата на 17.09.2026 (перенос из SQLite)', 'loaded'),
    'cbr':       ('Срез Банка России на 17.09.2026 (перенос из SQLite)', 'loaded'),
    'domrf':     ('Срез ДОМ.РФ на 17.09.2026 (перенос из SQLite)', 'loaded'),
    'rosreestr': ('Срез Росреестра на 17.09.2026 (перенос из SQLite)', 'loaded'),
    'fns':       ('Срез ФНС на 17.09.2026 (перенос из SQLite)', 'loaded'),
    'smartlab':  ('Срез МСФО девелоперов на 17.09.2026 (перенос из SQLite)', 'loaded'),
}


def load_aliases():
    """Прочитать алиасы регионов из репозитория."""
    path = os.path.join(REPO, 'data', 'region_aliases.csv')
    if not os.path.exists(path):
        raise SystemExit(f'нет файла алиасов: {path}')
    rows = []
    with open(path, encoding='utf-8') as f:
        for r in csv.DictReader(f):
            raw = (r.get('raw_name') or '').strip()
            code = (r.get('region_code') or '').strip()
            if raw and code:
                rows.append((raw, code, r.get('method') or 'exact',
                             r.get('sources') or None))
    return rows


# схема meta.region_alias: (alias, region_id, source_id, confidence)
# confidence ∈ {exact, manual, inferred, needs_review}
CONFIDENCE = {'exact': 'exact', 'normalized': 'inferred', 'manual': 'manual'}


def register_aliases(cur, rows, region_ids, source_ids, dry):
    """Записать алиасы в meta.region_alias."""
    ins = skip = 0
    by_source = Counter()
    for raw, code, method, sources in rows:
        rid = region_ids.get(code)
        if not rid:
            skip += 1
            continue
        # источник алиаса: из поля sources файла либо общий (rosstat)
        src_code = None
        if sources:
            for cand in re.split(r'[;,|]', str(sources)):
                cand = cand.strip().split('.')[0].strip()
                if cand in source_ids:
                    src_code = cand
                    break
        sid = source_ids.get(src_code or 'rosstat')
        if not sid:
            skip += 1
            continue
        if dry:
            ins += 1
            continue
        conf = CONFIDENCE.get((method or 'exact').lower(), 'inferred')
        cur.execute("""
            INSERT INTO meta.region_alias (alias, region_id, source_id, confidence)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (alias, source_id) DO UPDATE SET
                region_id = EXCLUDED.region_id, confidence = EXCLUDED.confidence
        """, (raw, rid, sid, conf))
        ins += 1
        by_source[src_code or 'rosstat'] += 1
    return ins, skip, by_source


def register_releases(cur, source_ids, dry):
    """Создать по одному релизу на источник."""
    ins = 0
    for code, (label, status) in RELEASES.items():
        sid = source_ids.get(code)
        if not sid:
            continue
        if dry:
            ins += 1
            continue
        cur.execute("SELECT release_id FROM core.release WHERE source_id=%s AND release_label=%s",
                    (sid, label))
        if cur.fetchone():
            continue
        cur.execute("""
            INSERT INTO core.release (source_id, release_label, published_at, status, notes)
            VALUES (%s, %s, now(), %s, %s)
        """, (sid, label, status, 'создан при первичной гармонизации'))
        ins += 1
    return ins


def main():
    dry = '--dry-run' in sys.argv
    conn = psycopg.connect(DSN)
    cur = conn.cursor()

    cur.execute("SELECT region_code, region_id FROM core.region")
    region_ids = dict(cur.fetchall())
    cur.execute("SELECT source_code, source_id FROM core.source")
    source_ids = dict(cur.fetchall())
    print(f"регионов: {len(region_ids)}, источников: {len(source_ids)}")

    print("\n1. Алиасы регионов")
    rows = load_aliases()
    print(f"  в файле: {len(rows)}")
    ins, skip, by_src = register_aliases(cur, rows, region_ids, source_ids, dry)
    print(f"  записано: {ins}, без региона/источника: {skip}")
    print(f"  по источникам: {dict(by_src)}")

    print("\n2. Релизы")
    n_rel = register_releases(cur, source_ids, dry)
    print(f"  создано: {n_rel}")

    if not dry:
        conn.commit()

    print("\n=== ПРОВЕРКА ===")
    cur.execute("SELECT count(*) FROM meta.region_alias")
    print(f"  meta.region_alias: {cur.fetchone()[0]}")
    cur.execute("""SELECT s.source_code, count(*) FROM core.release r
                   JOIN core.source s ON s.source_id=r.source_id GROUP BY 1 ORDER BY 1""")
    for c, n in cur.fetchall():
        print(f"  релизов {c}: {n}")
    conn.close()


if __name__ == '__main__':
    main()
