#!/usr/bin/env python3
"""
Бэкап PostgreSQL (ВМ research-db) с фактической проверкой восстановления.

Циклы работы:
  1. `pg_dump` в custom-формате (-Fc) во временный файл.
  2. Загрузка дампа в YC Object Storage (бакет wiki-research, префикс backups/).
  3. Проверка восстановления: `pg_restore` в ВРЕМЕННУЮ базу `research_wiki_verify`,
     затем сверка счётчиков строк по каждой таблице схем core/meta/derived/pipeline.
  4. Временная база удаляется.

Каждый бэкап — отдельный объект с датой в имени, плюс маркер `backups/latest.txt`.

Запуск (на ВМ, из-под пользователя ubuntu):
    python3 scripts/pg_backup.py            # полный цикл с проверкой
    python3 scripts/pg_backup.py --no-verify  # только дамп и загрузка

Коды возврата:
    0 — успех (дамп загружен, восстановление сошлось)
    1 — восстановление разошлось (бэкап негодный)
    2 — ошибка на этапе дампа или загрузки
"""
import os
import re
import sys
import json
import time
import subprocess
from datetime import datetime, timezone

# ── Конфигурация ──────────────────────────────────────────────────
DB = os.environ.get("PGDATABASE", "research_wiki")
VERIFY_DB = "research_wiki_verify"
BUCKET = os.environ.get("YC_BUCKET", "wiki-research")
RCLONE_REMOTE = os.environ.get("YC_REMOTE", "yc-s3")
BACKUP_PREFIX = "backups"

# схемы, попадающие в проверку (staging исключён: это слепок исходников,
# его бэкапить не нужно — данные восстановимы из бакета)
SCHEMAS = ("core", "meta", "derived", "pipeline")

TMP_DIR = "/tmp/pg_backup"

os.environ.setdefault("PGPASSFILE", "/home/ubuntu/.pgpass")


def run(cmd, **kw):
    """Выполнить команду, вернуть (rc, stdout+stderr)."""
    r = subprocess.run(cmd, capture_output=True, text=True, **kw)
    return r.returncode, (r.stdout + r.stderr)


def psql(sql, db=DB):
    """Выполнить SQL, вернуть вывод (убрать рамки)."""
    rc, out = run(["psql", "-h", "localhost", "-U", "wiki", "-d", db,
                   "-tAc", sql])
    if rc != 0:
        raise RuntimeError(f"psql failed: {out[:300]}")
    return out.strip()


def count_rows(db=DB):
    """Счётчики строк по всем таблицам целевых схем: {(schema, table): n}."""
    rows = psql(f"""
        SELECT schemaname, tablename FROM pg_tables
        WHERE schemaname IN ('{"','".join(SCHEMAS)}')
        ORDER BY schemaname, tablename
    """, db)
    out = {}
    for line in rows.splitlines():
        if "|" not in line:
            continue
        sch, tbl = line.split("|", 1)
        sch, tbl = sch.strip(), tbl.strip()
        try:
            n = int(psql(f'SELECT COUNT(*) FROM "{sch}"."{tbl}"', db))
        except Exception as e:
            n = f"ошибка: {str(e)[:40]}"
        out[f"{sch}.{tbl}"] = n
    return out


def main():
    verify = "--no-verify" not in sys.argv
    t0 = time.time()
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    os.makedirs(TMP_DIR, exist_ok=True)
    dump_file = os.path.join(TMP_DIR, f"{DB}-{stamp}.dump")
    report = {"started": stamp, "database": DB}

    # ── 1. дамп ──
    print(f"[backup] pg_dump {DB} → {dump_file}", flush=True)
    rc, out = run(["pg_dump", "-h", "localhost", "-U", "wiki",
                   "-Fc", "-d", DB, "-f", dump_file])
    if rc != 0:
        print(f"[backup] ДАМП НЕ УДАЛСЯ: {out[:300]}", file=sys.stderr)
        report["error"] = "pg_dump failed"
        print(json.dumps(report, ensure_ascii=False))
        return 2
    size = os.path.getsize(dump_file)
    report["dump_bytes"] = size
    print(f"[backup] дамп готов: {size/1e6:.1f} МБ", flush=True)

    # ── 2. загрузка в бакет ──
    key = f"{BACKUP_PREFIX}/{os.path.basename(dump_file)}"
    print(f"[backup] загружаю в {RCLONE_REMOTE}:{BUCKET}/{key}", flush=True)
    rc, out = run(["rclone", "copyto", dump_file,
                   f"{RCLONE_REMOTE}:{BUCKET}/{key}"])
    if rc != 0:
        print(f"[backup] ЗАГРУЗКА НЕ УДАЛАСЬ: {out[:300]}", file=sys.stderr)
        report["error"] = "upload failed"
        print(json.dumps(report, ensure_ascii=False))
        return 2
    # маркер последнего бэкапа
    run(["rclone", "copyto", dump_file,
         f"{RCLONE_REMOTE}:{BUCKET}/{BACKUP_PREFIX}/latest.dump"])
    report["remote_key"] = key
    print("[backup] загружено", flush=True)

    # ── 3. проверка восстановления ──
    if verify:
        print(f"[backup] проверка восстановления в {VERIFY_DB}", flush=True)
        before = count_rows()

        psql(f'DROP DATABASE IF EXISTS "{VERIFY_DB}"', db="postgres")
        psql(f'CREATE DATABASE "{VERIFY_DB}"', db="postgres")

        rc, out = run(["pg_restore", "-h", "localhost", "-U", "wiki",
                       "-d", VERIFY_DB, "--no-owner", "--no-acl", dump_file])
        # pg_restore возвращает 0 при полном успехе; предупреждения дают 1
        restored_ok = rc in (0, 1)
        report["restore_rc"] = rc
        if not restored_ok:
            print(f"[backup] ВОССТАНОВЛЕНИЕ НЕ УДАЛОСЬ: {out[:400]}",
                  file=sys.stderr)
            report["error"] = "pg_restore failed"
            psql(f'DROP DATABASE IF EXISTS "{VERIFY_DB}"', db="postgres")
            print(json.dumps(report, ensure_ascii=False))
            return 2

        after = count_rows(VERIFY_DB)
        mismatches = []
        for k, v in before.items():
            if k not in after:
                mismatches.append({"table": k, "in_source": v, "in_restore": "нет"})
            elif after[k] != v:
                mismatches.append({"table": k, "in_source": v, "in_restore": after[k]})

        report["tables_checked"] = len(before)
        report["mismatches"] = mismatches
        report["verified"] = not mismatches

        if mismatches:
            print(f"[backup] РАСХОЖДЕНИЙ: {len(mismatches)}", file=sys.stderr)
            for m in mismatches[:10]:
                print(f"    {m['table']}: {m['in_source']} vs {m['in_restore']}",
                      file=sys.stderr)
        else:
            print(f"[backup] восстановление сошлось: {len(before)} таблиц, "
                  f"счётчики совпадают", flush=True)

        psql(f'DROP DATABASE IF EXISTS "{VERIFY_DB}"', db="postgres")
        print("[backup] временная база удалена", flush=True)

    # ── 4. уборка и итог ──
    os.remove(dump_file)
    report["elapsed_s"] = round(time.time() - t0, 1)
    report["ok"] = report.get("verified", True)
    print(json.dumps(report, ensure_ascii=False, indent=1))

    # журнал
    log = "/home/ubuntu/backup_log.jsonl"
    with open(log, "a") as f:
        f.write(json.dumps(report, ensure_ascii=False) + "\n")

    return 0 if report["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
