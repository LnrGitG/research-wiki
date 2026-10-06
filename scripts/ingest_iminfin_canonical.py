#!/usr/bin/env python3
"""Канонический инжест iminfin (iМониторинг КРИСТА) в БД research_wiki.

Схема: catalog.source, catalog.metric, catalog.release, data.observation, catalog.region
Совместимость: только канонические таблицы, никаких compat-слоёв (core.*, derived.*).

Метрики (6):
- iminfin_exp_total_ytd_m   — исполнение расходов субъекта, нарастающий итог, млн руб [col 0]
- iminfin_exp_plan_ytd_m    — план расходов на год, млн руб [col 1]
- iminfin_exp_exec_share    — доля исполнения расходов (col4), п.п. → доля
- iminfin_exp_pc_ytd_m      — расходы на душу населения, тыс руб/чел [col 5]
- iminfin_trf_fed_ytd_m     — межбюджетные трансферты из федбюджета, млн руб [transferty col 1]
- iminfin_debt_share_econ   — госдолг к доходам (доля) [dolg[3] col 2]

Сырые данные: ~/yc-wiki/raw/iminfin/<date>/iminfin_*.json
Источник: www.iminfin.ru (НПО КРИСТА), еженедельные снапшоты.
"""
import json
import os
import re
import sys
import hashlib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import db_tunnel  # noqa: E402

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_BASE = os.path.expanduser("~/yc-wiki/raw/iminfin")

SOURCE_ID = 27  # catalog.source.iminfin

# ─── Маппинг имён регионов iminfin → catalog.region ───
ALIAS = {
    "республика татарстан (татарстан)": "республика татарстан",
    "республика адыгея (адыгея)": "республика адыгея",
    "чувашская республика - чувашия": "чувашская республика",
    "чувашская республика-чувашия": "чувашская республика",
    "г. санкт-петербург": "санкт-петербург",
    "г. москва": "москва",
    "г. севастополь": "севастополь",
    "республика северная осетия-алания": "республика северная осетия — алания",
    "республика северная осетия — алания": "республика северная осетия — алания",
    "кемеровская область": "кемеровская область — кузбасс",
    "ханты-мансийский автономный округ": "ханты-мансийский автономный округ — югра",
    "тюменская область": "тюменская область (без хмао и янао)",
    "архангельская область": "архангельская область (без нао)",
    "ямало-ненецкий автономный округ": "ямало-ненецкий автономный округ",
    "ненецкий автономный округ": "ненецкий автономный округ",
}

# ФО → region_id (из catalog.region)
FO_MAP = {
    "центральный федеральный округ": 2,
    "северо-западный федеральный округ": 3,
    "южный федеральный округ": 4,
    "северо-кавказский федеральный округ": 5,
    "приволжский федеральный округ": 6,
    "уральский федеральный округ": 7,
    "сибирский федеральный округ": 8,
    "дальневосточный федеральный округ": 9,
}


def norm_name(s):
    s = re.sub(r"\s+", " ", str(s)).strip().lower()
    return ALIAS.get(s, s)


def build_region_map(conn):
    """Построить маппинг нормализованное имя → region_id."""
    cur = conn.cursor()
    cur.execute("SELECT region_id, name_ru FROM catalog.region ORDER BY region_id")
    region_map = {}
    for region_id, name_ru in cur.fetchall():
        key = norm_name(name_ru)
        region_map[key] = region_id
    # Добавим частичные совпадения для проблемных
    # "тюменская область (без хмао и янао)" → также "тюменская область"
    cur.close()
    return region_map


def resolve_region(name, region_map):
    """Разрешить имя региона из iminfin в region_id."""
    norm = norm_name(name)
    if norm in region_map:
        return region_map[norm]
    # Частичные совпадения
    for key, rid in region_map.items():
        if norm == key or (len(norm) > 5 and norm in key):
            return rid
    # ФО
    if norm in FO_MAP:
        return FO_MAP[norm]
    return None


def ensure_metric(cur, metric_code, name_ru, unit_id, frequency_id, description=None, metric_type=None):
    """Найти или создать метрику в catalog.metric."""
    cur.execute("SELECT metric_id FROM catalog.metric WHERE metric_code=%s AND source_id=%s", (metric_code, SOURCE_ID))
    r = cur.fetchone()
    if r:
        return r[0]
    cur.execute("""
        INSERT INTO catalog.metric (metric_code, name_ru, unit_id, source_id, frequency_id, status, is_active, description, metric_type)
        VALUES (%s, %s, %s, %s, %s, 'active', true, %s, %s) RETURNING metric_id
    """, (metric_code, name_ru, unit_id, SOURCE_ID, frequency_id, description, metric_type))
    return cur.fetchone()[0]


def ensure_release(cur, label, published_at, notes=None):
    """Найти или создать релиз в catalog.release."""
    cur.execute("SELECT release_id FROM catalog.release WHERE source_id=%s AND label=%s", (SOURCE_ID, label))
    r = cur.fetchone()
    if r:
        return r[0]
    cur.execute("""
        INSERT INTO catalog.release (source_id, label, published_at, status, ingested_at, notes)
        VALUES (%s, %s, %s, 'active', now(), %s) RETURNING release_id
    """, (SOURCE_ID, label, published_at, notes))
    return cur.fetchone()[0]


def insert_observation(cur, metric_id, region_id, period_start, value, release_id, assessment_type="final"):
    """Вставить наблюдение в data.observation (с дедупликацией)."""
    cur.execute("""
        SELECT observation_id FROM data.observation
        WHERE metric_id=%s AND region_id=%s AND period_start=%s AND release_id=%s
    """, (metric_id, region_id, period_start, release_id))
    if cur.fetchone():
        return  # уже есть
    cur.execute("""
        INSERT INTO data.observation
        (metric_id, region_id, period_start, value, observation_status, assessment_type, release_id, source_id, frequency_id)
        VALUES (%s, %s, %s, %s, 'validated', %s, %s, %s, 4)
    """, (metric_id, region_id, period_start, value, assessment_type, release_id, SOURCE_ID))


def process_snapshot(conn, snap_dir, snap_date):
    """Обработать один снапшот iminfin."""
    cur = conn.cursor()
    region_map = build_region_map(conn)
    stats = {"exp_total": 0, "exp_plan": 0, "exec_share": 0, "exp_pc": 0, "trf_fed": 0, "debt_share": 0, "skip": 0}

    # Релиз
    release_label = f"iminfin_snapshot_{snap_date}"
    release_id = ensure_release(cur, release_label, snap_date, f"Снапшот iМониторинг КРИСТА на {snap_date}")

    # Метрики
    mid_exp_total = ensure_metric(cur, "iminfin_exp_total_ytd_m",
        "Исполнение расходов субъекта с начала года, млн руб", 11, 4,
        "Нарастающий итог исполнения расходов бюджета субъекта РФ", "level")
    mid_exp_plan = ensure_metric(cur, "iminfin_exp_plan_ytd_m",
        "План расходов субъекта на год, млн руб", 11, 4,
        "Утверждённый план расходов бюджета субъекта РФ на год", "level")
    mid_exec_share = ensure_metric(cur, "iminfin_exp_exec_share",
        "Доля исполнения расходов субъекта от плана", 12, 4,
        "Отношение исполненных расходов к плану (значение — доля, не %)", "ratio")
    mid_exp_pc = ensure_metric(cur, "iminfin_exp_pc_ytd_m",
        "Расходы субъекта на душу населения, руб./чел", 38, 4,
        "Нарастающий итог расходов на душу населения (значение в рублях)", "level")
    mid_trf_fed = ensure_metric(cur, "iminfin_trf_fed_ytd_m",
        "Межбюджетные трансферты из федбюджета субъекту, млн руб", 11, 4,
        "Трансферты из федерального бюджета бюджетам субъектов РФ", "level")
    mid_debt_share = ensure_metric(cur, "iminfin_debt_share_econ",
        "Госдолг субъекта к доходам, доля", 12, 4,
        "Отношение госдолга субъекта к доходам бюджета", "ratio")

    # ─── Расходы: iminfin_raskhody_ispoln.json data[2] ───
    raskhody_path = os.path.join(snap_dir, "iminfin_raskhody_ispoln.json")
    if os.path.exists(raskhody_path):
        with open(raskhody_path) as f:
            rdata = json.load(f)
        rows = rdata[2]["data"]  # 101 rows: [name, total, plan, None, exec_share, pc, ...]
        for row in rows:
            name = row[0]
            region_id = resolve_region(name, region_map)
            if not region_id:
                stats["skip"] += 1
                continue
            # col 0 = total (млн руб), col 1 = plan (млн руб), col 4 = exec_share, col 5 = pc (тыс руб/чел)
            total = row[1] if len(row) > 1 and row[1] is not None else None
            plan = row[2] if len(row) > 2 and row[2] is not None else None
            exec_share = row[4] if len(row) > 4 and row[4] is not None else None
            exp_pc = row[5] if len(row) > 5 and row[5] is not None else None

            if total is not None:
                insert_observation(cur, mid_exp_total, region_id, snap_date, total, release_id)
                stats["exp_total"] += 1
            if plan is not None:
                insert_observation(cur, mid_exp_plan, region_id, snap_date, plan, release_id)
                stats["exp_plan"] += 1
            if exec_share is not None:
                insert_observation(cur, mid_exec_share, region_id, snap_date, exec_share, release_id)
                stats["exec_share"] += 1
            if exp_pc is not None:
                insert_observation(cur, mid_exp_pc, region_id, snap_date, exp_pc, release_id)
                stats["exp_pc"] += 1

    # ─── Трансферты: iminfin_transferty.json data[3] ───
    trf_path = os.path.join(snap_dir, "iminfin_transferty.json")
    if os.path.exists(trf_path):
        with open(trf_path) as f:
            tdata = json.load(f)
        rows = tdata[3]["data"]  # 100 rows: [name, val1, val2, val3]
        for row in rows:
            name = row[0]
            region_id = resolve_region(name, region_map)
            if not region_id:
                stats["skip"] += 1
                continue
            # col 1 — трансферты из федбюджета (млн руб, в исходнике в рублях — делим на 1e6)
            trf = row[1] if len(row) > 1 and row[1] is not None else None
            if trf is not None:
                # В исходнике значения в рублях (1 098 923 174 ≈ 1098.9 млн), конвертируем
                trf_mln = trf / 1e6 if trf > 1e5 else trf
                insert_observation(cur, mid_trf_fed, region_id, snap_date, trf_mln, release_id)
                stats["trf_fed"] += 1

    # ─── Госдолг: iminfin_dolg.json data[3] ───
    # Только по ФО (9 строк), не по субъектам
    dolg_path = os.path.join(snap_dir, "iminfin_dolg.json")
    if os.path.exists(dolg_path):
        with open(dolg_path) as f:
            ddata = json.load(f)
        rows = ddata[3]["data"]  # 9 rows: [fo_name, fo_code, debt_share]
        for row in rows:
            name = row[0]
            region_id = resolve_region(name, region_map)
            if not region_id:
                # "Нет федерального округа" — пропускаем
                stats["skip"] += 1
                continue
            debt_share = row[2] if len(row) > 2 and row[2] is not None else None
            if debt_share is not None:
                insert_observation(cur, mid_debt_share, region_id, snap_date, debt_share, release_id)
                stats["debt_share"] += 1

    conn.commit()
    cur.close()
    return stats


def main():
    if not os.path.isdir(RAW_BASE):
        print(f"ERROR: raw dir not found: {RAW_BASE}")
        sys.exit(1)

    # Найти все снапшоты
    snapshots = sorted([d for d in os.listdir(RAW_BASE) if os.path.isdir(os.path.join(RAW_BASE, d))])
    print(f"Snapshots found: {snapshots}")

    conn = db_tunnel.connect()
    total_stats = {}
    for snap in snapshots:
        snap_dir = os.path.join(RAW_BASE, snap)
        snap_date = snap  # YYYY-MM-DD
        print(f"\nProcessing {snap_date}...")
        stats = process_snapshot(conn, snap_dir, snap_date)
        total_stats[snap] = stats
        print(f"  exp_total={stats['exp_total']} exp_plan={stats['exp_plan']} "
              f"exec_share={stats['exec_share']} exp_pc={stats['exp_pc']} "
              f"trf_fed={stats['trf_fed']} debt_share={stats['debt_share']} skip={stats['skip']}")

    conn.close()

    # Итог
    print("\n=== TOTAL ===")
    for snap, s in total_stats.items():
        total = s["exp_total"] + s["exp_plan"] + s["exec_share"] + s["exp_pc"] + s["trf_fed"] + s["debt_share"]
        print(f"  {snap}: {total} obs (skip={s['skip']})")


if __name__ == "__main__":
    main()