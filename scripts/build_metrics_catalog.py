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
DSN = os.environ.get("PGDSN", "host=localhost port=5432 dbname=research_wiki user=wiki")
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


def fetch_batch(cur, codes):
    """Все агрегаты по одному батчу метрик."""
    # 1. основная статистика
    cur.execute(f"""
        SELECT metric_code, metric_name, min(source_name), min(unit_name),
               min(year), max(year), count(*),
               count(*) FILTER (WHERE year >= 2025),
               count(DISTINCT year), count(DISTINCT region_code),
               string_agg(DISTINCT frequency_code, ','),
               count(DISTINCT release_label), count(DISTINCT sub_dimension)
        FROM core.v_datalens_observations
        WHERE {VAL_OK} AND metric_code = ANY(%s)
        GROUP BY metric_code, metric_name
    """, (codes,))
    stats = {r[0]: r for r in cur.fetchall()}

    # 2. метки релизов (топ-8 на пару метрика+источник)
    cur.execute(f"""
        SELECT metric_code, source_name, release_label, n FROM (
          SELECT metric_code, source_name, release_label, count(*) n,
                 row_number() OVER (PARTITION BY metric_code, source_name
                                    ORDER BY count(*) DESC) rn
          FROM core.v_datalens_observations
          WHERE {VAL_OK} AND metric_code = ANY(%s) AND release_label IS NOT NULL
          GROUP BY 1,2,3) x WHERE rn <= 8
    """, (codes,))
    rels = defaultdict(lambda: defaultdict(list))
    for code, src, rel, _n in cur.fetchall():
        rels[code][src].append(rel)

    # 3. единица из разрезов (сразу извлекаем — кардинальность падает)
    cur.execute(f"""
        SELECT metric_code,
               (regexp_match(sub_dimension, 'ед\\.:\\s*([^|]+)'))[1] AS u,
               count(*) n
        FROM core.v_datalens_observations
        WHERE {VAL_OK} AND metric_code = ANY(%s) AND sub_dimension LIKE '%%ед.:%%'
        GROUP BY 1,2 ORDER BY 1, 3 DESC
    """, (codes,))
    units = defaultdict(Counter)
    for code, u, n in cur.fetchall():
        if u:
            units[code][u.strip()] += n

    # 4. примеры разрезов (топ-3 на метрику)
    cur.execute(f"""
        SELECT metric_code, sub_dimension FROM (
          SELECT metric_code, sub_dimension, count(*) n,
                 row_number() OVER (PARTITION BY metric_code ORDER BY count(*) DESC) rn
          FROM core.v_datalens_observations
          WHERE {VAL_OK} AND metric_code = ANY(%s)
            AND coalesce(sub_dimension,'') <> ''
          GROUP BY 1,2) x WHERE rn <= 3
    """, (codes,))
    subs = defaultdict(list)
    for code, sd in cur.fetchall():
        subs[code].append(sd)

    # 5. теги гармонизации
    cur.execute("SELECT metric_code, tags FROM core.metric "
                "WHERE tags IS NOT NULL AND metric_code = ANY(%s)", (codes,))
    tags = defaultdict(set)
    for code, t in cur.fetchall():
        tags[code].update(t or [])

    return stats, rels, units, subs, tags


def main():
    conn = psycopg.connect(DSN)
    cur = conn.cursor()
    cur.execute("SELECT metric_code FROM core.metric ORDER BY metric_code")
    all_codes = [r[0] for r in cur.fetchall()]
    print("метрик в справочнике: %s, батч: %d" % (format(len(all_codes), ","), BATCH))

    if os.path.exists(STATE):
        os.remove(STATE)
    nbatch = (len(all_codes) + BATCH - 1) // BATCH
    total_recs = 0
    with open(STATE, "w", encoding="utf-8") as st:
        for i in range(nbatch):
            codes = all_codes[i * BATCH:(i + 1) * BATCH]
            stats, rels, units, subs, tags = fetch_batch(cur, codes)
            for code in codes:
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
            print("  батч %d/%d: %d метрик, всего %d" % (i + 1, nbatch, len(codes), total_recs))
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
