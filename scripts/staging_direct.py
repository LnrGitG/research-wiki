#!/usr/bin/env python3
"""Пункт 2: чтение лендингов напрямую, минуя схему `staging`.

Зачем. Гармонайзеры (`harmonize_6_rosstat_extra.py`, `harmonize_3b_observations.py`)
читают таблицы вида `staging.<db>__<таблица>`. Схема `staging` после переезда ВМ
пуста (0 таблиц), поэтому цепочка «SQLite → staging → канон» разорвана и данные
в канон не доходят. При этом запись УЖЕ идёт в канон: `core.observation_v2` и
`core.metric` — обновляемые представления (is_insertable_into=YES) поверх
`data.observation` / `catalog.metric`. Значит починить надо только чтение.

Как. Имя `staging.<tag>__<таблица>` разбирается на тег базы и имя таблицы, файл
берётся из `data/<tag>.db` (read-only). Для запросов с JOIN'ами собирается
in-memory SQLite: лендинг подключается как `src0`, а в схеме `staging` создаётся
представление `staging."<tag>__<таблица>"` → исходный SQL выполняется дословно.

Схема `staging` в PostgreSQL при этом больше не нужна: её можно не наполнять.
"""
import os
import re
import sqlite3
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(REPO, "data")

# Тег базы — тот же, что в имени таблицы staging (<tag>__<таблица>).
TAGS = (
    "rosstat_construction", "rosreestr_deals", "developers_ifrs",
    "regions_panel", "fns_tochno_sectors", "cbr_lending",
)
_REF = re.compile(r"staging\.(%s)__([A-Za-z0-9_]+)" % "|".join(TAGS))


def split_name(tbl):
    """'rosreestr_deals__ikv_region_quarter' -> ('rosreestr_deals', 'ikv_region_quarter')."""
    for tag in TAGS:
        if tbl.startswith(tag + "__"):
            return tag, tbl[len(tag) + 2:]
    raise KeyError("не разобрано имя staging-таблицы: %r" % tbl)


def _db_path(tag):
    p = os.path.join(DATA, tag + ".db")
    if not os.path.exists(p):
        raise FileNotFoundError("нет лендинга %s" % p)
    return p


def read_table(tbl, where="", order=""):
    """Прочитать таблицу лендинга по staging-имени.

    Возвращает (список имён колонок, список кортежей) — как psycopg-курсор.
    """
    tag, table = split_name(tbl)
    con = sqlite3.connect("file:%s?mode=ro" % _db_path(tag), uri=True)
    try:
        sql = 'SELECT * FROM "%s"' % table
        if where:
            sql += " WHERE " + where
        if order:
            sql += " ORDER BY " + order
        cur = con.execute(sql)
        cols = [d[0] for d in cur.description]
        return cols, cur.fetchall()
    finally:
        con.close()


def run_sql(sql):
    """Выполнить SQL с именами `staging.<tag>__<таблица>` на локальных лендингах.

    Возвращает (имена колонок, строки). Поддерживаются JOIN'ы таблиц одной базы.
    """
    refs, seen = [], set()
    for tag, table in _REF.findall(sql):
        if (tag, table) not in seen:
            seen.add((tag, table))
            refs.append((tag, table))
    if not refs:
        raise ValueError("в запросе нет ссылок staging.<база>__<таблица>")

    con = sqlite3.connect(":memory:", uri=True)
    try:
        con.execute("ATTACH ':memory:' AS staging")
        for i, (tag, table) in enumerate(refs):
            alias = "src%d" % i
            con.execute("ATTACH DATABASE 'file:%s?mode=ro' AS %s"
                        % (_db_path(tag), alias))
            # именно CREATE TABLE (a не VIEW): представление в SQLite не может
            # ссылаться на объекты другой базы, а копия таблицы — может.
            con.execute('CREATE TABLE staging."%s__%s" AS SELECT * FROM %s."%s"'
                        % (tag, table, alias, table))
        cur = con.execute(sql)
        cols = [d[0] for d in cur.description]
        return cols, cur.fetchall()
    finally:
        con.close()


def counts():
    """Диагностика: сколько строк в лендингах, которые нужны гармонайзерам."""
    out = {}
    for tag in TAGS:
        p = os.path.join(DATA, tag + ".db")
        if not os.path.exists(p):
            continue
        con = sqlite3.connect("file:%s?mode=ro" % p, uri=True)
        try:
            for (name,) in con.execute(
                    "SELECT name FROM sqlite_master WHERE type='table'"):
                out["%s__%s" % (tag, name)] = con.execute(
                    'SELECT count(*) FROM "%s"' % name).fetchone()[0]
        finally:
            con.close()
    return out


if __name__ == "__main__":
    sys.stdout.write("самопроверка staging_direct:\n")
    for tbl in ("rosreestr_deals__ikv_region_quarter",
                "developers_ifrs__dev_ifrs",
                "regions_panel__panel"):
        cols, rows = read_table(tbl, order="1")
        sys.stdout.write("  %-40s колонок=%d строк=%s\n"
                         % (tbl, len(cols), format(len(rows), ",")))
    cols, rows = run_sql(
        "SELECT count(*) FROM staging.rosstat_construction__observations o "
        "LEFT JOIN staging.rosstat_construction__indicators i "
        "ON i.id = o.indicator_id")
    sys.stdout.write("  JOIN-проверка: %s\n" % rows)
