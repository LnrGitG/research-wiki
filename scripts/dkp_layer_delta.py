#!/usr/bin/env python3
"""Дельта dkp-слоя по разбору Резюме 23.09 (кроссворк 464ca61):
1) эмбеддинги 256-dim (Yandex text-search) для 52 аргументов dkp.argument;
2) инжест полного текста Резюме 23.09 в kb.chunk (документ cbr_raw/dkp_text);
3) concern (confirm/surprise) для аргументов 11.09;
4) dkp.dissent — сентябрьский раскол по ДКУ.
Запуск: python3 scripts/dkp_layer_delta.py [--embed-only|--ingest-only]
"""
import json
import os
import subprocess
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
import db_tunnel

FOLDER = "b1gpe14c599s44v5dacm"
API = "https://llm.api.cloud.yandex.net/foundationModels/v1/textEmbedding"
MAX_INPUT = 4000
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SUMMARY_TXT = os.path.join(REPO, "data", "cbr_summary_key_rate_23092026.txt")


def yandex_key():
    for line in open(os.path.expanduser("~/.hermes/.env"), encoding="utf-8"):
        if line.startswith("YANDEX_CLOUD_API_KEY="):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    raise SystemExit("YANDEX_CLOUD_API_KEY не найден")


KEY = None


def embed(text, kind="doc", retries=3):
    global KEY
    if KEY is None:
        KEY = yandex_key()
    body = json.dumps({"modelUri": "emb://%s/text-search-%s/latest" % (FOLDER, kind),
                       "text": text[:MAX_INPUT]}, ensure_ascii=False)
    for attempt in range(retries):
        r = subprocess.run(["curl", "-s", "-m", "40", "-X", "POST", API,
                            "-H", "Authorization: Api-Key %s" % KEY,
                            "-H", "Content-Type: application/json",
                            "--data-binary", "@-"],
                           input=body, capture_output=True, text=True)
        try:
            v = json.loads(r.stdout).get("embedding")
            if v:
                return v
        except (json.JSONDecodeError, AttributeError):
            pass
        time.sleep(1.5 * (attempt + 1))
    return []


def embed_args():
    db_tunnel.connect()
    rows = db_tunnel.query("""SELECT argument_id, coalesce(text_short, '') || ' ' || coalesce(text_raw, '')
        FROM dkp.argument WHERE embedding IS NULL ORDER BY argument_id""")
    print("аргументов без эмбеддинга:", len(rows))
    ok = 0
    for aid, text in rows:
        text = (text or "").strip()
        if not text:
            continue
        v = embed(text)
        if not v:
            print("FAIL arg", aid)
            continue
        db_tunnel.execute("""UPDATE dkp.argument SET embedding = %s::vector
            WHERE argument_id = %s""",
            ("[" + ",".join("%.6f" % x for x in v) + "]", aid))
        ok += 1
        time.sleep(0.2)
    print("эмбеддингов записано:", ok)


def ingest_summary():
    """Полный текст Резюме 23.09 -> kb.document + kb.chunk с эмбеддингами."""
    db_tunnel.connect()
    text = open(SUMMARY_TXT, encoding="utf-8").read()
    import hashlib
    sha = hashlib.sha256(text.encode("utf-8")).hexdigest()
    # резать по строкам-заголовкам не нужно: чанки по ~1500 символов на границе абзацев
    paras = [p.strip() for p in text.split("\n") if p.strip()]
    chunks, cur = [], ""
    for p in paras:
        if len(cur) + len(p) + 1 > 1500 and cur:
            chunks.append(cur)
            cur = p
        else:
            cur = (cur + "\n" + p).strip()
    if cur:
        chunks.append(cur)
    print("чанков:", len(chunks))
    # документ
    r = db_tunnel.query("""SELECT doc_id FROM kb.document
        WHERE doc_type='cbr_summary' AND title ILIKE '%23.09.2026%'""")
    if r:
        doc_id = r[0][0]
        print("документ существует:", doc_id)
    else:
        doc_id = db_tunnel.query("""INSERT INTO kb.document (doc_type, title, url_or_path, origin_repo, sha256, published_at)
            VALUES ('cbr_raw', 'Резюме обсуждения ключевой ставки за 11.09.2026 (публ. 23.09.2026)', %s, 'research-wiki-private', %s, '2026-09-23')
            RETURNING doc_id""", (SUMMARY_TXT, sha))[0][0]
        print("документ создан:", doc_id)
    # чанки
    have = {r[0] for r in db_tunnel.query("SELECT seq_no FROM kb.chunk WHERE doc_id=%s", (doc_id,))}
    for i, ch in enumerate(chunks):
        if i in have:
            continue
        v = embed(ch)
        emb = "[" + ",".join("%.6f" % x for x in v) + "]" if v else None
        db_tunnel.execute("""INSERT INTO kb.chunk (doc_id, seq_no, kind, text, embedding)
            VALUES (%s, %s, 'section', %s, %s::vector)""", (doc_id, i, ch, emb))
    print("загружено:", len(chunks) - len(have))
    return doc_id


CONCERN = {
    59: ("uncertainty", "сложно оценить потребление без временных факторов"),
    60: ("surprise", "разрыв выпуска мог вновь открыться"),
    64: ("uncertainty", "ограничения экспортной логистики — двойной эффект"),
    65: ("uncertainty", "часть выручки могла направляться напрямую на импорт"),
    66: ("uncertainty", "дефицит может превзойти 2% ВВП до уточнения проектировок"),
    68: ("uncertainty", "отказ от сигнала как ответ на неопределённость"),
}


def fill_concern():
    db_tunnel.connect()
    for aid, (concern, note) in CONCERN.items():
        db_tunnel.execute("UPDATE dkp.argument SET concern=%s WHERE argument_id=%s AND concern IS NULL",
                          (concern, aid))
    print("concern обновлён:", len(CONCERN))


def make_dissent():
    db_tunnel.connect()
    r = db_tunnel.query("""SELECT 1 FROM information_schema.tables
        WHERE table_schema='dkp' AND table_name='dissent'""")
    if not r:
        db_tunnel.execute("""CREATE TABLE IF NOT EXISTS dkp.dissent (
            dissent_id serial PRIMARY KEY,
            meeting_id int REFERENCES dkp.meeting(meeting_id),
            topic text NOT NULL,
            consensus_view text,
            minority_view text,
            minority_evidence text,
            intensity text CHECK (intensity IN ('none','soft','strong')),
            created_at timestamptz DEFAULT now())""")
        print("таблица dkp.dissent создана")
    r = db_tunnel.query("SELECT 1 FROM dkp.dissent WHERE meeting_id=104 AND topic='dku_strictness'")
    if not r:
        db_tunnel.execute("""INSERT INTO dkp.dissent
            (meeting_id, topic, consensus_view, minority_view, minority_evidence, intensity)
            VALUES (104, 'dku_strictness',
            'ДКУ умеренно жесткие: реальные ставки положительны, неценовые условия жесткие, кредитные факторы временны',
            'ДКУ приблизились к нейтральным или умеренно мягкие',
            'корпоративный кредит высокими темпами; кредитный импульс в положительной области; снижение сберегательной активности; М2 выше диапазона 2016-2019',
            'soft')""")
        print("dissent 23.09 внесён")


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"
    if mode in ("all", "embed"):
        embed_args()
    if mode in ("all", "ingest"):
        ingest_summary()
    if mode in ("all", "markup"):
        fill_concern()
        make_dissent()
    print("готово")