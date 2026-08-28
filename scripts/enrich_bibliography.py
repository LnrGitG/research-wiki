#!/usr/bin/env python3
"""Enrich bibliography.json with links to wiki papers citing each entry + DOI link.

For each bibliography entry:
- find wiki documents whose References section contains the entry's normalized text
- extract DOI -> https://doi.org/... link
Output: docs/bibliography.json with added fields: cites (list of viewer paths),
        cite_titles (list of doc titles), doi (or '')
"""
import glob
import json
import os
import re
from collections import defaultdict

ROOT = os.path.join(os.path.dirname(__file__), "..")
OUT = os.path.join(ROOT, "docs/bibliography.json")
PAPERS = (
    glob.glob(os.path.join(ROOT, "papers/*.md"))
    + glob.glob(os.path.join(ROOT, "papers/ru_papers/*.RU.md"))
)


def norm(s):
    """Normalize for matching: no truncation here (truncation applied to probes only)."""
    s = s.lower()
    s = re.sub(r"<[^>]+>", "", s)          # strip html
    s = re.sub(r"\(?\d*\s*иссл\.\)\s*$", "", s)  # trailing citation-count marker
    # latin-only normalization: russian refs handled by cyrillic pass below
    s = s.replace("ё", "е").replace("—", " ").replace("–", " ").replace("‑", " ")
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return " ".join(s.split())


def norm_ru(s):
    s = s.lower()
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"[^a-zа-яё0-9]+", " ", s)
    return " ".join(s.split())


def refs_section(text):
    m = re.search(r"^#{1,3}\s*\**\s*(references|библиография|литература)\b.*$", text, re.M | re.I)
    if not m:
        return ""
    return text[m.end():]


def fulltext_norm(text):
    """Normalized full text (latin pass) - fallback when refs section not found."""
    return norm(text)


def main():
    bib = json.load(open(OUT, encoding="utf-8"))
    # normalized index of bib entries
    bib_norm = [norm(e["text"]) for e in bib]

    # map: bib index -> set of citing docs
    cites = [set() for _ in bib]
    cite_titles = [dict() for _ in bib]

    for path in PAPERS:
        rel = os.path.relpath(path, ROOT)
        try:
            text = open(path, encoding="utf-8", errors="replace").read()
        except Exception:
            continue
        # full-text matching: a wiki doc "cites" the entry if its normalized text
        # (inline citations or refs section) contains the entry's normalized prefix
        hay_latin = norm(text)
        hay_cyr = norm_ru(text)
        mt = re.search(r"^#{1,2} (.+)$", text, re.M)
        title = mt.group(1)[:80] if mt else os.path.basename(rel)
        for i, e in enumerate(bib):
            nb = norm(e["text"]) if e.get("lang") != "ru" else norm_ru(e["text"])
            if not nb:
                continue
            haystack = hay_latin if e.get("lang") != "ru" else hay_cyr
            probe = nb[:60]
            if probe in haystack:
                cites[i].add(rel)
                cite_titles[i][rel] = title

    n_linked = 0
    for i, e in enumerate(bib):
        # DOI link
        m = re.search(r"10\.\d{4,9}/[-._;()/:A-Za-z0-9]+", e["text"].rstrip(". "))
        doi = m.group(0).rstrip(".") if m else ""
        e["doi"] = doi
        e["cites"] = sorted(cites[i])
        e["cite_titles"] = [cite_titles[i][k] for k in sorted(cites[i])][:5]
        if cites[i]:
            n_linked += 1
    json.dump(bib, open(OUT, "w", encoding="utf-8"), ensure_ascii=False)
    print(f"OK: {n_linked}/{len(bib)} entries linked to citing wiki docs -> {OUT} ({os.path.getsize(OUT)/1024:.0f} KB)")


if __name__ == "__main__":
    main()