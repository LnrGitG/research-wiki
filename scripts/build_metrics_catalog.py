#!/usr/bin/env python3
"""
Генерация каталога метрик для GitHub Pages.

Собирает статистику по каждой метрике из витрины core.v_datalens_observations
и пишет два файла:
  docs/metrics-catalog.json   — основной каталог (оценки, периоды, покрытие);
  docs/metrics-details.json   — детали источника, грузятся по клику.

Разделение сделано по размеру: детали добавляют ~0.5 МБ, и держать их в
основном файле означало бы грузить их на каждом открытии страницы.

Оценки полезности:
- op  (оперативный анализ, 0–10): частота ряда (месячные весят больше),
  свежесть данных, широта географии, доля свежих наблюдений.
- res (исследования, 0–10): длина ряда в годах, панельная структура
  (число регионов), объём наблюдений, отсутствие накопительного характера.

Детали источника — то, чем метрику можно идентифицировать: метки релизов
с типом (сборник / файл / раздел / техническая), теги гармонизации, единицы
и примеры разрезов.

ВАЖНО про фильтр значений: плейсхолдеры Росстата -99999999 («нет
информации») и -77777777 («скрыто») исключаются, всё остальное — включая
нули и отрицательные проценты — учитывается. Фильтр `value > 0` был ошибкой:
он отбрасывал 416 652 строки (19% данных), из которых 93% легитимны.

ВАЖНО про память: агрегация всей витрины одним запросом (2.17 млн строк,
count(DISTINCT sub_dimension) без индекса) приводила к OOM. Поэтому запрос
идёт батчами по BATCH метрик, а результат каждого батча сразу дописывается
в JSONL-файл состояния. Память ограничена размером батча, прогресс не
теряется при сбое.

Запуск:  python3 scripts/build_metrics_catalog.py
"""
import json
import os
import re
import sys
from collections import Counter, defaultdict

import psycopg

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from normalize_units import normalize_unit

os.environ.setdefault("PGPASSFILE", os.path.expanduser("~/.pgpass"))
# Порт тоннеля 15432, хост строго 127.0.0.1: локального PostgreSQL на VDS нет
# (5432 — connection refused), а ~/.pgpass сопоставляется буквально, и при
# host=localhost драйвер скажет «no password supplied».
DSN = os.environ.get("PGDSN",
                     "host=127.0.0.1 port=15432 dbname=research_wiki user=wiki")
DOCS = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs"))
OUT_CAT = os.path.join(DOCS, "metrics-catalog.json")
OUT_DET = os.path.join(DOCS, "metrics-details.json")
STATE = os.path.join(DOCS, ".metrics-catalog-state.jsonl")

BATCH = 25
PLACEHOLDERS = (-99999999, -77777777)
# плейсхолдеры пишем явно, чтобы индекс/план не зависел от параметров
VAL_OK = "value IS NOT NULL AND value NOT IN (-99999999, -77777777)"

CATALOG_RE = re.compile(r"^(Регионы России|Жилищное хозяйство|Строительство в России|"
                        r"Инвестиции в России|Цены в России|Социальное положение|"
                        r"Российский статистический ежегодник|Труд и занятость)")
FILE_RE = re.compile(r"^(Stroit|Pril|Ejegodnik|Rosstat|roschart|vv-|info-stat|cbr_bulletin|"
                     r"gdp-quarters|vds_|rosstat_)", re.I)
SECTION_RE = re.compile(r"(\d+\.\d+(\.\d+)?|\bTable\s+\d+|R[-_]\d+|R-\d)")
TECH_RE = re.compile(r"(перенос из SQLite|ряды$|^rosstat ряды|^fns ряды|^rosreestr ряды|"
                     r"^smart-lab$|^cbr_api|^domrf_priceindex)")


def classify(rel):
    """Тип метки релиза: catalog | file | section | tech | other."""
    r = str(rel)
    if TECH_RE.search(r):
        return "tech"
    if CATALOG_RE.match(r):
        return "catalog"
    if SECTION_RE.search(r):
        return "section"
    if FILE_RE.match(r):
        return "file"
    return "other"


def score_operational(freqs, y1, recent, total, nreg):
    s = 3 if "M" in freqs else (2 if "Q" in freqs else 0)
    s += 3 if y1 >= 2026 else (1 if y1 >= 2025 else 0)
    if total:
        s += min(2, int(3 * recent / total))
    s += 2 if nreg >= 60 else (1 if nreg >= 20 else 0)
    return s


def score_research(freqs, y0, y1, nyears, nreg, total):
    s = 3 if nyears >= 20 else (2 if nyears >= 10 else (1 if nyears >= 5 else 0))
    s += 3 if nreg >= 60 else (2 if nreg >= 20 else (1 if nreg >= 5 else 0))
    s += 2 if total >= 5000 else (1 if total >= 1000 else 0)
    s += 1 if (y1 - y0 + 1) >= 20 else 0
    s += 1 if not ("M" in freqs or "Q" in freqs) else 0
    return s


def fetch_batch(cur, codes=None):
    """Все агрегаты каталога без тяжёлых DISTINCT по широкой view.

    Прежняя версия считала min/max/count(DISTINCT ...) прямо по
    core.v_datalens_observations: это 6,5 млн строк на 30 колонок, и на ВМ
    (work_mem 4 МБ, temp_file_limit 1,5 ГБ, диск 10 ГБ) сортировка уходила в
    base/pgsql_tmp и упиралась сначала в лимит, потом в «No space left on
    device» (инцидент 02.11.2026). Теперь узкие DISTINCT идут вместе с
    основными числами, а число уникальных подразрезов считается отдельно по
    парам «метрика — подразрез»: промежуточных данных на порядок меньше.
    Параметр `codes` оставлен для разовых прогонов по части справочника.
    """
    flt = " AND o.metric_id = ANY(%s)" if codes else ""
    args = (codes,) if codes else ()
    ok = VAL_OK.replace("value", "o.value")
    # параллельные воркеры множат временные файлы — на этой ВМ их лучше выключить
    cur.execute("SET max_parallel_workers_per_gather = 0")
    cur.execute("SET work_mem = '1GB'")

    # 1. основные числа — без DISTINCT: count(DISTINCT ...) по 6,5 млн строк
    #    Postgres считает сортировкой и снова упирается в temp_file_limit.
    cur.execute(f"""
        SELECT m.metric_code, m.name_ru, m.unit_id,
               min(extract(year from o.period_start))::int,
               max(extract(year from o.period_start))::int,
               count(*),
               count(*) FILTER (WHERE extract(year from o.period_start) >= 2025)
        FROM core.observation_v2 o
        JOIN core.metric m ON m.metric_id = o.metric_id
        WHERE {ok}{flt}
        GROUP BY 1,2,3
    """, args)
    base = {r[0]: list(r) for r in cur.fetchall()}

    # 1б. уникальные годы, регионы, релизы и частоты — по схлопнутым парам
    pairs = {
        "years": "extract(year from o.period_start)::int",
        "regions": "o.region_id",
        "releases": "o.release_id",
    }
    extra = {}
    for key, expr in pairs.items():
        cur.execute(f"""
            SELECT x.metric_code, count(*) FROM (
                SELECT m.metric_code AS metric_code, {expr} AS v
                FROM core.observation_v2 o
                JOIN core.metric m ON m.metric_id = o.metric_id
                WHERE {ok}{flt}
                GROUP BY 1,2) x
            GROUP BY 1
        """, args)
        extra[key] = {c: n for c, n in cur.fetchall()}

    cur.execute(f"""
        SELECT x.metric_code, string_agg(x.code, ',' ORDER BY x.code) FROM (
            SELECT m.metric_code AS metric_code, f.frequency_code AS code
            FROM core.observation_v2 o
            JOIN core.metric m ON m.metric_id = o.metric_id
            JOIN core.frequency f ON f.frequency_id = o.frequency_id
            WHERE {ok}{flt}
            GROUP BY 1,2) x
        GROUP BY 1
    """, args)
    freqs = {c: v for c, v in cur.fetchall()}

    # 2. число уникальных подразрезов — по схлопнутым парам
    cur.execute(f"""
        SELECT x.metric_code, count(*) FROM (
            SELECT m.metric_code AS metric_code, o.sub_dimension
            FROM core.observation_v2 o
            JOIN core.metric m ON m.metric_id = o.metric_id
            WHERE {ok}{flt}
            GROUP BY 1,2) x
        GROUP BY 1
    """, args)
    nsubd = {c: n for c, n in cur.fetchall()}

    # 3. источник и единица (справочники, по одной строке на метрику)
    cur.execute(f"""
        SELECT m.metric_code, min(s.name_ru), min(u.name_ru)
        FROM core.observation_v2 o
        JOIN core.metric m ON m.metric_id = o.metric_id
        LEFT JOIN core.source s ON s.source_id = o.source_id
        LEFT JOIN core.unit u ON u.unit_id = m.unit_id
        WHERE {ok}{flt}
        GROUP BY 1
    """, args)
    lookup = {c: (sname, uname) for c, sname, uname in cur.fetchall()}

    stats = {}
    for code, r in base.items():
        sname, uname = lookup.get(code, (None, None))
        stats[code] = (code, r[1], sname, uname, r[3], r[4], r[5], r[6],
                       extra["years"].get(code, 0), extra["regions"].get(code, 0),
                       freqs.get(code, ""), extra["releases"].get(code, 0),
                       nsubd.get(code, 0))

    # 4. метки релизов (топ-8 на пару метрика+источник)
    cur.execute(f"""
        SELECT metric_code, source_name, release_label, n FROM (
          SELECT m.metric_code, s.name_ru AS source_name, rl.release_label, count(*) n,
                 row_number() OVER (PARTITION BY m.metric_code, s.name_ru
                                    ORDER BY count(*) DESC) rn
          FROM core.observation_v2 o
          JOIN core.metric m ON m.metric_id = o.metric_id
          LEFT JOIN core.source s ON s.source_id = o.source_id
          LEFT JOIN core.release rl ON rl.release_id = o.release_id
          WHERE {ok} AND rl.release_label IS NOT NULL{flt}
          GROUP BY 1,2,3) x WHERE rn <= 8
    """, args)
    rels = defaultdict(lambda: defaultdict(list))
    for code, src, rel, _n in cur.fetchall():
        rels[code][src].append(rel)

    # 5. единица из разрезов (сразу извлекаем — кардинальность падает)
    cur.execute(f"""
        SELECT y.metric_code, y.u, count(*) FROM (
            SELECT m.metric_code AS metric_code,
                   (regexp_match(o.sub_dimension, 'ед\\.:\\s*([^|]+)'))[1] AS u
            FROM core.observation_v2 o
            JOIN core.metric m ON m.metric_id = o.metric_id
            WHERE {ok} AND o.sub_dimension LIKE '%%ед.:%%'{flt}
            GROUP BY 1,2) y
        WHERE y.u IS NOT NULL
        GROUP BY 1,2
    """, args)
    units = defaultdict(Counter)
    for code, u, n in cur.fetchall():
        units[code][u.strip()] += n

    # 6. примеры разрезов (топ-3 на метрику)
    cur.execute(f"""
        SELECT metric_code, sub_dimension FROM (
          SELECT m.metric_code AS metric_code, o.sub_dimension, count(*) n,
                 row_number() OVER (PARTITION BY m.metric_code ORDER BY count(*) DESC) rn
          FROM core.observation_v2 o
          JOIN core.metric m ON m.metric_id = o.metric_id
          WHERE {ok} AND coalesce(o.sub_dimension,'') <> ''{flt}
          GROUP BY 1,2) z WHERE rn <= 3
    """, args)
    subs = defaultdict(list)
    for code, sd in cur.fetchall():
        subs[code].append(sd)

    # 7. теги гармонизации
    cur.execute("SELECT metric_code, tags FROM core.metric "
                "WHERE tags IS NOT NULL", ())
    tags = defaultdict(set)
    for code, t in cur.fetchall():
        tags[code].update(t or [])

    return stats, rels, units, subs, tags


def main():
    conn = psycopg.connect(DSN)
    cur = conn.cursor()
    # Агрегат идёт по 6,5 млн строк view. При work_mem=4 МБ (умолчание сервера)
    # планировщик выбирает сортировочную агрегацию и сливает её на диск: на ВМ
    # с 10 ГБ это упирается в «No space left on device» (инцидент 02.11.2026).
    # 256 МБ хватает, чтобы хеш-агрегация и оконные сортировки шли в памяти.
    cur.execute("SET work_mem = '256MB'")
    cur.execute("SET temp_file_limit = '1GB'")
    cur.execute("SELECT metric_code FROM core.metric ORDER BY metric_code")
    all_codes = [r[0] for r in cur.fetchall()]
    print("метрик в справочнике: %s" % format(len(all_codes), ","))

    if os.path.exists(STATE):
        os.remove(STATE)
    total_recs = 0
    stats, rels, units, subs, tags = fetch_batch(cur)
    print("агрегаты собраны: метрик со статистикой %s" % format(len(stats), ","))
    with open(STATE, "w", encoding="utf-8") as st:
        if True:
            for code in all_codes:
                r = stats.get(code)
                if not r:
                    continue
                (_c, name, src, unit, y0, y1, n, recent, nyears, nreg,
                 freqs, nrel, nsubd) = r
                y0, y1 = int(y0 or 0), int(y1 or 0)
                n, recent, nyears = int(n), int(recent), int(nyears)
                nreg, nrel, nsubd = int(nreg), int(nrel), int(nsubd)
                fl = [f for f in (freqs or "").split(",") if f]
                u_raw = units[code].most_common(1)[0][0] if units.get(code) else None
                u_sub = normalize_unit(u_raw)
                u_metric = unit if unit and unit != "—" else None
                rec = {
                    "c": code, "n": name, "s": src or "—",
                    "u": u_sub or u_metric or "—",
                    "um": u_metric or "—",
                    "uu": u_raw or "",
                    "y0": y0, "y1": y1, "sp": (y1 - y0 + 1) if y0 else 0,
                    "r": n, "rec": recent, "ny": nyears, "nr": nreg, "f": fl,
                    "rel": nrel, "sd": nsubd,
                    "op": score_operational(fl, y1, recent, n, nreg),
                    "res": score_research(fl, y0, y1, nyears, nreg, n),
                }
                det = {}
                if rels.get(code) or subs.get(code) or tags.get(code) or u_raw:
                    det = {
                        "srcs": [{"s": s, "rel": [{"l": x, "k": classify(x)} for x in lst]}
                                 for s, lst in rels.get(code, {}).items()],
                        "tags": sorted(tags.get(code, [])),
                        "sub": subs.get(code, [])[:3],
                        "uu": u_raw or "",
                    }
                st.write(json.dumps({"rec": rec, "det": det}, ensure_ascii=False) + "\n")
                total_recs += 1
            print("  записано метрик: %d" % total_recs)
    conn.close()

    # сборка из состояния
    recs, dets, kinds = [], {}, Counter()
    with open(STATE, encoding="utf-8") as f:
        for line in f:
            o = json.loads(line)
            recs.append(o["rec"])
            if o["det"]:
                dets[o["rec"]["c"]] = o["det"]
                for s in o["det"]["srcs"]:
                    for rel in s["rel"]:
                        kinds[rel["k"]] += 1
    recs.sort(key=lambda x: (-x["res"], -x["r"]))
    os.makedirs(DOCS, exist_ok=True)
    with open(OUT_CAT, "w", encoding="utf-8") as f:
        json.dump(recs, f, ensure_ascii=False)
    with open(OUT_DET, "w", encoding="utf-8") as f:
        json.dump(dets, f, ensure_ascii=False)
    os.remove(STATE)

    print("\nметрик: %s" % format(len(recs), ","))
    print("каталог: %s (%.0f КБ)" % (OUT_CAT, os.path.getsize(OUT_CAT) / 1024))
    print("детали: %s (%.0f КБ)" % (OUT_DET, os.path.getsize(OUT_DET) / 1024))
    print("единиц уточнено из разрезов: %s"
          % sum(1 for r in recs if r["u"] != r["um"]))
    print("типы меток: %s" % dict(kinds))


if __name__ == "__main__":
    main()
