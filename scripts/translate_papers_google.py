#!/usr/bin/env python3
"""
Batch pipeline: PDF → .md (pymupdf4llm) → .RU.md (Google Translate)
Part of paper-translation skill. Free translation via Google Translate.

Usage:
  python3 scripts/translate_papers_google.py --dry-run --limit 5
  python3 scripts/translate_papers_google.py --limit 20
  python3 scripts/translate_papers_google.py --step extract-only --limit 50
  python3 scripts/translate_papers_google.py --step translate-only --limit 50
  python3 scripts/translate_papers_google.py                # all remaining
"""

import os, sys, time, argparse, subprocess, re
from pathlib import Path

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
PAPERS_DIR = os.path.expanduser("~/research-wiki/papers")
RAW_PAPERS_DIR = os.path.expanduser("~/research-wiki/raw/papers")
DATA_RAW_DIR = os.path.expanduser("~/research-wiki/data/raw")
CHUNK_SIZE = 4500  # Google Translate free limit ~5000 chars, keep margin
DELAY_BETWEEN_CHUNKS = 0.3  # seconds
DELAY_BETWEEN_FILES = 1.0   # seconds

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def is_foreign_pdf(pdf_path):
    """Detect if PDF is in a foreign (non-Russian) language."""
    try:
        import fitz
        doc = fitz.open(str(pdf_path))
        if len(doc) == 0:
            return False
        sample = ""
        for i in range(min(2, len(doc))):
            sample += doc[i].get_text()
        doc.close()
        cyrillic = sum(1 for c in sample if '\u0400' <= c <= '\u04ff')
        latin = sum(1 for c in sample if c.isalpha() and c.isascii())
        return latin > 50 and not (cyrillic > 50 and cyrillic > latin * 0.3)
    except Exception:
        return False


def extract_pdf_to_md(pdf_path, md_path):
    """Extract PDF to markdown using pymupdf4llm."""
    try:
        import pymupdf4llm
        md_text = pymupdf4llm.to_markdown(str(pdf_path))
        
        # Add YAML frontmatter
        basename = os.path.basename(pdf_path)
        frontmatter = f"""---
title: {basename.replace('.pdf', '')}
type: paper
source_pdf: raw/papers/{basename}
converted: {time.strftime('%Y-%m-%d')}
---

"""
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(frontmatter + md_text)
        return len(md_text), None
    except Exception as e:
        return 0, str(e)


def split_chunks(text, max_chars=CHUNK_SIZE):
    """Split text at paragraph boundaries."""
    chunks = []
    current = ""
    for para in text.split("\n\n"):
        if len(current) + len(para) + 2 > max_chars and current:
            chunks.append(current.strip())
            current = para + "\n\n"
        else:
            current += para + "\n\n"
    if current.strip():
        chunks.append(current.strip())
    return chunks


def translate_text(text):
    """Translate text using Google Translate (free)."""
    from deep_translator import GoogleTranslator
    translator = GoogleTranslator(source='en', target='ru')
    
    chunks = split_chunks(text)
    translated_parts = []
    
    for i, chunk in enumerate(chunks):
        try:
            tr = translator.translate(chunk)
            translated_parts.append(tr)
        except Exception as e:
            # Retry once after delay
            time.sleep(2)
            try:
                tr = translator.translate(chunk)
                translated_parts.append(tr)
            except Exception as e2:
                print(f"    Chunk {i+1} failed: {e2}", flush=True)
                translated_parts.append(chunk)  # fallback to English
        if i < len(chunks) - 1:
            time.sleep(DELAY_BETWEEN_CHUNKS)
    
    return "\n\n".join(translated_parts)


def translate_md_file(md_path, ru_md_path):
    """Translate .md file to .RU.md."""
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if not content.strip():
        return 0, "empty file"
    
    # Extract frontmatter
    frontmatter = ""
    body = content
    if content.startswith("---"):
        end = content.find("---", 4)
        if end > 0:
            frontmatter = content[:end+3] + "\n\n"
            body = content[end+3:].strip()
    
    translated_body = translate_text(body)
    output = frontmatter + translated_body
    
    with open(ru_md_path, "w", encoding="utf-8") as f:
        f.write(output)
    
    return len(output), None


def collect_foreign_pdfs():
    """Find all foreign-language PDFs across raw/papers and data/raw."""
    pdfs = []
    for d in [RAW_PAPERS_DIR, DATA_RAW_DIR]:
        if os.path.isdir(d):
            for f in Path(d).rglob("*.pdf"):
                if is_foreign_pdf(f):
                    pdfs.append(str(f))
    return sorted(set(pdfs))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description='Batch PDF→MD→RU.MD via Google Translate')
    parser.add_argument('--dry-run', action='store_true', help='Preview without translating')
    parser.add_argument('--limit', type=int, default=None, help='Max files to process')
    parser.add_argument('--step', choices=['all', 'extract-only', 'translate-only'], 
                        default='all', help='Which step to run')
    parser.add_argument('--file', type=str, default=None, help='Process single PDF path')
    args = parser.parse_args()

    # Collect PDFs
    if args.file:
        pdfs = [args.file]
    else:
        pdfs = collect_foreign_pdfs()
    
    print(f"Found {len(pdfs)} foreign PDFs", flush=True)
    
    # Filter: which need extraction, which need translation
    to_extract = []
    to_translate = []
    already_done = 0
    
    for pdf in pdfs:
        stem = Path(pdf).stem
        md_path = os.path.join(PAPERS_DIR, stem + ".md")
        ru_md_path = os.path.join(PAPERS_DIR, stem + ".RU.md")
        
        has_md = os.path.exists(md_path) and os.path.getsize(md_path) > 100
        has_ru = os.path.exists(ru_md_path) and os.path.getsize(ru_md_path) > 100
        
        if has_ru:
            already_done += 1
            continue
        
        if not has_md:
            to_extract.append((pdf, md_path, ru_md_path))
        else:
            to_translate.append((pdf, md_path, ru_md_path))
    
    print(f"  Already translated: {already_done}", flush=True)
    print(f"  Need extraction: {len(to_extract)}", flush=True)
    print(f"  Need translation only: {len(to_translate)}", flush=True)
    
    # Apply limit
    work_list = []
    if args.step in ('all', 'extract-only'):
        work_list.extend(to_extract)
    if args.step in ('all', 'translate-only'):
        work_list.extend(to_translate)
    
    if args.limit:
        work_list = work_list[:args.limit]
    
    print(f"  Will process: {len(work_list)}", flush=True)
    
    if args.dry_run:
        for pdf, md, ru in work_list[:20]:
            name = os.path.basename(pdf)[:60]
            print(f"  [DRY] {name}")
        if len(work_list) > 20:
            print(f"  ... and {len(work_list)-20} more")
        return
    
    if not work_list:
        print("Nothing to do.")
        return
    
    # Process
    results = {"ok": 0, "error": 0, "skip": 0}
    start_time = time.time()
    
    for i, (pdf, md_path, ru_md_path) in enumerate(work_list, 1):
        name = os.path.basename(pdf)[:60]
        print(f"\n[{i}/{len(work_list)}] {name}", flush=True)
        
        # Step 1: Extract if needed
        if args.step in ('all', 'extract-only') and not os.path.exists(md_path):
            print(f"  Extracting PDF→MD...", flush=True)
            t0 = time.time()
            n_chars, err = extract_pdf_to_md(pdf, md_path)
            if err:
                print(f"  ERROR extraction: {err}", flush=True)
                results["error"] += 1
                continue
            print(f"  Extracted {n_chars:,} chars in {time.time()-t0:.1f}s", flush=True)
            if args.step == 'extract-only':
                results["ok"] += 1
                continue
        
        # Step 2: Translate
        if args.step in ('all', 'translate-only'):
            if not os.path.exists(md_path) or os.path.getsize(md_path) < 100:
                print(f"  SKIP: no .md file", flush=True)
                results["skip"] += 1
                continue
            
            print(f"  Translating MD→RU.MD...", flush=True)
            t0 = time.time()
            n_chars, err = translate_md_file(md_path, ru_md_path)
            if err:
                print(f"  ERROR translation: {err}", flush=True)
                results["error"] += 1
                continue
            print(f"  Translated → {n_chars:,} chars in {time.time()-t0:.1f}s", flush=True)
            results["ok"] += 1
        
        if i < len(work_list):
            time.sleep(DELAY_BETWEEN_FILES)
    
    elapsed = time.time() - start_time
    print(f"\n{'='*60}")
    print(f"SUMMARY (in {elapsed:.0f}s)")
    print(f"  OK:    {results['ok']}")
    print(f"  ERROR: {results['error']}")
    print(f"  SKIP:  {results['skip']}")
    print(f"  Remaining: {len(work_list) - results['ok'] - results['error'] - results['skip']}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()