#!/usr/bin/env python3
"""Этап 1 (продолжение): ДОМ.РФ price-index → catalog + data.observation.

Вход: /home/ubuntu/sandbox_datasets/raw_domrf_price_index/domrf_priceindex_all_regions.csv
(ВМ; 5 025 строк данных, 2021-01 … 2026-07, 75 регионов: index_value, mom_pct, n_deals).
Логика resolve региона — из loader/parse_domrf_pi.py (алиасы сохранены).
Метрики: domrf_price_index_m (index_100→catalog 30), domrf_price_index_mom (pct→12),
ddu_count_m (count→29). Точка возврата: DELETE WHERE release_id=<новый>.
"""
import sys, os, json, hashlib, csv, datetime as dt
sys.path.insert(0, os.path.dirname(__file__))
import db_tunnel

import sys as _sys
RELEASE_LABEL = _sys.argv[1] if len(_sys.argv) > 1 else "domrf-price-index 2026-09-21 (перенос из v2-csv, этап 1)"
_release_date = RELEASE_LABEL.split()[1] if " " in RELEASE_LABEL and RELEASE_LABEL.split()[1].count("-") == 2 else "2026-09-21"
try:
    _rd = dt.date.fromisoformat(_release_date)
except ValueError:
    _rd = dt.date(2026, 9, 21)

UNIT_MAP = {30: 30, 12: 12, 29: 29}  # уже catalog-коды

NAMES = {
    "domrf_price_index_m":  ("ДОМ.РФ: индекс цен на новостройки, первичный рынок (уровень 2021-01=100)", 30),
    "domrf_price_index_mom":("ДОМ.РФ: индекс цен на новостройки, м/м, %", 12),
    "ddu_count_m":          ("ДОМ.РФ: число ДДУ (n_deals), шт, за месяц", 29),
}

ALIAS = {
    "архангельская область": "архангельская область (без нао)",
    "город москва": "москва",
    "город санкт-петербург": "санкт-петербург",
    "кемеровская область - кузбасс": "кемеровская область — кузбасс",
    "республика северная осетия": "республика северная осетия — алания",
    "тюменская область": "тюменская область (без хмао и янао)",
    "ханты-мансийский ао - югра": "ханты-мансийский автономный округ — югра",
    "ямало-ненецкий ао": "ямало-ненецкий автономный округ",
}

RUN_FILE_REMOTE = "/home/ubuntu/sandbox_datasets/raw_domrf_price_index/domrf_priceindex_all_regions.csv"
LOCAL_COPY = "/home/lnr/research-wiki-private/raw/domrf/price_index/domrf_priceindex_all_regions.csv"
# старый адрес ВМ (89.169.168.214) выведен из строя после переезда 14.10.2026;
# domrf_fetch_monthly.py уже пишет CSV локально — читаем его, к ВМ не ходим.


def fetch_file():
    if os.path.exists(LOCAL_COPY) and os.path.getsize(LOCAL_COPY) > 100000:
        return
    raise SystemExit("нет локального CSV ДОМ.РФ: %s — сначала запустите domrf_fetch_monthly.py" % LOCAL_COPY)


def main():
    fetch_file()
    sha = hashlib.sha256(open(LOCAL_COPY, 'rb').read()).hexdigest()
    print("sha256:", sha[:16], "…", "size:", os.path.getsize(LOCAL_COPY))

    with db_tunnel.connect() as conn:
        with conn.cursor() as cur:
            src_id = cur.execute("SELECT source_id FROM catalog.source WHERE source_code='domrf'").fetchone()[0]
            freq_m = cur.execute("SELECT frequency_id FROM catalog.frequency WHERE freq_code='M'").fetchone()[0]
            rel = cur.execute("SELECT release_id FROM catalog.release WHERE label=%s",(RELEASE_LABEL,)).fetchone()
            release_id = rel[0] if rel else cur.execute("""INSERT INTO catalog.release
                (source_id,label,published_at,status,notes) VALUES (%s,%s,%s,'loaded',
                'перенос domrf-price-index (этап 1; сырьё ВМ csv 2026-09-21)') RETURNING release_id""",
                (src_id, RELEASE_LABEL, _rd)).fetchone()[0]
            conn.commit()

            def ensure_metric(code):
                name, unit = NAMES[code]
                r = cur.execute("SELECT metric_id FROM catalog.metric WHERE metric_code=%s",(code,)).fetchone()
                if r: return r[0]
                rid = cur.execute("""INSERT INTO catalog.metric
                    (metric_code,name_ru,unit_id,source_id,frequency_id,metric_type,status,is_active)
                    VALUES (%s,%s,%s,%s,%s,'primary','active',true) RETURNING metric_id""",
                    (code,name,unit,src_id,freq_m)).fetchone()[0]
                conn.commit(); return rid

            rmap = {nm.strip().lower(): rid for rid, nm in
                    cur.execute("SELECT region_id, name_ru FROM catalog.region").fetchall()}
            def resolve_region(reg):
                k = reg.strip().lower()
                if k in rmap: return rmap[k]
                k2 = ALIAS.get(k)
                if k2: return rmap.get(k2)
                # прямой поиск по частичному совпадению (на случай формы «г.», «район»)
                return None

            rows=[]; rejects={}
            with open(LOCAL_COPY, newline='', encoding='utf-8') as fh:
                rdp = csv.DictReader(fh)
                for rec in rdp:
                    reg=(rec['region'] or '').strip()
                    rid=resolve_region(reg)
                    per=rec['month'].strip()[:10]
                    for mcode,col in (("domrf_price_index_m","index_value"),
                                      ("domrf_price_index_mom","mom_pct"),
                                      ("ddu_count_m","n_deals")):
                        val=rec[col]
                        if val in (None,'','nan'): continue
                        if not rid:
                            rejects[reg]=rejects.get(reg,0)+1
                            continue
                        rows.append((mcode,rid,per,float(val)))

            metrics={mc:ensure_metric(mc) for mc in {r[0] for r in rows}}
            conn.commit()
            # пакетная вставка (медленные построчные round-trip через тоннель — root cause таймаутов)
            inserted=0; B=2000
            for i in range(0, len(rows), B):
                chunk = rows[i:i+B]
                cur.executemany("""INSERT INTO data.observation
                    (metric_id,region_id,period_start,frequency_id,value,
                     assessment_type,observation_status,source_id,release_id,sub_dimension)
                    VALUES (%s,%s,%s,%s,%s,'final','validated',%s,%s,'')
                    ON CONFLICT (metric_id,region_id,period_start,frequency_id,
                                 assessment_type,sub_dimension,release_id) DO NOTHING""", [
                    (metrics[mcode],rid,per,freq_m,val,src_id,release_id)
                    for mcode,rid,per,val in chunk])
                inserted+=cur.rowcount
                print(f"  пакет {i//B+1}: вставлено нараст.={inserted:,}", flush=True)
            conn.commit()
            print(f"строк parsed={len(rows):,} вставлено={inserted:,} reject={sum(rejects.values()):,}; регионы-отказы: {list(rejects)[:6]}")

            # сверка с v2-эталоном — только если схема v2 существует (заморожена/удалена с 06.10)
            if cur.execute("SELECT to_regclass('v2.observation')").fetchone()[0] is None:
                print('v2 недоступна — сверка пропущена; canon:',
                      {mc: cur.execute('SELECT count(*) FROM data.observation WHERE metric_id=%s',
                                       (mid,)).fetchone()[0] for mc, mid in metrics.items()})
                return
            for mc, mid in metrics.items():
                ref=cur.execute("""SELECT count(*) FROM v2.observation o JOIN v2.metric m
                    ON m.metric_id=o.metric_id WHERE m.metric_code=%s AND o.is_current""",(mc,)).fetchone()[0]
                got=cur.execute("SELECT count(*) FROM data.observation WHERE metric_id=%s",(mid,)).fetchone()[0]
                print(f"  {mc:<24} canon={got:,} v2={ref:,} → {'OK' if got==ref else 'РАСХОЖДЕНИЕ'}")

            # EXCEPT по бизнес-ключам
            V2 = """SELECT m.metric_code mc, COALESCE(vr.name_ru,'?') rn, f.freq_code fc,
                    o.period_start::date ps, round(o.value,4) v FROM v2.observation o
                    JOIN v2.metric m ON m.metric_id=o.metric_id
                    LEFT JOIN v2.region vr ON vr.region_id=o.region_id
                    LEFT JOIN v2.frequency f ON f.frequency_id=o.frequency_id
                    WHERE m.metric_code IN ('domrf_price_index_m','domrf_price_index_mom','ddu_count_m') AND o.is_current"""
            D = """SELECT m.metric_code mc, COALESCE(cr.name_ru,'?') rn, fr.freq_code fc,
                    d.period_start::date ps, round(d.value,4) v FROM data.observation d
                    JOIN catalog.metric m ON m.metric_id=d.metric_id
                    LEFT JOIN catalog.region cr ON cr.region_id=d.region_id
                    LEFT JOIN catalog.frequency fr ON fr.frequency_id=d.frequency_id
                    WHERE m.metric_code IN ('domrf_price_index_m','domrf_price_index_mom','ddu_count_m')
                      AND d.release_id=%s"""
            n1=cur.execute(f"SELECT count(*) FROM (({V2}) EXCEPT ALL ({D})) x",(release_id,)).fetchone()[0]
            n2=cur.execute(f"SELECT count(*) FROM (({D}) EXCEPT ALL ({V2})) x",(release_id,)).fetchone()[0]
            print(f"EXCEPT round-4: v2-без-пары={n1}, canon-без-пары={n2}")
            if n1:
                for r in cur.execute(f"SELECT * FROM (({V2}) EXCEPT ALL ({D})) x LIMIT 6",(release_id,)):
                    print("   v2-сирота:", r)
            if n2:
                for r in cur.execute(f"SELECT * FROM (({D}) EXCEPT ALL ({V2})) x LIMIT 6",(release_id,)):
                    print("   canon-сирота:", r)

if __name__=="__main__":
    main()