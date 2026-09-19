#!/usr/bin/env python3
"""Извлечение списков литературы из корпуса (фаза 3).

Разбирает секцию `references` / `источники` / `литература` в массив
записей. Каждая запись — объект: {текст, авторы, год, издание, doi, url}.

Форматы в корпусе различаются (проверено на выборке):

  1. список с дефисом:  `- Akaike, H., 1974. A new look at ...`
  2. сплошной текст:    `Arbolino, R., & Di Caro, P. (2021). Can the EU ...`
     — записи разделены только началом новой фамилии, поэтому разбиваются
     по позициям «Заглавная фамилия, инициал(ы), год»;
  3. нумерованный:      `[1] Autor (2020) ...` / `1. Autor (2020) ...`

Разбиение делается поиском НАЧАЛ записей, а не разделителей: разделители
внутри записи (запятые, точки) не отличаются от межзаписных, поэтому
надёжнее искать начало следующей фамилии.

Внешнее подтверждение (Crossref) НЕ делается — только то, что есть в тексте.
DOI и URL извлекаются из самой записи, если присутствуют.

Запуск:  python3 extract_references.py                    # отчёт
         python3 extract_references.py --json out.json    # + результат
"""
import argparse
import collections
import glob
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO)

REF_HEAD_RE = re.compile(
    r"^#{0,4}\s*[*_<u>\s]*((?:\d+[\.\s]*)?(?:references?|bibliograph\w*|"
    r"источник\w*|литератур\w*|список\s+использованн\w*|литература))\s*[*_<>\s]*$",
    re.M | re.I)

# Начало записи: 'Фамилия, И. ...' либо 'Фамилия, И., 2019.' либо '[1] Фамилия'
ENTRY_START_RE = re.compile(
    r"(?:^|\n)\s*(?:(?:-|–|—|\*|\+)\s*|\[\d+\]\s*|(?<!\d)\d{1,3}[\.\)]\s*)*"
    r"(?P<surname>[A-ZА-ЯЁ][A-Za-zА-Яа-яЁё'\-]{1,24})"
    r"(?:,\s*[A-ZА-ЯЁ]\.(?:\s*[-–]?\s*[A-ZА-ЯЁ]\.)?)?"   # инициалы, если есть
    r"[^\n]{0,400}?\(?(?P<year>(?:19|20)\d{2})[a-z]?\)?",
    re.M)

DOI_RE = re.compile(r"\b10\.\d{4,9}/[^\s\)\]\>,\";'⟩]+")
URL_RE = re.compile(r"https?://[^\s\)\]\>,\";'⟩]+")

# Префиксы, которыми начинается текст рисунков/приложений, а не запись
# литературы: такие фрагменты нередко оказываются внутри секции references.
JUNK_PREFIX = re.compile(
    r"^(?:panel\s+[ab]|figure|fig\.|table|chart|comparison|suppose|note[:.]|"
    r"source[:.]|appendix|where\s+[A-Z]|proof\b|lemma|theorem|corollary|"
    r"legend|preferences|housing\s+construction|the\s+elasticity|"
    r"the\s+correlation|the\s+price|the\s+share|the\s+value|"
    r"this\s+figure|these\s+are|all\s+variables|for\s+a\s+definition)",
    re.I)

# Слова, не являющиеся фамилией в начале записи (продолжения текста)
NOT_SURNAME = {
    "the", "in", "and", "of", "for", "with", "working", "paper", "no", "vol",
    "journal", "review", "economics", "economic", "department", "university",
    "retrieved", "available", "from", "http", "https", "www", "figure", "table",
    "source", "note", "data", "results", "this", "that", "see", "also", "ed",
    "eds", "press", "pp", "cf", "ibid", "et", "al",
}


def body_of(path):
    s = open(path, encoding="utf-8", errors="ignore").read()
    if s.startswith("---") and s.count("---") >= 2:
        return s.split("---", 2)[2]
    return s


def ref_section(body, maxlen=120000):
    """Текст от заголовка литературы до конца или до явного приложения."""
    m = REF_HEAD_RE.search(body)
    if not m:
        return ""
    tail = body[m.end():]
    stop = re.search(r"\n#{1,3}\s*(?:appendix|приложени|annex)\w*", tail, re.I)
    if stop:
        tail = tail[:stop.start()]
    return tail[:maxlen]


def split_entries(text):
    """Текст секции -> список записей, разбиением по началам записей."""
    starts = []
    for m in ENTRY_START_RE.finditer(text):
        sur = m.group("surname")
        if sur.lower() in NOT_SURNAME:
            continue
        # отбросить совпадения глубоко внутри предложения: начало записи
        # либо в начале строки, либо после маркера списка (-, [N], N.) или
        # заглавной точки предыдущей записи
        # между началом совпадения и фамилией допустим только маркер списка
        # ('- ', '[12] ', '12. ') и/или пробелы с переносами
        gap = text[m.start():m.start("surname")]
        if not re.fullmatch(r"[\s\-–—\*\+\[\]\d\.\)]*", gap):
            continue
        starts.append(m.start("surname"))

    if not starts:
        return []

    starts = sorted(set(starts))
    entries = []
    for i, st in enumerate(starts):
        en = starts[i + 1] if i + 1 < len(starts) else len(text)
        raw = re.sub(r"\s+", " ", text[st:en]).strip(" -–—,;:")
        if not (25 < len(raw) < 1200):
            continue
        if JUNK_PREFIX.match(raw):
            continue
        # год в библиографической записи стоит у начала (после авторов);
        # если он глубоко в тексте — это фрагмент абзаца, а не запись
        y = re.search(r"\b(?:19|20)\d{2}\b", raw)
        if not y:
            continue
        # год у начала (IEEE/Elsevier) ЛИБО запись с названием в кавычках —
        # формат NBER/AER, где год стоит в конце
        if y.start() > 220 and not re.search(r"[\u201c\"]", raw):
            continue
        entries.append(raw)
    return entries


def parse_entry(raw):
    """Запись -> объект с полями. Ничего не додумывается."""
    rec = {"текст": raw, "авторы": "", "год": "", "издание": "", "doi": "", "url": ""}

    y = re.search(r"\b((?:19|20)\d{2})[a-z]?\b", raw)
    if y:
        rec["год"] = y.group(1)

    # формат NBER/AER: 'Авторы, "Название в кавычках", издание, год.'
    q = re.match(r"^(.{5,300}?)\s*[\u201c\"]", raw)
    if q:
        au = re.sub(r"\s+", " ", q.group(1)).strip(" ,;:&.\u201d\"*")
        au = re.sub(r"[*\u2020\u2021]+$", "", au).strip()
        if 3 < len(au) < 250:
            rec["авторы"] = au

    # авторы — текст от начала записи до года; год отделяется ", 1974",
    # " (2020)", ". 2009" и т.п. Отсекаем служебные префиксы.
    a = None if rec["авторы"] else re.match(r"^(.{3,250}?)[\s,;.]+\(?((?:19|20)\d{2})", raw)
    if a:
        au = re.sub(r"\s+", " ", a.group(1)).strip(" ,;:&.\u201d\"*")
        au = re.sub(r"[*\u2020\u2021]+$", "", au).strip()
        au = re.sub(r"^(?:and|&)\s+", "", au, flags=re.I)
        if 2 < len(au) < 140:
            rec["авторы"] = au

    d = DOI_RE.search(raw)
    if d:
        rec["doi"] = re.sub(r"[.,;:⟩»\)\]]+$", "", d.group(0))

    u = URL_RE.search(raw)
    if u:
        rec["url"] = re.sub(r"[.,;:⟩»\)\]]+$", "", u.group(0))
    elif rec["doi"]:
        rec["url"] = "https://doi.org/" + rec["doi"]

    # издание: фрагмент между годом-точкой и страницами/URL
    m = re.search(r"(?:19|20)\d{2}[a-z]?[\.\)]\s*(.{5,110}?)"
                  r"(?:\s+\d+\s*[\(\[][^\)\]]*[\)\]]|\s+\d+[-–]\d+|\s*https?:|\s*doi:|$)", raw)
    if m:
        rec["издание"] = re.sub(r"\s+", " ", m.group(1)).strip(" .,;:_")

    return rec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json")
    args = ap.parse_args()

    papers = sorted(glob.glob("papers/*.md"))
    out = []
    stats = collections.Counter()

    for p in papers:
        sec = ref_section(body_of(p))
        if not sec:
            out.append({"wiki_page": p, "stem": os.path.basename(p)[:-3],
                        "n_refs": 0, "refs": [], "has_ref_section": False})
            continue
        raw_entries = split_entries(sec)
        refs = [parse_entry(r) for r in raw_entries]
        with_doi = sum(1 for r in refs if r["doi"])
        with_url = sum(1 for r in refs if r["url"])
        stats["секции"] += 1
        stats["записей"] += len(refs)
        stats["с DOI"] += with_doi
        stats["с URL"] += with_url
        out.append({"wiki_page": p, "stem": os.path.basename(p)[:-3],
                    "n_refs": len(refs), "refs": refs, "has_ref_section": True})

    total = sum(r["n_refs"] for r in out)
    print("Обработано статей: %d\n" % len(out))
    print("Секции литературы найдены: %d (%.0f%%)" % (stats["секции"], 100 * stats["секции"] / len(out)))
    print("Разобрано записей: %d" % total)
    if total:
        print("  с DOI: %d (%.0f%%)" % (stats["с DOI"], 100 * stats["с DOI"] / total))
        print("  с URL: %d (%.0f%%)" % (stats["с URL"], 100 * stats["с URL"] / total))

    dist = collections.Counter()
    for r in out:
        n = r["n_refs"]
        key = "0" if n == 0 else "1-19" if n < 20 else "20-49" if n < 50 else "50-99" if n < 100 else "100+"
        dist[key] += 1
    print("\nРаспределение по числу записей:")
    for k in ("0", "1-19", "20-49", "50-99", "100+"):
        print("  %-6s %d" % (k, dist[k]))

    print("\nПримеры разобранных записей:")
    shown = 0
    for r in out:
        if r["n_refs"] >= 8:
            print("\n--- %s (%d записей) ---" % (r["stem"][:52], r["n_refs"]))
            for e in r["refs"][:2]:
                print("  авторы: %s" % e["авторы"][:56])
                print("  год: %s | doi: %s" % (e["год"] or "—", e["doi"][:40] or "—"))
                print("  издание: %s" % e["издание"][:60] or "—")
            shown += 1
            if shown >= 3:
                break

    bad = [r for r in out if r["n_refs"] > 400]
    if bad:
        print("\nПодозрительно много записей (проверить разбиение):")
        for r in bad[:6]:
            print("  %-52s %d" % (r["stem"][:52], r["n_refs"]))

    if args.json:
        json.dump(out, open(args.json, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print("\nJSON: %s (%.0f КБ)" % (args.json, os.path.getsize(args.json) / 1024))
    return 0


if __name__ == "__main__":
    sys.exit(main())
