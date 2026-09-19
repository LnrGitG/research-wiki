#!/usr/bin/env python3
"""Перенос локальных метрик ETL корпуса в БД YC.

Зачем: метрики прогонов копятся в `data/etl/pipeline_log.jsonl`, то есть
только на VDS. Таблица на ВМ переживёт переустановку, локальный файл — нет.

**Почему НЕ в pipeline.pipeline_log.** Проверено 19.09: та таблица
спроектирована под другой процесс — конвейер количественных данных
(`queries/database-architecture.md`, 9 этапов: получение файла → регистрация
релиза → staging → маппинг метрик → проверки → core.observation → производные
→ витрины). Её `stage` — это `smallint` со смыслом «номер этапа конвейера
данных» (1–9), и она привязана к `release_id`. Наши стадии (metadata, methods,
references, storage, index, cards) к тому конвейеру не относятся: у них статьи
вики, а не ряды наблюдений. Запись в чужую таблицу дала бы мусор, который
невозможно отфильтровать — `stage` числовой, а признака процесса нет.

Поэтому создаётся отдельная таблица `pipeline.corpus_etl_log` с текстовым
`stage` и полем `script`. Схема — минимально необходимая.

Идемпотентность: UNIQUE(stage, started_at) плюс ON CONFLICT DO NOTHING —
повторный перенос дублей не создаёт.

Почему пакетом: доступ к PostgreSQL на ВМ с VDS закрыт гео-фильтром, SQL
уходит через канал `agent-vm-exchange`, и агент исполняет ТОЛЬКО `command.sh`
(вспомогательные файлы он к себе не копирует, проверено 19.09) — поэтому SQL
встраивается в скрипт heredoc'ом.

Запуск:  python3 scripts/sync_pipeline_log.py --dry-run   # что перенесётся
         python3 scripts/sync_pipeline_log.py --push      # отправить на ВМ
         python3 scripts/sync_pipeline_log.py --status    # прочитать output.txt
"""
import argparse
import json
import os
import subprocess
import sys
import time

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO)
sys.path.insert(0, os.path.join(REPO, "scripts"))
import etl_common

CHANNEL = "yc-s3:agent-vm-exchange"

DDL = """CREATE SCHEMA IF NOT EXISTS pipeline;
CREATE TABLE IF NOT EXISTS pipeline.corpus_etl_log (
    log_id        bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    script        text NOT NULL,
    stage         text NOT NULL,
    started_at    timestamptz NOT NULL,
    finished_at   timestamptz,
    duration_ms   integer,
    rows_affected integer,
    status        text NOT NULL,
    error_text    text,
    artifacts     jsonb,
    UNIQUE (stage, started_at)
);
COMMENT ON TABLE pipeline.corpus_etl_log IS
    'Метрики прогонов ETL корпуса публикаций (отдельно от конвейера данных)';
CREATE INDEX IF NOT EXISTS corpus_etl_log_stage_idx
    ON pipeline.corpus_etl_log (stage, started_at DESC);"""


def esc(v):
    if v is None:
        return "NULL"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    return "'" + str(v).replace("'", "''") + "'"


def sql_from_log(records):
    """INSERT для pipeline.corpus_etl_log."""
    rows = []
    for e in records:
        art = e.get("artifacts") or []
        rows.append("(%s, %s, %s, %s, %s, %s, %s, %s, %s)" % (
            esc(e.get("script", "?")),
            esc(e.get("stage", "?")),
            esc(e.get("started_at", "1970-01-01T00:00:00")),
            esc(e.get("finished_at", "1970-01-01T00:00:00")),
            esc(int(e.get("duration_ms", 0))),
            esc(int(e.get("rows_affected", 0))),
            esc(e.get("status", "ok")),
            esc((e.get("error_text") or "")[:500]),
            (esc(json.dumps(art, ensure_ascii=False)) + "::jsonb") if art else "NULL",
        ))
    return ("INSERT INTO pipeline.corpus_etl_log\n"
            "   (script, stage, started_at, finished_at, duration_ms, rows_affected,\n"
            "    status, error_text, artifacts)\nVALUES\n"
            + ",\n".join(rows) +
            "\nON CONFLICT (stage, started_at) DO NOTHING;")


def send_and_read(script_body, wait=80):
    """Отправить command.sh на ВМ, вернуть output.txt."""
    path = "/tmp/_sync_cmd.sh"
    with open(path, "w", encoding="utf-8") as f:
        f.write(script_body)
    r = subprocess.run(["rclone", "copyto", path, CHANNEL + "/_cmd/command.sh"],
                       capture_output=True, text=True, timeout=300)
    if r.returncode:
        return "ОШИБКА отправки: %s" % r.stderr[:200]
    time.sleep(wait)
    out = subprocess.run(["rclone", "cat", CHANNEL + "/_cmd/output.txt"],
                         capture_output=True, text=True, timeout=120)
    return out.stdout or ""


def read_existing():
    """Пары (stage, started_at), уже лежащие в БД."""
    body = ("#!/bin/bash\n"
            "export PGPASSFILE=/home/ubuntu/.pgpass\n"
            "psql -h localhost -U wiki -d research_wiki -tAc \"SELECT stage||'|'||"
            "to_char(started_at,'YYYY-MM-DD\\\"T\\\"HH24:MI:SS') "
            "FROM pipeline.corpus_etl_log\" 2>/dev/null || echo ТАБЛИЦЫ_НЕТ\n"
            "echo '=== ГОТОВО ==='\n")
    return send_and_read(body)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--push", action="store_true", help="создать таблицу и перенести")
    ap.add_argument("--all", action="store_true", help="перенести всё без сверки")
    ap.add_argument("--status", action="store_true")
    args = ap.parse_args()

    if args.status:
        r = subprocess.run(["rclone", "cat", CHANNEL + "/_cmd/output.txt"],
                           capture_output=True, text=True, timeout=120)
        print(r.stdout[-2500:] or "(output.txt пуст)")
        return 0

    log = etl_common.run_log()
    if not log:
        print("Метрик нет: %s пуст" % etl_common.PIPELINE_LOG)
        return 0
    print("Локальных метрик: %d" % len(log))

    if args.dry_run:
        print("\nК переносу (первые 8):")
        for e in log[:8]:
            print("  %-12s %-20s rows=%-4d %6d мс  %s"
                  % (e.get("stage"), e.get("started_at", ""),
                     e.get("rows_affected", 0), e.get("duration_ms", 0),
                     e.get("status")))
        print("\nЦелевая таблица: pipeline.corpus_etl_log")
        return 0

    if args.push:
        have = set()
        if not args.all:
            print("\nЧитаю существующие записи...")
            out = read_existing()
            if "ТАБЛИЦЫ_НЕТ" in out:
                print("  таблицы ещё нет — будет создана")
            else:
                for line in out.split("\n"):
                    line = line.strip()
                    if "|" in line and not line.startswith("==="):
                        have.add(line)
                print("  в БД уже: %d записей" % len(have))

        todo = [e for e in log
                if args.all or "%s|%s" % (e.get("stage"), e.get("started_at")) not in have]
        print("\nК переносу: %d записей" % len(todo))
        if not todo:
            print("БД синхронна с локальным логом — переносить нечего.")
            return 0

        body = ("#!/bin/bash\n"
                "export PGPASSFILE=/home/ubuntu/.pgpass\n"
                "PSQL=\"psql -h localhost -U wiki -d research_wiki -v ON_ERROR_STOP=1\"\n"
                "echo '=== 1. схема ==='\n"
                "$PSQL << 'DDLEOF'\n" + DDL + "\nDDLEOF\n"
                "echo '  схема применена'\n"
                "echo '=== 2. перенос ==='\n"
                "$PSQL -tAc \"SELECT 'до: '||count(*) FROM pipeline.corpus_etl_log\"\n"
                "$PSQL << 'SQLEOF'\n" + sql_from_log(todo) + "\nSQLEOF\n"
                "echo '=== 3. контроль ==='\n"
                "$PSQL -tAc \"SELECT 'после: '||count(*) FROM pipeline.corpus_etl_log\"\n"
                "$PSQL -tAc \"SELECT 'суммарно мс: '||sum(duration_ms) FROM pipeline.corpus_etl_log\"\n"
                "$PSQL -tAc \"SELECT stage||' | '||count(*)||' прогонов | сред. '||"
                "round(avg(duration_ms))||' мс' FROM pipeline.corpus_etl_log "
                "GROUP BY stage ORDER BY avg(duration_ms) DESC\"\n"
                "$PSQL -tAc \"SELECT 'таблица: '||pg_size_pretty(pg_total_relation_size("
                "'pipeline.corpus_etl_log'))\"\n"
                "echo '=== ГОТОВО ==='\n")
        print("\nОтправляю на ВМ (ждём ~80 с)...")
        print(send_and_read(body))
        return 0

    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
