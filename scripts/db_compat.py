#!/usr/bin/env python3
"""
Слой совместимости: SQLite-API поверх PostgreSQL.

Скрипты вики написаны под `sqlite3` (`?`-плейсхолдеры, `PRAGMA`, обращения
к таблицам по короткому имени). При переезде на PostgreSQL их можно не
переписывать поштучно — достаточно заменить точку входа:

    # было
    import sqlite3
    db = sqlite3.connect('data/rosstat_construction.db')

    # стало
    import db_compat as sqlite3
    db = sqlite3.connect('rosstat_construction.db')

Что делает прокси:
  * `?` → `%s` в запросах;
  * имена таблиц без схемы разрешаются в `staging.<db>__<table>`;
  * `PRAGMA table_info(x)` → запрос к information_schema;
  * `executemany`, `fetchone/fetchall`, `cursor()`, `commit/rollback` — как в sqlite3;
  * `row_factory` не нужен: кортежи возвращаются как есть.

Переменные окружения:
  PGHOST/PGPORT/PGDATABASE/PGUSER или PGDSN — параметры подключения;
  PGPASSFILE — файл с паролем (права 600).
"""
import decimal
import os
import re
import sys
from pathlib import Path

try:
    import psycopg
except ImportError:  # pragma: no cover
    psycopg = None

# ── какие базы известны (для разрешения имён таблиц) ─────────────────
DB_FILES = [
    'developers_ifrs.db', 'rosreestr_deals.db', 'cbr_lending.db',
    'regions_panel.db', 'fns_tochno_sectors.db', 'rosstat_construction.db',
]

# ── классы исключений в стиле sqlite3 ────────────────────────────────
# Обязательны для pandas.read_sql: он делает `from sqlite3 import Error`
# (когда модуль подменён — импортирует отсюда) и оборачивает ошибки драйвера.
# Без них падают ikv_benchmarks, wnok_midas_lite, housing_supply_elasticity.


class Warning(Exception):
    pass


class Error(Exception):
    pass


class InterfaceError(Error):
    pass


class DatabaseError(Error):
    pass


class DataError(DatabaseError):
    pass


class OperationalError(DatabaseError):
    pass


class IntegrityError(DatabaseError):
    pass


class InternalError(DatabaseError):
    pass


class ProgrammingError(DatabaseError):
    pass


class NotSupportedError(DatabaseError):
    pass


def _dsn(dbname: str = None) -> str:
    """Собрать строку подключения из окружения."""
    if os.environ.get('PGDSN'):
        return os.environ['PGDSN']
    host = os.environ.get('PGHOST', '127.0.0.1')
    port = os.environ.get('PGPORT', '15432')
    db = dbname or os.environ.get('PGDATABASE', 'research_wiki')
    user = os.environ.get('PGUSER', 'wiki')
    pw = os.environ.get('PGPASSWORD')
    dsn = f"host={host} port={port} dbname={db} user={user}"
    if pw:
        dsn += f" password={pw}"
    return dsn


def _db_tag(name: str) -> str:
    """'rosstat_construction.db' -> 'rosstat_construction' (префикс в staging)."""
    return re.sub(r'[^a-z0-9_]', '_', Path(str(name)).stem.lower())


def _translate(sql: str) -> str:
    """Привести SQL к диалекту PostgreSQL."""
    s = sql
    # плейсхолдеры: ? -> %s (вне строковых литералов)
    if '?' in s:
        out, in_str, quote = [], False, ''
        i = 0
        while i < len(s):
            ch = s[i]
            if in_str:
                out.append(ch)
                if ch == quote:
                    # удвоенная кавычка — экранирование, остаёмся в строке
                    if i + 1 < len(s) and s[i + 1] == quote:
                        out.append(s[i + 1]); i += 1
                    else:
                        in_str = False
            else:
                if ch in ("'", '"'):
                    in_str, quote = True, ch
                    out.append(ch)
                elif ch == '?':
                    out.append('%s')
                else:
                    out.append(ch)
            i += 1
        s = ''.join(out)
    return s


class Cursor:
    """Курсор в стиле sqlite3 поверх psycopg."""

    def __init__(self, conn, db_tag: str):
        self._conn = conn
        self._db_tag = db_tag
        self._cur = conn._pg.cursor()
        self.rowcount = -1
        self.lastrowid = None

    @staticmethod
    def _coerce(row):
        """
        Привести значения к типам, которые отдавал sqlite3.
        PostgreSQL `numeric` → `Decimal`, а sqlite3 REAL → float; скрипты
        вики вызывают `json.dump` и `round()`, которые на Decimal расходятся
        (json.dumps(Decimal) падает с TypeError). Приводим Decimal к float.
        """
        if row is None:
            return None
        if isinstance(row, tuple):
            return tuple(Cursor._coerce(v) for v in row)
        if isinstance(row, decimal.Decimal):
            return float(row)
        return row

    # ── разрешение имён таблиц ──
    def _qualify(self, sql: str) -> str:
        """
        Подставить схему для коротких имён таблиц.
        `FROM observations` → `FROM staging.rosstat_construction__observations`

        Системные схемы (information_schema, pg_catalog, staging, pg_*)
        не подменяются — иначе information_schema.tables превратится в
        staging.<db>__information_schema (ошибка cross-database).
        """
        if not self._db_tag:
            return sql
        prefix = f'staging."{self._db_tag}__'
        SYSTEM = ('information_schema', 'pg_catalog', 'pg_tables', 'pg_class',
                  'pg_indexes', 'pg_stat_user_tables', 'pg_database',
                  'pg_extension', 'pg_namespace', 'sqlite_master')

        def repl(m):
            kw, name = m.group(1), m.group(2)
            # уже со схемой, служебное имя или скобка — не трогаем
            if '.' in name or name.startswith('"') or name.startswith('('):
                return m.group(0)
            if name.lower() in SYSTEM or name.lower().startswith('pg_'):
                return m.group(0)
            return f'{kw} {prefix}{name}"'

        pattern = re.compile(
            r'\b(FROM|JOIN|INTO|UPDATE|TABLE)\s+(?:IF\s+NOT\s+EXISTS\s+)?([A-Za-z_][\w]*)',
            re.I)
        return pattern.sub(repl, sql)

    def execute(self, sql, params=()):
        if isinstance(params, dict):
            raise NotImplementedError('именованные параметры не поддерживаются')
        s = _translate(sql)
        # PRAGMA table_info(x) — эмуляция через information_schema
        m = re.match(r'\s*PRAGMA\s+table_info\(([^)]+)\)', s, re.I)
        if m:
            tbl = m.group(1).strip().strip('"\'')
            full = f'{self._db_tag}__{tbl}' if self._db_tag else tbl
            self._cur.execute("""
                SELECT ordinal_position - 1, column_name, data_type, 0, NULL, 0
                FROM information_schema.columns
                WHERE table_schema = 'staging' AND table_name = %s
                ORDER BY ordinal_position
            """, (full,))
            self.rowcount = self._cur.rowcount
            return self
        s = self._qualify(s)
        self._cur.execute(s, params or None)
        self.rowcount = self._cur.rowcount
        return self

    def executemany(self, sql, seq):
        s = self._qualify(_translate(sql))
        self._cur.executemany(s, seq)
        self.rowcount = self._cur.rowcount
        return self

    def fetchone(self):
        return self._coerce(self._cur.fetchone())

    def fetchall(self):
        return [self._coerce(r) for r in self._cur.fetchall()]

    def fetchmany(self, size=1):
        return [self._coerce(r) for r in self._cur.fetchmany(size)]

    def __iter__(self):
        return iter(self.fetchall())

    def close(self):
        self._cur.close()

    @property
    def description(self):
        return self._cur.description


class Connection:
    """Соединение в стиле sqlite3."""

    def __init__(self, pg, db_tag: str):
        self._pg = pg
        self._db_tag = db_tag

    def cursor(self):
        return Cursor(self, self._db_tag)

    def execute(self, sql, params=()):
        cur = self.cursor()
        cur.execute(sql, params)
        return cur

    def executemany(self, sql, seq):
        cur = self.cursor()
        cur.executemany(sql, seq)
        return cur

    def commit(self):
        self._pg.commit()

    def rollback(self):
        self._pg.rollback()

    def close(self):
        self._pg.close()

    def __enter__(self):
        return self

    def __exit__(self, *a):
        try:
            self.commit()
        except Exception:
            self.rollback()

    # sqlite3-совместимые заглушки
    def create_function(self, *a, **kw):
        raise NotImplementedError('create_function не поддержан в прокси')

    def iterdump(self):
        raise NotImplementedError('iterdump не поддержан в прокси')


def connect(target, **kw):
    """
    Открыть соединение. `target` может быть:
      * именем SQLite-базы ('rosstat_construction.db') — тогда таблицы
        разрешаются в staging.<db>__<table>;
      * строкой PostgreSQL DSN ('postgresql://...') — прямое подключение;
      * None — подключение к research_wiki без разрешения имён.

    Совместимо с `sqlite3.connect(..., detect_types=..., check_same_thread=...)`:
    лишние аргументы игнорируются.
    """
    if psycopg is None:
        raise RuntimeError('нужен psycopg: pip install "psycopg[binary]"')

    tgt = str(target)
    if tgt.startswith('postgres'):
        pg = psycopg.connect(tgt)
        return Connection(pg, '')
    # sqlite-имя: определяем префикс схемы
    tag = _db_tag(tgt)
    known = {_db_tag(f) for f in DB_FILES}
    if tag not in known and tag not in ('', '_memory_'):
        # неизвестная база — подключаемся без квалификации
        tag = ''
    pg = psycopg.connect(_dsn())
    return Connection(pg, tag)


def binary(data):
    return memoryview(bytes(data))


__version__ = '3.0-compat'
