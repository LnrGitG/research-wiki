#!/usr/bin/env python3
"""Стенд разбора SDMX-ответа ЕМИСС: потоковый разбор против прежнего дерева.

Считает число строк, число названий справочника, sha по строкам, время и пик
RSS. Запускается отдельным процессом на каждый вариант, чтобы пик памяти не
смешивался.

    python3 scripts/emiss_sdmx_bench.py /tmp/sdmx_small.xml --impl new
    python3 scripts/emiss_sdmx_bench.py /tmp/sdmx_small.xml --impl old \
        --old-module /tmp/old_emiss_loader.py

Старый модуль берётся из истории: git show pre-emiss-stream:scripts/emiss_loader.py
"""

import argparse
import hashlib
import importlib.util
import json
import os
import resource
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def row_sha(rows):
    sig = hashlib.sha256()
    for r in rows:
        sig.update(json.dumps(r, sort_keys=True, ensure_ascii=False).encode())
    return sig.hexdigest()[:16]


def main():
    ap = argparse.ArgumentParser(description="стенд разбора SDMX ЕМИСС")
    ap.add_argument("fixture")
    ap.add_argument("--impl", choices=["new", "old"], default="new")
    ap.add_argument("--old-module", default=None,
                    help="путь к emiss_loader.py до правки (git show pre-emiss-stream:...)")
    args = ap.parse_args()

    if args.impl == "old":
        if not args.old_module:
            raise SystemExit("для --impl old нужен --old-module")
        mod = load_module(args.old_module, "emiss_old")
        blob = open(args.fixture, "rb").read()
        t0 = time.perf_counter()
        data = mod.Emiss.parse_sdmx(blob)
    else:
        import emiss_loader as mod
        t0 = time.perf_counter()
        data = mod.Emiss.parse_sdmx(args.fixture)

    elapsed = time.perf_counter() - t0
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
    out = {
        "impl": args.impl,
        "fixture": args.fixture,
        "bytes": os.path.getsize(args.fixture),
        "rows": len(data["rows"]),
        "names": len(data["names"]),
        "seconds": round(elapsed, 2),
        "maxrss_mb": round(rss),
        "sha": row_sha(data["rows"]),
    }
    print(json.dumps(out, ensure_ascii=False))


if __name__ == "__main__":
    main()
