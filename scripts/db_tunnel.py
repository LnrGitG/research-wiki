#!/usr/bin/env python3
"""Прямой доступ к PostgreSQL на ВМ YC через SSH-тоннель.

**Зачем.** До 19.09.2026 вся доставка SQL шла через канал `agent-vm-exchange`:
команда упаковывалась в `command.sh` (base64+gzip, тысячи строк heredoc),
клалась в S3-бакет, systemd-агент на ВМ её забирал, и результат читался из
`output.txt` — с ожиданием 70–90 секунд на операцию. Обоснованием был
«гео-фильтр YC, блокирующий SSH с зарубежного VDS».

Проверено фактически: **ограничение не действует**. Юнит `pg-tunnel.service`
держит тоннель `ssh -L 127.0.0.1:15432:localhost:5432 ubuntu@89.169.168.214`,
и прямой запрос к БД выполняется за доли секунды. `~/.pgpass` уже содержит
запись для порта 15432, поэтому подключение идёт без пароля в коде.

Тот же SQL, что раньше уходил через бакет за полторы минуты, здесь исполняется
напрямую. Именно это и даёт модуль.

**Порт 15432, не 5432.** Первая попытка подключения на 5432 дала «connection
refused» и породила ложный вывод о недоступности БД — на машине нет локального
PostgreSQL, тоннель слушает 15432.

Осторожность: не утверждается, что гео-фильтра нет вовсе — возможно, он
действует на другие подсети или менялся. Модуль проверяет доступность и
возвращает внятную ошибку, а не падает молча.

Использование:

    from db_tunnel import connect, query, execute, available

    if available():
        rows = query("SELECT count(*) FROM core.paper_card")
        execute("DELETE FROM t WHERE id = %s", (5,))
"""
import os
import subprocess
import sys

def _resolve_pg_target():
    """Хост и порт PostgreSQL — из `~/.pgpass`, с оглядкой на площадку.

    Тонкость `libpq`, которую легко не заметить: строка хоста в записи
    `~/.pgpass` сопоставляется **буквально**. Запись `127.0.0.1:15432:...`
    не сработает при `host=localhost`, а `localhost:5432:...` — при
    `host=127.0.0.1`; в обоих случаях драйвер скажет «no password supplied»,
    хотя пароль в файле есть.

    На двух площадках записи разные:
      * VPS (Франкфурт)  — `127.0.0.1:15432:research_wiki:wiki:<пароль>`
        (база за SSH-тоннелем `pg-tunnel.service`);
      * ВМ YC            — `localhost:5432:*:wiki:<пароль>`
        (PostgreSQL на той же машине).

    Поэтому источник истины — сам файл: берём первую запись, чей порт
    отвечает на TCP, и возвращаем её хост и порт. Явные PGHOST/PGPORT
    перекрывают файл.

    Возврат: (host, port).
    """
    env_host = os.environ.get("PGHOST")
    env_port = os.environ.get("PGPORT")
    if env_host and env_port:
        return env_host, int(env_port)

    entries = []
    for path in (os.environ.get("PGPASSFILE"), os.path.expanduser("~/.pgpass")):
        if not path or not os.path.exists(path):
            continue
        try:
            with open(path, encoding="utf-8") as fh:
                for line in fh:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    parts = line.split(":")
                    if len(parts) >= 5 and parts[1].isdigit():
                        entries.append((parts[0], int(parts[1])))
        except OSError:
            pass

    import socket
    for host, port in entries:
        probe = host if host not in ("*", "") else "127.0.0.1"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.5)
        try:
            if s.connect_ex((probe, port)) == 0:
                return (env_host or host), (int(env_port) if env_port else port)
        except OSError:
            pass
        finally:
            s.close()

    # Запасной путь: ничего не ответило — отдаём исторический дефолт VPS.
    return env_host or "127.0.0.1", int(env_port) if env_port else 15432


HOST, PORT = _resolve_pg_target()
DB = "research_wiki"
USER = "wiki"           # пароль берётся из ~/.pgpass




DB = "research_wiki"
USER = "wiki"           # пароль берётся из ~/.pgpass





try:
    import psycopg
except ImportError:
    psycopg = None


def tunnel_up():
    """Слушается ли порт тоннеля. Дешевле, чем пробное подключение."""
    try:
        r = subprocess.run(["ss", "-tln"], capture_output=True, text=True, timeout=10)
        return (":%d" % PORT) in r.stdout
    except (OSError, subprocess.TimeoutExpired):
        return False


def available(verbose=False):
    """Тоннель есть и БД отвечает."""
    if psycopg is None:
        if verbose:
            print("psycopg не установлен")
        return False
    if not tunnel_up():
        if verbose:
            print("Тоннель не поднят: порт %d не слушается.\n"
                  "  Поднять: systemctl --user start pg-tunnel.service" % PORT)
        return False
    try:
        c = psycopg.connect(host=HOST, port=PORT, dbname=DB, user=USER,
                            connect_timeout=8)
        c.close()
        return True
    except Exception as e:
        if verbose:
            print("БД не отвечает: %s" % str(e)[:160])
        return False


def connect():
    """Соединение с БД. Понятная ошибка, если тоннель не поднят."""
    if psycopg is None:
        raise RuntimeError("psycopg не установлен")
    if not tunnel_up():
        raise RuntimeError(
            "Тоннель к БД не поднят (порт %d не слушается).\n"
            "Поднять: systemctl --user start pg-tunnel.service\n"
            "Проверить: systemctl --user status pg-tunnel.service" % PORT)
    return psycopg.connect(host=HOST, port=PORT, dbname=DB, user=USER,
                           connect_timeout=10)


def query(sql, params=None):
    """SELECT -> список кортежей."""
    with connect() as c:
        with c.cursor() as cur:
            cur.execute(sql, params)
            return cur.fetchall()


def query_dict(sql, params=None):
    """SELECT -> список словарей (удобнее для отчётов)."""
    with connect() as c:
        with c.cursor() as cur:
            cur.execute(sql, params)
            cols = [d.name for d in cur.description] if cur.description else []
            return [dict(zip(cols, row)) for row in cur.fetchall()]


def execute(sql, params=None):
    """Одна команда, возвращает число затронутых строк."""
    with connect() as c:
        with c.cursor() as cur:
            cur.execute(sql, params)
            n = cur.rowcount if cur.rowcount and cur.rowcount > 0 else 0
        c.commit()
        return n


def execute_many(sql, rows):
    """Пакетная команда (для массовых вставок)."""
    with connect() as c:
        with c.cursor() as cur:
            cur.executemany(sql, rows)
            n = cur.rowcount if cur.rowcount and cur.rowcount > 0 else 0
        c.commit()
        return n


def load_sql_file(path):
    """Выполнить .sql-файл целиком. Возвращает число выполненных инструкций."""
    sql = open(path, encoding="utf-8").read()
    with connect() as c:
        with c.cursor() as cur:
            cur.execute(sql)
            n = 1 if cur.rowcount >= 0 else 0
        c.commit()
    return n


def table_counts(tables):
    """Быстрая сводка count(*) по списку таблиц — для контроля после загрузки."""
    out = {}
    for t in tables:
        try:
            out[t] = query("SELECT count(*) FROM %s" % t)[0][0]
        except Exception as e:
            out[t] = "ошибка: %s" % str(e)[:60]
    return out


if __name__ == "__main__":
    print("Тоннель: %s (порт %d)" % ("поднят" if tunnel_up() else "НЕ поднят", PORT))
    print("Доступ:  %s" % ("есть" if available(verbose=True) else "нет"))
    if available():
        for t in ("core.paper_card", "pipeline.corpus_etl_log", "core.metric",
                  "core.observation_v2"):
            try:
                print("  %-28s %s строк" % (t, query("SELECT count(*) FROM %s" % t)[0][0]))
            except Exception as e:
                print("  %-28s %s" % (t, str(e)[:50]))
