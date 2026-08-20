#!/usr/bin/env python3
"""
Server-side vector search for research-wiki.
Uses pre-computed embeddings from docs/vector-embeddings.json.
Query encoding via sentence-transformers (model cached, ~70s cold load).

Usage:
  python scripts/vector_search_server.py "housing supply elasticity"
  python scripts/vector_search_server.py "ипотека и цены на жильё" --limit 20
  python scripts/vector_search_server.py "monetary policy" --filter paper
"""
import json, base64, sys, argparse, os
from pathlib import Path
import numpy as np

WIKI_ROOT = Path("/home/lnr/research-wiki")
EMB_PATH = WIKI_ROOT / "docs" / "vector-embeddings.json"
MODEL_NAME = "paraphrase-multilingual-MiniLM-L12-v2"

_model = None
_embeddings = None
_meta = None

def load_index():
    """Load pre-computed embeddings and metadata."""
    global _embeddings, _meta
    if _embeddings is not None:
        return
    
    with open(EMB_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    binary = base64.b64decode(data['embeddings_b64'])
    _embeddings = np.frombuffer(binary, dtype=np.float16).reshape(
        data['count'], data['dim']).astype(np.float32)
    _meta = data['meta']

def get_model():
    """Lazy load sentence-transformers model."""
    global _model
    if _model is None:
        from sentence_transformers import SentenceTransformer
        _model = SentenceTransformer(MODEL_NAME, device='cpu')
    return _model

def search(query, limit=10, filter_type=None):
    """Semantic search."""
    load_index()
    model = get_model()
    
    # Encode query
    q_emb = model.encode([query], show_progress_bar=False,
                        convert_to_numpy=True, normalize_embeddings=True)[0]
    
    # Cosine similarity (embeddings already normalized)
    scores = _embeddings @ q_emb
    
    # Filter by type
    indices = list(range(len(_meta)))
    if filter_type:
        indices = [i for i in indices if _meta[i]['category'] == filter_type]
    
    # Sort by score
    indexed_scores = [(i, scores[i]) for i in indices]
    indexed_scores.sort(key=lambda x: -x[1])
    
    results = []
    for idx, score in indexed_scores[:limit]:
        m = _meta[idx]
        results.append({
            'score': float(score),
            'title': m['title'],
            'file': m['file'],
            'category': m['category'],
            'url': m['url'],
            'abstract': m.get('abstract', ''),
        })
    return results

def main():
    parser = argparse.ArgumentParser(description='Vector search for research-wiki')
    parser.add_argument('query', help='Search query')
    parser.add_argument('--limit', type=int, default=10, help='Max results')
    parser.add_argument('--filter', choices=['paper', 'ru_paper', 'query', 'bibliography'],
                       help='Filter by category')
    args = parser.parse_args()
    
    print(f"Query: '{args.query}'")
    print(f"Loading index...")
    
    results = search(args.query, limit=args.limit, filter_type=args.filter)
    
    print(f"\n{'Score':>6}  {'Type':<10}  {'Title':<60}  File")
    print("-" * 100)
    for r in results:
        score_pct = f"{r['score']*100:.0f}%"
        print(f"{score_pct:>6}  {r['category']:<10}  {r['title'][:60]:<60}  {r['file'][:40]}")
        if r['abstract']:
            print(f"         {r['abstract'][:150]}")
        print()

if __name__ == '__main__':
    main()