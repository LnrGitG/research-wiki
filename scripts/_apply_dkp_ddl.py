#!/usr/bin/env python3
"""Применение DDL схемы dkp к БД research_wiki (шаг 1 из плана)."""
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from db_tunnel import execute, query  # noqa: E402

SQL_PATH = os.path.join(HERE, "cbr_decision_ddl.sql")


def main() -> None:
    with open(SQL_PATH, encoding="utf-8") as fh:
        sql = fh.read()

    # Проверка: схема dkp ещё не должна существовать
    existing = query(
        "SELECT count(*) FROM information_schema.schemata WHERE schema_name='dkp'")
    if existing and existing[0][0] > 0:
        print("SKIP: схема dkp уже существует")
        return

    # Один транзакционный блок: либо всё, либо ничего
    execute(sql)
    tables = query(
        "SELECT table_name FROM information_schema.tables "
        "WHERE table_schema='dkp' ORDER BY 1")
    views = query(
        "SELECT viewname FROM pg_views WHERE schemaname='dkp' ORDER BY 1")
    print("tables:", [r[0] for r in tables])
    print("views:", [r[0] for r in views])


if __name__ == "__main__":
    main()