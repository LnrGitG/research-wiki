#!/usr/bin/env python3
"""Один прогон функции разбора под заданным движком xlsx (для сверки).

Запуск: python3 scripts/_xlsx_verify_call.py scripts/x.py parse '["file.xlsx"]' fastexcel

Печатает JSON: {"sha": ..., "n": ..., "sample": ...} — sha канонического
представления результата. Движок задаётся переменной окружения XLSX_ENGINE,
которую читает xlsx_engine.DEFAULT_ENGINE при импорте.
"""
import hashlib
import importlib.util
import json
import os
import sys


def main() -> int:
    script, func, files, engine = sys.argv[1:5]
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.environ["XLSX_ENGINE"] = engine
    for d in (os.path.join(root, "scripts"), os.path.join(root, "loader")):
        sys.path.insert(0, d)
    sys.path.insert(0, root)
    path = os.path.join(root, script)
    spec = importlib.util.spec_from_file_location("_verify_mod", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    fn = getattr(mod, func)
    wanted = json.loads(files)
    out = {}
    for f in wanted:
        out[f] = fn(f)
    text = json.dumps(out, ensure_ascii=False, sort_keys=True, default=str)
    print(json.dumps({
        "sha": hashlib.sha256(text.encode()).hexdigest()[:16],
        "n": len(out),
        "bytes": len(text),
        "engine": engine,
    }))
    return 0


if __name__ == "__main__":
    sys.exit(main())
