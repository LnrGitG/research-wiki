#!/usr/bin/env python3
"""Канон-перевод: СберИндекс (7 parquet на ВМ) → catalog + data.observation.

Этап 3 «единый приёмный контур»: первый переведённый живой loader.
Логика v2-парсера (loader/parse_sberindex.py), запись — в канон:
  - 12 метрик sber_* уже в catalog (source smartlab=12), переиспользуем;
  - релиз 'SberIndex raw <label>' (idempotent: если есть — только новые periods);
  - вставка COPY temp + INSERT ... ON CONFLICT DO NOTHING;
  - приёмка: счётчики + value-сверка против v2.observation (эталон) round-4.
Запуск на ВМ: /home/ubuntu/venv/bin/python3 scripts/parse_sberindex_canon.py [label]
"""
import glob
import hashlib
import io
import json
import os
import sys

import psycopg
import pandas as pd
import pyarrow.parquet as pq

RAW_GLOB = "/home/ubuntu/sandbox_datasets/raw_sberindex/*.parquet"
PGDSN = "host=127.0.0.1 port=5432 dbname=research_wiki user=wiki"
SOURCE_ID = 12

FILES = {
    "dinamika-tsen-obyavlenii": ("sber_px_list_{side}", "price_type", {"Первичный рынок": "primary", "Вторичный рынок": "secondary"}, None, None),
    "predlozheniya-nedvizhimosti": ("sber_offers_cnt_{side}", "offer_type", {"Первичный рынок": "primary", "Вторичный рынок": "secondary"}, None, None),
    "real_estate_deals": ("sber_deal_px_median_{side}", "realty", {"Первичный": "primary", "Вторичный": "secondary"}, None, None),
    "residential_real_estate_prices": ("sber_res_px_{nov}_{side}", "real_estate_type", {"Первичный рынок": "primary", "Вторичный рынок": "secondary"}, "real_estate_novelty", {"Всего": "total", "Построенные менее 5 лет назад": "new5", "Построенные более 5 лет назад": "old5"}),
}

ALIAS = {
    "архангельская область": "архангельская область (без нао)",
    "кемеровская область - кузбасс": "кемеровская область — кузбасс",
    "тюменская область": "тюменская область (без хмао и янао)",
}


def main(label):
    con = psycopg.connect(PGDSN)
    cur = con.cursor()

    rid_rf = cur.execute("SELECT region_id FROM catalog.region WHERE name_ru=%s", ("Российская Федерация",)).fetchone()[0]
    rmap = {}
    for rid_, nm in cur.execute("SELECT region_id, name_ru FROM catalog.region"):
        rmap[str(nm).strip().lower().replace("ё", "е")] = rid_

    def resolve_region(reg):
        k = reg.strip().lower().replace("ё", "е")
        if k in rmap:
            return rmap[k]
        k2 = ALIAS.get(k)
        if k2:
            return rmap.get(k2.lower().replace("ё", "е"))
        return None

    mids = {}
    for mc, mid, fid in cur.execute("SELECT metric_code, metric_id, frequency_id FROM catalog.metric WHERE metric_code LIKE 'sber_%'"):
        mids[mc] = (mid, fid)

    rel_label = f"SberIndex raw {label}"
    row = cur.execute("SELECT release_id FROM catalog.release WHERE source_id=%s AND label=%s", (SOURCE_ID, rel_label)).fetchone()
    if row:
        release_id = row[0]
        print("релиз существует:", release_id)
    else:
        release_id = cur.execute(
            "INSERT INTO catalog.release (source_id, label, published_at, status, notes) VALUES (%s,%s,%s,%s,%s) RETURNING release_id",
            (SOURCE_ID, rel_label, label, "loaded", "СберИндекс, прямой прогон из parquet (канон-путь, этап 3)")).fetchone()[0]
        con.commit()
        print("создан release_id:", release_id)

    obs = []  # (metric_code, region_id, freq, period, value)
    report = {}
    for path in sorted(glob.glob(RAW_GLOB)):
        base = os.path.basename(path)
        sha = hashlib.sha256(open(path, "rb").read()).hexdigest()
        df = pq.read_table(path).to_pandas()
        stem = base.split("_ru_")[0]
        if stem not in FILES:
            report[base] = "skipped"
            continue
        tmpl, dim, sides, nov_col, nov_map = FILES[stem]
        inserted_c = 0
        rejected = 0
        for _, rec in df.iterrows():
            side = sides.get(rec[dim]) if dim is not None else None
            if side is None:
                continue
            if nov_col is not None:
                nov = nov_map.get(rec[nov_col])
                if nov is None:
                    continue
                mcode = tmpl.format(nov=nov, side=side)
            else:
                mcode = tmpl.format(side=side)
            if mcode not in mids:
                rejected += 1
                continue
            reg = rec["ref_area"]
            if reg == "Россия":
                rid_ = rid_rf
            else:
                rid_ = resolve_region(reg)
                if rid_ is None:
                    rejected += 1
                    continue
            val = float(rec["value"])
            d_ = pd.to_datetime(rec["period"])
            per = f"{d_.year:04d}-{d_.month:02d}-01"
            obs.append((mcode, rid_, mids[mcode][1], per, val))
            inserted_c += 1
        report[base] = {"rows": inserted_c, "rejected": rejected}

    obs = list({(mc, r_, f, p): (mc, r_, f, p, v) for mc, r_, f, p, v in obs}.values())
    print("строк к вставке:", len(obs))

    cur.execute("DROP TABLE IF EXISTS _tmp_sber_obs")
    cur.execute("CREATE TEMP TABLE _tmp_sber_obs (metric_code text, region_id integer, period_start date, frequency_id integer, value numeric, release_id integer)")
    buf = io.StringIO()
    for mc, r_, f, p, v in obs:
        buf.write("\t".join(map(str, (mc, r_, p, f, v, release_id))) + "\n")
    buf.seek(0)
    with cur.copy("COPY _tmp_sber_obs FROM STDIN") as cp:
        cp.write(buf.read())
    cur.execute(f"""
        INSERT INTO data.observation
        (metric_id, region_id, period_start, frequency_id, value,
         assessment_type, observation_status, source_id, release_id, sub_dimension)
        SELECT tm.metric_id, t.region_id, t.period_start, t.frequency_id, t.value,
               'final', 'validated', {SOURCE_ID}, t.release_id, ''
        FROM _tmp_sber_obs t
        JOIN catalog.metric tm ON tm.metric_code = t.metric_code
        ON CONFLICT (metric_id, region_id, period_start, frequency_id,
                     assessment_type, sub_dimension, release_id) DO NOTHING""")
    con.commit()
    cur.execute("DROP TABLE IF EXISTS _tmp_sber_obs")
    n = cur.execute("SELECT count(*) FROM data.observation WHERE release_id=%s", (release_id,)).fetchone()[0]
    print("canon по релизу:", n)

    # приёмка: сверка с v2-эталоном (is_current) round-4 по ИМЕНАМ регионов
    # (id-пространства v2/catalog различны)
    cur.execute("""
        SELECT m.metric_code, vr.name_ru, o.period_start::text, o.value
        FROM v2.observation o
        JOIN v2.metric m USING(metric_id)
        JOIN v2.region vr ON vr.region_id = o.region_id
        WHERE m.metric_code LIKE 'sber\_%' AND o.is_current AND o.frequency_id = 2""")
    v2pairs = [(mc, str(rn).strip().lower().replace("ё", "е"), p, float(val)) for mc, rn, p, val in cur]
    mids2 = {mc: mid for mc, mid in cur.execute("SELECT metric_code, metric_id FROM catalog.metric WHERE metric_code LIKE 'sber\_%'")}
    exp = got = 0
    mism = []
    for mc, rn, p, val in v2pairs:
        exp += 1
        mid_ = mids2.get(mc)
        row = cur.execute("""SELECT o.value FROM data.observation o
            JOIN catalog.metric m ON m.metric_code=%s
            JOIN catalog.region r ON r.region_id=o.region_id
            WHERE o.metric_id=%s AND lower(r.name_ru)=%s
              AND o.period_start=%s AND o.release_id=%s""",
            (mc, mid_, rn, p, release_id)).fetchone()
        if row is None:
            mism.append((mc, rn, p, val, "MISS"))
            continue
        if abs(float(row[0]) - val) <= 5.1e-5:  # numeric(4)-округление эталона v2
            got += 1
        else:
            mism.append((mc, rn, p, val, float(row[0])))
    print(f"v2-эталон: {exp}; совпало: {got}; расхождений: {len(mism)}")
    for m_ in mism[:10]:
        print("  ", m_)
    print(json.dumps(report, ensure_ascii=False))
    con.close()
    return 0 if len(mism) == 0 else 1


if __name__ == "__main__":
    label = sys.argv[1] if len(sys.argv) > 1 else "2026-09-21"
    sys.exit(main(label))
