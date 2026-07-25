#!/usr/bin/env python3
"""Cheap integrity checks for the research wiki.

Default mode is non-blocking: content debt (broken links, missing index entries,
missing catalog cards) is reported as warnings. Use --strict to turn broken
wikilinks into exit-code problems after the baseline is cleaned.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPERS = ROOT / "raw" / "papers"
# Workpapers is intentionally gitignored in this vault; keep it out of default lint/convert.
SKIP_DIRS = {".git", ".obsidian", "_archive", "Workpapers"}
PAGE_DIRS = ["entities", "concepts", "comparisons", "queries"]
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")

problems: list[str] = []
warnings: list[str] = []


def md_files(base: Path) -> list[Path]:
    if not base.exists():
        return []
    return [
        p
        for p in base.rglob("*.md")
        if not any(part in SKIP_DIRS for part in p.parts)
    ]


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return ""


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true", help="Fail on broken wikilinks too")
    args = parser.parse_args()

    for required in ["SCHEMA.md", "index.md", "log.md"]:
        if not (ROOT / required).exists():
            problems.append(f"missing required file: {required}")

    catalog = PAPERS / "_catalog.md"
    catalog_text = read(catalog)
    if not catalog.exists():
        problems.append("missing raw/papers/_catalog.md")

    pdfs = [
        p
        for p in PAPERS.rglob("*.pdf")
        if not any(part in SKIP_DIRS for part in p.parts)
    ] if PAPERS.exists() else []
    raw_mds = [p for p in md_files(PAPERS) if p.name != "_catalog.md"]

    for pdf in pdfs:
        if not pdf.with_suffix(".md").exists():
            problems.append(f"PDF without extracted markdown: {rel(pdf)}")

    for md in raw_mds:
        if md.stat().st_size < 200:
            warnings.append(f"very small extracted markdown (check image-only/error page): {rel(md)}")
        if catalog_text and md.name not in catalog_text:
            warnings.append(f"raw markdown missing catalog card: {rel(md)}")
        if not md.with_suffix(".pdf").exists():
            warnings.append(f"markdown has no sibling PDF (ok for web sources, check provenance): {rel(md)}")

    all_md = md_files(ROOT)
    stems = {p.stem for p in all_md}
    rel_no_ext = {str(p.relative_to(ROOT).with_suffix("")) for p in all_md}

    index_text = read(ROOT / "index.md")
    for page_dir in PAGE_DIRS:
        for page in md_files(ROOT / page_dir):
            if page.name.startswith("_"):
                continue
            if f"[[{page.stem}" not in index_text and str(page.relative_to(ROOT).with_suffix("")) not in index_text:
                warnings.append(f"page not listed in index.md: {rel(page)}")

    link_check_files = [ROOT / "index.md"]
    for page_dir in PAGE_DIRS:
        link_check_files.extend(md_files(ROOT / page_dir))

    for page in link_check_files:
        if not page.exists():
            continue
        text = read(page)
        for match in WIKILINK_RE.finditer(text):
            target = match.group(1).strip()
            if not target or target.startswith(("http://", "https://")):
                continue
            target_stem = Path(target).stem
            if target not in rel_no_ext and target_stem not in stems:
                message = f"broken wikilink in {rel(page)}: [[{target}]]"
                if args.strict:
                    problems.append(message)
                else:
                    warnings.append(message)

    log_path = ROOT / "log.md"
    if log_path.exists():
        entries = sum(1 for line in read(log_path).splitlines() if line.startswith("## ["))
        if entries > 500:
            warnings.append(f"log.md has {entries} entries; rotate to log-YYYY.md")

    print(f"wiki_lint root={ROOT} strict={args.strict}")
    print(f"problems={len(problems)} warnings={len(warnings)}")
    for item in problems[:100]:
        print(f"PROBLEM {item}")
    for item in warnings[:100]:
        print(f"WARN {item}")
    if len(problems) > 100:
        print(f"... {len(problems) - 100} more problems")
    if len(warnings) > 100:
        print(f"... {len(warnings) - 100} more warnings")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
