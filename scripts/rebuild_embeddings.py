#!/usr/bin/env python3
import os, json, base64, numpy as np, gc, re, sys
from sentence_transformers import SentenceTransformer

print("Loading model...", flush=True)
model = SentenceTransformer("paraphrase-MiniLM-L3-v2", device="cpu")
print("Model loaded.", flush=True)

# Gather all files
all_files = []
papers_dir = "/home/lnr/research-wiki/papers"
ru_dir = "/home/lnr/research-wiki/papers/ru_papers"
q_dir = "/home/lnr/research-wiki/queries"

for f in os.listdir(papers_dir):
    if f.endswith(".md"):
        all_files.append({"path": os.path.join(papers_dir, f), "file": f, "category": "paper", "url": f"https://github.com/LnrGitG/research-wiki/blob/main/papers/{f}"})
for f in os.listdir(ru_dir):
    if f.endswith(".RU.md"):
        all_files.append({"path": os.path.join(ru_dir, f), "file": f, "category": "paper_ru", "url": f"https://github.com/LnrGitG/research-wiki/blob/main/papers/ru_papers/{f}"})
for f in os.listdir(q_dir):
    if f.endswith(".md"):
        all_files.append({"path": os.path.join(q_dir, f), "file": f, "category": "query", "url": f"https://github.com/LnrGitG/research-wiki/blob/main/queries/{f}"})

print(f"Total files: {len(all_files)}", flush=True)

def chunk_text(text, chunk_size=1000, overlap=100):
    if len(text) <= chunk_size:
        return [text] if text.strip() else []
    chunks = []
    i = 0
    while i < len(text):
        chunk = text[i:i+chunk_size]
        if chunk.strip():
            chunks.append(chunk)
        i += chunk_size - overlap
    return chunks

def extract_title(text):
    for line in text.split("\n"):
        line = line.strip()
        if line and not line.startswith("---") and not line.startswith("#") and len(line) > 5:
            return line[:100]
    for line in text.split("\n"):
        if line.startswith("#"):
            return line.lstrip("#").strip()[:100]
    return "unknown"

def extract_abstract(text, max_len=200):
    text = re.sub(r"^---.*?---", "", text, flags=re.DOTALL)
    for line in text.split("\n"):
        line = line.strip()
        if len(line) > 30:
            return line[:max_len]
    return ""

metas = []
emb_list = []

for i, finfo in enumerate(all_files):
    try:
        with open(finfo["path"], "r", encoding="utf-8", errors="replace") as f:
            text = f.read()
        title = extract_title(text)
        abstract = extract_abstract(text)
        chunks = chunk_text(text)
        if not chunks:
            chunks = [text[:1000]]
        embs = model.encode(chunks, show_progress_bar=False, batch_size=4)
        doc_emb = np.mean(embs, axis=0).astype(np.float32)
        emb_list.append(doc_emb)
        metas.append({"t": title, "f": finfo["file"], "c": finfo["category"], "u": finfo["url"], "a": abstract})
        if (i + 1) % 50 == 0:
            print(f"  {i+1}/{len(all_files)}", flush=True)
            gc.collect()
    except Exception as e:
        emb_list.append(np.zeros(384, dtype=np.float32))
        metas.append({"t": finfo["file"], "f": finfo["file"], "c": finfo["category"], "u": finfo["url"], "a": f"Error: {e}"})

print(f"Embedding done: {len(emb_list)}", flush=True)

# Save as JSON (base64 encoded float32)
emb_array = np.array(emb_list, dtype=np.float32)
raw_bytes = emb_array.tobytes()
emb_b64 = base64.b64encode(raw_bytes).decode("ascii")

output = {
    "dim": 384,
    "count": len(emb_list),
    "embeddings_b64": emb_b64,
    "meta": metas,
}

out_path = "/home/lnr/research-wiki/docs/embeddings-f32.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False)

print(f"Saved: {out_path} ({os.path.getsize(out_path)/1024:.0f} KB)", flush=True)

# Also update search-index.json
search_entries = []
for m in metas:
    viewer_url = f"https://lnrgitg.github.io/research-wiki/viewer.html?p="
    if m["c"] == "paper_ru":
        viewer_url += f"papers/ru_papers/{m['f']}"
    elif m["c"] == "query":
        viewer_url += f"queries/{m['f']}"
    else:
        viewer_url += f"papers/{m['f']}"
    search_entries.append({"title": m["t"], "file": m["f"], "category": m["c"], "url": viewer_url, "abstract": m["a"]})

idx_path = "/home/lnr/research-wiki/docs/search-index.json"
with open(idx_path, "w", encoding="utf-8") as f:
    json.dump(search_entries, f, ensure_ascii=False)

print(f"Search index: {idx_path} ({len(search_entries)} entries, {os.path.getsize(idx_path)/1024:.0f} KB)", flush=True)
print("ALL DONE", flush=True)
