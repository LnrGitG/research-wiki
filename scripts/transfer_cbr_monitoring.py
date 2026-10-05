#!/usr/bin/env python3
"""Этап 2.2: ЦБ мониторинг (cbr_monitoring_* из rosstat_construction.db) → catalog + data.observation.

Вход: 3 таблицы SQLite на VPS:
  cbr_monitoring_api (312 612) — ОПРОС ЦБ «Мониторинг предприятий»: dataset (18 секторов+
    спец-срезы), size_group (4), adjustment (2), question (49), unit (пунктов|%),
    периоды M (2002-01…2026-08) и Q (2002Q1…2026Q2). Полный ключ: M 300 комбинаций
    (dataset|size|adj|question) × ~290 мес + квартальные × 100 кв.
  cbr_monitoring_construction (6 808) — срез «Строительство» без size-групп,
    12 вопросов × 296 мес.
  cbr_monitoring_invest_factors (728) — факторы инвестиций, 7 факторов × 4 группы
    × 26 кварталов (Q, %).

Ключ метрики: cbrmon__<dataset>__<size>__<adj>__<question_slug> — слаг из
транслита вопроса. Частота метрики M/Q по формату периода.
Дамп исходника: yc-s3:wiki-research/backups/transfers/cbr_monitoring_dump_20261006.db (99,5 МБ).
Точка возврата: DELETE data.observation по релизу + DELETE метрик cbrmon_%.

Правила проекта: приёмка до доклада; value-сверка round-4.
"""
import re
import sqlite3
import sys
import unicodedata
from datetime import date

sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
import db_tunnel

WIKI = "/home/lnr/research-wiki-private"
SRC_DB = f"{WIKI}/data/rosstat_construction.db"
SOURCE_ID = 7  # cbr
RELEASE_LABEL = "cbr_monitoring_v2 (перенос из sqlite, этап 2.2)"
UNIT_MAP = {"пунктов": 37, "%": 12}  # ratio=37 (пункты индикатора), pct=12
FREQ_M, FREQ_Q = 5, 6

SLUG_TRANS = {
    "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ё": "e", "ж": "zh",
    "з": "z", "и": "i", "й": "y", "к": "k", "л": "l", "м": "m", "н": "n", "о": "o",
    "п": "p", "р": "r", "с": "s", "т": "t", "у": "u", "ф": "f", "х": "h", "ц": "ts",
    "ч": "ch", "ш": "sh", "щ": "sch", "ъ": "", "ы": "y", "ь": "", "э": "e", "ю": "yu",
    "я": "ya",
}


def slug(s, maxlen=60):
    s = unicodedata.normalize("NFKC", s).strip().lower().replace("ё", "е").replace("\xa0", " ")
    s = "".join(SLUG_TRANS.get(ch, ch) for ch in s)
    s = re.sub(r"[^a-z0-9]+", "_", s).strip("_")
    return s[:maxlen].rstrip("_")


def period_mq(p):
    """(period_start, freq_id) из '2002-01-01' | '2002Q1'."""
    if re.fullmatch(r"\d{4}Q[1-4]", p):
        y, q = int(p[:4]), int(p[5])
        return date(y, 3 * (q - 1) + 1, 1).isoformat(), FREQ_Q
    y, m, d = map(int, p.split("-"))
    return date(y, m, 1).isoformat(), FREQ_M


def main():
    sq = sqlite3.connect(f"file:{SRC_DB}?mode=ro", uri=True)
    conn = db_tunnel.connect()
    cur = conn.cursor()

    cur.execute("SELECT release_id FROM catalog.release WHERE source_id=%s AND label=%s",
                (SOURCE_ID, RELEASE_LABEL))
    row = cur.fetchone()
    if row:
        release_id = row[0]
        print("релиз существует:", release_id)
    else:
        cur.execute("""INSERT INTO catalog.release (source_id, label, published_at, status, notes)
                       VALUES (%s,%s,%s,'loaded','Полный срез cbr_monitoring_v2, перенос из sqlite (этап 2.2)')
                       RETURNING release_id""", (SOURCE_ID, RELEASE_LABEL, "2026-10-05"))
        release_id = cur.fetchone()[0]
        conn.commit()
        print("создан release_id:", release_id)

    mids = {}
    cur.execute("SELECT metric_code, metric_id FROM catalog.metric WHERE metric_code LIKE 'cbrmon_%'")
    for c_, mid in cur.fetchall():
        mids[c_] = mid

    obs = []  # (metric_code, region_id_rf, freq, period_start, value)

    def ensure_metric(code, name_ru, unit_id, freq_id):
        if code in mids:
            return mids[code]
        cur.execute("""INSERT INTO catalog.metric (metric_code, name_ru, unit_id, source_id,
                       frequency_id, metric_type, is_derived, status, tags)
                       VALUES (%s,%s,%s,%s,%s,'primary',false,'active','{cbr_survey}')
                       RETURNING metric_id""",
                    (code, name_ru, unit_id, SOURCE_ID, freq_id))
        mids[code] = cur.fetchone()[0]
        return mids[code]

    # --- cbr_monitoring_api ---
    regions = {n: rid for rid, n in cur.execute("SELECT region_id, name_ru FROM catalog.region")}
    rid_rf = regions["Российская Федерация"]
    n_miss_unit = 0
    for ds, sg, adj, question, unit, period, val, src_ in sq.execute(
            "SELECT dataset, size_group, adjustment, question, unit, period, value, source FROM cbr_monitoring_api WHERE value IS NOT NULL"):
        ps, freq = period_mq(period)
        uid = UNIT_MAP.get(unit)
        if uid is None:
            n_miss_unit += 1
            continue
        code = f"cbrmon__{slug(ds)}__{slug(sg)}__{slug(adj)}__{slug(question)}"
        name = f"{question} — {ds} / {sg} / {adj} (ЦБ мониторинг)"
        ensure_metric(code, name, uid, freq)
        # опрос секторальный: регион — РФ (сектор живёт в составе кода метрики)
        obs.append((code, rid_rf, freq, ps, float(val)))

    print("api строки:", len(obs), "| отказные unit:", n_miss_unit)

    # --- cbr_monitoring_construction (все — строительство, без size) ---
    for question, adj, unit, d, val, src_ in sq.execute(
            "SELECT question, adjustment, unit, date, value, source FROM cbr_monitoring_construction WHERE value IS NOT NULL"):
        ps, freq = period_mq(d)
        uid = UNIT_MAP.get(unit)
        if uid is None:
            n_miss_unit += 1
            continue
        code = f"cbrmon__stroitelstvo__vse__{slug(adj)}__{slug(question)}"
        name = f"{question} — Строительство / все группы / {adj} (ЦБ мониторинг)"
        ensure_metric(code, name, uid, freq)
        obs.append((code, rid_rf, freq, ps, float(val)))

    # --- cbr_monitoring_invest_factors (квартальные) ---
    for sg, factor, period, val, src_ in sq.execute(
            "SELECT size_group, factor, period, value, source FROM cbr_monitoring_invest_factors WHERE value IS NOT NULL"):
        ps, freq = period_mq(period)
        code = f"cbrmon__invest__{slug(sg)}__f__{slug(factor)}"
        name = f"{factor} — инвестиционный фактор / {sg} (ЦБ опрос, % доля)"
        ensure_metric(code, name, UNIT_MAP["%"], freq)
        obs.append((code, rid_rf, freq, ps, float(val)))

    conn.commit()
    print("всего строк собрано:", len(obs), "| метрик:", len(mids))

    # вставка через COPY во временную таблицу + INSERT SELECT ON CONFLICT
    # (executemany падал DatatypeMismatch на 300+ тыс. строк — обход через COPY)
    import io
    cur.execute("DROP TABLE IF EXISTS _tmp_cbrmon_obs")
    cur.execute("CREATE TEMP TABLE _tmp_cbrmon_obs (metric_id integer, region_id integer, period_start date, frequency_id integer, value numeric, source_id integer, release_id integer)")
    buf = io.StringIO()
    for mc, r_, f, ps, v in obs:
        buf.write("	".join(map(str, (mids[mc], r_, ps, f, v, SOURCE_ID, release_id))) + "\n")
    buf.seek(0)
    with cur.copy("COPY _tmp_cbrmon_obs FROM STDIN") as cp:
        cp.write(buf.read())
    cur.execute("""
        INSERT INTO data.observation
        (metric_id,region_id,period_start,frequency_id,value,
         assessment_type,observation_status,source_id,release_id,sub_dimension)
        SELECT metric_id,region_id,period_start,frequency_id,value,
               'final','validated',source_id,release_id,''
        FROM _tmp_cbrmon_obs
        ON CONFLICT (metric_id,region_id,period_start,frequency_id,
                     assessment_type,sub_dimension,release_id) DO NOTHING""")
    conn.commit()
    cur.execute("DROP TABLE IF EXISTS _tmp_cbrmon_obs")
    print("вставка COPY завершена")
    n = cur.execute("SELECT count(*) FROM data.observation WHERE release_id=%s", (release_id,)).fetchone()[0]
    print("canon по релизу:", n)
    conn.close(); sq.close()
    import json
    json.dump({"release_id": release_id}, open("/tmp/cbrmon_state.json", "w"))


if __name__ == "__main__":
    main()
