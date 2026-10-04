#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
kb_search — гибридный семантический поиск по KB копилота
(research_wiki, PostgreSQL + pgvector; схема kb, таблицы document/chunk).

Каналы поиска и слияние:
  1. dense:    cosine(embedding запроса, kb.chunk.embedding); запрос
               эмбеддится Yandex text-search-query (та же папка YC, что и
               документная модель text-search-doc в kb_loader.py).
  2. lexical: plainto_tsquery('russian', ...) + ts_rank_cd по kb.chunk.tsv.
  Слияние:     Reciprocal Rank Fusion: score = Σ 1/(60 + rank) по каналам.

Использование:
  python3 scripts/kb_search.py "запрос" [-n 8] [--type papers] [--json]
  python3 scripts/kb_search.py --demo

Типы: wiki_paper | wiki_concept | wiki_query | wiki_other | repo_note |
      cbr_raw | dkp_text | metric_card
"""
import argparse
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

FOLDER = "b1gpe14c599s499s"  # заменяется реальным в embed_query()
K_RRF = 60
TOP_PER_CHANNEL = 40


def _key():
    for line in open(os.path.expanduser("~/.hermes/.env"), encoding="utf-8"):
        if line.startswith("YANDEX_CLOUD_API_KEY="):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    raise SystemExit("YANDEX_CLOUD_API_KEY не найден в ~/.hermes/.env")


def _folder():
    """YC folder_id — как в build_yandex_embeddings.py."""
    import re
    src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "build_yandex_embeddings.py"), encoding="utf-8").read()
    m = re.search(r'FOLDER\s*=\s*"([^"]+)"', src)
    return m.group(1) if m else None


def embed_query(text, retries=3):
    """Запрос -> 256-dim (text-search-query, modelUri emb://<folder>/...)."""
    folder = _folder()
    if not folder:
        raise SystemExit("FOLDER не найден в build_yandex_embeddings.py")
    body = json.dumps({
        "modelUri": "emb://%s/text-search-query/latest" % folder,
        "text": text[:4000],
    }, ensure_ascii=False)
    for attempt in range(retries):
        r = subprocess.run(
            ["curl", "-s", "-m", "40", "-X", "POST",
             "https://llm.api.cloud.yandex.net/foundationModels/v1/textEmbedding",
             "-H", "Authorization: Api-Key " + _key(),
             "-H", "Content-Type: application/json", "--data-binary", "@-"],
            input=body, capture_output=True, text=True)
        try:
            v = json.loads(r.stdout).get("embedding")
            if v and len(v) == 256:
                return v
        except (json.JSONDecodeError, AttributeError):
            pass
        import time
        time.sleep(1.5 * (attempt + 1))
    raise SystemExit("эмбеддинг запроса не получен")


def _vec_literal(v):
    return "[" + ",".join(repr(float(x)) for x in v) + "]"


def search(query, limit=8, doc_type=None):
    """Гибридный поиск. Возвращает список dict с полями результата."""
    from db_tunnel import query as db_query

    q = query.strip()
    if not q:
        return []

    type_filter = "AND d.doc_type = %(doc_type)s" if doc_type else ""

    # канал 1: векторный.
    # Пул отбирается ДО сортировки по расстоянию и материализуется. Без этого
    # планировщик берёт HNSW-индекс (hnsw.ef_search=40), а фильтр по doc_type
    # применяет ПОСЛЕ него — и для мелких типов (metric_card 127 чанков,
    # dkp_text 664, wiki_query 2039) канал возвращает 0 из 40. Замер 04.10.2026:
    # с MATERIALIZED-пулом — 40 из 40 для всех типов.
    emb = embed_query(q)
    vec_sql = """
        WITH pool AS MATERIALIZED (
            SELECT c.chunk_id, c.doc_id, c.seq_no, c.kind, c.text, c.embedding
            FROM kb.chunk c
            JOIN kb.document d ON d.doc_id = c.doc_id
            WHERE c.embedding IS NOT NULL {tf}
        )
        SELECT d.doc_id, d.title, d.doc_type, d.url_or_path, p.chunk_id, p.seq_no,
               left(p.text, %(maxtext)s) AS snippet, p.kind,
               1 - (p.embedding <=> %(emb)s::vector) AS cos
        FROM pool p
        JOIN kb.document d ON d.doc_id = p.doc_id
        ORDER BY p.embedding <=> %(emb)s::vector
        LIMIT %(top)s
    """.format(tf=type_filter)
    vec_rows = db_query(vec_sql, {"emb": "[" + ",".join(repr(float(x)) for x in emb) + "]",
                               "doc_type": doc_type, "top": TOP_PER_CHANNEL,
                               "maxtext": 700})

    # канал 2: лексический (russian)
    lex_sql = """
        SELECT d.doc_id, d.title, d.doc_type, d.url_or_path, c.chunk_id, c.seq_no,
               left(c.text, %(maxtext)s) AS snippet, c.kind,
               ts_rank_cd(c.tsv, plainto_tsquery('russian', %(q)s)) AS rank
        FROM kb.chunk c
        JOIN kb.document d ON d.doc_id = c.doc_id
        WHERE c.tsv @@ plainto_tsquery('russian', %(q)s) {tf}
        ORDER BY rank DESC
        LIMIT %(top)s
    """.format(tf=type_filter)
    lex_rows = db_query(lex_sql, {"q": q, "doc_type": doc_type,
                               "top": TOP_PER_CHANNEL, "maxtext": 700})

    # RRF-слияние
    scores = {}
    info = {}
    for rank, row in enumerate(vec_rows, 1):
        key = row[4]  # chunk_id
        scores[key] = scores.get(key, 0.0) + 1.0 / (K_RRF + rank)
        info[key] = row
    for rank, row in enumerate(lex_rows, 1):
        key = row[4]
        scores[key] = scores.get(key, 0.0) + 1.0 / (K_RRF + rank)
        info.setdefault(key, row)

    ranked = sorted(scores.items(), key=lambda kv: -kv[1])[:limit]
    out = []
    for chunk_id, sc in ranked:
        doc_id, title, dtype, path, cid, seq, snippet, kind = info[chunk_id][:8]
        in_vec = any(r[4] == chunk_id for r in vec_rows)
        in_lex = any(r[4] == chunk_id for r in lex_rows)
        out.append(dict(score=round(sc, 5), chunk_id=chunk_id, doc_id=doc_id,
                        title=title, doc_type=dtype, seq=seq, kind=kind,
                        channels=("vec" if in_vec else "") + ("+lex" if in_lex else ""),
                        snippet=snippet))
    return out


DEMO_QUERIES = [
    "разрыв выпуска оценка потенциального выпуска Россия",
    "когда ЦБ ужесточал политику при растущих инфляционных ожиданиях",
    "комбинирование прогнозов экспертные поправки центральный банк",
    "перетоки трудовых ресурсов между отраслями инфляция",
    "бюджетное правило нефтегазовые доходы ДКП",
]


def demo():
    print("Контрольные запросы (demo):\n")
    for q in DEMO_QUERIES:
        res = search(q, limit=3)
        print("Q:", q)
        for r in res:
            print("  [%.4f %s] %s :: %s" % (r["score"], r["channels"],
                                            r["title"][:60],
                                            (r["snippet"] or "")[:90].replace("\n", " ")))
        if not res:
            print("  (нет результатов)")
        print()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("query", nargs="*", help="поисковый запрос")
    ap.add_argument("-n", "--limit", type=int, default=8)
    ap.add_argument("--type", default=None,
                    help="фильтр doc_type: wiki_paper|wiki_concept|wiki_query|"
                         "wiki_other|repo_note|cbr_raw|dkp_text|metric_card")
    ap.add_argument("--demo", action="store_true", help="прогон контрольных запросов")
    ap.add_argument("--json", action="store_true", help="JSON-вывод")
    a = ap.parse_args()

    if a.demo:
        demo()
        sys.exit(0)

    q = " ".join(a.query).strip()
    if not q:
        ap.print_help()
        sys.exit(1)
    res = search(q, limit=a.limit, doc_type=a.type)
    if a.json:
        print(json.dumps(res, ensure_ascii=False, indent=1))
    else:
        for r in res:
            print("[%.5f %s] %s (%s, chunk %s)" % (r["score"], r["channels"],
                                                   r["title"], r["doc_type"], r["seq"]))
            print("    %s" % (r["snippet"] or "").replace("\n", " ")[:200])
            print()