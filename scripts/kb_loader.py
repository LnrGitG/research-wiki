# -*- coding: utf-8 -*-
"""
kb_loader_v1 — полный индекс всех знаний в kb.document/kb.chunk (research_wiki).

Корпуса:
  1. ~/research-wiki        *.md (papers, concepts, queries, entities...) + raw/*.txt
  2. ~/macroeconomist       *.md + raw/*.txt
  3. ~/research-wiki-private queries/*.md + корневые *.md
  4. БД: core.paper_card (findings/methods как отдельные чанки kind=finding/method)
  5. БД: dkp.decision headline (kind=headline), dkp.argument text_raw
  6. БД: v2.metric name_ru (kind=paragraph, meta.metric_id)

Модель: Yandex text-search-doc 256-dim. Дедуп: sha256 документа.
Чанк: ~1000 символов с перекрытием 100, границы абзацев.
"""
import sys, os, json, hashlib, subprocess, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from db_tunnel import connect

HOME = os.path.expanduser("~")
PIPELINE_V = "kb_loader_v1"
EMBED_MODEL = "yandex:text-search-doc:latest"
FOLDER = "b1gpe14c599s44v5dacm"
API = "https://llm.api.cloud.yandex.net/foundationModels/v1/textEmbedding"
CHUNK = 1000
OVERLAP = 100

# ------------------------------------------------------------------- embed --
def api_key():
    for line in open(os.path.expanduser("~/.hermes/.env"), encoding="utf-8"):
        if line.startswith("YANDEX_CLOUD_API_KEY="):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    raise SystemExit("нет ключа YANDEX_CLOUD_API_KEY")

KEY = api_key()
_cache = {}  # sha(text) -> vector

def embed(text, retries=3):
    h = hashlib.sha256(text.encode()).hexdigest()[:16]
    if h in _cache:
        return _cache[h]
    body = json.dumps({"modelUri": "emb://%s/text-search-doc/latest" % FOLDER,
                       "text": text[:4000]}, ensure_ascii=False)
    for attempt in range(retries):
        r = subprocess.run(["curl", "-s", "-m", "40", "-X", "POST", API,
                            "-H", "Authorization: Api-Key " + KEY,
                            "-H", "Content-Type: application/json",
                            "--data-binary", "@-"],
                           input=body, capture_output=True, text=True)
        try:
            v = json.loads(r.stdout).get("embedding")
            if v and len(v) == 256:
                _cache[h] = v
                return v
        except (json.JSONDecodeError, AttributeError):
            pass
        time.sleep(1.5 * (attempt + 1))
    return []

# ------------------------------------------------------------------ chunks --
def body_of(path):
    s = open(path, encoding="utf-8", errors="ignore").read()
    if s.startswith("---") and s.count("---") >= 2:
        s = s.split("---", 2)[2]
    return s

def chunks_of(text):
    """Чанки по абзацам с бюджетом; короткие склеиваются."""
    paras = [p.strip() for p in text.split("\n\n") if p.strip()]
    out, buf = [], ""
    for p in paras:
        if len(p) > CHUNK:
            if buf:
                out.append(buf); buf = ""
            i = 0
            while i < len(p):
                out.append(p[i:i + CHUNK]); i += CHUNK - OVERLAP
            continue
        if len(buf) + len(p) + 2 > CHUNK:
            out.append(buf); buf = p
        else:
            buf = (buf + "\n\n" + p) if buf else p
    if buf:
        out.append(buf)
    return [c for c in out if c.strip()][:400]  # предохранитель на документ

def sha(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

# ------------------------------------------------------------ document upsert
def upsert_document(c, doc_type, title, lang, origin_repo, url_or_path, content_sha, meta):
    """Возвращает doc_id (существующий по origin_repo+path или новый)."""
    with c.cursor() as cur:
        cur.execute("SELECT doc_id FROM kb.document WHERE origin_repo=%s AND url_or_path=%s",
                    (origin_repo, url_or_path))
        row = cur.fetchone()
        if row:
            return row[0], False
        cur.execute("""INSERT INTO kb.document
            (doc_type, title, lang, origin_repo, url_or_path, sha256, meta)
            VALUES (%s,%s,%s,%s,%s,%s,%s) RETURNING doc_id""",
            (doc_type, title, lang, origin_repo, url_or_path, content_sha,
             json.dumps(meta, ensure_ascii=False)))
        return cur.fetchone()[0], True

def insert_chunks(c, doc_id, chunks):
    """Вставка чанков с эмбеддингами. Возвращает (n, n_embedded)."""
    n = 0
    for i, ch in enumerate(chunks):
        v = embed(ch)
        emb = "[" + ",".join(repr(x) for x in v) + "]" if v else None
        with c.cursor() as cur:
            cur.execute("""INSERT INTO kb.chunk (doc_id, seq_no, kind, text, tsv, embedding)
                VALUES (%s,%s,'paragraph',%s,
                        to_tsvector('russian', %s),
                        %s::vector)""",
                (doc_id, i, ch[:8000],
                 ch[:8000],
                 emb))
        n += 1
    return n, sum(1 for _ in range(1) if True) and n if False else n  # заглушка не нужна

# ------------------------------------------------------------------ loaders --
def walk_md(root, skip_dirs=("raw", ".git", "_archive", "node_modules")):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in skip_dirs]
        for fn in filenames:
            if fn.endswith((".md", ".txt")):
                yield os.path.join(dirpath, fn)

def file_docs():
    """Все файловые документы трёх репозиториев."""
    specs = [
        (os.path.join(HOME, "research-wiki"), "research-wiki"),
        (os.path.join(HOME, "macroeconomist"), "macroeconomist"),
        (os.path.join(HOME, "research-wiki-private"), "research-wiki-private"),
    ]
    for root, repo in specs:
        if not os.path.isdir(root):
            continue
        for p in walk_md(root):
            rel = os.path.relpath(p, root)
            # private: только queries/ и корень (там скрипты и тяжёлые данные)
            if repo == "research-wiki-private":
                top = rel.split(os.sep)[0]
                if top not in ("queries",) and os.sep in rel:
                    continue
            doc_type = "cbr_raw" if "/raw/" in p.replace(os.sep, "/") else (
                "wiki_paper" if "/papers/" in p.replace(os.sep, "/") else
                "wiki_concept" if "/concepts/" in p.replace(os.sep, "/") else
                "wiki_query" if "/queries/" in p.replace(os.sep, "/") else
                "wiki_other" if repo == "research-wiki" else "repo_note")
            title = os.path.splitext(os.path.basename(p))[0]
            yield dict(path=p, repo=repo, doc_type=doc_type, title=title,
                       rel=rel, body=body_of(p))

def db_docs():
    """Текстовые объекты БД: paper_card, dkp, metrics."""
    import psycopg
    from db_tunnel import connect as _c
    with _c() as c:
        with c.cursor() as cur:
            # paper_card findings/methods
            cur.execute("""SELECT paper_code, coalesce(title_ru, title_orig, paper_code),
                                  findings, methods_text, coalesce(year::text,''), wiki_page
                           FROM core.paper_card""")
            for code, title, findings, methods, year, wiki in cur.fetchall():
                for kind, txt in (("finding", findings), ("method", methods)):
                    if txt and len(txt.strip()) > 40:
                        yield dict(doc_type="wiki_paper", title="%s — %s" % (title, kind),
                                   lang="ru", origin_repo="db",
                                   url_or_path="db://paper_card/%s/%s" % (code, kind),
                                   content=txt, meta={"paper_code": code, "year": year},
                                   chunk_kind=kind)
            # dkp decision headlines
            cur.execute("""SELECT d.decision_id, d.headline_ru, m.meeting_date
                           FROM dkp.decision d JOIN dkp.meeting m USING (meeting_id)""")
            for did, headline, mdate in cur.fetchall():
                if headline:
                    yield dict(doc_type="dkp_text", title="Решение СД %s" % mdate,
                               lang="ru", origin_repo="db",
                               url_or_path="db://dkp/decision/%s" % did,
                               content=headline, meta={"decision_id": did},
                               chunk_kind="headline")
            # dkp arguments
            cur.execute("""SELECT a.argument_id, a.text_raw, a.block, m.meeting_date
                           FROM dkp.argument a
                           JOIN dkp.decision d USING (decision_id)
                           JOIN dkp.meeting m USING (meeting_id)""")
            for aid, txt, block, mdate in cur.fetchall():
                yield dict(doc_type="dkp_text", title="Аргумент ЦБ %s [%s]" % (mdate, block),
                           lang="ru", origin_repo="db",
                           url_or_path="db://dkp/argument/%s" % aid,
                           content=txt, meta={"argument_id": aid, "block": block},
                           chunk_kind="paragraph")
            # metrics
            cur.execute("""SELECT metric_id, metric_code, name_ru FROM v2.metric
                           WHERE name_ru IS NOT NULL""")
            for mid, code, name in cur.fetchall():
                yield dict(doc_type="metric_card", title=name, lang="ru",
                           origin_repo="db",
                           url_or_path="db://metric/%s" % mid,
                           content="%s (metric_code: %s, metric_id: %s)" % (name, code, mid),
                           meta={"metric_id": mid, "metric_code": code},
                           chunk_kind="paragraph")

# -------------------------------------------------------------------- main --
def main(dry=False, limit_files=None):
    import psycopg
    started = time.time()
    stats = dict(docs=0, chunks=0, embedded=0, skipped=0, fail_chunks=0)

    with connect() as c:
        cur = c.cursor()
        cur.execute("INSERT INTO kb.ingest_log (started_at, pipeline_v, embed_model) "
                    "VALUES (now(), %s, %s) RETURNING run_id", (PIPELINE_V, EMBED_MODEL))
        run_id = cur.fetchone()[0]
        c.commit()

        docs = list(file_docs())
        if limit_files:
            docs = docs[:limit_files]
        print("file docs:", len(docs))

        for d in docs:
            content = d["body"]
            if len(content.strip()) < 60:
                stats["skipped"] += 1
                continue
            csha = sha(content)
            try:
                doc_id, new = upsert_document(
                    c, d["doc_type"], d["title"],
                    "en" if sum(1 for ch in content if ord(ch) > 1000) < len(content) * 0.005 else "ru",
                    d["repo"], "file://" + d["rel"], csha,
                    {"abs_path": d["path"], "size": len(content)})
            except Exception as e:
                print("doc FAIL", d["rel"], str(e)[:100])
                stats["skipped"] += 1
                continue
            if not new:
                # перечитываем контент: если sha сменился — реиндекс
                with c.cursor() as cur:
                    cur.execute("SELECT sha256 FROM kb.document WHERE doc_id=%s", (doc_id,))
                    old = cur.fetchone()[0]
                if old == csha:
                    stats["skipped"] += 1
                    continue
                with c.cursor() as cur:
                    cur.execute("DELETE FROM kb.chunk WHERE doc_id=%s", (doc_id,))
                    cur.execute("UPDATE kb.document SET sha256=%s, ingested_at=now() WHERE doc_id=%s",
                                (csha, doc_id))
            chs = chunks_of(content)
            with c.cursor() as cur:
                cur.execute("UPDATE kb.document SET n_chunks=%s WHERE doc_id=%s", (len(chs), doc_id))
            for i, ch in enumerate(chs):
                v = embed(ch)
                emb = "[" + ",".join(repr(x) for x in v) + "]" if v else None
                if v:
                    stats["embedded"] += 1
                else:
                    stats["fail_chunks"] += 1
                with c.cursor() as cur:
                    cur.execute("""INSERT INTO kb.chunk (doc_id, seq_no, kind, text, tsv, embedding)
                        VALUES (%s,%s,'paragraph',%s,to_tsvector('russian',%s),%s::vector)""",
                        (doc_id, i, ch[:8000], ch[:8000], emb))
                stats["chunks"] += 1
            c.commit()
            stats["docs"] += 1
            if stats["docs"] % 50 == 0:
                print("  ...%d docs, %d chunks, %.0fs" % (stats["docs"], stats["chunks"], time.time() - started))

        # БД-документы
        print("db docs...")
        for d in db_docs():
            content = d["content"]
            if len(content.strip()) < 20:
                continue
            doc_id, new = upsert_document(
                c, d["doc_type"], d["title"], d["lang"], d["origin_repo"],
                d["url_or_path"], sha(content), d["meta"])
            if not new:
                stats["skipped"] += 1
                continue
            v = embed(content)
            emb = "[" + ",".join(repr(x) for x in v) + "]" if v else None
            if v:
                stats["embedded"] += 1
            else:
                stats["fail_chunks"] += 1
            with c.cursor() as cur:
                cur.execute("""INSERT INTO kb.chunk (doc_id, seq_no, kind, text, tsv, embedding)
                    VALUES (%s,0,%s,%s,to_tsvector('russian',%s),%s::vector)""",
                    (doc_id, d["chunk_kind"], content[:8000], content[:8000], emb))
                cur.execute("UPDATE kb.document SET n_chunks=1 WHERE doc_id=%s", (doc_id,))
            stats["chunks"] += 1
            stats["docs"] += 1
        c.commit()

        finished = time.time()
        with c.cursor() as cur:
            cur.execute("""UPDATE kb.ingest_log SET finished_at=now(), n_docs=%s, n_chunks=%s,
                           n_embedded=%s, n_skipped=%s, notes=%s WHERE run_id=%s""",
                        (stats["docs"], stats["chunks"], stats["embedded"],
                         stats["skipped"],
                         "fail_chunks=%d; %.0fs" % (stats["fail_chunks"], finished - started),
                         run_id))
        c.commit()

    print("DONE: docs=%(docs)d chunks=%(chunks)d embedded=%(embedded)d skipped=%(skipped)d fail_chunks=%(fail_chunks)d in %(sec).0fs"
          % dict(stats, sec=time.time() - started))

if __name__ == "__main__":
    dry = "--dry" in sys.argv
    lim = None
    for a in sys.argv:
        if a.startswith("--limit="):
            lim = int(a.split("=")[1])
    main(dry=dry, limit_files=lim)