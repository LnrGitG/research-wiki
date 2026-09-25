# -*- coding: utf-8 -*-
"""
Извлечение полного коммуникационного стека с ленты
https://www.cbr.ru/dkp/mp_dec/decision_key_rate/ (88 записей):
  press_release -> dkp.statement (kind='press_release')
  statement (Заявление Председателя) -> dkp.statement (kind='chair_statement')
  summary (Резюме обсуждения) -> dkp.minutes
Соответствие meeting_id по дате из dkp.meeting.
Тела чанкуются и векторизуются (Яндекс text-search-doc 256-dim).
"""
import sys
import re
import time
import json
import subprocess
import urllib.request
import urllib.parse
import html as htmllib
import hashlib
from html.parser import HTMLParser

sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import query, execute  # noqa: E402

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
BASE = "https://www.cbr.ru"
DRY = "--dry" in sys.argv
LIMIT = 200
for a in sys.argv:
    if a.startswith("--limit="):
        LIMIT = int(a.split("=")[1])

# ---------------------------------------------------------------- utils

def http_get(url, timeout=30):
    """GET с ретраями; возвращает текст или None."""
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                raw = resp.read()
            for enc in ("utf-8", "cp1251"):
                try:
                    return raw.decode(enc)
                except UnicodeDecodeError:
                    continue
            return raw.decode("utf-8", errors="ignore")
        except Exception as e:
            print(f"    retry {attempt+1} {url}: {e}", flush=True)
            time.sleep(2 + attempt * 3)
    return None


class _Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self._skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self._skip += 1

    def handle_endtag(self, tag):
        if tag in ("script", "style") and self._skip:
            self._skip -= 1

    def handle_data(self, d):
        if not self._skip:
            self.parts.append(d)


from html.parser import HTMLParser  # noqa: E402  (двойной импорт безвреден)


def clean_text(html):
    p = _Text()
    p.feed(html)
    t = "".join(p.parts)
    t = t.replace("\xa0", " ").replace("&nbsp;", " ")
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r" ?\n ?", "\n", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()


def extract_releases(html):
    """Парсинг ленты: [(date_str, url, title)]."""
    blocks = re.split(r'document-regular_date">', html)
    rows = []
    for b in blocks[1:]:
        date = b[:10].strip()
        m = re.search(r'href="([^"]+)"', b)
        t = re.search(r'_visible">([^<]+)<', b)
        url = m.group(1) if m else None
        title = htmllib.unescape(t.group(1)).strip() if t else ""
        rows.append((date, url, title))
    return rows


def classify(url, title):
    if url and "file=" in url:
        return "press_release"
    if url and "summary_key_rate" in url:
        return "summary"
    if "Заявление" in title:
        return "chair_statement"
    if "Среднесрочный прогноз" in title:
        return "forecast_pdf"
    if "Комментарий" in title:
        return "comment_pdf"
    return "other"


# ------------------------------------------------------------- extractors

FOOT_MARKS = (
    "Противодействие коррупции", "Версия для слабовидящих",
    "Технические ресурсы", "О сайте Контакты",
)


def body_press_release(text):
    """Тело пресс-релиза: от заголовка решения до подвала."""
    i = text.find("Пресс-релиз")
    j = text.find("Банк России принял решение")
    if j < 0:
        j = text.find("Совет директоров Банка России")
    if j < 0:
        return None
    k = len(text)
    for mark in FOOT_MARKS:
        p = text.find(mark, j)
        if 0 < p < k:
            k = p
    return text[j:k].strip()


def body_chair_statement(text):
    """Стенограмма: от 'Добрый день!/вечер!' до подвала."""
    i = text.find("Добрый день")
    if i < 0:
        i = text.find("Добрый вечер")
    if i < 0:
        i = text.find("Уважаемые")
    if i < 0:
        return None
    k = len(text)
    for mark in FOOT_MARKS:
        p = text.find(mark, i)
        if 0 < p < k:
            k = p
    return text[i:k].strip()


def body_summary(text):
    """Резюме: от 'Участники обсуждения' до подвала."""
    i = text.find("Участники обсуждения")
    if i < 0:
        i = text.find("члены Совета директоров")
    if i < 0:
        return None
    k = len(text)
    for mark in FOOT_MARKS:
        p = text.find(mark, i)
        if 0 < p < k:
            k = p
    return text[i:k].strip()


FOLDER = "b1gpe14c599s44v5dacm"  # Янд. облако, folder id сервисного аккаунта

# ------------------------------------------------------------ embedding

EMB_URL = "https://llm.api.cloud.yandex.net/foundationModels/v1/textEmbedding"


def load_api_key():
    for line in open("/home/lnr/.hermes/.env", encoding="utf-8"):
        if line.startswith("YANDEX_CLOUD_API_KEY"):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    return None


_api_key = None


def embed(text):
    """Яндекс text-search-doc, 256-dim. Текст >8000 симв. — head-обрезка."""
    global _api_key
    if _api_key is None:
        _api_key = load_api_key()
    t = text[:8000]
    payload = json.dumps({
        "modelUri": "emb://%s/text-search-doc/latest" % FOLDER,
        "text": t,
    }).encode()
    req = urllib.request.Request(
        EMB_URL, data=payload, method="POST",
        headers={
            "Authorization": f"Api-Key {_api_key}",
            "Content-Type": "application/json",
        })
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                data = json.loads(resp.read())
            return data["embedding"]
        except Exception as e:
            print(f"    embed retry {attempt+1}: {str(e)[:120]}", flush=True)
            time.sleep(3 + attempt * 4)
    return None


# ------------------------------------------------------------ chunking

def chunk_text(text, size=900, overlap=150):
    paras = [p.strip() for p in text.split("\n\n") if p.strip()]
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


# ----------------------------------------------------------------- main

def main():
    rows_all = []
    html = http_get(BASE + "/dkp/mp_dec/decision_key_rate/")
    if not html:
        print("FATAL: лента не загрузилась")
        return 1
    rows_all = extract_releases(html)
    print(f"лента: {len(rows_all)} записей", flush=True)

    # соответствие дат -> meeting_id
    meetings = {str(r[1]): r[0] for r in
                query("SELECT meeting_id, meeting_date::text FROM dkp.meeting")}
    have_stmt = {str(r[1]): (r[0], r[2]) for r in query(
        "SELECT statement_id, event_date::text, kind FROM dkp.statement")}
    have_min = {str(r[1]): r[0] for r in query(
        "SELECT minutes_id, meeting_id::text FROM dkp.minutes")}

    stats = {"press_release": 0, "chair_statement": 0, "summary": 0,
             "skip_kind": 0, "no_meeting": 0, "fail": 0}

    for date, url, title in rows_all:
        kind = classify(url, title)
        if kind in ("forecast_pdf", "comment_pdf", "other"):
            stats["skip_kind"] += 1
            continue
        # дата ленты в формате ДД.ММ.ГГГГ -> ISO
        dmy = date.split(".")
        iso_date = "%s-%s-%s" % (dmy[2], dmy[1], dmy[0]) if len(dmy) == 3 else date
        if kind == "summary":
            # Резюме публикуется через ~2 недели после заседания:
            # привязываем к последнему заседанию <= даты публикации
            got = query(
                "SELECT meeting_id FROM dkp.meeting "
                "WHERE meeting_date <= '%s' ORDER BY meeting_date DESC LIMIT 1" % iso_date)
            mid = got[0][0] if got else None
        else:
            mid = meetings.get(iso_date)
        if not mid:
            print(f"  ! нет meeting для {date} ({kind})")
            stats["no_meeting"] += 1
            continue
        full_url = BASE + url if url and url.startswith("/") else url

        if kind == "press_release":
            # дедуп по (meeting_id, kind) в statement
            dup = query(
                "SELECT count(*) FROM dkp.statement WHERE meeting_id=%s AND kind='press_release'"
                % mid)
            if DRY:
                print(f"  [dry] PR {date} mid={mid}")
                stats["press_release"] += 1
                continue
            if dup[0][0]:
                stats["skip_kind"] += 1
                continue
            page = http_get(full_url)
            body = body_press_release(clean_text(page)) if page else None
            if not body or len(body) < 300:
                print(f"  FAIL PR {date}: body={len(body) if body else 0}")
                stats["fail"] += 1
                continue
            insert_document(kind, date, mid, full_url, body, stats)

        elif kind == "chair_statement":
            if DRY:
                print(f"  [dry] ST {date} mid={mid}")
                stats["chair_statement"] += 1
                continue
            # дедуп: существующее заявление того же вида на то же заседание
            dupst = query("SELECT count(*) FROM dkp.statement WHERE meeting_id=%s AND kind='chair_statement'" % mid)
            if dupst[0][0]:
                stats["skip_kind"] += 1
                continue
            page = http_get(full_url)
            body = body_chair_statement(clean_text(page)) if page else None
            if not body or len(body) < 200:
                print(f"  FAIL ST {date}: body={len(body) if body else 0}")
                stats["fail"] += 1
                continue
            insert_document(kind, date, mid, full_url, body, stats)

        elif kind == "summary":
            if DRY:
                print(f"  [dry] MIN {date} mid={mid}")
                stats["summary"] += 1
                continue
            # minutes уникальны по meeting_id
            dupm = query("SELECT count(*) FROM dkp.minutes WHERE meeting_id=%s" % mid)
            if dupm[0][0]:
                stats["skip_kind"] += 1
                continue
            page = http_get(full_url)
            body = body_summary(clean_text(page)) if page else None
            if not body or len(body) < 200:
                print(f"  FAIL MIN {date}: body={len(body) if body else 0}")
                stats["fail"] += 1
                continue
            insert_minutes(date, mid, full_url, body, stats)

    print("\nИТОГ:", json.dumps(stats, ensure_ascii=False), flush=True)
    return 0


def insert_document(kind, date, mid, url, body, stats):
    """INSERT в dkp.statement + чанки + эмбеддинги."""
    dmy = date.split(".")
    iso_date = "%s-%s-%s" % (dmy[2], dmy[1], dmy[0]) if len(dmy) == 3 else date
    chunks = chunk_text(body)
    embs = []
    for c in chunks:
        e = embed(c)
        if e is None:
            print(f"  embed FAIL {kind} {date}")
            stats["fail"] += 1
            return
        embs.append(e)
    # основной ряд
    q = ("INSERT INTO dkp.statement (kind, event_date, meeting_id, url, body) "
         "VALUES ('%s','%s',%s,'%s','%s') RETURNING statement_id"
         % (kind, iso_date, mid, url.replace("'", "''"), body.replace("'", "''")))
    r = execute(q)
    sid = None
    got = query("SELECT statement_id FROM dkp.statement WHERE meeting_id=%s AND kind='%s' ORDER BY statement_id DESC LIMIT 1" % (mid, kind))
    if got:
        sid = got[0][0]
    # чанки-векторы: перезаписываем body-ряд embedding'ом первого чанка,
    # полные чанки — в kb.chunk (document_id=созданного dkp-документа не требуется;
    # векторы кладём прямо в dkp.statement.embedding — только первый чанк) — упрощение:
    if sid:
        vec = "[%s]" % ",".join("%.7f" % x for x in embs[0])
        try:
            execute("UPDATE dkp.statement SET embedding='%s'::vector WHERE statement_id=%s"
                    % (vec, sid))
            print(f"  + {kind} {date} mid={mid} chunks={len(chunks)} len={len(body)}")
        except Exception as e:
            print(f"  embed UPDATE FAIL {kind} {date}: {str(e)[:100]}")
    stats[kind] += 1


def insert_minutes(date, mid, url, body, stats):
    chunks = chunk_text(body)
    e0 = embed(chunks[0])
    if e0 is None:
        print(f"  embed FAIL minutes {date}")
        stats["fail"] += 1
        return
    q = ("INSERT INTO dkp.minutes (meeting_id, url, body) "
         "VALUES (%s,'%s','%s')" % (mid, url.replace("'", "''"), body.replace("'", "''")))
    execute(q)
    got = query("SELECT minutes_id FROM dkp.minutes WHERE meeting_id=%s ORDER BY minutes_id DESC LIMIT 1" % mid)
    if got and e0:
        vec = "[%s]" % ",".join("%.7f" % x for x in e0)
        try:
            execute("UPDATE dkp.minutes SET embedding='%s'::vector WHERE minutes_id=%s"
                    % (vec, got[0][0]))
            print(f"  + minutes {date} mid={mid} chunks={len(chunks)} len={len(body)}")
        except Exception as e:
            print(f"  embed UPDATE FAIL minutes {date}: {str(e)[:100]}")
    stats["summary"] += 1


if __name__ == "__main__":
    sys.exit(main())