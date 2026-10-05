#!/usr/bin/env python3
"""Этап 1.5: Wordstat (недельные срезы) → catalog + data.observation.

Вход: /home/ubuntu/sandbox_datasets/wordstat_weekly_construction.csv (ВМ, 9 040 строк).
Логика — 1:1 из loader/parse_wordstat.py: ws_phrases_raw (count по фразам) +
ws_composite_s25 (сумма share групп S2–S5 по неделям), регион — РФ.
Вставка executemany. Внимание: периодичность W — частота недели в эталоне v2 (fid=2),
в catalog.frequency должна быть 'W'; проверяем и находим, иначе создаём.
"""
import sys, os, io, datetime, hashlib, subprocess
sys.path.insert(0, os.path.dirname(__file__))
import db_tunnel

RELEASE_LABEL = "yandex-wordstat 2026-09-21 (перенос из v2, этап 1.5)"
SSH = ["ssh", "-o", "BatchMode=yes", "-i", "/home/lnr/.ssh/id_yc", "ubuntu@89.169.168.214"]
RUN_FILE = "/home/ubuntu/sandbox_datasets/wordstat_weekly_construction.csv"
S2_S5 = {"S2_mat","S3_mach","S4_b2b","S4_procure","S5_permits"}
NAMES = {
    "ws_phrases_raw":   ("Яндекс Wordstat: поисковые запросы по фразам (конструкция), сырой счёт, шт, за неделю", 29),
    "ws_composite_s25": ("Яндекс Wordstat: композитный спрос S2-S5 (сумма долей групп), доля, за неделю", 37),
}
ALIAS_WFREQ = {}


def main():
    raw = subprocess.run(SSH + ["cat", RUN_FILE], capture_output=True).stdout
    sha = hashlib.sha256(raw).hexdigest()
    print("sha256:", sha[:16], "…", "size:", len(raw))
    with db_tunnel.connect() as conn:
        with conn.cursor() as cur:
            src = cur.execute("SELECT source_id FROM catalog.source WHERE source_code ILIKE '%yandex%'").fetchone()
            src_id = src[0] if src else cur.execute("""INSERT INTO catalog.source (source_code,name_ru)
                VALUES ('yandex','Яндекс') RETURNING source_id""").fetchone()[0]
            fw = cur.execute("SELECT frequency_id FROM catalog.frequency WHERE freq_code='W'").fetchone()
            if fw: freq_w = fw[0]
            else:
                ref_m = cur.execute("SELECT frequency_id FROM catalog.frequency WHERE freq_code='M'").fetchone()[0]
                freq_w = cur.execute("""INSERT INTO catalog.frequency (freq_code,name_ru)
                    VALUES ('W','неделя') RETURNING frequency_id""").fetchone()[0]
            rel = cur.execute("SELECT release_id FROM catalog.release WHERE label=%s",(RELEASE_LABEL,)).fetchone()
            release_id = rel[0] if rel else cur.execute("""INSERT INTO catalog.release
                (source_id,label,published_at,status,notes) VALUES (%s,%s,%s,'loaded',
                'перенос Wordstat (этап 1.5); сырьё ВМ csv, срез 2026-09-21') RETURNING release_id""",
                (src_id, RELEASE_LABEL, datetime.date(2026,9,21))).fetchone()[0]
            conn.commit()
            rid = cur.execute("SELECT region_id FROM catalog.region WHERE region_code='ru'").fetchone()
            rid = rid[0] if rid else None
            midmap = {}
            for mc,(name,unit) in NAMES.items():
                r = cur.execute("SELECT metric_id FROM catalog.metric WHERE metric_code=%s",(mc,)).fetchone()
                if r: midmap[mc]=r[0]
                else:
                    midmap[mc]=cur.execute("""INSERT INTO catalog.metric
                        (metric_code,name_ru,unit_id,source_id,frequency_id,metric_type,status,is_active)
                        VALUES (%s,%s,%s,%s,%s,'primary','active',true) RETURNING metric_id""",
                        (mc,name,unit,src_id,freq_w)).fetchone()[0]
                    conn.commit()
            # parse
            import csv as _csv
            f = io.StringIO(raw.decode("utf-8"))
            rd = _csv.DictReader(f)
            rows_phr=[]; comp={}
            n_parse=0
            for rec in rd:
                per = rec['date'].strip()[:10]; grp = rec['group'].strip(); val = float(rec['count'])
                rows_phr.append((midmap["ws_phrases_raw"], rid, per, freq_w, val, src_id, release_id))
                n_parse+=1
                if grp in S2_S5:
                    comp[per] = comp.get(per, 0.0) + float(rec['share'])
            rows_comp = [(midmap["ws_composite_s25"], rid, per, freq_w, v, src_id, release_id)
                         for per,v in sorted(comp.items())]
            print("строк фраз:", len(rows_phr), "| недель композита:", len(rows_comp))
            allrows = rows_phr + rows_comp
            B=4000; inserted=0
            for i in range(0,len(allrows),B):
                cur.executemany("""INSERT INTO data.observation
                    (metric_id,region_id,period_start,frequency_id,value,
                     assessment_type,observation_status,source_id,release_id,sub_dimension)
                    VALUES (%s,%s,%s,%s,%s,'final','validated',%s,%s,'')
                    ON CONFLICT (metric_id,region_id,period_start,frequency_id,
                                 assessment_type,sub_dimension,release_id) DO NOTHING""", allrows[i:i+B])
                inserted += cur.rowcount
            conn.commit()
            print(f"вставлено: {inserted:,}")
            for mc, mid in midmap.items():
                ref = cur.execute("""SELECT count(*) FROM v2.observation o JOIN v2.metric m
                    ON m.metric_id=o.metric_id WHERE m.metric_code=%s AND o.is_current""",(mc,)).fetchone()[0]
                got = cur.execute("SELECT count(*) FROM data.observation WHERE metric_id=%s",(mid,)).fetchone()[0]
                print(f"  {mc:<18} canon={got:>5,} v2={ref:>5,} {'OK' if got==ref else 'РАСХ'}")

if __name__ == "__main__":
    main()