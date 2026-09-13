#!/usr/bin/env python3
"""
Nightly backup: VACUUM + sync SQLite DBs to GCS.

- VACUUMs each DB to reclaim space and reduce upload size
- Syncs all DB files to GCS bucket via gcs_sync.py
- Logs results to data/backup_log.jsonl
- Designed for cron: hermes cronjob with no_agent=True

Exit codes:
  0 — success (all DBs vacuumed and synced)
  1 — partial failure (some DBs failed, logged)
  2 — fatal (gsutil not available or GCS auth issue)
"""

import json
import os
import sqlite3
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"
LOG_FILE = DATA_DIR / "backup_log.jsonl"

# All DB files to back up (including ones not in DB_FILES dict)
DB_PATTERNS = ["*.db"]

# Minimum free disk space after VACUUM (GB)
MIN_FREE_GB = 2.0


def log_entry(entry: dict):
    """Append a JSONL log entry."""
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def get_db_files() -> list[Path]:
    """Find all .db files in data/."""
    files = []
    for pattern in DB_PATTERNS:
        files.extend(sorted(DATA_DIR.glob(pattern)))
    return files


def vacuum_db(db_path: Path, skip_if_small_freed: bool = True) -> dict:
    """VACUUM a single SQLite DB. Returns stats dict.
    
    Args:
        skip_if_small_freed: If True, skip VACUUM for DBs where previous
            VACUUM freed <5% of size (they're already compact).
    """
    size_before = db_path.stat().st_size
    
    # Skip VACUUM for large already-compact DBs (freed <5% last time)
    # Heuristic: if DB size >100MB, check last VACUUM result in log
    if skip_if_small_freed and size_before > 100 * 1024 * 1024:
        last_freed = get_last_vacuum_freed(db_path.name)
        if last_freed is not None and last_freed < 0.05:
            return {
                "status": "skipped_compact",
                "size_before": size_before,
                "size_after": size_before,
                "freed_mb": 0.0,
                "elapsed_s": 0.0,
            }
    
    start = time.time()
    try:
        conn = sqlite3.connect(str(db_path))
        conn.execute("PRAGMA journal_mode=DELETE")  # Ensure no WAL artifacts
        conn.execute("VACUUM")
        conn.close()
        size_after = db_path.stat().st_size
        elapsed = time.time() - start
        return {
            "status": "ok",
            "size_before": size_before,
            "size_after": size_after,
            "freed_mb": round((size_before - size_after) / 1024 / 1024, 1),
            "freed_pct": round((size_before - size_after) / size_before, 4) if size_before > 0 else 0,
            "elapsed_s": round(elapsed, 1),
        }
    except Exception as e:
        return {"status": "error", "error": str(e), "size_before": size_before}


def get_last_vacuum_freed(db_name: str) -> float | None:
    """Get freed_pct from last successful VACUUM of this DB in log."""
    if not LOG_FILE.exists():
        return None
    try:
        result = None
        with open(LOG_FILE) as f:
            for line in f:
                try:
                    entry = json.loads(line)
                    v = entry.get("vacuum", {}).get(db_name, {})
                    if v.get("status") == "ok" and "freed_pct" in v:
                        result = v["freed_pct"]
                except (json.JSONDecodeError, KeyError):
                    continue
        return result
    except Exception:
        return None


def check_free_disk(path: Path) -> float:
    """Return free disk space in GB."""
    stat = os.statvfs(str(path))
    return (stat.f_bavail * stat.f_frsize) / (1024**3)


def main():
    ts = datetime.now(timezone.utc).isoformat()
    print(f"[nightly_backup] Starting at {ts}")

    # Check free disk
    free_before = check_free_disk(DATA_DIR)
    print(f"[nightly_backup] Free disk: {free_before:.1f} GB")

    if free_before < MIN_FREE_GB:
        print(f"[nightly_backup] WARNING: Low disk space ({free_before:.1f} GB < {MIN_FREE_GB} GB)")
        print("[nightly_backup] Skipping VACUUM to avoid disk full")
        log_entry({
            "timestamp": ts,
            "action": "nightly_backup",
            "status": "skipped_vacuum_low_disk",
            "free_disk_gb": round(free_before, 2),
        })

    # Find all DB files
    db_files = get_db_files()
    if not db_files:
        print("[nightly_backup] No DB files found in data/")
        log_entry({"timestamp": ts, "action": "nightly_backup", "status": "no_db_files"})
        sys.exit(0)

    print(f"[nightly_backup] Found {len(db_files)} DB files")

    # Step 1: VACUUM each DB
    vacuum_results = {}
    total_freed = 0
    for db_path in db_files:
        name = db_path.name
        size_mb = db_path.stat().st_size / 1024 / 1024
        print(f"  VACUUM {name} ({size_mb:.1f} MB)... ", end="", flush=True)

        if free_before < MIN_FREE_GB:
            # Skip VACUUM for large DBs when disk is tight
            print("SKIPPED (low disk)")
            vacuum_results[name] = {"status": "skipped_low_disk"}
            continue

        result = vacuum_db(db_path)
        vacuum_results[name] = result
        if result["status"] == "ok":
            total_freed += result.get("freed_mb", 0)
            print(f"→ {result['size_after']/1024/1024:.1f} MB, freed {result['freed_mb']} MB in {result['elapsed_s']}s")
        else:
            print(f"ERROR: {result.get('error', 'unknown')}")

    free_after_vacuum = check_free_disk(DATA_DIR)
    print(f"[nightly_backup] VACUUM freed {total_freed:.1f} MB total, disk now: {free_after_vacuum:.1f} GB")

    # Step 2: Sync to GCS via gcs_sync.py
    print("[nightly_backup] Syncing to GCS...")
    sync_start = time.time()
    gsutil_path = str(Path.home() / "opt" / "google-cloud-sdk" / "bin" / "gsutil")
    env = {**os.environ, "GSUTIL_PATH": gsutil_path}
    try:
        result = subprocess.run(
            [sys.executable, str(REPO_ROOT / "scripts" / "gcs_sync.py"), "sync"],
            capture_output=True,
            text=True,
            timeout=600,
            cwd=str(REPO_ROOT),
            env=env,
        )
        sync_elapsed = time.time() - sync_start
        sync_status = "ok" if result.returncode == 0 else "error"
        sync_output = result.stdout[-500:] if result.stdout else ""
        sync_error = result.stderr[-500:] if result.stderr else ""

        if result.returncode != 0:
            print(f"[nightly_backup] GCS sync FAILED: {sync_error}")
        else:
            print(f"[nightly_backup] GCS sync OK ({sync_elapsed:.1f}s)")

    except subprocess.TimeoutExpired:
        sync_status = "timeout"
        sync_output = ""
        sync_error = "sync timed out after 600s"
        sync_elapsed = 600
        print("[nightly_backup] GCS sync TIMED OUT")
    except Exception as e:
        sync_status = "error"
        sync_output = ""
        sync_error = str(e)
        sync_elapsed = time.time() - sync_start
        print(f"[nightly_backup] GCS sync ERROR: {e}")

    # Step 3: Verify
    print("[nightly_backup] Verifying GCS consistency...")
    try:
        result = subprocess.run(
            [sys.executable, str(REPO_ROOT / "scripts" / "gcs_sync.py"), "verify"],
            capture_output=True,
            text=True,
            timeout=120,
            cwd=str(REPO_ROOT),
            env=env,
        )
        verify_output = result.stdout
    except Exception as e:
        verify_output = f"verify error: {e}"

    # Log entry
    log_entry({
        "timestamp": ts,
        "action": "nightly_backup",
        "vacuum": vacuum_results,
        "total_freed_mb": round(total_freed, 1),
        "free_disk_before_gb": round(free_before, 2),
        "free_disk_after_vacuum_gb": round(free_after_vacuum, 2),
        "sync": {
            "status": sync_status,
            "elapsed_s": round(sync_elapsed, 1),
            "error": sync_error[:200] if sync_error else None,
        },
        "verify": verify_output[:500] if verify_output else None,
    })

    # Final status
    final_free = check_free_disk(DATA_DIR)
    print(f"[nightly_backup] Done. Free disk: {final_free:.1f} GB")

    if sync_status != "ok":
        sys.exit(1)


if __name__ == "__main__":
    main()