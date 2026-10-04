#!/usr/bin/env python3
"""Планировщик автообновления: обход точек публикации и разбор нового.

Живёт на ВМ (российские источники с рабочего VPS недоступны). Делает две вещи:

  1. ОБХОД. Идёт по активным точкам catalog.source_endpoint, забирает
     страницу, извлекает список файлов публикации и считает отпечаток по
     этому списку. Отпечаток по списку, а не по всей странице: разметка
     сайта меняется от счётчиков и баннеров, а состав публикаций — нет.
     Новый отпечаток -> ops.enqueue_release ставит задачу в очередь.

  2. РАЗБОР. Забирает задачи из очереди через ops.claim_ingest (FOR UPDATE
     SKIP LOCKED — два планировщика не возьмут одну задачу), запускает
     скрипт точки, пишет результат через ops.finish_ingest.

Запуск: python3 ingest_watcher.py [--check-only] [--run-only] [--limit N]

Сеть — через curl с повторами: на urllib чтение ответа отваливается
посреди тела (питфолл зафиксирован в навыке research-db-v2).
"""
import argparse
import hashlib
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

try:
    import psycopg
except ImportError:
    print("нужен psycopg", file=sys.stderr)
    sys.exit(1)

SCRIPTS_DIR = os.environ.get("INGEST_SCRIPTS_DIR",
                            "/home/ubuntu/research-wiki-private/scripts")

# Парсерам нужен интерпретатор с pandas и openpyxl, а не системный python3,
# под которым запускается служба: иначе разбор падает на первом же импорте.
PYTHON_CANDIDATES = [
    os.environ.get("INGEST_PYTHON"),
    "/home/ubuntu/.hermes/hermes-agent/venv/bin/python3",
    "/home/lnr/.hermes/hermes-agent/venv/bin/python3",
    sys.executable,
]


def parser_python():
    """Интерпретатор для парсеров: первый существующий из кандидатов."""
    for p in PYTHON_CANDIDATES:
        if p and os.path.exists(p):
            return p
    return sys.executable
CURL_TIMEOUT = 60
CURL_RETRIES = 3
PAYLOAD_RE = re.compile(
    r'href=["\']([^"\']+\.(?:pdf|xlsx?|csv|zip|rar|html?))["\']', re.IGNORECASE)


def log(msg):
    print(f"[watcher] {datetime.now(timezone.utc).strftime('%H:%M:%S')} {msg}",
          flush=True)


def connect():
    """Подключение: на ВМ локально, на VPS через тоннель.

    Строка PGDSN может оказаться непригодной (например, systemd разбирает
    значение Environment= по пробелам, и переменной достаётся только первый
    параметр). Поэтому отказ строки не прекращает попытки: дальше идут
    обычные адреса.
    """
    dsn = os.environ.get("PGDSN")
    if dsn:
        try:
            return psycopg.connect(dsn, autocommit=True)
        except Exception as e:
            log(f"PGDSN не сработала ({str(e)[:80]}), пробую адреса")
    for host, port in (("localhost", 5432), ("127.0.0.1", 15432)):
        try:
            return psycopg.connect(host=host, port=port, dbname="research_wiki",
                                   user="wiki", autocommit=True)
        except Exception:
            continue
    raise RuntimeError("не удалось подключиться к research_wiki")


def fetch(url):
    """Забрать страницу через curl с повторами. Возврат: (текст | None).

    Две тонкости источников:
      - Росстат не проходит проверку сертификата (код 000 против 200 с -k),
        поэтому вторая попытка идёт без проверки;
      - часть страниц отдаётся в Windows-1251, и жёсткое декодирование
        UTF-8 падает на первом же байте кириллицы. Поэтому байты
        раскодируются вручную с запасными кодировками.
    """
    for attempt in range(1, CURL_RETRIES + 1):
        insecure = attempt >= 2
        cmd = ["curl", "-sL", "--max-time", str(CURL_TIMEOUT),
               "-A", "Mozilla/5.0 (research-wiki ingest watcher)",
               "-w", "\n%{http_code}"]
        if insecure:
            cmd.append("-k")
        cmd.append(url)
        r = subprocess.run(cmd, capture_output=True)
        if r.returncode == 0 and r.stdout:
            body, _, code = decode(r.stdout).rpartition("\n")
            if code.strip().startswith("2"):
                return body
        if attempt < CURL_RETRIES:
            log(f"   попытка {attempt} не удалась, повтор"
                + (" (без проверки сертификата)" if not insecure else ""))
    return None


def decode(raw):
    """Раскодировать ответ: UTF-8, затем однобайтовые кириллические."""
    for enc in ("utf-8", "cp1251", "koi8-r", "latin-1"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", "replace")


TAG_RE = re.compile(r"<(script|style)[^>]*>.*?</\1>", re.IGNORECASE | re.DOTALL)
ANY_TAG_RE = re.compile(r"<[^>]+>")
WS_RE = re.compile(r"\s+")


def normalized_text(body):
    """Видимый текст страницы без разметки: устойчивее сырого HTML."""
    t = TAG_RE.sub(" ", body)
    t = ANY_TAG_RE.sub(" ", t)
    return WS_RE.sub(" ", t).strip()


def fingerprint(body):
    """Отпечаток публикации: сначала состав файлов, затем видимый текст.

    Состав файлов — лучший признак, но он есть не у всех страниц (таблица
    ставки, витрина без прямых ссылок). Тогда берётся нормализованный
    видимый текст: он не реагирует на счётчики и вёрстку, на которые
    реагирует хэш всего тела. Ложное срабатывание стоит одного лишнего
    прогона разбора (разбор идемпотентен), пропуск публикации — дороже.
    """
    links = sorted({m.group(1).split("?")[0] for m in PAYLOAD_RE.finditer(body)})
    if links:
        basis = "\n".join(links)
        return hashlib.sha256(basis.encode("utf-8", "ignore")).hexdigest(), len(links), "files"
    text = normalized_text(body)
    if len(text) < 80:
        return None, 0, "none"
    return hashlib.sha256(text.encode("utf-8", "ignore")).hexdigest(), 0, "text"


def sweep(conn, dry=False):
    """Обход точек: заметить новые публикации."""
    cur = conn.cursor()
    cur.execute("""SELECT e.endpoint_id, e.url, s.source_code, e.kind
                   FROM catalog.source_endpoint e
                   JOIN catalog.source s ON s.source_id = e.source_id
                   WHERE e.is_active ORDER BY e.endpoint_id""")
    endpoints = cur.fetchall()
    log(f"точек к обходу: {len(endpoints)}")
    new_count = 0
    for ep_id, url, source, kind in endpoints:
        body = fetch(url)
        if body is None:
            log(f"   {source:14s} недоступна: {url[:60]}")
            continue
        h, n_links, kind = fingerprint(body)
        if h is None:
            log(f"   {source:14s} страница пуста — точку так не отследить")
            continue
        if dry:
            log(f"   {source:14s} отпечаток {h[:12]} по {kind}, файлов {n_links}")
            continue
        if kind == "text":
            # Страницы без ссылок (таблица ставки, витрина) меняются от
            # динамических вставок, и по тексту они дают «новизну» на каждом
            # обходе. Такую точку запоминаем, но в очередь не ставим: разбор
            # нужен по признаку содержимого, а не по вёрстке. Пока признак не
            # задан, точка видна в ops.v_ingest_board как неподконтрольная.
            cur.execute("""INSERT INTO ops.release_seen
                             (endpoint_id, content_hash, published_hint, payload_ref, note)
                           VALUES (%s, %s, NULL, %s, 'текстовый отпечаток, в очередь не ставится')
                           ON CONFLICT (endpoint_id, content_hash) DO NOTHING""",
                        (ep_id, h, url))
            cur.execute("""UPDATE catalog.source_endpoint
                              SET last_checked_at = now(), last_hash = %s
                            WHERE endpoint_id = %s""", (h, ep_id))
            log(f"   {source:14s} отпечаток по тексту, в очередь не ставлю")
            continue
        cur.execute("SELECT ops.enqueue_release(%s, %s, %s, %s) AS q",
                    (ep_id, h, None, url))
        qid = cur.fetchone()[0]
        if qid:
            new_count += 1
            log(f"   {source:14s} НОВОЕ, задача {qid} (по {kind}, файлов {n_links})")
        else:
            log(f"   {source:14s} без изменений")
    return new_count


def work(conn, limit=3):
    """Разбор очереди: запустить скрипты точек."""
    cur = conn.cursor()
    cur.execute("SELECT queue_id, endpoint_id, url, parser_script, attempts FROM ops.claim_ingest(%s)",
                (limit,))
    tasks = cur.fetchall()
    if not tasks:
        log("очередь пуста")
        return 0
    done = 0
    for qid, ep_id, url, parser, attempts in tasks:
        if not parser:
            log(f"   задача {qid}: скрипт разбора не указан, пропуск")
            cur.execute("SELECT ops.finish_ingest(%s,'skipped',NULL,NULL,%s,NULL)",
                        (qid, "нет parser_script у точки публикации"))
            continue
        path = os.path.join(SCRIPTS_DIR, parser)
        if not os.path.exists(path):
            log(f"   задача {qid}: скрипт не найден {path}")
            cur.execute("SELECT ops.finish_ingest(%s,'failed',NULL,NULL,%s,NULL)",
                        (qid, f"нет файла {path}"))
            continue
        log(f"   задача {qid}: запускаю {parser}")
        interp = parser_python()
        log(f"   задача {qid}: интерпретатор {interp}")
        r = subprocess.run([interp, path], capture_output=True,
                           timeout=1800)
        ok = r.returncode == 0
        tail = (decode(r.stdout) + decode(r.stderr))[-1500:]
        cur.execute("SELECT ops.finish_ingest(%s,%s,NULL,%s,%s,%s)",
                    (qid, "done" if ok else "failed", r.returncode,
                     None if ok else tail[:400], tail))
        log(f"   задача {qid}: {'готово' if ok else 'сбой'} (код {r.returncode})")
        if ok:
            done += 1
    return done


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check-only", action="store_true", help="только обход")
    ap.add_argument("--run-only", action="store_true", help="только разбор")
    ap.add_argument("--dry", action="store_true", help="обход без постановки")
    ap.add_argument("--limit", type=int, default=3)
    args = ap.parse_args()

    conn = connect()
    if not args.run_only:
        n = sweep(conn, dry=args.dry)
        log(f"новых публикаций: {n}")
    if not args.check_only:
        d = work(conn, args.limit)
        log(f"разобрано: {d}")
    conn.close()


if __name__ == "__main__":
    main()