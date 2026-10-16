#!/usr/bin/env python3
"""[ОСИРОТЕЛ 16.10.2026] Лендинг data/rosstat_construction.db удалён вместе с
гармонайзером 6, поэтому у этого скрипта больше нет потребителя/источника.
Оставлен как справка. Возврат: тег pre-del-construction-h6.

Этап 2.1: Доклад Росстата 08-2026 (SQLite data/rosstat_construction.db) → catalog + data.observation.

Вход локальный, 3 таблицы (175 строк): doklad_housing_input (74),
doklad_construction_volume (69), doklad_construction_dynamics (32).
Релиз — Doklad 08-2026, source rosstat (source_id 11).

Правила проекта: приёмка до доклада об успехе; точка возврата — DELETE по release_id.
Мусорные имена (битые суррогаты из .doc) пропускаются с явной печатью.
"""
import re
import sqlite3
import sys

sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
import db_tunnel

WIKI = "/home/lnr/research-wiki-private"
SOURCE_ID = 11  # rosstat
RELEASE_LABEL = "Doklad Rosstata 08-2026 (перенос из sqlite, этап 2.1)"
DB_PATH = f"{WIKI}/data/rosstat_construction.db"

# Мусорные имена регионов (суррогаты из catdoc) — не резолвятся, пропускаем явно
GARBAGE = ("\u0400", "\u7461")

ALIAS = {
    "архангельская область": "архангельская область (без нао)",
    "кемеровская область": "кемеровская область — кузбасс",
    "тюменская область": "тюменская область (с хмао и янао)",
    "тюменская область без авт. округов": "тюменская область (без хмао и янао)",
    "ханты-мансийский авт. округ - югра": "ханты-мансийский автономный округ — югра",
    "республика северная осетия - алания": "республика северная осетия — алания",
    "еврейская авт. область": "еврейская автономная область",
    "г. москва": "москва",
    "чукотский авт. округ": "чукотский автономный округ",
    "ямало-ненецкий авт. округ": "ямало-ненецкий автономный округ",
}

PERIOD_MAP = {
    "I квартал": "2026-04-01", "II квартал": "2026-07-01",
    "III квартал": "2026-10-01", "IV квартал": "2026-01-01",
    "Январь": "2026-01-01", "Февраль": "2026-02-01", "Март": "2026-03-01",
    "Апрель": "2026-04-01", "Май": "2026-05-01", "Июнь": "2026-06-01",
    "Июль": "2026-07-01", "Август": "2026-08-01", "Сентябрь": "2026-09-01",
    "Октябрь": "2026-10-01", "Ноябрь": "2026-11-01", "Декабрь": "2026-12-01",
    "Год": "2026-01-01",
    "Январь-август": "2026-01-01", "Январь-сентябрь": "2026-01-01",
    "I полугодие": "2026-01-01",
}
# динамика содержит ПРОГНОЗНЫЕ строки (сент…декабрь и накопительные) —
# доклад даёт уровень+темпы помесячно; грузим только факт (январь–август),
# сентябрь→декабрь из статдоклада не грузим (прогноз, не наблюдение).
FACT_MONTHS = {"Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
               "Июль", "Август"}


def norm(r):
    return r.strip().lower().replace("ё", "е").replace("\xa0", " ")


def main():
    sq = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
    conn = db_tunnel.connect()
    cur = conn.cursor()

    rmap = {norm(nm): rid for rid, nm in
            cur.execute("SELECT region_id, name_ru FROM catalog.region")}

    # релиз (идемпотентно)
    cur.execute("SELECT release_id FROM catalog.release WHERE source_id=%s AND label=%s",
                (SOURCE_ID, RELEASE_LABEL))
    row = cur.fetchone()
    if row:
        release_id = row[0]
        print(f"релиз существует: {release_id}, продолжаю")
    else:
        cur.execute("""INSERT INTO catalog.release (source_id, label, published_at, status, notes)
                       VALUES (%s,%s,%s,'loaded','Доклад 08-2026, перенос из sqlite (этап 2.1)')
                       RETURNING release_id""", (SOURCE_ID, RELEASE_LABEL, "2026-10-05"))
        release_id = cur.fetchone()[0]
        conn.commit()
        print("создан release_id:", release_id)

    rej_reg = set()
    metrics = {
        "doklad_housing_input_tthm_sqm": ("Ввод жилья, тыс. м2 (Доклад 08-2026, STROIT-1-1)", 16),
        "doklad_housing_input_tthm_sqm_yoy": ("Ввод жилья, %% г/г (Доклад 08-2026, STROIT-1-1)", 12),
        "doklad_construction_volume_mlnrub": ("СМР, млн руб. (Доклад 08-2026, STR-PODR)", 11),
        "doklad_construction_volume_mlnrub_yoy": ("СМР %% г/г (Доклад 08-2026, STR-PODR)", 12),
        "doklad_construction_dynamics_blnrub": ("СМР помесячно, млрд руб. (Доклад 08-2026, 2-1-6)", 10),
        "doklad_construction_dynamics_blnrub_yoy": ("СМР помесячно %% г/г (Доклад 08-2026, 2-1-6)", 12),
        "doklad_construction_dynamics_blnrub_mom": ("СМР помесячно %% м/м (Доклад 08-2026, 2-1-6)", 12),
    }
    UNITS = {"doklad_housing_input_tthm_sqm": 16,
             "doklad_housing_input_tthm_sqm_yoy": 12,
             "doklad_construction_volume_mlnrub": 11,
             "doklad_construction_volume_mlnrub_yoy": 12,
             "doklad_construction_dynamics_blnrub": 10,
             "doklad_construction_dynamics_blnrub_yoy": 12,
             "doklad_construction_dynamics_blnrub_mom": 12}

    mids = {}
    units = {u: uid for u, uid in cur.execute("SELECT unit_code, unit_id FROM catalog.unit")}
    for code, (name, unit_code) in metrics.items():
        if unit_code not in units.values():
            print(f"НЕТ unit_id {unit_code} для {code} — остановка")
            sys.exit(1)
        cur.execute("""SELECT metric_id FROM catalog.metric WHERE metric_code=%s""", (code,))
        row = cur.fetchone()
        if row:
            mids[code] = row[0]
            continue
        cur.execute("""INSERT INTO catalog.metric (metric_code, name_ru, unit_id, source_id,
                       frequency_id, metric_type, is_derived, status, tags)
                       VALUES (%s,%s,%s,%s,5,'primary',false,'active','{doklad}')
                       RETURNING metric_id""",
                    (code, name, unit_code, SOURCE_ID))
        mids[code] = cur.fetchone()[0]
    conn.commit()

    obs = []  # (metric_code, region_id, period_start, value)
    for region, period, val, yoy in sq.execute(
            "SELECT region, period, value_thousand_m2, yoy_pct FROM doklad_housing_input WHERE value_thousand_m2 IS NOT NULL"):
        if any(g in region for g in GARBAGE):
            rej_reg.add(region.strip())
            region = region.replace("\u0400", "").strip()
        rid_ = rmap.get(norm(ALIAS.get(norm(region), norm(region))))
        if rid_ is None:
            rej_reg.add(region)
            continue
        # '2026-01-08' — дата отчёта, не период; данные января–августа → период 2026-08-01
        obs.append(("doklad_housing_input_tthm_sqm", rid_, "2026-08-01", val))
        if yoy is not None:
            obs.append(("doklad_housing_input_tthm_sqm_yoy", rid_, "2026-08-01", yoy))
    for region, period, val, yoy in sq.execute(
            "SELECT region, period, value_mln_rub, yoy_pct FROM doklad_construction_volume WHERE value_mln_rub IS NOT NULL"):
        if any(g in region for g in GARBAGE):
            rej_reg.add(region.strip())
            region = region.replace("\u0400", "").strip()
        rid_ = rmap.get(norm(ALIAS.get(norm(region), norm(region))))
        if rid_ is None:
            rej_reg.add(region)
            continue
        obs.append(("doklad_construction_volume_mlnrub", rid_, "2026-08-01", val))
        if yoy is not None:
            obs.append(("doklad_construction_volume_mlnrub_yoy", rid_, "2026-08-01", yoy))
    # динамика: таблица содержит ДВА года (ids 1-20 = 2025, ids 21-32 = 2026 факт).
    # Грузим только 2026 факт-месяцы (Январь-Август второго полублока); кварталы/накопительные не грузим (частота M).
    rows_dyn = sq.execute("SELECT id, period_label, value_bln_rub, yoy_pct, mom_pct FROM doklad_construction_dynamics").fetchall()
    labels_2026 = {r[1] for r in rows_dyn if r[0] >= 21}
    for i, plabel, val, yoy, mom in rows_dyn:
        if i < 21 or plabel not in ("Январь","Февраль","Март","Апрель","Май","Июнь","Июль","Август"):
            continue
        ps = PERIOR_MAP if False else PERIOD_MAP[plabel]
        rid_ = rmap["российская федерация"]
        obs.append(("doklad_construction_dynamics_blnrub", rid_, ps, val))
        if yoy is not None:
            obs.append(("doklad_construction_dynamics_blnrub_yoy", rid_, ps, yoy))
        if mom is not None:
            obs.append(("doklad_construction_dynamics_blnrub_mom", rid_, ps, mom))
    del labels_2026

    print("собрано строк:", len(obs), "| отказные регионы:", sorted(rej_reg), f"({len(rej_reg)})")

    # вставка пачками (схема вставки — как в transfer_domrf_price.py)
    n0 = 0
    for i in range(0, len(obs), 2000):
        chunk = obs[i:i+2000]
        cur.executemany("""INSERT INTO data.observation
            (metric_id,region_id,period_start,frequency_id,value,
             assessment_type,observation_status,source_id,release_id,sub_dimension)
            VALUES (%s,%s,%s,5,%s,'final','validated',%s,%s,'')
            ON CONFLICT (metric_id,region_id,period_start,frequency_id,
                         assessment_type,sub_dimension,release_id) DO NOTHING""",
            [(mids[mc], rr, ps, float(v), SOURCE_ID, release_id) for mc, rr, ps, v in chunk])
        n0 += len(chunk)
    conn.commit()
    print("вставлено (попыткой):", n0)

    # приёмка: счётчики в каноне по релизу
    total = cur.execute("""SELECT count(*) FROM data.observation WHERE release_id=%s""", (release_id,)).fetchone()[0]
    print("canon по релизу:", total)
    for code, mid in mids.items():
        n = cur.execute("""SELECT count(*) FROM data.observation
            WHERE metric_id=%s AND release_id=%s""", (mid, release_id)).fetchone()[0]
        print(f"  {code:45} canon={n}")
    conn.close(); sq.close()


if __name__ == "__main__":
    main()