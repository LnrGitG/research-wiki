#!/usr/bin/env python3
"""Пункт 1: ikv_rf_quarter (rosreestr_deals.db) → канон.

Единственный ряд, который жил только в SQLite-лендинге и был нужен читателю
`ikv_benchmarks.py`. Переносим в `catalog.metric` + `data.observation`, чтобы
скрипт читал канон, а лендинг можно было снять.

Метрики:
  ikv_rf_q_bln  — ИКВ РФ (инвестиции в основной капитал), млрд руб., квартал
  ikv_rf_q_yoy  — ИКВ РФ, % к соответствующему периоду, квартал

Калибровка: уровни ikv_rf_q_bln совпадают с каноническим `kep1_63` (КЭП 1.6,
уровень) значение-в-значение (2020Q1 = 2986.8). Ряд yoy в лендинге ОТЛИЧАЕТСЯ
от канонического `kep1_6_y3` начиная со II квартала (2020Q2: лендинг 99.4
против КЭП 95.8 при совпадающих Q1) — похоже на накопленный итог против
квартального; противоречие фиксируем, ряд переносим как есть под своим кодом.

Точка возврата: DELETE FROM data.observation WHERE release_id=<новый>.
"""
import os
import sqlite3
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from db_tunnel import connect  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(REPO, "data", "rosreestr_deals.db")
SRC = "rosstat_inv_reg_kv_2020-2026"
RELEASE = "ikv-rf-quarter 2026-10-16 (перенос из SQLite-лендинга, пункт 1)"

NAMES = {
    "ikv_rf_q_bln": "ИКВ РФ (инвестиции в основной капитал), млрд руб., квартал",
    "ikv_rf_q_yoy": "ИКВ РФ, % к соответствующему периоду, квартал",
}


def main():
    con = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    rows = con.execute("SELECT year,q,value_bln,yoy_pct FROM ikv_rf_quarter").fetchall()
    print(f"лендинг: {len(rows)} кварталов (источник {SRC})")

    conn = connect()
    with conn.cursor() as cur:
        src = cur.execute("SELECT source_id FROM catalog.source WHERE source_code='rosstat'").fetchone()[0]
        fq = cur.execute("SELECT frequency_id FROM catalog.frequency WHERE freq_code='Q'").fetchone()[0]
        rel = cur.execute("SELECT release_id FROM catalog.release WHERE label=%s", (RELEASE,)).fetchone()
        if rel:
            rid = rel[0]
        else:
            rid = cur.execute("""INSERT INTO catalog.release (source_id,label,published_at,status,notes)
                VALUES (%s,%s,'2026-10-16','loaded','перенос ikv_rf_quarter из rosreestr_deals.db')
                RETURNING release_id""", (src, RELEASE)).fetchone()[0]
        conn.commit()

        mids = {}
        for code, name in NAMES.items():
            r = cur.execute("SELECT metric_id FROM catalog.metric WHERE metric_code=%s", (code,)).fetchone()
            if r:
                mids[code] = r[0]
            else:
                mids[code] = cur.execute("""INSERT INTO catalog.metric
                    (metric_code,name_ru,unit_id,source_id,frequency_id,metric_type,status,is_active)
                    VALUES (%s,%s,%s,%s,%s,'primary','active',true) RETURNING metric_id""",
                    (code, name, 30 if code.endswith("bln") else 12, src, fq)).fetchone()[0]
        conn.commit()

        data = []
        for y, q, bln, yoy in rows:
            per = f"{y}-{(q - 1) * 3 + 1:02d}-01"
            if bln is not None:
                data.append((mids["ikv_rf_q_bln"], per, float(bln)))
            if yoy is not None:
                data.append((mids["ikv_rf_q_yoy"], per, float(yoy)))

        ins = 0
        for mid, per, val in data:
            cur.execute("""INSERT INTO data.observation
                (metric_id,region_id,period_start,frequency_id,value,
                 assessment_type,observation_status,source_id,release_id,sub_dimension)
                VALUES (%s,1,%s,%s,%s,'final','validated',%s,%s,'')
                ON CONFLICT (metric_id,region_id,period_start,frequency_id,
                             assessment_type,sub_dimension,release_id) DO NOTHING""",
                (mid, per, fq, val, src, rid))
            ins += cur.rowcount
        conn.commit()
        print(f"вставлено: {ins} из {len(data)}")
        for code, mid in mids.items():
            n = cur.execute("SELECT count(*),min(period_start),max(period_start) "
                            "FROM data.observation WHERE metric_id=%s", (mid,)).fetchone()
            print(f"  {code:<14} n={n[0]} {n[1]}..{n[2]}")


if __name__ == "__main__":
    main()
