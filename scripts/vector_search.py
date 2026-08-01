#!/usr/bin/env python3
"""
Vector Search for research-wiki
Supports semantic search across:
- Papers (papers/*.md)
- Reviews (reviews/*.md)
- Concepts (concepts/*.md)
- Data catalog descriptions
"""

import os
import re
import gc
from pathlib import Path
from typing import List, Dict, Any, Optional
import lancedb
from sentence_transformers import SentenceTransformer
import pandas as pd
import yaml

# Configuration
WIKI_ROOT = Path("/home/lnr/research-wiki")
LANCEDB_DIR = WIKI_ROOT / "data" / "embeddings"
LANCEDB_DIR.mkdir(parents=True, exist_ok=True)

# Embedding model (multilingual, good for Russian)
EMBED_MODEL_NAME = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
EMBED_DIM = 384

# Table names
TABLE_PAPERS = "papers"
TABLE_REVIEWS = "reviews"
TABLE_CONCEPTS = "concepts"
TABLE_CATALOG = "data_catalog"

# Processing config
BATCH_SIZE = 8  # Very small batch size for low memory
CHUNK_MAX_CHARS = 1000
CHUNK_OVERLAP = 100

_model = None


def get_model():
    """Lazy load embedding model."""
    global _model
    if _model is None:
        _model = SentenceTransformer(EMBED_MODEL_NAME, device='cpu')
    return _model


def get_db():
    """Get LanceDB connection."""
    return lancedb.connect(str(LANCEDB_DIR))


def chunk_text(text: str, max_chars: int = CHUNK_MAX_CHARS, overlap: int = CHUNK_OVERLAP) -> List[str]:
    """Split text into overlapping chunks."""
    if len(text) <= max_chars:
        return [text]
    
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + max_chars, len(text))
        # Try to break at sentence boundary
        if end < len(text):
            # Look for sentence end backwards
            for i in range(end, max(start + max_chars // 2, end - 200), -1):
                if text[i] in '.!?\n':
                    end = i + 1
                    break
        chunks.append(text[start:end])
        start = end - overlap
        if start >= len(text):
            break
    return chunks


def extract_frontmatter(content: str) -> Dict[str, Any]:
    """Extract YAML frontmatter from markdown."""
    frontmatter = {}
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            try:
                frontmatter = yaml.safe_load(parts[1]) or {}
            except:
                pass
    return frontmatter


def remove_frontmatter(content: str) -> str:
    """Remove YAML frontmatter from markdown."""
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            return parts[2].strip()
    return content


def get_file_type(filepath: Path) -> str:
    """Determine document type from path."""
    rel = filepath.relative_to(WIKI_ROOT)
    if rel.parts[0] == 'papers':
        return 'paper'
    elif rel.parts[0] == 'reviews':
        return 'review'
    elif rel.parts[0] == 'concepts':
        return 'concept'
    elif rel.parts[0] == 'data':
        return 'data'
    elif rel.parts[0] == 'queries':
        return 'query'
    elif rel.parts[0] == 'annotations':
        return 'annotation'
    return 'other'


def extract_metadata(filepath: Path, content: str, fm: Dict) -> Dict[str, Any]:
    """Extract metadata for indexing."""
    rel = filepath.relative_to(WIKI_ROOT)
    file_type = get_file_type(filepath)
    
    meta = {
        "filepath": str(rel),
        "filename": filepath.name,
        "type": file_type,
        "title": fm.get('title', filepath.stem),
        "tags": fm.get('tags', []),
        "created": str(fm.get('created', '')),
        "updated": str(fm.get('updated', '')),
    }
    
    # Type-specific metadata
    if file_type == 'paper':
        meta.update({
            "doi": fm.get('doi', ''),
            "authors": fm.get('authors', ''),
            "year": fm.get('year', ''),
            "journal": fm.get('journal', ''),
        })
    elif file_type == 'review':
        meta.update({
            "cluster": fm.get('cluster', ''),
            "cluster_size": fm.get('cluster_size', 0),
            "papers_in_cluster": fm.get('papers_in_cluster', []),
        })
    elif file_type == 'concept':
        meta.update({
            "concept_type": fm.get('type', ''),
        })
    
    return meta


def index_documents():
    """Index all markdown documents in the wiki (streaming, low memory)."""
    db = get_db()
    model = get_model()
    
    # Collect all markdown files
    md_files = []
    for pattern in ['papers/*.md', 'reviews/*.md', 'concepts/*.md', 'annotations/*.md', 'queries/*.md']:
        md_files.extend(WIKI_ROOT.glob(pattern))
    
    # Filter out backup files and translation duplicates
    md_files = [f for f in md_files if not f.name.endswith('.bak') and not f.name.endswith('.RU.md')]
    
    print(f"Found {len(md_files)} markdown files to index")
    
    table_name = "wiki_documents"
    if table_name in db.table_names():
        db.drop_table(table_name)
    
    table = None
    total_chunks = 0
    
    # Process files in streaming fashion
    for filepath in md_files:
        try:
            content = filepath.read_text(encoding='utf-8')
            fm = extract_frontmatter(content)
            body = remove_frontmatter(content)
            meta = extract_metadata(filepath, body, fm)
            
            # Chunk the body
            chunks = chunk_text(body)
            
            # Process chunks in small batches
            for i in range(0, len(chunks), BATCH_SIZE):
                batch_chunks = chunks[i:i+BATCH_SIZE]
                batch_texts = batch_chunks
                
                # Create embeddings for this batch
                embeddings = model.encode(batch_texts, batch_size=BATCH_SIZE, show_progress_bar=False)
                
                # Prepare data for LanceDB
                data = []
                for j, chunk in enumerate(batch_chunks):
                    chunk_idx = i + j
                    data.append({
                        "vector": embeddings[j].tolist(),
                        "text": chunk,
                        "filepath": meta["filepath"],
                        "filename": meta["filename"],
                        "type": meta["type"],
                        "title": meta["title"],
                        "tags": str(meta.get("tags", [])),
                        "chunk_id": chunk_idx,
                        "total_chunks": len(chunks),
                        # Paper-specific
                        "doi": meta.get("doi", ""),
                        "authors": meta.get("authors", ""),
                        "year": meta.get("year", ""),
                        "journal": meta.get("journal", ""),
                        # Review-specific
                        "cluster": meta.get("cluster", ""),
                        "cluster_size": meta.get("cluster_size", 0),
                        # Concept-specific
                        "concept_type": meta.get("concept_type", ""),
                    })
                
                # Add to table (create on first batch)
                if table is None:
                    table = db.create_table(table_name, data=data)
                else:
                    table.add(data)
                
                total_chunks += len(data)
                
                # Progress
                if total_chunks % 50 == 0:
                    print(f"  Indexed {total_chunks} chunks...")
                    
                # Force garbage collection every 10 batches
                if total_chunks % 500 == 0:
                    gc.collect()
                    
        except Exception as e:
            print(f"Error reading {filepath}: {e}")
    
    if table is None:
        print("No documents to index")
        return
    
    print(f"Total chunks: {total_chunks}")
    
    # Create index for faster search
    print("Creating vector index...")
    table.create_index(metric="cosine")
    print("Created vector index")
    
    return total_chunks


def index_catalog():
    """Index data catalog entries."""
    db = get_db()
    model = get_model()
    
    catalog_path = WIKI_ROOT / "data" / "catalog.yaml"
    if not catalog_path.exists():
        print("Catalog not found")
        return
    
    import yaml
    with open(catalog_path) as f:
        catalog = yaml.safe_load(f)
    
    sources = catalog.get('sources', [])
    print(f"Indexing {len(sources)} catalog sources...")
    
    data = []
    for src in sources:
        text = f"{src.get('name', '')}. {src.get('description', '')}. Type: {src.get('type', '')}. Format: {src.get('format', '')}. Schedule: {src.get('schedule', '')}."
        
        vec = model.encode(text).tolist()
        data.append({
            "vector": vec,
            "text": text,
            "source_id": src.get('id', ''),
            "name": src.get('name', ''),
            "type": src.get('type', ''),
            "format": src.get('format', ''),
            "schedule": src.get('schedule', ''),
            "path": src.get('path', ''),
            "url": src.get('url', ''),
        })
    
    table_name = "data_catalog"
    if table_name in db.table_names():
        db.drop_table(table_name)
    
    table = db.create_table(table_name, data=data)
    table.create_index(metric="cosine")
    print(f"Created catalog table with {len(data)} sources")
    
    return len(data)


def search(query: str, table_name: str = "wiki_documents", limit: int = 10, 
           filter_type: str = None, filter_tags: List[str] = None) -> List[Dict]:
    """Semantic search across indexed documents."""
    db = get_db()
    model = get_model()
    
    if table_name not in db.table_names():
        print(f"Table '{table_name}' not found. Run index_documents() first.")
        return []
    
    table = db.open_table(table_name)
    query_vec = model.encode(query).tolist()
    
    # Build filter
    where_clause = None
    if filter_type:
        where_clause = f"type = '{filter_type}'"
    
    results = table.search(query_vec).metric("cosine").limit(limit)
    if where_clause:
        results = results.where(where_clause)
    
    results = results.to_list()
    
    # Format results
    formatted = []
    for r in results:
        formatted.append({
            "score": 1 - r["_distance"],  # cosine similarity
            "filepath": r["filepath"],
            "title": r["title"],
            "type": r["type"],
            "text_preview": r["text"][:300] + "..." if len(r["text"]) > 300 else r["text"],
            "tags": r["tags"],
            "chunk_id": r["chunk_id"],
            "total_chunks": r["total_chunks"],
        })
    
    return formatted


def search_catalog(query: str, limit: int = 5) -> List[Dict]:
    """Search data catalog."""
    return search(query, table_name="data_catalog", limit=limit)


def get_stats():
    """Get index statistics."""
    db = get_db()
    stats = {}
    for table_name in db.table_names():
        table = db.open_table(table_name)
        stats[table_name] = table.count_rows()
    return stats


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python vector_search.py <command> [args]")
        print("Commands:")
        print("  index          - Index all wiki documents")
        print("  index-catalog  - Index data catalog")
        print("  search <query> - Search documents")
        print("  catalog <query> - Search data catalog")
        print("  stats          - Show index statistics")
        sys.exit(1)
    
    cmd = sys.argv[1]
    
    if cmd == "index":
        index_documents()
    elif cmd == "index-catalog":
        index_catalog()
    elif cmd == "search":
        query = " ".join(sys.argv[2:])
        results = search(query, limit=10)
        for r in results:
            print(f"[{r['score']:.3f}] {r['filepath']} ({r['type']}) - {r['title']}")
            print(f"  {r['text_preview']}")
            print()
    elif cmd == "catalog":
        query = " ".join(sys.argv[2:])
        results = search_catalog(query, limit=10)
        for r in results:
            print(f"[{r['score']:.3f}] {r['source_id']} - {r['name']}")
            print(f"  {r['text'][:200]}...")
            print()
    elif cmd == "stats":
        stats = get_stats()
        for table, count in stats.items():
            print(f"{table}: {count} rows")
    else:
        print(f"Unknown command: {cmd}")