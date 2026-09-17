#!/usr/bin/env python3
"""
Миграция SQLite → PostgreSQL: зеркалирование в staging.

Этап 1: точный слепок исходных данных без преобразований.
  - читает SQLite из S3-бакета agent-vm-exchange;
  - создаёт в PostgreSQL staging.<db>__<table> с теми же колонками;
  - заливает строки батчами;
  - сверяет COUNT(*) по каждой таблице.

Идемпотентен: DROP + CREATE на каждую таблицу.

Запуск:  python3 mirror_to_staging.py [часть_имени_базы]
Выход:   /tmp/migrate_report.json
"""
import sqlite3, json, os, sys, re
import urllib.request

EP = "https://storage.yandexcloud.net/agent-vm-exchange"
DSN = os.environ.get("PGDSN", "postgresql:///research_wiki")


def meta_token() -> str:
    """IAM-токен сервисного аккаунта ВМ."""
    r = urllib.request.Request(
        "http://169.254.169.254/computeMetadata/v1/instance/service-accounts/default/token",
        headers={"Metadata-Flavor": "Google"})
    return json.load(urllib.request.urlopen(r, timeout=20))["access_token"]


TOK = meta_token()


def s3get(key: str) -> bytes:
    r = urllib.request.Request(f"{EP}/{key}", headers={"X-YaCloud-SubjectToken": TOK})
    return urllib.request.urlopen(r, timeout=900).read()


def pg():
    import psycopg
    # локальное peer-подключение от имени postgres невозможно под ubuntu;
    # используем роль wiki через TCP с паролем из окружения
    return psycopg.connect(DSN)


def sqlite_type_to_pg(t: str) -> str:
    t = (t or '').upper()
    if 'INT' in t:
        return 'bigint'
    if any(x in t for x in ('REAL', 'FLOA', 'DOUB', 'NUM', 'DEC')):
        return 'numeric'
    return 'text'


def stg_name(db: str, table: str) -> str:
    return re.sub(r'[^a-z0-9_]', '_', f"{db.replace('.db', '')}__{table}".lower())


def migrate(db_name: str, s3_key: str, report: dict) -> None:
    print(f"\n=== {db_name} ===", flush=True)
    raw = s3get(s3_key)
    tmp = f"/tmp/{db_name}"
    with open(tmp, 'wb') as f:
        f.write(raw)
    print(f"  скачан: {len(raw) / 1e6:.1f} МБ", flush=True)

    sc = sqlite3.connect(tmp)
    tables = [r[0] for r in sc.execute(
        "SELECT name FROM sqlite_master WHERE type='table' "
        "AND name NOT LIKE 'sqlite_%' ORDER BY name")]
    print(f"  таблиц: {len(tables)}", flush=True)

    pc = pg()
    pcur = pc.cursor()
    pcur.execute("CREATE SCHEMA IF NOT EXISTS staging")
    pc.commit()

    total_rows = 0
    for t in tables:
        cols = list(sc.execute(f'PRAGMA table_info("{t}")'))
        if not cols:
            continue
        colnames = [c[1] for c in cols]
        coltypes = [sqlite_type_to_pg(c[2]) for c in cols]
        stg = stg_name(db_name, t)

        defs = ", ".join(f'"{cn}" {ct}' for cn, ct in zip(colnames, coltypes))
        pcur.execute(f'DROP TABLE IF EXISTS staging."{stg}"')
        pcur.execute(f'CREATE TABLE staging."{stg}" ({defs})')
        pc.commit()

        qmarks = ",".join(["%s"] * len(colnames))
        ins = f'INSERT INTO staging."{stg}" VALUES ({qmarks})'
        cur = sc.execute(f'SELECT * FROM "{t}"')
        n = 0
        while True:
            rows = cur.fetchmany(5000)
            if not rows:
                break
            batch = [tuple(str(v) if isinstance(v, (bytes, bytearray)) else v for v in r)
                     for r in rows]
            try:
                pcur.executemany(ins, batch)
            except Exception as e:
                # при несовпадении типов пересоздаём таблицу как text
                print(f"    ! {t}: пересоздаю как text ({str(e)[:60]})", flush=True)
                pc.rollback()
                defs2 = ", ".join(f'"{cn}" text' for cn in colnames)
                pcur.execute(f'DROP TABLE IF EXISTS staging."{stg}"')
                pcur.execute(f'CREATE TABLE staging."{stg}" ({defs2})')
                pcur.executemany(
                    ins, [tuple(str(x) if x is not None else None for x in b) for b in batch])
            pc.commit()
            n += len(batch)
        total_rows += n
        print(f"    {stg}: {n:,} строк", flush=True)

    # ── верификация: счётчики строк ──
    print(f"  --- проверка {db_name} ---", flush=True)
    ok = True
    mismatches = []
    for t in tables:
        sq = sc.execute(f'SELECT COUNT(*) FROM "{t}"').fetchone()[0]
        stg = stg_name(db_name, t)
        try:
            pq = pcur.execute(f'SELECT COUNT(*) FROM staging."{stg}"').fetchone()[0]
        except Exception:
            pq = -1
        if sq != pq:
            ok = False
            mismatches.append({"table": t, "sqlite": sq, "pg": pq})
            print(f"    РАСХОЖДЕНИЕ {t}: sqlite={sq} pg={pq}", flush=True)
    print(f"  счётчики: {'СОВПАДАЮТ' if ok else 'ЕСТЬ РАСХОЖДЕНИЯ'}", flush=True)

    report[db_name] = {"tables": len(tables), "rows": total_rows,
                       "verified": ok, "mismatches": mismatches}
    pc.close()
    sc.close()
    os.remove(tmp)


if __name__ == "__main__":
    report = {}
    dbs = [
        ("developers_ifrs.db",      "_cmd/db/developers_ifrs.db"),
        ("rosreestr_deals.db",      "_cmd/db/rosreestr_deals.db"),
        ("cbr_lending.db",          "_cmd/db/cbr_lending.db"),
        ("regions_panel.db",        "_cmd/db/regions_panel.db"),
        ("fns_tochno_sectors.db",   "_cmd/db/fns_tochno_sectors.db"),
        ("rosstat_construction.db", "_cmd/db/rosstat_construction.db"),
    ]
    only = sys.argv[1] if len(sys.argv) > 1 else None
    for name, key in dbs:
        if only and only not in name:
            continue
        try:
            migrate(name, key, report)
        except Exception as e:
            print(f"  ОШИБКА {name}: {e}", flush=True)
            report[name] = {"error": str(e)[:300]}
    print("\n=== ИТОГ ===")
    print(json.dumps(report, ensure_ascii=False, indent=1))
    with open('/tmp/migrate_report.json', 'w') as f:
        json.dump(report, f, ensure_ascii=False, indent=1)
