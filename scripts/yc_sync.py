#!/usr/bin/env python3
"""
Синхронизация тяжёлых данных research-wiki с YC Object Storage.

Хранилище:
  - бакет `wiki-research` (Yandex Object Storage) = источник правды
    для raw/ и data/db/;
  - локальный VPS = горячий кэш активных баз;
  - raw/ доступен через rclone-mount в ~/yc-wiki/raw/, есть fallback
    на локальный каталог и на скачивание по требованию.

Было: GCS (бакет wiki-research-508405) через gsutil и gcsfuse. Миграция
выполнена 17.09.2026 — Google Cloud выведен из эксплуатации.

Использование:
  from yc_sync import ensure_db, DATA_DIR, RAW_DIR

  db_path = ensure_db('rosstat_construction.db')
  con = sqlite3.connect(db_path)

CLI:
  python3 scripts/yc_sync.py sync    # загрузить локальное → бакет
  python3 scripts/yc_sync.py pull    # скачать все базы из бакета
  python3 scripts/yc_sync.py status  # состояние кэша и хранилища
  python3 scripts/yc_sync.py verify  # сверка бакета с локальными копиями
"""
import os
import sys
import subprocess
import time
from pathlib import Path

# ── Конфигурация ─────────────────────────────────────────────────

BUCKET = os.environ.get("YC_BUCKET", "wiki-research")
REMOTE = os.environ.get("YC_REMOTE", "yc-s3")           # имя rclone-remote
RAW_PREFIX = f"{REMOTE}:{BUCKET}/raw"
DB_PREFIX = f"{REMOTE}:{BUCKET}/data/db"
ARCHIVE_PREFIX = f"{REMOTE}:{BUCKET}/data/archive"
RAW_URI = f"yc:{BUCKET}/raw"                            # для справки в коде

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"
RAW_DIR = REPO_ROOT / "raw"
YC_MOUNT = Path(os.environ.get("YC_MOUNT", os.path.expanduser("~/yc-wiki")))

# Базы, живущие в бакете (имя → локальный путь)
DB_FILES = {
    name: {"local": DATA_DIR / name, "remote": f"{DB_PREFIX}/{name}"}
    for name in (
        "rosstat_construction.db", "regions_panel.db", "cbr_lending.db",
        "fns_tochno_sectors.db", "rosreestr_deals.db", "developers_ifrs.db",
    )
}

MAX_CACHE_BYTES = int(os.environ.get("MAX_CACHE_BYTES", 2 * 1024 ** 3))


# ── Вспомогательное ──────────────────────────────────────────────

def _rclone(*args: str, check: bool = True) -> subprocess.CompletedProcess:
    """Вызвать rclone."""
    cmd = ["rclone"] + list(args)
    r = subprocess.run(cmd, capture_output=True, text=True)
    if check and r.returncode != 0:
        raise RuntimeError(f"rclone failed: {r.stderr[:300]}")
    return r


def _format_size(n: float) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024:
            return f"{n:.1f} {unit}"
        n /= 1024
    return f"{n:.1f} TB"


def _mount_alive() -> bool:
    """Смонтирован ли бакет в YC_MOUNT."""
    try:
        return YC_MOUNT.is_mount()
    except AttributeError:
        return os.path.ismount(str(YC_MOUNT))


# ── Основные функции ─────────────────────────────────────────────

def ensure_db(name: str, force: bool = False) -> Path:
    """
    Убедиться, что база есть локально; при отсутствии — скачать из бакета.

    Args:
        name: имя файла базы (например 'rosstat_construction.db')
        force: скачать заново, даже если локальная копия есть

    Returns:
        Путь к локальному файлу

    Raises:
        KeyError: если база неизвестна
        RuntimeError: если скачивание не удалось
    """
    if name not in DB_FILES:
        raise KeyError(f"Неизвестная база '{name}'. Известны: {', '.join(DB_FILES)}")
    info = DB_FILES[name]
    local = info["local"]
    if local.exists() and not force:
        return local
    print(f"[yc_sync] Скачиваю {name} из бакета…", file=sys.stderr)
    local.parent.mkdir(parents=True, exist_ok=True)
    _rclone("copyto", info["remote"], str(local))
    print(f"[yc_sync] Готово: {local} ({_format_size(local.stat().st_size)})",
          file=sys.stderr)
    return local


def evict_db(name: str) -> bool:
    """Удалить локальную копию базы, чтобы освободить место."""
    if name not in DB_FILES:
        raise KeyError(f"Неизвестная база '{name}'")
    p = DB_FILES[name]["local"]
    if p.exists():
        p.unlink()
        print(f"[yc_sync] Удалена локальная копия {name}", file=sys.stderr)
        return True
    return False


def raw_path(relative_path: str) -> Path:
    """
    Путь к сырому файлу. Порядок поиска:
      1. монтирование бакета (~/yc-wiki/raw/…);
      2. локальный каталог raw/;
      3. скачивание из бакета по требованию.
    """
    if _mount_alive():
        p = YC_MOUNT / "raw" / relative_path
        if p.exists():
            return p
    local = RAW_DIR / relative_path
    if local.exists():
        return local
    print(f"[yc_sync] Скачиваю сырой файл из бакета: {relative_path}", file=sys.stderr)
    local.parent.mkdir(parents=True, exist_ok=True)
    _rclone("copyto", f"{RAW_PREFIX}/{relative_path}", str(local))
    return local


# ── CLI ──────────────────────────────────────────────────────────

def cmd_sync():
    """Загрузить локальные raw/ и data/db/ в бакет (аддитивно)."""
    print("Синхронизация raw/ → бакет…")
    _rclone("copy", str(RAW_DIR), RAW_PREFIX, "--transfers", "8")
    print("Синхронизация data/db/ → бакет…")
    for name, info in DB_FILES.items():
        if info["local"].exists():
            _rclone("copyto", str(info["local"]), info["remote"])
    print("Синхронизация завершена.")


def cmd_pull():
    """Скачать все базы из бакета в локальный кэш."""
    for name, info in DB_FILES.items():
        if info["local"].exists():
            print(f"  {name}: уже в кэше ({_format_size(info['local'].stat().st_size)})")
            continue
        print(f"  {name}: скачиваю…")
        ensure_db(name)


def cmd_status():
    """Состояние кэша и хранилища."""
    print("Локальный кэш баз:")
    print(f"  {'База':<30} {'Размер':>12} {'В кэше':>8}")
    print("-" * 55)
    total = 0
    for name, info in DB_FILES.items():
        if info["local"].exists():
            sz = info["local"].stat().st_size
            total += sz
            print(f"  {name:<30} {_format_size(sz):>12} {'да':>8}")
        else:
            print(f"  {name:<30} {'—':>12} {'нет':>8}")
    print(f"  {'ИТОГО':<30} {_format_size(total):>12}")
    print()
    st = os.statvfs(str(DATA_DIR))
    print(f"Свободно на диске: {st.f_bavail * st.f_frsize / 1024**3:.1f} ГБ")
    print(f"Монтирование бакета: {'активно' if _mount_alive() else 'нет'} ({YC_MOUNT})")
    r = _rclone("size", f"{REMOTE}:{BUCKET}", check=False)
    if r.returncode == 0:
        print(f"Бакет: {r.stdout.strip()}")


def cmd_verify():
    """Сверка бакета с локальными копиями баз по размеру."""
    print("Сверка баз с бакетом…")
    ok = True
    for name, info in DB_FILES.items():
        local, remote = info["local"], info["remote"]
        le = local.exists()
        re_ = None
        r = _rclone("size", remote, check=False)
        if r.returncode == 0:
            # rclone печатает две строки: «Total objects: N» и
            # «Total size: X MiB (NNNN Byte)» — берём байты из скобок
            for line in r.stdout.splitlines():
                if line.startswith("Total size") and "(" in line:
                    re_ = int(line.split("(")[1].split()[0])
        print(f"\n  {name}:")
        print(f"    бакет:    {'есть' if re_ is not None else 'НЕТ'}")
        print(f"    локально: {'есть' if le else 'НЕТ'}")
        if le and re_ is not None:
            ls = local.stat().st_size
            match = ("СОВПАДАЕТ" if ls == re_
                     else f"РАСХОЖДЕНИЕ (локально={ls}, бакет={re_})")
            print(f"    размер:   {match}")
            ok = ok and (ls == re_)
    sys.exit(0 if ok else 1)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    cmd = sys.argv[1]
    {'sync': cmd_sync, 'pull': cmd_pull,
     'status': cmd_status, 'verify': cmd_verify}.get(
        cmd, lambda: (print(f"Неизвестная команда: {cmd}"),
                      print("Команды: sync, pull, status, verify"),
                      sys.exit(1)))()


if __name__ == "__main__":
    main()
