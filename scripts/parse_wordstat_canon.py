#!/usr/bin/env python3
"""Канон-перевод: Wordstat (недельные срезы, ВМ csv) → catalog + data.observation.

Этап 3 «единый приёмный контур»: лоадер для будущих недельных выгрузок.
  - 2 метрики ws_phrases_raw / ws_composite_s25 (unit 29/37), частота W, регион РФ;
  - композит = comp4 (S2_mat+S3_mach+S4_b2b+S5_permits, БЕЗ S4_procure);
  - релиз 'yandex-wordstat <label>' (идемпотентно);
  - вставка COPY temp + INSERT SELECT ON CONFLICT;
  - приёмка: счёт + value-сверка против v2-эталона (is_current),
    допуск numeric(4) эталона 5.1e-5.
Запуск на ВМ: /home/ubuntu/venv/bin/python3 scripts/parse_wordstat_canon.py [label]
"""
import csv
import hashlib
import io
import sys

import psycopg

CSV = "/home/ubuntu/sandbox_datasets/wordstat_weekly_construction.csv"
PGDSN = "host=127.0.0.1 port=5432 dbname=research_wiki user=wiki"
SOURCE_ID = 30  # yandex

COMP4 = {"S2_mat", "S3_mach", "S4_b2b", "S5_permits"}
NAMES = {
    "ws_phrases_raw": ("Yandex Wordstat: поисковые запросы по фразам (конструкция), сырой счёт, шт, за неделю", 29),
    "ws_composite_s25": ("Yandex Wordstat: композитный спрос S2-S5 (сумма долей групп), доля, за неделю", 37),
}


def main(label):
    raw = open(CSV, "rb").read()
    sha = hashlib.sha256(raw).hexdigest()
    print("sha256:", sha[:16], "size:", len(raw))

    con = psycopg.connect(PGDSN)
    cur = con.cursor()
    fw = cur.execute("SELECT frequency_id FROM catalog.frequency WHERE freq_code='W'").fetchone()
    if fw:
        freq_w = fw[0]
    else:
        freq_w = cur.execute("INSERT INTO catalog.frequency (freq_code,name_ru) VALUES ('W','неделя') RETURNING frequency_id").fetchone()[0]
    rid = cur.execute("SELECT region_id FROM catalog.region WHERE region_code='ru'").fetchone()[0]

    rel = cur.execute("SELECT release_id FROM catalog.release WHERE source_id=%s AND label=%s", (SOURCE_ID, "yandex-wordstat " + label)).fetchone()
    if rel:
        release_id = rel[0]
        print("релиз существует:", release_id)
    else:
        release_id = cur.execute("""INSERT INTO catalog.release (source_id,label,published_at,status,notes)
            VALUES (%s,%s,%s,'loaded','wordstat срез, канон-путь (этап 3)') RETURNING release_id""",
            (SOURCE_ID, "yandex-wordstat " + label, label)).fetchone()[0]
        con.commit()
        print("release_id:", release_id)

    mids = {}
    for mc, (n_, unit) in NAMES.items():
        row = cur.execute("SELECT metric_id FROM catalog.metric WHERE metric_code=%s", (mc,)).fetchone()
        if row:
            mids[mc] = row[0]
        else:
            mids[mc] = cur.execute("""INSERT INTO catalog.metric
                (metric_code,name_ru,unit_id,source_id,frequency_id,metric_type,is_derived,status,tags)
                VALUES (%s,%s,%s,%s,%s,'primary',false,'active','{}') RETURNING metric_id""",
                (mc, n_, unit, SOURCE_ID, freq_w)).fetchone()[0]
    con.commit()

    obs = []
    comp = {}
    rd = csv.DictReader(io.StringIO(raw.decode("utf-8")))
    for rec in rd:
        per = rec["date"].strip()[:10]
        grp = rec["group"].strip()
        val = float(rec["count"])
        obs.append(("ws_phrases_raw", per, val))
        if grp in COMP4:
            comp[per] = comp.get(per, 0.0) + float(rec["share"])
    rows_comp = [("ws_composite_s25", per, v) for per, v in sorted(comp.items())]
    print("строк фраз:", len(obs), "| недель композита:", len(rows_comp))

    cur.execute("DROP TABLE IF EXISTS _tmp_ws_obs")
    cur.execute("CREATE TEMP TABLE _tmp_ws_obs (metric_code text, period_start date, value numeric, release_id integer)")
    buf = io.StringIO()
    for mc, p, v in obs + rows_comp:
        buf.write("\t".join(map(str, (mc, p, v, release_id))) + "\n")
    buf.seek(0)
    with cur.copy("COPY _tmp_ws_obs FROM STDIN") as cp:
        cp.write(buf.read())
    cur.execute(f"""
        INSERT INTO data.observation
        (metric_id, region_id, period_start, frequency_id, value,
         assessment_type, observation_status, source_id, release_id, sub_dimension)
        SELECT tm.metric_id, {rid}, t.period_start, {freq_w}, t.value,
               'final', 'validated', {SOURCE_ID}, t.release_id, ''
        FROM _tmp_ws_obs t
        JOIN catalog.metric tm ON tm.metric_code = t.metric_code
        ON CONFLICT (metric_id, region_id, period_start, frequency_id,
                     assessment_type, sub_dimension, release_id) DO NOTHING""")
    con.commit()
    cur.execute("DROP TABLE IF EXISTS _tmp_ws_obs")
    n = cur.execute("SELECT count(*) FROM data.observation WHERE release_id=%s", (release_id,)).fetchone()[0]
    print("canon по релизу:", n)

    exp = got = 0
    mism = []
    for mc in NAMES:
        ref = cur.execute("""SELECT o.period_start::text, o.value FROM v2.observation o
            JOIN v2.metric m USING(metric_id) WHERE m.metric_code=%s AND o.is_current ORDER BY 1""", (mc,)).fetchall()
        canon = {p: float(v) for p, v in cur.execute("""SELECT o.period_start::text, o.value FROM data.observation o
            JOIN catalog.metric m USING(metric_id) WHERE m.metric_code=%s AND o.release_id=%s""", (mc, release_id)).fetchall()}
        for p, val in ref:
            exp += 1
            cv = canon.get(p)
            if cv is None:
                mism.append((mc, p, float(val), "MISS"))
            else:
                dv = abs(cv - float(val))
                if dv > 5.1e-5 and dv > 1e-6 * abs(cv):
                    mism.append((mc, p, float(val), cv))
                else:
                    got += 1
        print(f"  {mc}: canon={len(canon)} v2={len(ref)}")
    print(f"v2-эталон: {exp}; совпало: {got}; расхождений: {len(mism)}")
    for m_ in mism[:10]:
        print("  ", m_)
    con.close()
    return 0 if not mism else 1


if __name__ == "__main__":
    label = sys.argv[1] if len(sys.argv) > 1 else "2026-09-21"
    sys.exit(main(label))