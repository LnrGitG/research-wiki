#!/usr/bin/env python3
"""Разведка служб PostgreSQL на ВМ: что установлено, что доступно, чего не хватает.

Только чтение. Ничего не меняет. Запуск:
    ~/.hermes/hermes-agent/venv/bin/python3 scripts/pg_capability_probe.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import db_tunnel  # noqa: E402


def show(title: str) -> None:
    print(f"\n=== {title} ===")


def rows(sql: str, params=None):
    try:
        return db_tunnel.query(sql, params)
    except Exception as exc:  # noqa: BLE001
        print(f"  запрос не прошёл: {type(exc).__name__}: {exc}")
        return []


def main() -> int:
    show("Кто мы и что за сервер")
    for r in rows(
        "SELECT version(), current_user, "
        "current_setting('is_superuser') AS superuser, "
        "current_setting('server_version_num') AS ver_num"
    ):
        print(f"  {r[0].split(',')[0]}")
        print(f"  роль: {r[1]} | суперпользователь: {r[2]}")

    show("Предзагруженные библиотеки (shared_preload_libraries)")
    for r in rows("SELECT current_setting('shared_preload_libraries')"):
        print(f"  {r[0] or '(пусто)'}")
    for key in (
        "cron.database_name",
        "cron.use_background_workers",
        "autovacuum",
        "autovacuum_naptime",
        "max_worker_processes",
        "max_parallel_workers",
        "track_counts",
        "jit",
    ):
        for r in rows("SELECT current_setting(%s, true)", (key,)):
            print(f"  {key} = {r[0]}")

    show("Установленные расширения")
    for r in rows(
        "SELECT extname, extversion FROM pg_extension ORDER BY extname"
    ):
        print(f"  {r[0]:<24} {r[1]}")

    show("Доступные расширения (можно поставить)")
    for r in rows(
        "SELECT name, default_version, "
        "coalesce(comment,'') FROM pg_available_extensions "
        "WHERE name NOT IN (SELECT extname FROM pg_extension) ORDER BY name"
    ):
        print(f"  {r[0]:<26} {r[1]:<12} {r[2][:52]}")

    show("Права роли на создание объектов")
    for r in rows(
        "SELECT rolname, rolsuper, rolcreaterole, rolcreatedb, rolbypassrls "
        "FROM pg_roles WHERE rolname = current_user"
    ):
        print(
            f"  {r[0]}: super={r[1]} createrole={r[2]} "
            f"createdb={r[3]} bypassrls={r[4]}"
        )

    show("Схемы и их владельцы")
    for r in rows(
        "SELECT nspname, pg_get_userbyid(nspowner) "
        "FROM pg_namespace WHERE nspname NOT LIKE 'pg\\_%' ORDER BY nspname"
    ):
        print(f"  {r[0]:<20} владелец: {r[1]}")

    show("Крупнейшие таблицы (топ-12 по размеру)")
    for r in rows(
        "SELECT schemaname||'.'||relname, n_live_tup, "
        "pg_size_pretty(pg_total_relation_size(relid)) "
        "FROM pg_stat_user_tables ORDER BY pg_total_relation_size(relid) DESC LIMIT 12"
    ):
        print(f"  {r[0]:<38} {r[1]:>9} строк  {r[2]:>10}")

    show("Свежесть автоочистки по крупным таблицам")
    for r in rows(
        "SELECT schemaname||'.'||relname, last_vacuum, last_autovacuum, "
        "last_analyze, last_autoanalyze, n_dead_tup "
        "FROM pg_stat_user_tables "
        "ORDER BY pg_total_relation_size(relid) DESC LIMIT 8"
    ):
        print(
            f"  {r[0]:<38} autovac={r[2]} autoan={r[4]} "
            f"мёртвых={r[5]}"
        )

    show("Есть ли уже что-то вроде планировщика внутри базы")
    for r in rows(
        "SELECT n.nspname||'.'||c.relname FROM pg_class c "
        "JOIN pg_namespace n ON n.oid = c.relnamespace "
        "WHERE c.relname LIKE '%job%' OR c.relname LIKE '%cron%' "
        "ORDER BY 1 LIMIT 10"
    ):
        print(f"  {r[0]}")

    show("Готовность статистики запросов (для разбора наследия)")
    for r in rows(
        "SELECT name FROM pg_available_extensions WHERE name = 'pg_stat_statements'"
    ):
        print(f"  доступно: {r[0]}")
    for r in rows("SELECT count(*) FROM pg_stat_statements"):
        print(f"  уже накоплено записей: {r[0]}")

    show("Место на диске у базы")
    for r in rows("SELECT pg_size_pretty(pg_database_size(current_database()))"):
        print(f"  размер базы: {r[0]}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())