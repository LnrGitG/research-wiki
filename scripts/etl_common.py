#!/usr/bin/env python3
"""Общий слой ETL-пайплайна: артефакты, инкремент, метрики прогонов.

Зачем нужен: до 19.09.2026 пять скриптов анализа корпуса запускались вручную,
каждый читал все статьи целиком (139 с на одну новую), промежуточные
результаты лежали в /tmp и умирали при перезагрузке, метрики никуда не
писались. Этот модуль устраняет все три проблемы разом.

Что даёт:

1. **Артефакты вне /tmp.** Все промежуточные результаты лежат в `data/etl/`
   и переживают перезапуск, падение и перезагрузку.
2. **Инкремент.** `changed_files()` сравнивает mtime и размер каждого файла с
   манифестом и возвращает только новые и изменённые. Скрипт досчитывает их
   и дописывает к сохранённому артефакту — полный корпус не пересчитывается.
3. **Метрики прогонов.** `record_run()` пишет строку в
   `data/etl/pipeline_log.jsonl`. БД на ВМ YC недоступна напрямую с VDS
   (гео-фильтр), поэтому метрики копятся локально, а на ВМ уходят пакетом
   через канал `agent-vm-exchange` — см. `sync_pipeline_log.py`.

Схема манифеста (`data/etl/manifest.json`):

    {"extract_references.py": {"papers/x.md": {"mtime": 1234, "size": 5678}}}

Скрипт видит записи только по СВОЕМУ имени — так их можно запускать
независимо, и один не сбрасывает инкремент другого.
"""
import json
import os
import time

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ETL_DIR = os.path.join(REPO, "data", "etl")
MANIFEST = os.path.join(ETL_DIR, "manifest.json")
PIPELINE_LOG = os.path.join(ETL_DIR, "pipeline_log.jsonl")


def ensure_dir():
    os.makedirs(ETL_DIR, exist_ok=True)


# ── артефакты ────────────────────────────────────────────────────────

def artifact_path(name):
    """data/etl/<name>.json — путь артефакта (name без расширения)."""
    ensure_dir()
    return os.path.join(ETL_DIR, "%s.json" % name)


def load_artifact(name):
    """Сохранённый артефакт. Отсутствует или битый -> {}."""
    p = artifact_path(name)
    if not os.path.exists(p):
        return {}
    try:
        d = json.load(open(p, encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    if isinstance(d, list):
        return {r.get("wiki_page") or r.get("stem"): r for r in d if isinstance(r, dict)}
    return d


def save_artifact(name, data):
    """Записать артефакт, вернуть путь и размер."""
    p = artifact_path(name)
    tmp = p + ".tmp"
    json.dump(data, open(tmp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    os.replace(tmp, p)          # атомарно: падение не оставит битый файл
    return p, os.path.getsize(p)


# ── манифест и инкремент ─────────────────────────────────────────────

def load_manifest():
    if not os.path.exists(MANIFEST):
        return {}
    try:
        return json.load(open(MANIFEST, encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def save_manifest(m):
    ensure_dir()
    tmp = MANIFEST + ".tmp"
    json.dump(m, open(tmp, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    os.replace(tmp, MANIFEST)


def _stat(path):
    try:
        st = os.stat(path)
        return {"mtime": int(st.st_mtime), "size": st.st_size}
    except OSError:
        return None


def changed_files(script, files, only=None, since=None, force=False):
    """Файлы, требующие обработки.

    only  — список конкретных путей (обработать ровно их);
    since — unix-время или дата 'YYYY-MM-DD': файлы новее;
            либо список стемов (тогда фильтр по имени, см. `only_stems`);
    force — игнорировать манифест, вернуть все.

    Возвращает (нужные, пропущено_как_неизменные).
    """
    m = load_manifest().get(script, {})

    if only:
        want = [f for f in files if f in set(only) or os.path.basename(f)[:-3] in set(only)]
        return want, len(files) - len(want)

    if force:
        return list(files), 0

    cutoff = None
    if isinstance(since, str) and since:
        try:
            cutoff = time.mktime(time.strptime(since, "%Y-%m-%d"))
        except ValueError:
            cutoff = None
    elif isinstance(since, (int, float)):
        cutoff = float(since)

    need, skipped = [], 0
    for f in files:
        st = _stat(f)
        if st is None:
            continue
        prev = m.get(f)
        if prev and prev.get("mtime") == st["mtime"] and prev.get("size") == st["size"]:
            skipped += 1
            continue
        if cutoff is not None and st["mtime"] < cutoff:
            skipped += 1
            continue
        need.append(f)
    return need, skipped


def mark_done(script, files):
    """Отметить файлы как обработанные (после успешного прогона)."""
    m = load_manifest()
    per = m.setdefault(script, {})
    for f in files:
        st = _stat(f)
        if st:
            per[f] = st
    save_manifest(m)
    return len(files)


def reset(script=None):
    """Сбросить инкремент: для скрипта или целиком (--force пересборка)."""
    m = load_manifest()
    if script:
        m.pop(script, None)
    else:
        m = {}
    save_manifest(m)


# ── метрики прогонов ─────────────────────────────────────────────────

def record_run(script, stage, started, finished, rows=0, status="ok",
               error="", artifacts=None, extra=None):
    """Строка метрик в data/etl/pipeline_log.jsonl.

    Формат согласован с таблицей pipeline.pipeline_log в БД
    (stage, started_at, finished_at, rows_affected, status, error_text)
    плюс поля artifacts и duration_ms, которых в таблице нет.
    """
    ensure_dir()
    rec = {
        "script": script,
        "stage": stage,
        "started_at": time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(started)),
        "finished_at": time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(finished)),
        "duration_ms": int((finished - started) * 1000),
        "rows_affected": rows,
        "status": status,
        "error_text": (error or "")[:500],
        "artifacts": artifacts or [],
    }
    if extra:
        rec.update(extra)
    with open(PIPELINE_LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    return rec


def run_log():
    """Прочитанные метрики прогонов (для отчётов и синхронизации)."""
    if not os.path.exists(PIPELINE_LOG):
        return []
    out = []
    for line in open(PIPELINE_LOG, encoding="utf-8"):
        line = line.strip()
        if line:
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return out


def add_args(ap):
    """Общие флаги инкремента для argparse каждого скрипта."""
    ap.add_argument("--only", nargs="*", default=None,
                    help="обработать только указанные файлы/стемы")
    ap.add_argument("--since", default=None,
                    help="только файлы новее даты YYYY-MM-DD")
    ap.add_argument("--force", action="store_true",
                    help="игнорировать манифест, обработать всё")
    ap.add_argument("--no-save", action="store_true",
                    help="не писать артефакт и манифест (сухой прогон)")
    return ap
