# -*- coding: utf-8 -*-
"""kb_refresh_dkp.py — обновление dkp-корпуса в векторном слое (kb.document/kb.chunk).

Зачем отдельный скрипт. Загрузчик `kb_loader.py` опознаёт документы по паре
(origin_repo, url_or_path) и при повторном прогоне существующие БД-документы
пропускает («if not new: skipped») — то есть исправления в dkp в индекс не
попадают, а удалённые решения остаются в индексе навсегда. Этот скрипт
обновляет корпус dkp по фактическому состоянию базы: переиндексирует
изменившиеся документы, добавляет появившиеся и удаляет осиротевшие.

Порядок:
  1. собрать ожидаемый набор документов из dkp.decision (headline) и dkp.argument;
  2. для каждого: если документ есть — обновить sha/title/дату и перезалить чанк
     с новым эмбеддингом; если нет — вставить;
  3. удалить из kb документы db://dkp/%, которых больше нет в базе;
  4. отчёт: обновлено, добавлено, удалено, чанков, эмбеддингов, ошибок.

Модель эмбеддингов и размерность берутся из kb_loader (yandex text-search-doc, 256).
"""
import sys, os, json, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kb_loader as L  # noqa: E402
from db_tunnel import connect

DRY = "--dry" in sys.argv


def expected_docs(cur):
    """Ожидаемый корпус dkp: заголовки решений и аргументы."""
    cur.execute("""SELECT d.decision_id, d.headline_ru, m.meeting_date::text
                   FROM dkp.decision d JOIN dkp.meeting m USING (meeting_id)""")
    for did, headline, mdate in cur.fetchall():
        if not headline:
            continue
        yield dict(doc_type="dkp_text", title="Решение СД %s" % mdate, lang="ru",
                   origin_repo="db", url_or_path="db://dkp/decision/%s" % did,
                   content=headline, chunk_kind="headline",
                   meta={"decision_id": did})
    cur.execute("""SELECT a.argument_id, a.text_raw, a.block, m.meeting_date::text
                   FROM dkp.argument a
                   JOIN dkp.decision d USING (decision_id)
                   JOIN dkp.meeting m USING (meeting_id)""")
    for aid, txt, block, mdate in cur.fetchall():
        if not txt:
            continue
        yield dict(doc_type="dkp_text", title="Аргумент ЦБ %s [%s]" % (mdate, block), lang="ru",
                   origin_repo="db", url_or_path="db://dkp/argument/%s" % aid,
                   content=txt, chunk_kind="paragraph",
                   meta={"argument_id": aid, "block": block})


def main():
    started = time.time()
    stats = dict(docs_seen=0, updated=0, inserted=0, deleted=0, chunks=0, embedded=0, fail=0)
    with connect() as c:
        cur = c.cursor()
        cur.execute("""INSERT INTO kb.ingest_log (started_at, pipeline_v, embed_model)
                       VALUES (now(), %s, %s) RETURNING run_id""",
                    ("kb_refresh_dkp_v1", L.EMBED_MODEL))
        run_id = cur.fetchone()[0]
        c.commit()

        seen_paths = []
        for d in expected_docs(cur):
            stats["docs_seen"] += 1
            seen_paths.append(d["url_or_path"])
            content = d["content"]
            csha = L.sha(content)
            cur.execute("""SELECT doc_id, sha256 FROM kb.document
                           WHERE origin_repo=%s AND url_or_path=%s""",
                        (d["origin_repo"], d["url_or_path"]))
            row = cur.fetchone()
            if row and row[1] == csha:
                # содержимое не менялось: чанк и эмбеддинг уже актуальны
                continue
            v = None if DRY else L.embed(content)
            emb = "[" + ",".join(repr(x) for x in v) + "]" if v else None
            if v:
                stats["embedded"] += 1
            elif not DRY:
                stats["fail"] += 1
            if row:
                doc_id = row[0]
                if not DRY:
                    cur.execute("DELETE FROM kb.chunk WHERE doc_id=%s", (doc_id,))
                    cur.execute("""UPDATE kb.document SET title=%s, sha256=%s, ingested_at=now(),
                                   n_chunks=1, meta=%s WHERE doc_id=%s""",
                                (d["title"], csha, json.dumps(d["meta"], ensure_ascii=False), doc_id))
                    cur.execute("""INSERT INTO kb.chunk (doc_id, seq_no, kind, text, tsv, embedding)
                                   VALUES (%s,0,%s,%s,to_tsvector('russian',%s),%s::vector)""",
                                (doc_id, d["chunk_kind"], content[:8000], content[:8000], emb))
                stats["updated"] += 1
            else:
                if not DRY:
                    cur.execute("""INSERT INTO kb.document
                        (doc_type, title, lang, origin_repo, url_or_path, sha256, ingested_at, n_chunks, meta)
                        VALUES (%s,%s,%s,%s,%s,%s,now(),1,%s) RETURNING doc_id""",
                        (d["doc_type"], d["title"], d["lang"], d["origin_repo"],
                         d["url_or_path"], csha, json.dumps(d["meta"], ensure_ascii=False)))
                    doc_id = cur.fetchone()[0]
                    cur.execute("""INSERT INTO kb.chunk (doc_id, seq_no, kind, text, tsv, embedding)
                                   VALUES (%s,0,%s,%s,to_tsvector('russian',%s),%s::vector)""",
                                (doc_id, d["chunk_kind"], content[:8000], content[:8000], emb))
                stats["inserted"] += 1
            stats["chunks"] += 1
            if stats["docs_seen"] % 100 == 0:
                c.commit()
                print("  ...обработано %d (обновлено %d, добавлено %d), %.0fs"
                      % (stats["docs_seen"], stats["updated"], stats["inserted"], time.time() - started))
        c.commit()

        # осиротевшие документы: есть в kb, нет в базе
        cur.execute("""SELECT doc_id, url_or_path FROM kb.document WHERE url_or_path LIKE 'db://dkp/%%'""")
        orphans = [(r[0], r[1]) for r in cur.fetchall() if r[1] not in set(seen_paths)]
        for doc_id, path in orphans:
            if not DRY:
                cur.execute("DELETE FROM kb.chunk WHERE doc_id=%s", (doc_id,))
                cur.execute("DELETE FROM kb.document WHERE doc_id=%s", (doc_id,))
            stats["deleted"] += 1
            print("  осиротевший документ удалён:", path)
        c.commit()

        if not DRY:
            cur.execute("""UPDATE kb.ingest_log SET finished_at=now(), n_docs=%s, n_chunks=%s,
                           n_embedded=%s, n_skipped=%s, notes=%s WHERE run_id=%s""",
                        (stats["updated"] + stats["inserted"], stats["chunks"], stats["embedded"],
                         stats["docs_seen"] - stats["updated"] - stats["inserted"],
                         "deleted=%d; fail_chunks=%d; %.0fs; режим=%s"
                         % (stats["deleted"], stats["fail"], time.time() - started,
                            "dry" if DRY else "apply"), run_id))
        c.commit()

    print("ИТОГ: %s" % stats)
    print("время, с: %.0f" % (time.time() - started))


if __name__ == "__main__":
    main()