#!/usr/bin/env python3
"""Инвентаризация корпуса публикаций (фаза 0 анализа).

Сводит метаданные из четырёх источников в один промежуточный JSON и считает
заполненность целевых полей. Ничего не пишет в БД — только отчёт.

Источники:
  1. фронтматтер статей     papers/*.md
  2. фронтматтер переводов  papers/ru_papers/*.md
  3. docs/paper-details.json (сборка из текста)
  4. PDF на бакете          raw/papers/*.pdf (через симлинк на YC)

Ключевой момент: связка «статья ↔ перевод ↔ PDF» делается НЕ по полю
source_pdf (оно заполнено частично и у переводов бывает обрезано без
расширения), а по нормализованному имени файла плюс префиксному
сопоставлению. Проверено: статьи Panova, Kolennikova, Drechsler, Louie,
Broxterman не имеют source_pdf, но PDF лежат под тем же именем, что и .md.

Запуск:  python3 corpus_inventory.py                  # отчёт
         python3 corpus_inventory.py --json out.json  # + промежуточный JSON
"""
import argparse
import glob
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO)

TARGET_FIELDS = [
    "title_ru", "title_orig", "doi", "source_url", "authors", "year",
    "venue", "findings", "data_sources", "methods", "references",
    "pdf_file", "doc_type", "has_translation_ru", "wiki_page",
]


def frontmatter(path):
    """(словарь полей, тело) — из markdown с YAML-подобной шапкой."""
    try:
        s = open(path, encoding="utf-8", errors="ignore").read()
    except OSError:
        return {}, ""
    if not s.startswith("---"):
        return {}, s
    parts = s.split("---", 2)
    if len(parts) < 3:
        return {}, s
    fm = {}
    for m in re.finditer(r"^([a-z_]+):\s*(.*)$", parts[1], re.M):
        v = m.group(2).strip().strip('"').strip("'")
        if v and v not in ("[]", "null", "~"):
            fm[m.group(1)] = v
    return fm, parts[2]


def norm_key(s):
    """Нормализованное имя для сопоставления: без пути, расширения, не-букв."""
    s = os.path.basename(s or "").lower()
    s = re.sub(r"\.(pdf|md)$", "", s)
    return re.sub(r"[^a-zа-я0-9]+", " ", s).strip()


def find_sections(body, names):
    """Тексты секций по заголовкам.

    Заголовки в корпусе бывают обёрнуты в **жирный**, подчёркнуты <u>, и
    содержат нумерацию — поэтому регекс терпим к разметке. Проверено: без
    этого поиск «Выводы» находил 8 секций из 314, потому что реальные
    заголовки выглядели как `## **1. Introduction**`.
    """
    pat = re.compile(
        r"^#{1,4}\s*[*_<u>\s]*(" + "|".join(names) + r")[^\n]*\n(.*?)(?=\n#{1,4}\s|\Z)",
        re.M | re.I | re.S)
    out = []
    for m in pat.finditer(body):
        # снять остатки разметки со строки заголовка перед текстом
        out.append(m.group(2).strip())
    return out


def _fallback_abs(body):
    """Первые осмысленные абзацы после заголовка аннотации или начала текста."""
    m = re.search(r"^.*?(?:аннотация|abstract).*?$\n(.*?)(?=\n#{1,4}\s|\Z)",
                  body, re.M | re.I | re.S)
    text = m.group(1) if m else body
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if len(p.strip()) > 120]
    return " ".join(paras[:2])


def match_pdf(md_stem, pdf_index, refs):
    """Найти PDF для статьи: по source_pdf, затем по имени .md, затем префиксом."""
    n = norm_key(md_stem)
    if n in pdf_index:
        return pdf_index[n]
    for k, p in pdf_index.items():
        if len(k) > 25 and (k.startswith(n[:40]) or n.startswith(k[:40])):
            return p
    return ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", help="куда сохранить промежуточный JSON")
    args = ap.parse_args()

    papers = sorted(glob.glob("papers/*.md"))
    trans = sorted(glob.glob("papers/ru_papers/*.md"))
    pdfs = sorted(glob.glob("raw/papers/*.pdf"))

    pdf_index = {norm_key(p): p for p in pdfs}

    # индекс переводов: по нормализованному source_pdf и по нормализованному title
    tr_by_key = {}
    for p in trans:
        f = frontmatter(p)[0]
        for key in (norm_key(f.get("source_pdf", "")), norm_key(f.get("title", ""))):
            if len(key) > 12:
                tr_by_key.setdefault(key, p)

    try:
        details = json.load(open("docs/paper-details.json", encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        details = {}

    records = []
    for p in papers:
        fm, body = frontmatter(p)
        stem = os.path.basename(p)[:-3]

        # перевод: по source_pdf статьи, затем по имени, затем по названию
        tr = tr_by_key.get(norm_key(fm.get("source_pdf", ""))) or \
             tr_by_key.get(norm_key(stem)) or \
             tr_by_key.get(norm_key(fm.get("title", "")))
        fm_tr = frontmatter(tr)[0] if tr else {}

        def pick(*keys):
            for d in (fm_tr, fm):
                for k in keys:
                    if d.get(k):
                        return d[k]
            return ""

        d = details.get(p) or details.get("papers/%s.md" % stem) or {}
        pdf = match_pdf(stem, pdf_index, fm.get("source_pdf", ""))

        records.append({
            "wiki_page": p,
            "translation_page": tr or "",
            "title_orig": pick("title") or (d.get("t") or "").strip("*").strip(),
            "title_ru": "",
            "authors": pick("authors") or ", ".join(d.get("authors") or []),
            "year": pick("year") or str(d.get("year") or ""),
            "venue": pick("venue", "journal", "publisher") or (d.get("venue") or ""),
            "doi": pick("doi"),
            "source_url": pick("url", "source_url") or (d.get("url") or ""),
            "doc_type": pick("type") or (d.get("type") or ""),
            "pdf_file": pdf,
            "pdf_source_pdf": fm.get("source_pdf") or fm_tr.get("source_pdf") or "",
            "has_translation_ru": bool(tr),
            "findings": " ".join(
                find_sections(body, ["Выводы", "Основные выводы", "Заключение",
                                     "Основные результаты", "Conclusion",
                                     "Conclusions", "Findings"])
                or find_sections(body, ["Аннотация", "Abstract", "Аннотация \\(ru\\)",
                                        "Нетехническое резюме"])
                or [_fallback_abs(body)]
            )[:4000],
            "methods": ", ".join(d.get("models") or []),
            "data_sources": ", ".join(d.get("data") or []),
            "references": len(find_sections(
                body, ["References", "Список литературы", "Bibliography",
                       "Литература"])),
        })

    # --- отчёт ---
    total = len(records)
    print("Корпус: %d статей, %d переводов, %d PDF" % (len(papers), len(trans), len(pdfs)))
    print("Записей: %d\n" % total)

    print("Заполненность целевых полей:")
    for f in TARGET_FIELDS:
        n = sum(1 for r in records if r.get(f))
        print("  %-20s %6d %5.0f%%  %s" % (f, n, 100 * n / total, "#" * int(30 * n / total)))

    print("\nГде нужно дозаполнение:")
    for f in ("title_ru", "authors", "year", "doi", "venue", "source_url",
              "findings", "methods", "references"):
        miss = sum(1 for r in records if not r.get(f))
        print("  %-14s отсутствует у %d (%.0f%%)" % (f, miss, 100 * miss / total))

    have_pdf = sum(1 for r in records if r["pdf_file"] and os.path.exists(r["pdf_file"]))
    print("\nPDF: найден у %d (%.0f%%), не найден у %d"
          % (have_pdf, 100 * have_pdf / total, total - have_pdf))

    refs = {r["pdf_file"] for r in records if r["pdf_file"]}
    unproc = [p for p in pdfs if p not in refs]
    print("PDF без markdown-статьи: %d" % len(unproc))
    for u in unproc[:6]:
        print("    %s" % os.path.basename(u)[:70])

    if args.json:
        json.dump(records, open(args.json, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        print("\nПромежуточный JSON: %s (%.0f КБ)" % (args.json, os.path.getsize(args.json) / 1024))
    return 0


if __name__ == "__main__":
    sys.exit(main())
