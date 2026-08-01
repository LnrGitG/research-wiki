#!/usr/bin/env python3
"""
Batch translation of research papers EN → RU for wiki.
Usage: python translate_papers.py [--dry-run] [--limit N] [--file FILE]
"""

import os, sys, glob, json, time, argparse, shutil
from pathlib import Path

# OpenRouter config
API_KEY = os.environ.get("OPENROUTER_API_KEY", "")
if not API_KEY:
    env_file = os.path.expanduser("~/.hermes/.env")
    with open(env_file) as f:
        for line in f:
            if line.startswith("OPENROUTER_API_KEY=") and not line.startswith("OPENROUTER_API_KEY=#"):
                API_KEY = line.strip().split("=", 1)[1]
                break

BASE_URL = "https://openrouter.ai/api/v1"
MODEL = "qwen/qwen3.6-35b-a3b"
MODEL_PROVIDER = "openrouter"
BASE_DIR = os.path.expanduser("~/research-wiki/papers")

def is_english_file(path):
    """Check if file is English (>15% latin, <5% cyrillic)."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        return False
    cyrillic = sum(1 for c in content if '\u0400' <= c <= '\u04ff')
    latin = sum(1 for c in content if ('a' <= c <= 'z') or ('A' <= c <= 'Z'))
    total = len(content) if content else 1
    # Must have >15% latin AND <5% cyrillic AND >1000 latin chars
    return latin / total > 0.15 and cyrillic / total < 0.05 and latin > 1000

def translate_chunk(text, system_prompt, max_retries=3):
    """Translate text chunk via OpenRouter API with retry."""
    import urllib.request
    
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Переведи следующий академический текст на русский язык:\n\n{text}"}
        ],
        "temperature": 0.3,
        "max_tokens": 48000
    }
    
    req = urllib.request.Request(
        f"{BASE_URL}/chat/completions",
        data=json.dumps(payload).encode('utf-8'),
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://localhost",
            "X-Title": "Wiki Paper Translation"
        },
        method="POST"
    )
    
    last_error = None
    for attempt in range(max_retries):
        try:
            with urllib.request.urlopen(req, timeout=180) as resp:
                raw = resp.read().decode('utf-8')
                if not raw.strip():
                    last_error = "Empty response body"
                    time.sleep(2 ** attempt)
                    continue
                result = json.loads(raw)
                if 'choices' not in result or not result['choices']:
                    last_error = f"No choices in response: {raw[:200]}"
                    time.sleep(2 ** attempt)
                    continue
                content = result['choices'][0]['message']['content']
                if not content:
                    last_error = "Empty content in response"
                    time.sleep(2 ** attempt)
                    continue
                return content
        except Exception as e:
            status_code = getattr(e, 'code', None)
            if status_code == 429:
                wait = 5 * (attempt + 1)
                print(f"      Rate limit (429), retrying in {wait}s...")
                time.sleep(wait)
                continue
            last_error = f"HTTP {status_code}: {getattr(e, 'reason', str(e))}"
            time.sleep(2 ** attempt)
    
    return f"ERROR: {last_error}"

def smart_split(text, max_chars=25000):
    """Split text at paragraph boundaries, respecting max size."""
    if len(text) <= max_chars:
        return [text]
    
    chunks = []
    current = ""
    for para in text.split('\n\n'):
        if len(current) + len(para) + 2 > max_chars and current:
            chunks.append(current.strip())
            current = para + '\n\n'
        else:
            current += para + '\n\n'
    if current.strip():
        chunks.append(current.strip())
    return chunks

def translate_file(src_path, dry_run=False):
    """Translate a single paper file."""
    basename = os.path.basename(src_path)
    ru_path = src_path.replace('.md', '.RU.md')
    
    if os.path.exists(ru_path):
        return "SKIP", f"Already translated: {basename}"
    
    # Safety: skip Russian/mixed files
    try:
        with open(src_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return "ERROR", f"Cannot read {basename}: {e}"
    
    cyrillic = sum(1 for c in content if '\u0400' <= c <= '\u04ff')
    latin = sum(1 for c in content if ('a' <= c <= 'z') or ('A' <= c <= 'Z'))
    total = len(content) if content else 1
    if latin / total <= 0.15 or cyrillic / total >= 0.05 or latin <= 1000:
        return "SKIP", f"Not English (<15% latin or >5% cyrillic or <1000 latin): {basename}"
    
    if not content.strip():
        return "SKIP", f"Empty file: {basename}"
    
    print(f"  Translating: {basename} ({len(content)/1024:.1f} KB)...")
    
    if dry_run:
        return "DRY_RUN", f"Would translate {basename} ({len(content)} chars)"
    
    # System prompt with glossary
    system_prompt = """You are a professional academic translator. Translate English academic papers to Russian.

RULES:
- Preserve ALL markdown formatting: ##, **, |, ---, <sup>, <br>
- PRESERVE (never translate): formulas, tables data, references, ARIMA/VAR/MIDAS/GARCH, RMSE/R², nowcasting, Diebold-Mariano, Big Data, DFM, Kalman filter
- forecast/forecasting → прогноз/прогнозировать (NEVER "предсказывать")
- predict → прогнозировать (in economic context)
- nowcasting → nowcasting
- robustness → робастность
- benchmark → базовая модель / бенчмарк
- unemployment → безработица
- Google Trends → Google Trends
- Translate all section headings, body paragraphs, abstracts, figure captions
- Keep YAML frontmatter structure, translate only 'title' field
- Preserve footnotes (digit + space) and blockquotes
"""
    
    # Split if too large
    chunks = smart_split(content, max_chars=28000)
    
    translated_parts = []
    for i, chunk in enumerate(chunks):
        if len(chunks) > 1:
            print(f"    Chunk {i+1}/{len(chunks)} ({len(chunk)} chars)...")
        
        result = translate_chunk(chunk, system_prompt)
        if result.startswith("ERROR:"):
            return "ERROR", f"Chunk {i+1} failed for {basename}: {result}"
        
        translated_parts.append(result)
        
        if i < len(chunks) - 1:
            time.sleep(2)  # rate limit缓冲
    
    # Write output
    output = '\n\n'.join(translated_parts)
    with open(ru_path, 'w', encoding='utf-8') as f:
        f.write(output)
    
    return "OK", f"Translated {basename} -> {os.path.basename(ru_path)}"

def main():
    parser = argparse.ArgumentParser(description='Translate wiki papers EN→RU')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be translated')
    parser.add_argument('--limit', type=int, default=None, help='Max files to translate')
    parser.add_argument('--file', type=str, default=None, help='Translate single file')
    parser.add_argument('--size-limit', type=int, default=200, help='Max file size in KB')
    args = parser.parse_args()
    
    # Find files
    if args.file:
        files = [os.path.join(BASE_DIR, args.file)]
    else:
        files = sorted(glob.glob(os.path.join(BASE_DIR, "*.md")))
        files = [f for f in files if not f.endswith('.bak') and not f.endswith('.RU.md')]
        files = [f for f in files if is_english_file(f)]
        files = [f for f in files if os.path.getsize(f) / 1024 <= args.size_limit]
    
    print(f"Found {len(files)} files to translate")
    if not files:
        print("No files found.")
        return
    
    if args.limit:
        files = files[:args.limit]
        print(f"Limited to first {args.limit} files")
    
    # Stats
    total_size = sum(os.path.getsize(f) for f in files)
    print(f"Total size: {total_size/1024/1024:.1f} MB")
    print()
    
    # Translate
    results = {"OK": 0, "SKIP": 0, "ERROR": 0, "DRY_RUN": 0}
    
    for i, f in enumerate(files, 1):
        print(f"[{i}/{len(files)}]", end=" ")
        status, msg = translate_file(f, dry_run=args.dry_run)
        results[status] = results.get(status, 0) + 1
        print(f"  [{status}] {msg}")
        
        if status == "OK" and i < len(files):
            time.sleep(3)  # rate limit between files
    
    print()
    print("=" * 50)
    print("SUMMARY:")
    for k, v in results.items():
        if v:
            print(f"  {k}: {v}")
    print("=" * 50)

if __name__ == "__main__":
    main()
