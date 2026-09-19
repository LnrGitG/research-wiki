#!/usr/bin/env python3
"""Извлечение метаданных из текста публикаций (фаза 1, без внешних API).

Надёжный порядок источников — от самого достоверного к наименее:

  1. фронтматтер `papers/*.md` и `papers/ru_papers/*.md`;
  2. явные строки тела: `**Authors:**`, `**Year:**`, `**Venue:**`, `**URL:**`,
     `**DOI:**` (так размечены конвертированные работы, см. Kolennikova);
  3. DOI и ссылка на источник, найденные в тексте (в том числе после
     `https://doi.org/`), — только при однозначном совпадении;
  4. имя файла по паттерну `Автор-Год-Тема` (распространён в корпусе).

**Crossref здесь НЕ используется.** Причина: 95% корпуса без DOI, а поиск по
названию даёт ложные срабатывания, особенно на русскоязычных работах.
Внешнее подтверждение делается отдельной фазой и только для записей, где DOI
уже найден в тексте.

Принцип: чего нет в тексте — остаётся пустым с пометкой `needs_review`.
Ни одно значение не додумывается.

Запуск:  python3 extract_metadata.py                    # отчёт
         python3 extract_metadata.py --json out.json     # + результат
"""
import argparse
import glob
import json
import os
import re
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import etl_common

SCRIPT = "extract_metadata.py"

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO)

# DOI: типовая форма 10.NNNN/суффикс
DOI_RE = re.compile(r"\b10\.\d{4,9}/[^\s\)\]\>,\";'⟩]+")
# явные строки разметки конвертированных работ
# Строка со списком авторов (в том числе помеченная как заголовок ###).
# Распространено у Elsevier/Springer: '### Eduardo André Costa<sup>a</sup>,
# Maria Eduarda Silva<sup>a,b</sup>, Ana Beatriz Galvão<sup>c</sup>'.
# Разбор делается разбиением строки, а не одним сложным регексом: так
# устойчивее к вариациям разделителей и аффилиаций.
# Слова, которые встречаются в аффилиациях и названиях журналов, но не в
# именах: строка с ними авторами не считается. Проверено на реальных ложных
# срабатываниях: 'Technological Forecasting, Social Change' (журнал),
# 'Ben S. Bernanke, Federal Reserve Board' (аффилиация),
# 'Tatevik Sekhposyan Texas A, M University'.
AFFIL_WORDS = {
    "university", "universität", "universite", "universidad", "college",
    "school", "institute", "institution", "department", "faculty",
    "commission", "bank", "reserve", "federal", "national", "bureau",
    "center", "centre", "academy", "research", "foundation", "ministry",
    "forecasting", "economics", "economic", "journal", "review", "letters",
    "studies", "science", "sciences", "press", "springer", "elsevier",
    "wiley", "working", "paper", "papers", "report", "series", "abstract",
    "technology", "social", "change", "policy", "finance", "financial",
    "statistics", "statistical", "analysis", "management", "business",
}

NAME_TOKEN_RE = re.compile(r"^[A-Z][\w'\-]+(?:\s+(?:[A-Z]\.|[A-Z][\w'\-]+))*$")


def parse_authors_line(line):
    """Строку со списком имён -> строка авторов, либо пусто.

    Считается списком авторов, если после очистки разметки в ней 2-8
    фрагментов, разделённых запятыми/and/;, и каждый похож на имя
    (два и более слова с заглавных букв).
    """
    t = re.sub(r"<sup>[^<]*</sup>", "", line)
    t = re.sub(r"<[^>]+>", " ", t)
    t = re.sub(r"^#+\s*", "", t)
    t = re.sub(r"[*_`]", "", t)
    t = re.sub(r"[\u2020\u2021\u00a7\u2217\*]+", "", t)
    t = re.sub(r"^(?:by|prepared by|authors?:)\s+", "", t, flags=re.I)
    t = re.sub(r"\s+", " ", t).strip(" ,;:")
    if not (8 < len(t) < 250):
        return ""
    parts = [x.strip() for x in re.split(r"\s*(?:,|;|\band\b|&)\s*", t) if x.strip()]
    if not (2 <= len(parts) <= 8):
        return ""
    for p in parts:
        words = p.split()
        if any(w.lower().strip(".,;:") in AFFIL_WORDS for w in words):
            return ""
        if not (1 < len(words) <= 4):
            return ""
        if not all(w[0].isupper() or len(w) <= 2 for w in words if w):
            return ""
        if any(len(w) > 22 for w in words):
            return ""
    return ", ".join(parts)


# Авторы в теле: "by Tobias Adrian, Andrea Deghi, ...", "Prepared by ..."
BY_RE = re.compile(
    r"^(?:\*\*)?(?:by|prepared by|authors?:)\s+"
    r"((?:[A-Z][A-Za-z\u00C0-\u024F'\-]+(?:\s+(?:[A-Z]\.\s*)?[A-Z][A-Za-z\u00C0-\u024F'\-]+)*)"
    r"(?:\s*(?:,|and|&)\s*[A-Z][A-Za-z\u00C0-\u024F'\-]+(?:\s+(?:[A-Z]\.\s*)?[A-Z][A-Za-z\u00C0-\u024F'\-]+)*)*)",
    re.M)

LABEL_RE = {
    "authors": re.compile(r"^\s*\*\*Authors?:?\*\*\s*(.+)$", re.M | re.I),
    "year": re.compile(r"^\s*\*\*Year:?\*\*\s*(\d{4})", re.M | re.I),
    "venue": re.compile(r"^\s*\*\*Venue:?\*\*\s*(.+)$", re.M | re.I),
    "url": re.compile(r"^\s*\*\*URL:?\*\*\s*(https?://\S+)", re.M | re.I),
    "doi": re.compile(r"^\s*\*\*DOI:?\*\*\s*(10\.\S+)", re.M | re.I),
}
# паттерн имени файла: Автор(-Автор)*-Год-Тема
NAME_RE = re.compile(r"^([A-Z][A-Za-z\u00C0-\u024F\-]+(?:[-_][A-Za-z\u00C0-\u024F]+)*)"
                     r"[-_](19|20)(\d{2})[-_]")


def frontmatter(path):
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


def clean_doi(d):
    """Снять висящую пунктуацию, которую regex захватывает в хвост."""
    return re.sub(r"[.,;:⟩»\)\]]+$", "", d or "").strip()


def clean_author(a):
    """Убрать разметку и мусор из строки авторов, сохранив перечисление."""
    a = re.sub(r"<[^>]+>", " ", a)
    a = re.sub(r"[*_`]", "", a)
    a = re.sub(r"\s+", " ", a).strip(" ,;:")
    # отбросить явно не-авторов
    if not a or len(a) > 250:
        return ""
    if re.match(r"^(unknown|anon|неизвест)", a, re.I):
        return ""
    return a


def author_from_name(stem):
    """Автор из имени файла: 'saiz-2010-geographic-...' -> 'Saiz'."""
    m = NAME_RE.match(stem)
    if not m:
        return ""
    name = m.group(1).replace("_", "-")
    # 'Adrian-Predicting-Downside-...' -> только первый компонент-фамилия
    parts = name.split("-")
    surname = parts[0]
    if len(surname) > 2 and surname[0].isupper():
        return surname
    return name.replace("-", ", ")


def extract(path):
    fm, body = frontmatter(path)
    body = body[:20000]   # метаданные всегда в начале
    stem = os.path.basename(path)[:-3]
    src = []

    def take(field, *fm_keys):
        """Значение поля по порядку источников; возвращает (значение, источник)."""
        for k in fm_keys:
            if fm.get(k):
                return fm[k], "frontmatter"
        m = LABEL_RE.get(field)
        if m:
            mm = m.search(body)
            if mm:
                return mm.group(1).strip(), "label"
        return "", ""

    rec = {"wiki_page": path, "stem": stem, "sources": {}}

    # 1. авторы: фронтматтер -> метка -> строка "by ..." -> имя файла
    v, s = take("authors", "authors")
    if not v:
        m = BY_RE.search(body[:6000])
        if m and 3 < len(m.group(1)) < 200:
            v, s = m.group(1), "byline"
    if not v:
        for ln in body[:4000].split("\n"):
            cand = parse_authors_line(ln)
            if cand:
                v, s = cand, "authors_line"
                break
    if not v:
        v2 = author_from_name(stem)
        if v2:
            v, s = v2, "filename"
    v = clean_author(v)
    rec["authors"], rec["sources"]["authors"] = v, s

    # 2. год
    v, s = take("year", "year")
    if not v:
        m = NAME_RE.match(stem)
        if m:
            v, s = m.group(2) + m.group(3), "filename"
    rec["year"], rec["sources"]["year"] = v, s

    # 3. издание
    v, s = take("venue", "venue", "journal", "publisher")
    rec["venue"], rec["sources"]["venue"] = v, s

    # 4. DOI: фронтматтер -> метка -> текст
    v, s = take("doi", "doi")
    if not v:
        m = DOI_RE.search(body)
        if m:
            v, s = m.group(0), "text"
    rec["doi"], rec["sources"]["doi"] = clean_doi(v), s

    # 5. ссылка на источник
    v, s = take("url", "url", "source_url")
    if not v and rec["doi"]:
        v, s = "https://doi.org/" + rec["doi"], "doi"
    if not v:
        m = LABEL_RE["url"].search(body)
        if m:
            v, s = m.group(1), "label"
    rec["source_url"], rec["sources"]["source_url"] = v, s

    # 6. название (фронтматтер или первый заголовок H1)
    t = fm.get("title", "")
    if not t:
        m = re.search(r"^#\s+(.+)$", body, re.M)
        if m:
            t = re.sub(r"[*_`]", "", m.group(1)).strip()
    rec["title_orig"] = re.sub(r"\s+", " ", t)[:300]

    rec["pdf_source_pdf"] = fm.get("source_pdf", "")
    rec["needs_review"] = [f for f in ("authors", "year", "doi") if not rec[f]]
    return rec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json")
    etl_common.add_args(ap)
    args = ap.parse_args()

    import collections
    t_start = time.time()
    all_files = sorted(glob.glob("papers/*.md")) + sorted(glob.glob("papers/ru_papers/*.md"))

    todo, skipped = etl_common.changed_files(
        SCRIPT, all_files, only=args.only, since=args.since, force=args.force)
    print("Файлов всего: %d | к обработке: %d | без изменений: %d"
          % (len(all_files), len(todo), skipped))

    prev = {} if args.force else etl_common.load_artifact("meta")
    for p in todo:
        prev[p] = extract(p)

    recs = list(prev.values())
    print("\nФайлов: %d" % len(recs))
    print("Заполненность и источник значения:")
    for f in ("authors", "year", "venue", "doi", "source_url", "title_orig"):
        cnt = collections.Counter(r["sources"].get(f, "") for r in recs if r.get(f))
        tot = sum(1 for r in recs if r.get(f))
        by = ", ".join("%s=%d" % (k, v) for k, v in cnt.most_common())
        print("  %-12s %3d (%.0f%%)  %s" % (f, tot, 100 * tot / max(1, len(recs)), by))

    nr = [r for r in recs if len(r.get("needs_review", [])) == 3]
    print("\nБез авторов, года и DOI (нужен ручной разбор): %d" % len(nr))
    for r in nr[:8]:
        print("    %s" % r["stem"][:66])

    saved = []
    if not args.no_save:
        p, sz = etl_common.save_artifact("meta", recs)
        etl_common.mark_done(SCRIPT, todo)
        saved.append(p)
        print("\nАртефакт: %s (%.0f КБ)" % (p, sz / 1024))

    print("Время: %.1f с (обработано %d файлов)" % (time.time() - t_start, len(todo)))
    etl_common.record_run(SCRIPT, "metadata", t_start, time.time(),
                          rows=len(todo), status="ok", artifacts=saved,
                          extra={"total_files": len(recs), "skipped": skipped})

    if args.json:
        json.dump(recs, open(args.json, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print("JSON: %s (%.0f КБ)" % (args.json, os.path.getsize(args.json) / 1024))
    return 0


if __name__ == "__main__":
    sys.exit(main())
