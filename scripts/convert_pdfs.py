#!/usr/bin/env python3
"""Idempotent PDF -> markdown conversion for raw/papers.

Default: convert every PDF under <wiki>/raw/papers that has no sibling .md.
Skips legacy/ignored folders. Does not OCR. Flags suspicious files for review.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Workpapers is intentionally gitignored in this vault; keep it out of default lint/convert.
SKIP_DIRS = {".git", ".obsidian", "_archive", "Workpapers"}


def iter_pdfs(root: Path, recursive: bool = True):
    paths = root.rglob("*.pdf") if recursive else root.glob("*.pdf")
    for path in sorted(paths):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        yield path


def classify_pdf(pdf: Path) -> str:
    try:
        import fitz  # PyMuPDF

        doc = fitz.open(str(pdf))
        if doc.page_count == 0:
            return "empty-pdf"
        first = doc[0]
        text = (first.get_text() or "").strip()
        images = first.get_images(full=True)
        lowered = text.lower()
        if "access denied" in lowered or "you don't have permission" in lowered:
            return "error-page"
        if not text and images:
            return "image-only"
        return "ok"
    except Exception as exc:  # pragma: no cover - diagnostic only
        return f"check-failed:{type(exc).__name__}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "root",
        nargs="?",
        default=str(Path(__file__).resolve().parents[1] / "raw" / "papers"),
        help="Folder with PDFs (default: <wiki>/raw/papers)",
    )
    parser.add_argument("--no-recursive", action="store_true", help="Only convert PDFs directly in root")
    parser.add_argument("--force", action="store_true", help="Reconvert even if .md exists")
    parser.add_argument("--include-skipped", action="store_true", help="Also process skipped dirs such as Workpapers")
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    if not root.exists():
        print(f"FAIL: root does not exist: {root}")
        return 2

    try:
        import pymupdf4llm
    except Exception as exc:
        print("FAIL: pymupdf4llm is not available in this Python environment.")
        print("Hint: source ~/.hermes/hermes-agent/venv/bin/activate")
        print(str(exc))
        return 2

    if args.include_skipped:
        SKIP_DIRS.clear()
        SKIP_DIRS.update({".git", ".obsidian"})

    converted = skipped = failed = 0
    for pdf in iter_pdfs(root, recursive=not args.no_recursive):
        md = pdf.with_suffix(".md")
        if md.exists() and not args.force:
            skipped += 1
            continue
        try:
            text = pymupdf4llm.to_markdown(str(pdf))
            md.write_text(text, encoding="utf-8")
            flag = classify_pdf(pdf)
            size_kb = max(md.stat().st_size, 1) // 1024
            print(f"OK {pdf.relative_to(root)} -> {md.name} ({size_kb}KB) [{flag}]")
            converted += 1
        except Exception as exc:
            print(f"FAIL {pdf.relative_to(root)}: {type(exc).__name__}: {exc}")
            failed += 1

    print(f"SUMMARY converted={converted} skipped={skipped} failed={failed}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
