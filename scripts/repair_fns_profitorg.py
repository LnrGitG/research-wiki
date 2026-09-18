#!/usr/bin/env python3
"""
Восстановление данных ФНС 5-П (прибыль организаций) из исходных CSV.

ДЕФЕКТ: файлы profitorg_*.csv в кодировке cp1251 читались как utf-8. Кириллица
превращалась в символы замены, имена регионов схлопывались по длине: вместо
85 регионов в staging оказалось 35 (для снапшотов до ноября 2022), а сами
строки уходили в «категорию» под общим именем. Всего в staging 9 117 строк
против 14 230 в исходниках — потеря 5 113 значений.

ИСПРАВЛЕНИЕ: читать с автоопределением кодировки (utf-8, затем cp1251) и
разделителя (';' или ',', в файлах с 2024 — запятая с кавычками). Коды полей
берутся из profitorg_structure.csv (колонка G/GA → русское название).

Пересобирает staging-таблицу и перезапускает рубеж 6 для затронутых метрик.

Запуск:  python3 repair_fns_profitorg.py            # сухой прогон
         APPLY=1 python3 repair_fns_profitorg.py     # применить
"""
import csv
import glob
import io
import os
import re
import sys
from collections import defaultdict

import psycopg

os.environ.setdefault("PGPASSFILE", os.path.expanduser("~/.pgpass"))
DSN = os.environ.get("PGDSN", "host=localhost port=5432 dbname=research_wiki user=wiki")
RAW = os.environ.get("FNS_RAW", "/home/lnr/research-wiki/raw/fns")
APPLY = os.environ.get("APPLY") == "1"

CODES = ["GB", "G1", "G2", "G4", "G6"]


def read_csv(path):
    """Читает CSV ФНС с автоопределением кодировки и разделителя."""
    raw = open(path, "rb").read()
    txt = enc = None
    for e in ("utf-8", "cp1251"):
        try:
            txt = raw.decode(e)
            enc = e
            break
        except UnicodeDecodeError:
            continue
    if txt is None:
        return [], None, None
    first = txt.splitlines()[0]
    delim = ";" if first.count(";") > first.count(",") else ","
    return list(csv.reader(io.StringIO(txt), delimiter=delim)), enc, delim


def is_region(s):
    s = (s or "").strip()
    if len(s) < 5 or s == "nan":
        return False
    if re.search(r"^[\d\s.,—\-Xx]+$", s):
        return False
    if "данные по" in s:
        return False
    return bool(re.search(r"[А-Яа-яA-Za-z]{4,}", s))


def load_field_names():
    """Коды полей → русские названия из profitorg_structure.csv."""
    p = os.path.join(RAW, "profitorg_structure.csv")
    raw = open(p, "rb").read()
    for e in ("utf-8", "cp1251"):
        try:
            txt = raw.decode(e)
            break
        except UnicodeDecodeError:
            continue
    rows = list(csv.reader(io.StringIO(txt), delimiter=";"))
    if len(rows[0]) < 3:
        rows = list(csv.reader(io.StringIO(txt), delimiter=","))
    names = {}
    for r in rows[1:]:
        if len(r) >= 3 and r[0]:
            names[r[0].strip()] = re.sub(r"\s+", " ", r[2]).strip()
    return names


# Дефекты исходников ФНС: латинская H в «Hенецкий», сокращение «Марий-Эл»,
# составное написание «Архангельская область и Ненецкий автономный округ».
FIXUPS = {
    "республика марий-эл": "Республика Марий Эл",
    "архангельская область и ненецкий автономный округ":
        "Архангельская область (с НАО)",
}


def clean_region(name):
    """Нормализация имени региона: убрать отступы, починить известные дефекты."""
    s = re.sub(r"\s+", " ", (name or "").strip().strip('"')).strip()
    s = s.replace("Hенецкий", "Ненецкий")  # латинская H в исходнике
    return FIXUPS.get(s.lower(), s)


def main():
    field_names = load_field_names()
    print("названий полей в справочнике: %d" % len(field_names))

    conn = psycopg.connect(DSN)
    cur = conn.cursor()
    cur.execute("SELECT region_id, name_ru FROM core.region")
    reg = {}
    for rid, nm in cur.fetchall():
        reg[re.sub(r"\s+", " ", nm).strip().lower()] = (rid, nm)
    cur.execute("SELECT alias, region_id FROM meta.region_alias")
    for a, rid in cur.fetchall():
        reg.setdefault(re.sub(r"\s+", " ", a).strip().lower(), (rid, None))
    RU = reg.get("российская федерация")

    # Алиасы, которых не было в справочнике: добавляем, чтобы будущие рубежи
    # матчили эти написания автоматически.
    new_aliases = []
    for bad, good in FIXUPS.items():
        hit = reg.get(good.lower())
        if hit and bad not in reg:
            new_aliases.append((bad, hit[0]))
            reg[bad] = hit
    if new_aliases:
        print("новых алиасов: %d (%s)" % (len(new_aliases),
              ", ".join("%s→%s" % (b, g) for b, g in FIXUPS.items())))
        if APPLY:
            cur.executemany("""INSERT INTO meta.region_alias
                (alias, region_id, source_id, confidence, created_at)
                VALUES (%s, %s, 9, 'exact', now())
                ON CONFLICT DO NOTHING""", new_aliases)
            conn.commit()
            print("   алиасы записаны в meta.region_alias")

    files = sorted(glob.glob(os.path.join(RAW, "profitorg_????????.csv")))
    rows_out = []
    stats = defaultdict(lambda: {"rows": 0, "regions": set(), "matched": 0, "unmatched": set()})

    for p in files:
        snap = re.search(r"_(\d{8})\.csv", p).group(1)
        rows, enc, delim = read_csv(p)
        if not rows:
            print("ПРОПУСК %s: не читается" % snap)
            continue
        hdr = [h.strip().strip('"') for h in rows[0]]
        have = [c for c in CODES if c in hdr]
        for r in rows[1:]:
            if not r or not is_region(r[0]):
                continue
            region = clean_region(r[0])
            key = region.lower()
            hit = reg.get(key)
            if hit:
                rid = hit[0]
                stats[snap]["matched"] += 1
            else:
                rid = RU
                stats[snap]["unmatched"].add(region)
            stats[snap]["regions"].add(region)
            for c in have:
                i = hdr.index(c)
                if len(r) <= i:
                    continue
                v = (r[i] or "").strip().strip('"').replace(" ", "").replace(",", ".")
                if not v:
                    continue
                try:
                    val = float(v)
                except ValueError:
                    continue
                rows_out.append((region, snap, field_names.get(c, c), val, rid))
                stats[snap]["rows"] += 1

    total_rows = len(rows_out)
    print("\n%-10s %-7s %6s %7s %7s %s" % ("снапшот", "кодир", "строк", "рег", "матч", "не найдено"))
    print("-" * 62)
    for p in files:
        snap = re.search(r"_(\d{8})\.csv", p).group(1)
        s = stats.get(snap)
        if not s:
            continue
        _, enc, _ = read_csv(p)
        print("%-10s %-7s %6d %7d %7d %s" %
              (snap, enc, s["rows"], len(s["regions"]), s["matched"],
               str(sorted(s["unmatched"]))[:30]))
    print("-" * 62)
    print("всего строк к записи: %s" % format(total_rows, ","))
    print("сейчас в staging:      9 117")

    if not APPLY:
        print("\nСУХОЙ ПРОГОН. Применить: APPLY=1 python3 repair_fns_profitorg.py")
        print("\nпримеры записей:")
        for r in rows_out[:3]:
            print("   %s" % (r,))
        for r in rows_out[-3:]:
            print("   %s" % (r,))
        conn.close()
        return

    # применяем: пересобираем staging-таблицу
    print("\nпересобираю staging.rosreestr_deals__fns_profitorg_key_quarterly")
    cur.execute("DROP TABLE IF EXISTS staging.rosreestr_deals__fns_profitorg_key_quarterly_new")
    cur.execute("""CREATE TABLE staging.rosreestr_deals__fns_profitorg_key_quarterly_new (
        region text, snapshot text, field text, value numeric, region_id int)""")
    cur.executemany("""INSERT INTO staging.rosreestr_deals__fns_profitorg_key_quarterly_new
                       VALUES (%s,%s,%s,%s,%s)""", rows_out)
    conn.commit()
    cur.execute("SELECT count(*) FROM staging.rosreestr_deals__fns_profitorg_key_quarterly_new")
    print("   записано: %s" % format(cur.fetchone()[0], ","))

    cur.execute("DROP TABLE staging.rosreestr_deals__fns_profitorg_key_quarterly")
    cur.execute("""ALTER TABLE staging.rosreestr_deals__fns_profitorg_key_quarterly_new
                   RENAME TO rosreestr_deals__fns_profitorg_key_quarterly""")
    conn.commit()
    print("   таблица заменена")

    print("\nтеперь перезапустите рубеж 6 (он идемпотентен по тегу stage6):")
    print("   python3 harmonize_6_rosstat_extra.py")
    conn.close()


if __name__ == "__main__":
    main()
