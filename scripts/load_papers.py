#!/usr/bin/env python3
"""Сборка карточек публикаций и загрузка в БД YC (фаза 5).

Сводит результаты фаз 1-4 в одну запись на статью и готовит SQL для
`core.paper_card`:

    meta.json      (фаза 1) — авторы, год, издание, DOI, ссылка, название
    methods.json   (фаза 2) — методы, источники данных, выводы, текст методов
    refs.json      (фаза 3) — список литературы
    storage.json   (фаза 4) — путь, размер, sha256, presigned-ссылка

Доставка в БД: прямой доступ к ВМ YC с зарубежного VDS заблокирован
гео-фильтром (порт 22 открыт только из РФ), поэтому используется канал
`agent-vm-exchange`: SQL-файл кладётся в `_cmd/`, туда же — `command.sh`,
systemd-агент на ВМ его исполняет и пишет `_cmd/output.txt`.

Идемпотентность: UPSERT по `paper_code`, повторный запуск не создаёт дублей.

Запуск:  python3 load_papers.py --build                 # собрать карточки
         python3 load_papers.py --build --sql out.sql     # собрать SQL
         python3 load_papers.py --upload out.sql          # отправить на ВМ
         python3 load_papers.py --status                  # прочитать output.txt
"""
import argparse
import glob
import json
import os
import re
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO)

BUCKET = "wiki-research"
CHANNEL = "yc-s3:agent-vm-exchange"


def load(path):
    if not path or not os.path.exists(path):
        return {}
    try:
        d = json.load(open(path, encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    if isinstance(d, list):
        return {r.get("wiki_page") or r.get("stem"): r for r in d if isinstance(r, dict)}
    return d


def esc(v):
    """SQL-литерал. Пустое значение -> NULL."""
    if v is None or v == "":
        return "NULL"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    return "'" + str(v).replace("'", "''") + "'"


def sql_array(items):
    """text[] из списка строк."""
    if not items:
        return "NULL"
    parts = ",".join("'" + str(x).replace("'", "''") + "'" for x in items)
    return "ARRAY[%s]::text[]" % parts


def sql_jsonb(obj):
    if not obj:
        return "NULL"
    s = json.dumps(obj, ensure_ascii=False)
    return "'" + s.replace("'", "''") + "'::jsonb"


def title_from_body(path):
    """Название: из фронтматтера или первого заголовка."""
    try:
        s = open(path, encoding="utf-8", errors="ignore").read()
    except OSError:
        return ""
    if s.startswith("---") and s.count("---") >= 2:
        s = s.split("---", 2)[2]
    m = re.search(r"^#\s+(.+)$", s, re.M)
    return re.sub(r"[*_`]", "", m.group(1)).strip()[:300] if m else ""


def build(args):
    meta = load(args.meta)
    meth = load(args.methods)
    refs = load(args.refs)
    stor = load(args.storage)
    details = {}
    try:
        details = json.load(open("docs/paper-details.json", encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        pass

    pages = sorted(glob.glob("papers/*.md"))
    rows = []
    for p in pages:
        stem = os.path.basename(p)[:-3]
        m = meta.get(p) or meta.get(stem) or {}
        me = meth.get(p) or meth.get(stem) or {}
        rf = refs.get(p) or refs.get(stem) or {}
        st = stor.get(p) or stor.get(stem) or {}
        d = details.get(p) or {}

        title_orig = m.get("title_orig") or d.get("t") or title_from_body(p)
        doc_type = "перевод" if "ru_papers" in p else ("статья" if st else "публикация")

        refs_list = rf.get("refs") or []
        rows.append({
            "paper_code": stem, "title_ru": d.get("t") or "", "title_orig": title_orig,
            "doc_type": doc_type, "source_url": m.get("source_url", ""),
            "doi": m.get("doi", ""), "venue": m.get("venue", ""),
            "year": int(m["year"]) if str(m.get("year", "")).isdigit() else None,
            "authors": m.get("authors", ""),
            "authors_source": (m.get("sources") or {}).get("authors", ""),
            "findings": me.get("findings", ""), "findings_source": me.get("findings_source", ""),
            "methods": me.get("methods") or [], "data_sources": me.get("data_sources") or [],
            "methods_text": me.get("methods_text", ""),
            "references_json": refs_list, "n_references": len(refs_list),
            "file_path": st.get("storage_path", ""), "file_name": st.get("file_name", ""),
            "file_size_bytes": st.get("size_bytes") or None,
            "file_sha256": st.get("sha256", ""), "presigned_url": st.get("presigned_url", ""),
            "file_match": st.get("match", ""), "file_available": bool(st.get("storage_path")),
            "wiki_page": p,
        })

    print("Карточек собрано: %d\n" % len(rows))
    for f, label in (("title_orig", "название"), ("authors", "авторы"), ("year", "год"),
                     ("doi", "DOI"), ("source_url", "ссылка"), ("findings", "выводы"),
                     ("methods", "методы"), ("data_sources", "данные"),
                     ("n_references", "литература"), ("file_available", "файл")):
        n = sum(1 for r in rows if r.get(f))
        print("  %-12s %3d (%2.0f%%)" % (label, n, 100 * n / len(rows)))

    cols = ("paper_code title_ru title_orig doc_type source_url doi venue year authors "
            "authors_source findings findings_source methods data_sources methods_text "
            "references_json n_references file_path file_name file_size_bytes file_sha256 "
            "presigned_url file_match file_available wiki_page").split()
    values = []
    for r in rows:
        values.append("(" + ", ".join([
            esc(r["paper_code"]), esc(r["title_ru"]), esc(r["title_orig"]), esc(r["doc_type"]),
            esc(r["source_url"]), esc(r["doi"]), esc(r["venue"]), esc(r["year"]),
            esc(r["authors"]), esc(r["authors_source"]), esc(r["findings"]),
            esc(r["findings_source"]), sql_array(r["methods"]), sql_array(r["data_sources"]),
            esc(r["methods_text"][:6000]), sql_jsonb(r["references_json"]),
            esc(r["n_references"]), esc(r["file_path"]), esc(r["file_name"]),
            esc(r["file_size_bytes"]), esc(r["file_sha256"]), esc(r["presigned_url"]),
            esc(r["file_match"]), esc(r["file_available"]), esc(r["wiki_page"]),
        ]) + ")")

    update = ", ".join("%s = EXCLUDED.%s" % (c, c) for c in cols[1:])
    sql = ["BEGIN;",
           "INSERT INTO core.paper_card (%s) VALUES" % ", ".join(cols),
           ",\n".join(values),
           "ON CONFLICT (paper_code) DO UPDATE SET %s, updated = now();" % update,
           "COMMIT;"]
    out_sql = "\n".join(sql)

    if args.sql:
        open(args.sql, "w", encoding="utf-8").write(out_sql)
        print("\nSQL: %s (%.1f МБ)" % (args.sql, os.path.getsize(args.sql) / 1e6))

    if args.cards:
        json.dump(rows, open(args.cards, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print("Карточки: %s (%.0f КБ)" % (args.cards, os.path.getsize(args.cards) / 1024))
    return rows


def upload(path):
    if not os.path.exists(path):
        print("Файл не найден: %s" % path)
        return 1
    for cmd in (["rclone", "copyto", path, CHANNEL + "/_cmd/load_paper_card.sql"],
                ["rclone", "copyto", "scripts/load_papers_cmd.sh", CHANNEL + "/_cmd/command.sh"]):
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        print("  %s -> rc=%d %s" % (cmd[2].split("/")[-1], r.returncode, r.stderr.strip()[:80]))
    return 0


def status():
    r = subprocess.run(["rclone", "cat", CHANNEL + "/_cmd/output.txt"],
                       capture_output=True, text=True, timeout=120)
    print(r.stdout[-3000:] if r.stdout else "(output.txt пуст)")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--meta", default="/tmp/meta.json")
    ap.add_argument("--methods", default="/tmp/methods.json")
    ap.add_argument("--refs", default="/tmp/refs.json")
    ap.add_argument("--storage", default="/tmp/storage-signed.json")
    ap.add_argument("--sql")
    ap.add_argument("--cards")
    ap.add_argument("--build", action="store_true")
    ap.add_argument("--upload")
    ap.add_argument("--status", action="store_true")
    args = ap.parse_args()
    if args.status:
        return status()
    if args.upload:
        return upload(args.upload)
    if args.build:
        build(args)
        return 0
    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
