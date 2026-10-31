#!/usr/bin/env python3
"""Сверка потокового разбора ЕМИСС с прежним кодом на одном и том же ответе.

Берёт живой ответ одним запросом, сохраняет его в файл и разбирает двумя
реализациями: потоковой (текущей) и прежней (из git-ссылки, по умолчанию
pre-emiss-stream). Печатает число строк, справочников, sha и первое расхождение.
Если ответ уже сохранён, сеть не нужна:

    python3 scripts/emiss_verify_live.py 43062 --from-file /tmp/43062_live.xml
    python3 scripts/emiss_verify_live.py 43062 --save-raw /tmp/43062_live.xml \
        --filter "Классификатор объектов администр...=Свердловская область"
"""

import argparse
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
import emiss_loader  # noqa: E402

REPO = os.path.dirname(HERE)


def row_sha(rows):
    sig = hashlib.sha256()
    for r in rows:
        sig.update(json.dumps(r, sort_keys=True, ensure_ascii=False).encode())
    return sig.hexdigest()[:16]


def load_old(ref):
    """Достаёт прежний emiss_loader.py из git и импортирует его."""
    src = subprocess.check_output(["git", "-C", REPO, "show", "%s:%s" % (ref, "scripts/emiss_loader.py")])
    fd, path = tempfile.mkstemp(prefix="emiss_old_", suffix=".py")
    with os.fdopen(fd, "wb") as fh:
        fh.write(src)
    spec = importlib.util.spec_from_file_location("emiss_old", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    os.remove(path)
    return mod


def first_diff(new_rows, old_rows):
    for i, (a, b) in enumerate(zip(new_rows, old_rows)):
        if a != b:
            return {"row": i, "new": a, "old": b}
    if len(new_rows) != len(old_rows):
        return {"row": min(len(new_rows), len(old_rows)),
                "new_len": len(new_rows), "old_len": len(old_rows)}
    return None


def main():
    ap = argparse.ArgumentParser(description="сверка нового и прежнего разбора ЕМИСС")
    ap.add_argument("indicator_id", nargs="?", default=None)
    ap.add_argument("--filter", action="append", default=[])
    ap.add_argument("--save-raw", default=None, help="куда сохранить живой ответ")
    ap.add_argument("--from-file", default=None, help="уже сохранённый ответ, без сети")
    ap.add_argument("--old-ref", default="pre-emiss-stream")
    args = ap.parse_args()

    if args.from_file:
        path = args.from_file
    else:
        if not args.indicator_id:
            raise SystemExit("нужен indicator_id или --from-file")
        wanted = {}
        for flt in args.filter:
            if "=" not in flt:
                raise SystemExit("фильтр должен быть вида Поле=значение: %s" % flt)
            k, v = flt.split("=", 1)
            wanted[k.strip()] = "*" if v.strip() == "*" else [x for x in v.split(",")]
        path = args.save_raw or os.path.join(tempfile.gettempdir(), "emiss_%s.xml" % args.indicator_id)
        data = emiss_loader.Emiss().load(args.indicator_id, wanted=wanted, save_raw=path)
        print("загружено: %d байт, строк %d, попыток %d -> %s"
              % (data["bytes"], len(data["rows"]), data["attempts"], path))

    new = emiss_loader.Emiss.parse_sdmx(path)
    old = load_old(args.old_ref).Emiss.parse_sdmx(open(path, "rb").read())
    diff = first_diff(new["rows"], old["rows"])
    out = {
        "source": path,
        "bytes": os.path.getsize(path),
        "rows": [len(new["rows"]), len(old["rows"])],
        "names": [len(new["names"]), len(old["names"])],
        "sha": [row_sha(new["rows"]), row_sha(old["rows"])],
        "match": diff is None and new["names"] == old["names"],
        "first_diff": diff,
    }
    print(json.dumps(out, ensure_ascii=False))
    return 0 if out["match"] else 1


if __name__ == "__main__":
    sys.exit(main())
