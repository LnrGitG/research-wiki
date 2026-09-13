#!/usr/bin/env python3
"""
GCS sync utility for research-wiki heavy data.

Architecture:
  - GCS bucket (wiki-research-508405) = source of truth for raw/ and data/db/
  - Local VPS = hot cache for active DB files
  - raw/ accessed via gcsfuse mount at ~/gcs-wiki/raw/
  - data/*.db fetched on-demand via ensure_db(), cached locally

Usage:
  from gcs_sync import ensure_db, DATA_DIR, RAW_DIR, GCS_BUCKET

  db_path = ensure_db('rosstat_construction.db')
  con = sqlite3.connect(db_path)

CLI:
  python3 scripts/gcs_sync.py sync    # Upload local → GCS (one-way)
  python3 scripts/gcs_sync.py pull    # Download all DBs from GCS
  python3 scripts/gcs_sync.py status  # Show cache status
  python3 scripts/gcs_sync.py verify  # Check GCS vs local consistency
"""

import os
import sys
import subprocess
import hashlib
import json
import time
from pathlib import Path

# ── Configuration ────────────────────────────────────────────────

GCS_BUCKET = os.environ.get(
    "GCS_BUCKET", "wiki-research-508405"
)
GCS_RAW_PREFIX = f"gs://{GCS_BUCKET}/raw"
GCS_DB_PREFIX = f"gs://{GCS_BUCKET}/data/db"

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"
RAW_DIR = REPO_ROOT / "raw"
GCS_MOUNT = Path(os.environ.get("GCS_MOUNT", os.path.expanduser("~/gcs-wiki")))

# DB files that live on GCS and are cached locally
# (filename → local path, gcs path)
DB_FILES = {
    "rosstat_construction.db": {
        "local": DATA_DIR / "rosstat_construction.db",
        "gcs": f"{GCS_DB_PREFIX}/rosstat_construction.db",
    },
    "regions_panel.db": {
        "local": DATA_DIR / "regions_panel.db",
        "gcs": f"{GCS_DB_PREFIX}/regions_panel.db",
    },
    "cbr_lending.db": {
        "local": DATA_DIR / "cbr_lending.db",
        "gcs": f"{GCS_DB_PREFIX}/cbr_lending.db",
    },
    "fns_tochno_sectors.db": {
        "local": DATA_DIR / "fns_tochno_sectors.db",
        "gcs": f"{GCS_DB_PREFIX}/fns_tochno_sectors.db",
    },
    "rosreestr_deals.db": {
        "local": DATA_DIR / "rosreestr_deals.db",
        "gcs": f"{GCS_DB_PREFIX}/rosreestr_deals.db",
    },
    "developers_ifrs.db": {
        "local": DATA_DIR / "developers_ifrs.db",
        "gcs": f"{GCS_DB_PREFIX}/developers_ifrs.db",
    },
}

# Maximum local cache size in bytes (default: 2 GB)
MAX_CACHE_BYTES = int(os.environ.get("MAX_CACHE_BYTES", 2 * 1024 ** 3))

# ── Helpers ──────────────────────────────────────────────────────

def _gsutil(*args: str, check: bool = True) -> subprocess.CompletedProcess:
    """Run gsutil command."""
    gsutil_path = os.environ.get("GSUTIL_PATH", "gsutil")
    cmd = [gsutil_path, "-q"] + list(args)
    result = subprocess.run(cmd, capture_output=True, text=True)
    if check and result.returncode != 0:
        raise RuntimeError(f"gsutil failed: {result.stderr}")
    return result


def _file_hash(path: Path, algorithm: str = "md5") -> str:
    """Compute hash of a local file."""
    h = hashlib.new(algorithm)
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def _format_size(nbytes: int) -> str:
    """Human-readable file size."""
    for unit in ("B", "KB", "MB", "GB"):
        if nbytes < 1024:
            return f"{nbytes:.1f} {unit}"
        nbytes /= 1024
    return f"{nbytes:.1f} TB"


# ── Core functions ───────────────────────────────────────────────

def ensure_db(name: str, force: bool = False) -> Path:
    """
    Ensure a DB file is available locally, downloading from GCS if needed.

    Args:
        name: DB filename (e.g. 'rosstat_construction.db')
        force: Re-download even if local file exists

    Returns:
        Path to local DB file

    Raises:
        KeyError: if name is not a known DB file
        RuntimeError: if download fails
    """
    if name not in DB_FILES:
        raise KeyError(
            f"Unknown DB '{name}'. Known: {', '.join(DB_FILES)}"
        )

    info = DB_FILES[name]
    local_path = info["local"]

    if local_path.exists() and not force:
        return local_path

    print(f"[gcs_sync] Downloading {name} from GCS...", file=sys.stderr)
    _gsutil("cp", info["gcs"], str(local_path))
    print(f"[gcs_sync] Done: {local_path} ({_format_size(local_path.stat().st_size)})",
          file=sys.stderr)
    return local_path


def evict_db(name: str) -> bool:
    """
    Remove a local DB cache copy to free disk space.
    Returns True if file was removed, False if it didn't exist.
    """
    if name not in DB_FILES:
        raise KeyError(f"Unknown DB '{name}'")
    local_path = DB_FILES[name]["local"]
    if local_path.exists():
        local_path.unlink()
        print(f"[gcs_sync] Evicted {name}", file=sys.stderr)
        return True
    return False


def evict_lru_until(free_needed_bytes: int) -> int:
    """
    Evict least-recently-used DB files until free_needed_bytes are available.
    Returns number of files evicted.
    """
    evicted = 0
    # Sort by access time, oldest first
    files = []
    for name, info in DB_FILES.items():
        if info["local"].exists():
            files.append((info["local"].stat().st_atime, name, info["local"].stat().st_size))
    files.sort()

    freed = 0
    for _, name, size in files:
        if freed >= free_needed_bytes:
            break
        evict_db(name)
        freed += int(size)
        evicted += 1

    return evicted


def raw_path(relative_path: str) -> Path:
    """
    Get path to a raw data file. Uses gcsfuse mount if available,
    falls back to local raw/ directory.

    Args:
        relative_path: path relative to raw/ (e.g. 'rosstat/yearbooks/Stroit_2022.pdf')

    Returns:
        Path via gcsfuse mount if mounted, else local path
    """
    gcs_path = GCS_MOUNT / "raw" / relative_path
    if gcs_path.exists():
        return gcs_path
    local_path = RAW_DIR / relative_path
    if local_path.exists():
        return local_path
    # Try downloading from GCS to local raw/
    print(f"[gcs_sync] Downloading raw file from GCS: {relative_path}", file=sys.stderr)
    local_path.parent.mkdir(parents=True, exist_ok=True)
    _gsutil("cp", f"{GCS_RAW_PREFIX}/{relative_path}", str(local_path))
    return local_path


# ── CLI commands ─────────────────────────────────────────────────

def cmd_sync():
    """Upload local raw/ and data/db/ to GCS (additive)."""
    print("Syncing raw/ → GCS...")
    _gsutil("-m", "rsync", "-r", str(RAW_DIR), f"{GCS_RAW_PREFIX}/")
    print("Syncing data/db/ → GCS...")
    # Create temp dir with just the DB files
    import tempfile
    tmpdir = Path(tempfile.mkdtemp(prefix="gcs_sync_"))
    try:
        db_tmp = tmpdir / "db"
        db_tmp.mkdir()
        for name, info in DB_FILES.items():
            if info["local"].exists():
                import shutil
                shutil.copy2(info["local"], db_tmp / name)
        _gsutil("-m", "rsync", "-r", str(db_tmp), f"{GCS_DB_PREFIX}/")
    finally:
        import shutil
        shutil.rmtree(tmpdir, ignore_errors=True)
    print("Sync complete.")


def cmd_pull():
    """Download all DB files from GCS to local cache."""
    for name, info in DB_FILES.items():
        if info["local"].exists():
            sz = info["local"].stat().st_size
            print(f"  {name}: already cached ({_format_size(sz)})")
            continue
        print(f"  {name}: downloading...")
        ensure_db(name)


def cmd_status():
    """Show local cache status vs GCS."""
    print("DB cache status:")
    print(f"  {'Name':<30} {'Local size':>12} {'Cached':>8}")
    print("-" * 55)
    total_cached = 0
    for name, info in DB_FILES.items():
        if info["local"].exists():
            sz = info["local"].stat().st_size
            total_cached += sz
            print(f"  {name:<30} {_format_size(sz):>12} {'yes':>8}")
        else:
            print(f"  {name:<30} {'—':>12} {'no':>8}")
    print(f"  {'TOTAL':<30} {_format_size(total_cached):>12}")
    print()

    # Disk space
    stat = os.statvfs(str(DATA_DIR))
    free_gb = (stat.f_bavail * stat.f_frsize) / (1024 ** 3)
    print(f"Free disk: {free_gb:.1f} GB")

    # GCS bucket size
    result = _gsutil("du", "-s", f"gs://{GCS_BUCKET}/", check=False)
    if result.returncode == 0:
        print(f"GCS bucket: {result.stdout.strip()}")


def cmd_verify():
    """Check GCS vs local consistency for DB files."""
    print("Verifying DB consistency...")
    for name, info in DB_FILES.items():
        local_exists = info["local"].exists()
        print(f"\n  {name}:")

        # Check GCS
        result = _gsutil("stat", info["gcs"], check=False)
        gcs_exists = result.returncode == 0
        print(f"    GCS:    {'present' if gcs_exists else 'MISSING'}")
        print(f"    Local:  {'present' if local_exists else 'MISSING'}")

        if local_exists and gcs_exists:
            local_sz = info["local"].stat().st_size
            # Parse GCS size from stat output
            for line in result.stdout.splitlines():
                if line.startswith("Content-Length:"):
                    gcs_sz = int(line.split(":")[1].strip())
                    match = "✓ MATCH" if local_sz == gcs_sz else f"✗ MISMATCH (local={local_sz}, gcs={gcs_sz})"
                    print(f"    Size:   {match}")
                    break


# ── Main ──────────────────────────────────────────────────────────

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "sync":
        cmd_sync()
    elif cmd == "pull":
        cmd_pull()
    elif cmd == "status":
        cmd_status()
    elif cmd == "verify":
        cmd_verify()
    else:
        print(f"Unknown command: {cmd}")
        print("Commands: sync, pull, status, verify")
        sys.exit(1)


if __name__ == "__main__":
    main()