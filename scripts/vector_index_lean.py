#!/usr/bin/env python3
"""
Single-pass vector indexer — minimal memory.
Processes one file at a time, appends embeddings to pre-allocated file.
"""
import os, gc, json, time
from pathlib import Path
import numpy as np

WIKI_ROOT = Path("/home/lnr/research-wiki")
INDEX_DIR = WIKI_ROOT / "data" / "vector_index"
INDEX_DIR.mkdir(parents=True, exist_ok=True)

EMBED_DIM = 384
CHUNK_MAX = 1500
CHUNK_OVERLAP = 100

def chunk_text(text, max_chars=CHUNK_MAX, overlap=CHUNK_OVERLAP):
    if len(text) <= max_chars:
        return [text]
    chunks, start = [], 0
    while start < len(text):
        end = min(start + max_chars, len(text))
        if end < len(text):
            for i in range(end, max(start + max_chars // 2, end - 200), -1):
                if text[i] in '.!?\n':
                    end = i + 1
                    break
        chunks.append(text[start:end])
        start = end - overlap
        if start >= len(text):
            break
    return chunks

def extract_title(content, filepath):
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            for line in parts[1].split('\n'):
                if line.strip().startswith('title:'):
                    return line.split(':', 1)[1].strip().strip('"\'')
    for line in content.split('\n'):
        s = line.strip()
        if s.startswith('# ') and len(s) > 5:
            return s[2:].strip()
    return filepath.stem.replace('_', ' ')

def remove_frontmatter(content):
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            return parts[2].strip()
    return content

def get_type(filepath):
    rel = filepath.relative_to(WIKI_ROOT)
    mapping = {'papers': 'paper', 'queries': 'query', 'reviews': 'review',
               'concepts': 'concept', 'annotations': 'annotation'}
    return mapping.get(rel.parts[0], 'other')

def main():
    from sentence_transformers import SentenceTransformer
    
    # Collect files
    patterns = ['papers/*.md', 'papers/ru_papers/*.md', 'queries/*.md']
    md_files = []
    for p in patterns:
        md_files.extend(WIKI_ROOT.glob(p))
    md_files = sorted(set(f for f in md_files if not f.name.endswith('.bak')))
    print(f"Files: {len(md_files)}")
    
    # Count total chunks first (just count, don't store text)
    total_chunks = 0
    file_chunk_counts = []
    for fp in md_files:
        try:
            content = fp.read_text(encoding='utf-8', errors='ignore')
            body = remove_frontmatter(content)
            n = len(chunk_text(body))
            file_chunk_counts.append((fp, n))
            total_chunks += n
        except:
            file_chunk_counts.append((fp, 0))
    
    print(f"Total chunks: {total_chunks}")
    print(f"Memmap size: {total_chunks * EMBED_DIM * 4 / 1024 / 1024:.1f} MB")
    
    # Pre-allocate memmap
    emb_path = INDEX_DIR / "embeddings.npy"
    emb = np.memmap(str(emb_path), dtype=np.float32, mode='w+',
                    shape=(total_chunks, EMBED_DIM))
    
    # Load model
    print("Loading model...")
    model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2', device='cpu')
    print("Model loaded")
    
    # Process files one at a time
    meta = []
    offset = 0
    t0 = time.time()
    files_done = 0
    
    for fp, n_chunks in file_chunk_counts:
        if n_chunks == 0:
            continue
        try:
            content = fp.read_text(encoding='utf-8', errors='ignore')
            body = remove_frontmatter(content)
            title = extract_title(content, fp)
            ftype = get_type(fp)
            rel = str(fp.relative_to(WIKI_ROOT))
            chunks = chunk_text(body)
            
            # Embed this file's chunks (batch_size=8 for low memory)
            embs = model.encode(chunks, batch_size=8, show_progress_bar=False,
                               convert_to_numpy=True, normalize_embeddings=True)
            
            # Write to memmap
            for j in range(len(chunks)):
                emb[offset + j] = embs[j]
                meta.append({
                    'filepath': rel, 'filename': fp.name, 'type': ftype,
                    'title': title[:200], 'chunk_id': j, 'total_chunks': len(chunks),
                    'text_preview': chunks[j][:300]
                })
            
            offset += len(chunks)
            files_done += 1
            del content, body, chunks, embs
            
            if files_done % 20 == 0:
                elapsed = time.time() - t0
                pct = files_done / len(md_files) * 100
                print(f"  {files_done}/{len(md_files)} files ({pct:.0f}%) — {offset} chunks — {elapsed:.0f}s")
                gc.collect()
                
        except Exception as e:
            print(f"  SKIP {fp.name}: {e}")
    
    emb.flush()
    del emb
    gc.collect()
    
    # Save metadata
    with open(INDEX_DIR / "metadata.json", 'w', encoding='utf-8') as f:
        json.dump(meta, f, ensure_ascii=False, separators=(',', ':'))
    
    with open(INDEX_DIR / "config.json", 'w') as f:
        json.dump({
            'dim': EMBED_DIM, 'count': offset,
            'chunk_max': CHUNK_MAX, 'chunk_overlap': CHUNK_OVERLAP,
            'model': 'paraphrase-multilingual-MiniLM-L12-v2',
            'created': time.strftime('%Y-%m-%d %H:%M')
        }, f, indent=2)
    
    elapsed = time.time() - t0
    print(f"\nDone: {offset} chunks from {files_done} files in {elapsed:.0f}s")
    print(f"Embeddings: {emb_path} ({os.path.getsize(emb_path)/1024/1024:.1f} MB)")
    print(f"Metadata: {os.path.getsize(INDEX_DIR / 'metadata.json')/1024:.0f} KB")

if __name__ == '__main__':
    main()