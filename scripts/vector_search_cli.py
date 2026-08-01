#!/usr/bin/env python3
"""
Vector Search CLI for research-wiki
Usage: python scripts/vector_search_cli.py <command> [args]
"""

import sys
from pathlib import Path
import lancedb
from sentence_transformers import SentenceTransformer

WIKI_ROOT = Path("/home/lnr/research-wiki")
LANCEDB_DIR = WIKI_ROOT / "data" / "embeddings"

# Use the same model
EMBED_MODEL_NAME = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"

_model = None


def get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer(EMBED_MODEL_NAME, device='cpu')
    return _model


def get_db():
    return lancedb.connect(str(LANCEDB_DIR))


def search_wiki(query: str, limit: int = 10, filter_type: str = None):
    """Search wiki documents."""
    model = get_model()
    db = get_db()
    
    if "wiki_documents" not in db.table_names():
        print("Index not found. Run indexing first.")
        return []
    
    table = db.open_table("wiki_documents")
    query_vec = model.encode(query).tolist()
    
    results = table.search(query_vec).metric("cosine").limit(limit)
    if filter_type:
        results = results.where(f"type = '{filter_type}'")
    
    return results.to_list()


def search_catalog(query: str, limit: int = 10):
    """Search data catalog."""
    model = get_model()
    db = get_db()
    
    if "data_catalog" not in db.table_names():
        print("Catalog index not found.")
        return []
    
    table = db.open_table("data_catalog")
    query_vec = model.encode(query).tolist()
    results = table.search(query_vec).metric("cosine").limit(limit)
    
    return results.to_list()


def format_result(r, score_key="_distance"):
    score = 1 - r[score_key]
    filepath = r.get("filepath", r.get("source_id", "N/A"))
    title = r.get("title", r.get("name", "N/A"))
    text = r.get("text", "")[:200]
    return f"[{score:.3f}] {filepath} - {title}\n  {text}..."


def main():
    if len(sys.argv) < 2:
        print("Vector Search for research-wiki")
        print("Commands:")
        print("  search <query>           - Search wiki documents")
        print("  search-type <type> <query> - Search filtered by type (papers/reviews/concepts/annotations/queries)")
        print("  catalog <query>          - Search data catalog")
        print("  stats                    - Show index statistics")
        sys.exit(1)
    
    cmd = sys.argv[1]
    
    if cmd == "search":
        query = " ".join(sys.argv[2:])
        if not query:
            print("Please provide a query")
            sys.exit(1)
        results = search_wiki(query, limit=10)
        print(f"Results for: '{query}'")
        for r in results:
            print(format_result(r))
            print()
    
    elif cmd == "search-type":
        if len(sys.argv) < 4:
            print("Usage: search-type <type> <query>")
            sys.exit(1)
        filter_type = sys.argv[2]
        query = " ".join(sys.argv[3:])
        results = search_wiki(query, limit=10, filter_type=filter_type)
        print(f"Results for: '{query}' (type: {filter_type})")
        for r in results:
            print(format_result(r))
            print()
    
    elif cmd == "catalog":
        query = " ".join(sys.argv[2:])
        if not query:
            print("Please provide a query")
            sys.exit(1)
        results = search_catalog(query, limit=10)
        print(f"Catalog results for: '{query}'")
        for r in results:
            print(format_result(r))
            print()
    
    elif cmd == "stats":
        db = get_db()
        for table_name in db.table_names():
            table = db.open_table(table_name)
            print(f"{table_name}: {table.count_rows()} rows")
    
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)


if __name__ == "__main__":
    main()