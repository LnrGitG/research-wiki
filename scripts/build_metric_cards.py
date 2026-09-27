#!/usr/bin/env python3
"""Карточки метрик v2: описание, темы, свежесть, охват и векторный индекс.

Зачем: в базе ~4 тыс. метрик и миллионы наблюдений, но найти ряд можно только по коду.
Скрипт собирает по каждой метрике машиночитаемую карточку (единица, частота, источник,
охват регионов, период, свежесть, тематические метки), строит текстовое описание и
вектор (Яндекс text-search-doc, 256 измерений), кладёт всё в derived.metric_card.

Поиск: scripts/metric_search.py "<запрос>".
"""
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import time

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, 'scripts'))
import db_tunnel  # noqa: E402

FOLDER = 'b1gpe14c599s44v5dacm'  # ID каталога Yandex Cloud
API = 'https://llm.api.cloud.yandex.net/foundationModels/v1/textEmbedding'
CACHE = os.path.join(REPO, 'data', 'etl', 'metric-card-embed-cache.json')

DDL = """
CREATE TABLE IF NOT EXISTS derived.metric_card (
    metric_id       bigint PRIMARY KEY,
    metric_code     text NOT NULL,
    name_ru         text,
    description     text,
    unit_code       text,
    unit_ru         text,
    frequency_ru    text,
    sources         text[],
    themes          text[],
    level           text,
    n_obs           integer,
    n_regions       integer,
    period_min      date,
    period_max      date,
    freshness_days  integer,
    status          text,
    search_text     text,
    embedding       vector(256),
    built_at        timestamptz DEFAULT now(),
    embedded_at     timestamptz
);
CREATE INDEX IF NOT EXISTS metric_card_code_idx ON derived.metric_card (metric_code);
CREATE INDEX IF NOT EXISTS metric_card_themes_idx ON derived.metric_card USING gin (themes);
CREATE INDEX IF NOT EXISTS metric_card_search_trgm ON derived.metric_card USING gin (search_text gin_trgm_ops);
"""

# Тематические правила: ключевые фрагменты -> тема. Порядок важен (первое совпадение не мешает остальным).
THEME_RULES = [
    ('ипотека', ['ипотеч', 'ижк', 'mortgage', 'vmd', 'vhdt', 'vhlvt', 'vsdt', 'vsrr', 'vscr', 'vsvr',
                 'oipfl', 'spsipfl', 'irz', 'izhk', 'zhilich', 'жилищн кред']),
    ('жильё и строительство', ['ввод жил', 'жилищн строит', 'строительств', 'смр', 'подряд', 'ижс',
                               'квартир', 'кв.м', 'жилой дом', 'жилых дом', 'domrf', 'дом.рф', 'объём работ']),
    ('цены и инфляция', ['инфляц', 'ипц', 'базов', 'дефлятор', 'удорожание', 'цена', 'цен ']),
    ('кредит и денежная политика', ['кредит', 'ставк', 'ключев', 'процент', 'дкп', 'денежн', 'м0', 'м1', 'м2',
                                    'банк', 'вклад', 'депозит', 'задолженност']),
    ('труд и занятость', ['безработ', 'занятост', 'зарплат', 'оплата труда', 'ваканс', 'работник',
                          'трудовых ресурс', 'мото', 'trud']),
    ('налоги и бюджет', ['налог', 'взнос', 'бюджет', 'ндфл', 'ндс', 'акциз', 'госдолг', 'трансферт',
                         'доходы бюджет', 'расходы бюджет', 'фнс', 'крист']),
    ('население и демография', ['населен', 'рождаем', 'смертн', 'миграц', 'демограф', 'численност',
                                'возраст', 'ожидаемая продолжительность']),
    ('корпоративный сектор', ['юрлиц', 'юридических лиц', 'корпоратив', 'прибыл', 'предприят', 'компани',
                              'индивидуальных предпринимател']),
    ('потребительский спрос', ['потреб', 'розниц', 'платных услуг', 'ккт', 'чек', 'касс', 'домохозяйств',
                               'оборот торговли']),
    ('промышленность', ['промышл', 'производств', 'добыч', 'обрабатыв', 'электроэнерг', 'выпуск товаров']),
    ('внешний сектор', ['экспорт', 'импорт', 'валют', 'курс', 'нефт', 'газ', 'внешнеторг']),
    ('региональная экономика', ['субъект', 'регион', 'федеральн округ', 'муниципал', 'консолидирован']),
    ('уровень жизни', ['реальные располагаемые', 'уровень жизни', 'прожиточн', 'бедност', 'неравенств']),
]

FREQ_RU = {'A': 'годовая', 'D': 'дневная', 'M': 'месячная', 'Q': 'квартальная',
           '3': 'годовая', '4': 'дневная', '5': 'месячная', '6': 'квартальная'}


def api_key():
    for line in open(os.path.expanduser('~/.hermes/.env'), encoding='utf-8'):
        if line.startswith('YANDEX_CLOUD_API_KEY='):
            return line.split('=', 1)[1].strip().strip('"').strip("'")
    raise SystemExit('YANDEX_CLOUD_API_KEY не найден в ~/.hermes/.env')


KEY = None


def embed(text, retries=3):
    global KEY
    if KEY is None:
        KEY = api_key()
    body = json.dumps({'modelUri': 'emb://%s/text-search-doc/latest' % FOLDER,
                       'text': text[:4000]}, ensure_ascii=False)
    for attempt in range(retries):
        r = subprocess.run(['curl', '-s', '-m', '40', '-X', 'POST', API,
                            '-H', f'Authorization: Api-Key {KEY}',
                            '-H', 'Content-Type: application/json',
                            '--data-binary', '@-'], input=body, capture_output=True, text=True)
        try:
            v = json.loads(r.stdout).get('embedding')
            if v and len(v) == 256:
                return v
        except (json.JSONDecodeError, AttributeError):
            pass
        time.sleep(1.5 * (attempt + 1))
    return None


def themes_of(text, extra_tags):
    low = text.lower()
    out = []
    for theme, keys in THEME_RULES:
        if any(k in low for k in keys):
            out.append(theme)
    for t in (extra_tags or []):
        if t and t not in out and t in ('emiss', 'operational', 'housing', 'fns', 'cbr', 'rosstat'):
            out.append(t)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--skip-embed', action='store_true')
    ap.add_argument('--limit', type=int, default=0)
    args = ap.parse_args()

    conn = db_tunnel.connect()
    with conn.cursor() as cur:
        cur.execute(DDL)
    conn.commit()

    sql = """
    SELECT m.metric_id, m.metric_code, coalesce(m.name_ru,''), coalesce(m.description,''),
           coalesce(u.unit_code,''), coalesce(u.name_ru,''), coalesce(f.frequency_code,'5'), coalesce(f.name_ru,''),
           coalesce(array_agg(DISTINCT s.source_code) FILTER (WHERE s.source_code IS NOT NULL), '{}'),
           count(*) FILTER (WHERE o.observation_status <> 'rejected'),
           count(DISTINCT o.region_id) FILTER (WHERE o.observation_status <> 'rejected'),
           min(o.period_start), max(o.period_start),
           coalesce(m.tags, '{}'), coalesce(m.status,'active')
    FROM core.metric m
    LEFT JOIN core.unit u ON u.unit_id = m.unit_id
    LEFT JOIN core.frequency f ON f.frequency_id = m.frequency_id
    LEFT JOIN core.observation_v2 o ON o.metric_id = m.metric_id
    LEFT JOIN core.source s ON s.source_id = o.source_id
    GROUP BY 1,2,3,4,5,6,7,8,14,15
    HAVING count(*) FILTER (WHERE o.observation_status <> 'rejected') > 0
    ORDER BY 2
    """
    rows = db_tunnel.query(sql)
    if args.limit:
        rows = rows[:args.limit]
    print(f'метрик с наблюдениями: {len(rows)}')

    from datetime import date
    cache = {}
    if os.path.exists(CACHE):
        try:
            cache = json.load(open(CACHE, encoding='utf-8'))
        except (json.JSONDecodeError, OSError):
            cache = {}

    payload, n_emb, n_fail = [], 0, 0
    for (mid, code, name, descr, ucode, uru, fcode, fru, srcs, n_obs, n_reg, pmin, pmax, tags, status) in rows:
        themes = themes_of(' '.join([name, descr, code, ' '.join(srcs or [])]), tags)
        level = 'региональный' if (n_reg or 0) > 3 else 'федеральный'
        fresh = (date.today() - pmax).days if pmax else None
        src_txt = ', '.join(sorted(srcs or [])) or '—'
        text = (f'{name}. {descr}. '
                f'Источник данных: {src_txt}. Единица измерения: {uru or ucode or "—"}. '
                f'Частота: {fru or FREQ_RU.get(fcode, "—")}. Уровень: {level}. '
                f'Темы: {", ".join(themes) if themes else "—"}. '
                f'Охват: {n_obs} наблюдений, {n_reg} регионов, период {pmin}..{pmax}. '
                f'Свежесть: последние данные за {pmax}. Код метрики: {code}.')
        text = re.sub(r'\s+', ' ', text).strip()
        h = hashlib.sha256(text.encode('utf-8')).hexdigest()
        vec = cache.get(code)
        if not vec or cache.get(code + '|h') != h:
            vec = None
        payload.append((mid, code, name, descr, ucode, uru, fru or FREQ_RU.get(fcode, ''), list(srcs or []),
                        themes, level, n_obs, n_reg, pmin, pmax, fresh, status, text, (h, vec)))
        if vec:
            n_emb += 1

    if not args.skip_embed:
        conn = db_tunnel.connect()
        with conn.cursor() as cur:
            for i, rec in enumerate(payload):
                vec = rec[-1][1]
                if not vec:
                    v = embed(rec[16])
                    if v:
                        cache[rec[1]] = v
                        cache[rec[1] + '|h'] = rec[-1][0]
                        rec = list(rec)
                        rec[-1] = (rec[-1][0], v)
                        payload[i] = tuple(rec)
                        n_emb += 1
                    else:
                        n_fail += 1
                if (i + 1) % 200 == 0:
                    print(f'  вложение {i+1}/{len(payload)} (в кэше {n_emb}, сбоев {n_fail})', flush=True)
                    json.dump(cache, open(CACHE, 'w', encoding='utf-8'))
                time.sleep(0.05)
            cur.executemany("""
                INSERT INTO derived.metric_card (metric_id, metric_code, name_ru, description, unit_code, unit_ru,
                    frequency_ru, sources, themes, level, n_obs, n_regions, period_min, period_max,
                    freshness_days, status, search_text, embedding, embedded_at)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s::vector, now())
                ON CONFLICT (metric_id) DO UPDATE SET
                    metric_code=EXCLUDED.metric_code, name_ru=EXCLUDED.name_ru, description=EXCLUDED.description,
                    unit_code=EXCLUDED.unit_code, unit_ru=EXCLUDED.unit_ru, frequency_ru=EXCLUDED.frequency_ru,
                    sources=EXCLUDED.sources, themes=EXCLUDED.themes, level=EXCLUDED.level, n_obs=EXCLUDED.n_obs,
                    n_regions=EXCLUDED.n_regions, period_min=EXCLUDED.period_min, period_max=EXCLUDED.period_max,
                    freshness_days=EXCLUDED.freshness_days, status=EXCLUDED.status, search_text=EXCLUDED.search_text,
                    embedding=EXCLUDED.embedding, embedded_at=now(), built_at=now()
            """, [r[:17] + ('[' + ','.join(repr(float(x)) for x in r[17][1]) + ']',) for r in payload])
        conn.commit()
        json.dump(cache, open(CACHE, 'w', encoding='utf-8'))

    in_db = db_tunnel.query('SELECT count(*), count(embedding) FROM derived.metric_card')
    print(f'карточек в базе: {in_db[0][0]}, с вектором: {in_db[0][1]}, сбоев вложения: {n_fail}')
    print('темы:', db_tunnel.query("""SELECT t, count(*) FROM derived.metric_card, unnest(themes) AS t
        GROUP BY 1 ORDER BY 2 DESC LIMIT 15"""))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())