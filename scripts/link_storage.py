#!/usr/bin/env python3
"""Связка статей с файлами в хранилище (фаза 4).

Для каждой статьи находит первичный PDF в бакете `wiki-research` (Object
Storage Yandex Cloud, смонтирован в ~/yc-wiki, симлинк raw/) и собирает
метаданные файла: путь, размер, sha256, presigned-ссылку.

Хранилище: бакет `wiki-research` в Object Storage YC, смонтирован через
rclone. Старый GCS-бакет `wiki-research-508405` выведен из эксплуатации
(~/gcs-wiki пуст и не смонтирован) — актуально только YC.

Сопоставление имён — по нормализованной форме: в бакете имена могут быть с
подчёркиваниями, пробелами и точками, а страницы вики — с дефисами.
  'Adrian_Predicting Downside Risks to House Prices and Macro-Financial S.pdf'
  <-> 'Adrian-Predicting-Downside-Risks-to-House-Prices-and-Macro-Financi.md'

Порядок источников (от точного к приблизительному):
  1. поле `source_pdf` из фронтматтера;
  2. точное совпадение нормализованного имени;
  3. префиксное совпадение (первые 30 символов) — единственный кандидат;
  4. префиксное совпадение — несколько кандидатов: НЕ выбираем, помечаем
     как неоднозначное (`ambiguous`), чтобы не подставить чужой файл.

sha256 считается потоково; для файлов >20 МБ это заметно, поэтому результат
кэшируется в `data/pdf_hashes.json`.

Запуск:  python3 link_storage.py                  # отчёт
         python3 link_storage.py --json out.json    # + результат
         python3 link_storage.py --sign --json out.json  # + presigned URL
"""
import argparse
import glob
import hashlib
import json
import os
import re
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO)

BUCKET = "wiki-research"
PAPERS_DIR = "raw/papers"
HASH_CACHE = "data/pdf_hashes.json"


def norm(s):
    """Нормализованная форма имени для сопоставления."""
    s = s.lower()
    s = re.sub(r"[_\s\.\+]+", "-", s)
    s = re.sub(r"-+", "-", s)
    return s.strip("-")


def frontmatter(path):
    try:
        s = open(path, encoding="utf-8", errors="ignore").read()
    except OSError:
        return {}
    if not s.startswith("---"):
        return {}
    parts = s.split("---", 2)
    if len(parts) < 3:
        return {}
    fm = {}
    for m in re.finditer(r"^([a-z_]+):\s*(.*)$", parts[1], re.M):
        v = m.group(2).strip().strip('"').strip("'")
        if v:
            fm[m.group(1)] = v
    return fm


def sha256_of(path, cache):
    """sha256 с кэшем по (путь, размер, mtime)."""
    try:
        st = os.stat(path)
    except OSError:
        return ""
    key = path
    c = cache.get(key)
    if c and c.get("size") == st.st_size and c.get("mtime") == int(st.st_mtime):
        return c.get("sha256", "")
    h = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(1 << 20), b""):
                h.update(chunk)
    except OSError:
        return ""
    digest = h.hexdigest()
    cache[key] = {"size": st.st_size, "mtime": int(st.st_mtime), "sha256": digest}
    return digest


def presign(path):
    """Presigned-ссылка на объект бакета (на 7 дней).

    `rclone link` для S3-бэкенда выдаёт именно подписанную ссылку
    (X-Amz-Signature, Expires), а не публичный доступ — это важно: бакет
    приватный, PDF под копирайтом, публичный URL был бы нарушением.
    Ключ объекта — путь внутри бакета, то есть 'raw/papers/...' целиком.
    """
    # remote и путь обязаны быть ОДНИМ токеном: 'yc-s3:bucket/raw/papers/x.pdf'.
    # Двумя аргументами rclone отвечает подсказкой об использовании и rc=1 —
    # на этом молча терялись все 196 ссылок в первом прогоне.
    key = path[len("raw/"):] if path.startswith("raw/") else path
    target = "yc-s3:%s/%s/%s" % (BUCKET, PAPERS_DIR, os.path.basename(key))
    cmd = ["rclone", "link", target, "--expire", "168h"]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        line = (r.stdout + r.stderr).strip().splitlines()
        for ln in line:
            if ln.startswith("http"):
                return ln.strip()
    except (OSError, subprocess.TimeoutExpired):
        pass
    return ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json")
    ap.add_argument("--sign", action="store_true", help="считать presigned-ссылки")
    args = ap.parse_args()

    cache = {}
    if os.path.exists(HASH_CACHE):
        try:
            cache = json.load(open(HASH_CACHE, encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            cache = {}

    pdfs = sorted(glob.glob(os.path.join(PAPERS_DIR, "*.pdf")))
    by_norm = {}
    for p in pdfs:
        by_norm.setdefault(norm(os.path.basename(p)[:-4]), []).append(p)

    papers = sorted(glob.glob("papers/*.md"))
    out = []
    stats = {"source_pdf": 0, "exact": 0, "prefix": 0, "ambiguous": 0, "none": 0}

    for p in papers:
        stem = os.path.basename(p)[:-3]
        fm = frontmatter(p)
        found = ""
        how = ""

        # 1. поле source_pdf
        sp = fm.get("source_pdf", "")
        if sp:
            cand = os.path.join(PAPERS_DIR, os.path.basename(sp))
            if not cand.lower().endswith(".pdf"):
                cand += ".pdf"
            if os.path.exists(cand):
                found, how = cand, "source_pdf"

        # 2. точное совпадение нормализованного имени
        if not found:
            hits = by_norm.get(norm(stem))
            if hits and len(hits) == 1:
                found, how = hits[0], "exact"

        # 3-4. префиксное совпадение
        if not found:
            key = norm(stem)[:30]
            if len(key) > 15:
                cands = [v[0] for k, v in by_norm.items() if k.startswith(key)]
                if len(cands) == 1:
                    found, how = cands[0], "prefix"
                elif len(cands) > 1:
                    how = "ambiguous"

        if not found:
            how = how or "none"

        rec = {"wiki_page": p, "stem": stem, "storage_path": "", "bucket": BUCKET,
               "file_name": "", "size_bytes": 0, "sha256": "", "presigned_url": "",
               "match": how}
        if found:
            st = os.stat(found)
            rec.update({
                "storage_path": found,
                "storage_key": found[len("raw/"):] if found.startswith("raw/") else found,
                "file_name": os.path.basename(found),
                "size_bytes": st.st_size,
                "sha256": sha256_of(found, cache),
            })
            if args.sign:
                rec["presigned_url"] = presign(found)
        stats[how] = stats.get(how, 0) + 1
        out.append(rec)

    json.dump(cache, open(HASH_CACHE, "w", encoding="utf-8"), ensure_ascii=False, indent=0)

    print("Статей: %d\n" % len(out))
    print("Связка с PDF в бакете %s (%s):" % (BUCKET, PAPERS_DIR))
    for k in ("source_pdf", "exact", "prefix", "ambiguous", "none"):
        v = stats.get(k, 0)
        print("  %-14s %3d (%.0f%%)" % (k, v, 100 * v / len(out)))
    linked = sum(v for k, v in stats.items() if k in ("source_pdf", "exact", "prefix"))
    print("  %-14s %3d (%.0f%%)" % ("ВСЕГО найдено", linked, 100 * linked / len(out)))

    sizes = [r["size_bytes"] for r in out if r["size_bytes"]]
    if sizes:
        print("\nРазмер найденных PDF: сумма %.0f МБ, медиана %.1f МБ" % (
            sum(sizes) / 1e6, sorted(sizes)[len(sizes) // 2] / 1e6))
    hashed = sum(1 for r in out if r["sha256"])
    print("sha256 посчитан: %d (кэш %d записей)" % (hashed, len(cache)))

    amb = [r for r in out if r["match"] == "ambiguous"]
    if amb:
        print("\nНеоднозначные (несколько кандидатов, файл НЕ подставлен): %d" % len(amb))
        for r in amb[:8]:
            print("  %s" % r["stem"][:66])

    print("\nПримеры связок:")
    for r in [x for x in out if x["match"] in ("source_pdf", "exact", "prefix")][:6]:
        print("  %-38s -> %s (%.1f МБ, %s)" % (
            r["stem"][:36], r["file_name"][:40], r["size_bytes"] / 1e6, r["match"]))
    if args.sign:
        signed = [r for r in out if r["presigned_url"]]
        print("\npresigned-ссылок получено: %d" % len(signed))
        for r in signed[:2]:
            print("  %s..." % r["presigned_url"][:110])

    if args.json:
        json.dump(out, open(args.json, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print("\nJSON: %s (%.0f КБ)" % (args.json, os.path.getsize(args.json) / 1024))
    return 0


if __name__ == "__main__":
    sys.exit(main())
