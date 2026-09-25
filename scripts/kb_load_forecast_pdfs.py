# -*- coding: utf-8 -*-
"""
Загрузка PDF-документов ленты decision_key_rate (среднесрочный прогноз +
комментарий к нему) в kb.document/kb.chunk с векторизацией.

PDF извлекаются pymupdf (fitz) прямо из URL, без записи в raw/ (git-дисциплина:
PDF в репозиторий не попадают). doc_type='cbr_raw', meta.genre=
forecast|forecast_comment. Дедуп: UNIQUE(origin_repo, url_or_path).
"""
import sys
import json
import time
import hashlib
import io
import urllib.request
import re

sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import query, execute  # noqa: E402

import fitz  # pymupdf

FOLDER = "b1gpe14c599s44v5dacm"
DRY = "--dry" in sys.argv

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"


def http_get(url, timeout=90):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def embed(text, kind="text-search-doc"):
    key = None
    for line in open("/home/lnr/.hermes/.env", encoding="utf-8"):
        if line.startswith("YANDEX_CLOUD_API_KEY"):
            key = line.split("=", 1)[1].strip().strip('"').strip("'")
    payload = json.dumps({
        "modelUri": "emb://%s/%s/latest" % (FOLDER, kind),
        "text": text[:8000],
    }).encode()
    req = urllib.request.Request(
        "https://llm.api.cloud.yandex.net/foundationModels/v1/textEmbedding",
        data=payload, method="POST",
        headers={"Authorization": "Api-Key " + key,
                 "Content-Type": "application/json"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read())["embedding"]
        except Exception as e:
            print("  embed retry", attempt + 1, str(e)[:100])
            time.sleep(3 + attempt * 3)
    return None


def chunk_text(text, size=900, overlap=150):
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    chunks, cur = [], ""
    for p in paras:
        if len(cur) + len(p) + 2 <= size:
            cur = (cur + "\n\n" + p).strip()
        else:
            if cur:
                chunks.append(cur)
            while len(p) > size:
                chunks.append(p[:size])
                p = p[size - overlap:]
            cur = p
    if cur:
        chunks.append(cur)
    return chunks or ([text[:size]] if text else [])


def extract_pdf_text(raw):
    doc = fitz.open(stream=raw, filetype="pdf")
    pages = []
    for page in doc:
        pages.append(page.get_text("text"))
    doc.close()
    return "\n\n".join(pages)


def main():
    import time as _t
    t0 = _t.time()
    # лента -> PDF-ссылки
    req = urllib.request.Request(
        "https://www.cbr.ru/dkp/mp_dec/decision_key_rate/",
        headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        html = r.read().decode("utf-8", errors="ignore")
    blocks = re.split(r'document-regular_date">', html)
    targets = []  # (date, url, genre)
    for b in blocks[1:]:
        date = b[:10]
        m = re.search(r'href="([^"]+)"', b)
        t = re.search(r'_visible">([^<]+)<', b)
        if not m or not t:
            continue
        url, title = m.group(1), t.group(1)
        if "/Content/Document/File/" in url and "forecast" in url:
            targets.append((date, url, "forecast"))
        elif "/Content/Document/File/" in url and "comment" in url:
            targets.append((date, url, "forecast_comment"))
    print("PDF-документов на ленте:", len(targets))

    have = {r[0] for r in query(
        "SELECT url_or_path FROM kb.document WHERE doc_type='cbr_raw'")}
    stats = {"ok": 0, "skip": 0, "fail": 0}

    for date, url, genre in targets:
        full = "https://www.cbr.ru" + url if url.startswith("/") else url
        if full in have:
            stats["skip"] += 1
            continue
        if DRY:
            print(f"  [dry] {genre} {date} {url}")
            stats["ok"] += 1
            continue
        try:
            raw = http_get(full)
            text = extract_pdf_text(raw)
        except Exception as e:
            print(f"  FAIL fetch/pdf {genre} {date}: {str(e)[:100]}")
            stats["fail"] += 1
            continue
        if len(text) < 500:
            print(f"  FAIL text too short {genre} {date}: {len(text)}")
            stats["fail"] += 1
            continue
        title = ("Среднесрочный прогноз Банка России (публ. %s)" % date
                 if genre == "forecast"
                 else "Комментарий к среднесрочному прогнозу (публ. %s)" % date)
        sha = hashlib.sha256(text.encode()).hexdigest()
        dmy = date.split(".")
        iso = "%s-%s-%s" % (dmy[2], dmy[1], dmy[0]) if len(dmy) == 3 else date
        # kb.document
        execute("INSERT INTO kb.document (doc_type, title, lang, published_at, url_or_path, origin_repo, sha256, n_chunks, meta) "
                "VALUES ('cbr_raw','%s','ru','%s','%s','research-wiki-private','%s',0,"
                "'{\"genre\":\"%s\"}')"
                % (esc(title), iso, esc(full), sha, genre))
        doc_id = query("SELECT doc_id FROM kb.document WHERE url_or_path='%s'"
                       % esc(full))[0][0]
        chunks = chunk_text(text)
        n_ok = 0
        for i, ch in enumerate(chunks):
            emb = embed(ch)
            if emb is None:
                print(f"  embed FAIL {genre} {date} chunk {i}")
                continue
            tsv = "to_tsvector('russian', '%s')" % esc(ch).replace("'","''")
            execute("INSERT INTO kb.chunk (doc_id, seq_no, kind, text, tsv, embedding, meta) "
                    "VALUES (%s,%s,'paragraph','%s',%s,'%s'::vector,'{}')"
                    % (doc_id, i, esc(ch), tsv,
                       "[%s]" % ",".join("%.7f" % x for x in emb)))
            n_ok += 1
        execute("UPDATE kb.document SET n_chunks=%s WHERE doc_id=%s" % (n_ok, doc_id))
        print(f"  + {genre} {date}: {n_ok}/{len(chunks)} chunks, {len(text)} chars")
        stats["ok"] += 1

    print("\nИТОГ:", stats, "in %.1fs" % (_t.time() - t0))
    return 0


def esc(s):
    return s.replace("'", "''")


if __name__ == "__main__":
    sys.exit(main())