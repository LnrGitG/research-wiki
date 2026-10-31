#!/usr/bin/env python3
"""ЦБ VFS (формы 0420218) → канон catalog/data, БЕЗ промежуточной SQLite.

Вход — уже скачанные файлы raw/cbr/vfs/:
  01_04_D_New_loans_subj.xlsx  объём новых кредитов юрлицам по регионам
  01_05_D_Debt_subj.xlsx       задолженность по кредитам юрлицам по регионам
  02_04_New_loans_ind.xlsx     объём новых кредитов физлицам по регионам
  02_05_Debt_ind.xlsx          задолженность по кредитам физлицам по регионам

Важно: 02_04/02_05 — это ВСЕ кредиты физлицам, а не только ИЖК. Ипотечные
ряды (02_06–02_15) грузит cbr_mortgage_vfs_sync.py; здесь они не дублируются.

Лист «итого» (рубли + валюта). Загрузка идемпотентна: вставляются только
ключи (метрика, регион, период), которых ещё нет в каноне ни под каким
релизом; повторный прогон даёт 0 новых строк. Изменения уже записанных
значений печатаются как ревизии, но историю не перезаписывают.

Запуск: python3 scripts/transfer_cbr_vfs.py
"""
try:
    from xlsx_engine import open_workbook  # noqa: E402
except ImportError:  # запуск из другого каталога
    import os as _os
    import sys as _sys
    _sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
    from xlsx_engine import open_workbook  # noqa: E402

import datetime as dt
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import db_tunnel  # noqa: E402

try:
    from xlsx_engine import engine_from_argv, open_workbook  # noqa: E402
except ImportError:  # запуск из другого каталога
    import os as _os
    import sys as _sys
    _sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
    from xlsx_engine import engine_from_argv, open_workbook  # noqa: E402
ENGINE = engine_from_argv()  # --xlsx-engine openpyxl|fastexcel, резерв — XLSX_ENGINE


BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VFS_DIR = os.path.join(BASE, "raw", "cbr", "vfs")

FILES = {
    "01_04_D_New_loans_subj.xlsx": ("cbr_corp_new_loans_reg_m", "итого"),
    "01_05_D_Debt_subj.xlsx": ("cbr_corp_debt_reg_m", "итого"),
    "02_04_New_loans_ind.xlsx": ("cbr_ind_new_loans_reg_m", "итого"),
    "02_05_Debt_ind.xlsx": ("cbr_ind_debt_reg_m", "итого"),
}
NAMES = {
    "cbr_corp_new_loans_reg_m": "ЦБ: объём новых кредитов, предоставленных юридическим лицам, млн руб. (рег.)",
    "cbr_corp_debt_reg_m": "ЦБ: задолженность по кредитам, предоставленным юридическим лицам, млн руб. (рег.)",
    "cbr_ind_new_loans_reg_m": "ЦБ: объём новых кредитов, предоставленных физическим лицам, млн руб. (рег.)",
    "cbr_ind_debt_reg_m": "ЦБ: задолженность по кредитам, предоставленным физическим лицам, млн руб. (рег.)",
}
UNIT_MLN_RUB = 11
MONTHS = {"январь": 1, "февраль": 2, "март": 3, "апрель": 4, "май": 5, "июнь": 6,
          "июль": 7, "август": 8, "сентябрь": 9, "октябрь": 10, "ноябрь": 11,
          "декабрь": 12}


def num(x):
    if x is None:
        return None
    if isinstance(x, (int, float)):
        return float(x)
    s = str(x).replace(" ", "").replace("\xa0", "").replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return None


def period_of(v):
    if isinstance(v, (dt.datetime, dt.date)):
        return dt.date(v.year, v.month, 1)
    if isinstance(v, str):
        m = re.match(r"(\S+)\s+(\d{4})", v.strip())
        if m and m.group(1).lower() in MONTHS:
            return dt.date(int(m.group(2)), MONTHS[m.group(1).lower()], 1)
    return None


BASE_ALIAS = {
    "архангельская область": "архангельская область (с нао)",
    "архангельская область без данных по ненецкому автономному округу":
        "архангельская область (без нао)",
    "тюменская область": "тюменская область (с хмао и янао)",
    "тюменская область без данных по ханты-мансийскому автономному округу - югре "
    "и ямало-ненецкому автономному округу": "тюменская область (без хмао и янао)",
    "кемеровская область - кузбасс": "кемеровская область — кузбасс",
    "республика северная осетия - алания": "республика северная осетия — алания",
    "чувашская республика - чувашия": "чувашская республика",
    "г. москва": "москва",
    "г. санкт-петербург": "санкт-петербург",
    "г. севастополь": "севастополь",
    "ханты-мансийский автономный округ - югра":
        "ханты-мансийский автономный округ — югра",
}


def region_key(nm, rmap):
    """Нормализовать название региона источника под catalog.region."""
    k = nm.lower().replace("ё", "е").replace("  ", " ").strip()
    if k.startswith("в том числе "):
        k = k[len("в том числе "):].strip()
    candidates = []
    if k in BASE_ALIAS:
        candidates.append(BASE_ALIAS[k])
    candidates.append(k)
    if k.endswith(")") and " (" in k:
        base = k[:k.rindex(" (")].strip()
        if base in BASE_ALIAS:
            candidates.append(BASE_ALIAS[base])
        candidates.append(base)
    for c in candidates:
        if c in rmap:
            return c
    return k


def find_header(rows):
    """Строка шапки — та, где больше трёх ячеек с датой/месяцем."""
    for i, row in enumerate(rows[:6]):
        n = sum(1 for c in row[1:] if c is not None and period_of(c))
        if n > 3:
            return i
    return None


def main():
    with db_tunnel.connect() as conn:
        with conn.cursor() as cur:
            src_id = cur.execute(
                "SELECT source_id FROM catalog.source WHERE source_code='cbr'").fetchone()[0]
            freq_m = cur.execute(
                "SELECT frequency_id FROM catalog.frequency WHERE freq_code='M'").fetchone()[0]
            now = dt.datetime.utcnow()
            label = f"cbr-vfs-direct {now:%Y-%m-%d} (сырьё → канон)"
            rel = cur.execute(
                "SELECT release_id FROM catalog.release WHERE label=%s", (label,)).fetchone()
            if rel:
                release_id = rel[0]
                cur.execute("DELETE FROM data.observation WHERE release_id=%s", (release_id,))
            else:
                release_id = cur.execute(
                    """INSERT INTO catalog.release (source_id,label,published_at,status,notes)
                       VALUES (%s,%s,%s,'loaded','формы 0420218: прямые загрузчики, без SQLite')
                       RETURNING release_id""", (src_id, label, now.date())).fetchone()[0]
            conn.commit()

            rmap = {(nm or "").strip().lower().replace("ё", "е"): rid for rid, nm in
                    cur.execute("SELECT region_id, name_ru FROM catalog.region").fetchall()}
            midmap = {}
            for mc, name in NAMES.items():
                r = cur.execute("SELECT metric_id FROM catalog.metric WHERE metric_code=%s",
                                (mc,)).fetchone()
                if r:
                    midmap[mc] = r[0]
                else:
                    midmap[mc] = cur.execute(
                        """INSERT INTO catalog.metric
                           (metric_code,name_ru,unit_id,source_id,frequency_id,metric_type,status,is_active)
                           VALUES (%s,%s,%s,%s,%s,'primary','active',true) RETURNING metric_id""",
                        (mc, name, UNIT_MLN_RUB, src_id, freq_m)).fetchone()[0]
                    conn.commit()

            total_new = total_rev = total_seen = 0
            all_rej = {}
            for fname, (mcode, sheet) in FILES.items():
                path = os.path.join(VFS_DIR, fname)
                if not os.path.exists(path):
                    raise SystemExit(f"нет файла: {path}")
                wb = open_workbook(path, engine=ENGINE)
                if sheet not in wb.sheetnames:
                    raise SystemExit(f"{fname}: нет листа {sheet!r} ({wb.sheetnames})")
                rows = list(wb[sheet].iter_rows(values_only=True))
                wb.close()
                hi = find_header(rows)
                if hi is None:
                    raise SystemExit(f"{fname}/{sheet}: не найдена шапка с периодами")
                hdr = rows[hi]
                periods = {j: period_of(hdr[j]) for j in range(1, len(hdr))}
                periods = {j: p for j, p in periods.items() if p}
                mid = midmap[mcode]
                candidates = []
                rej = set()
                for row in rows[hi + 1:]:
                    nm = str(row[0]).strip() if row[0] else ""
                    if not nm:
                        continue
                    kk = region_key(nm, rmap)
                    rid = rmap.get(kk)
                    if rid is None:
                        rej.add(nm)
                        continue
                    for j, p in periods.items():
                        val = num(row[j])
                        if val is None:
                            continue
                        candidates.append((mid, rid, p, freq_m, val, src_id, release_id))
                # уже существующие ключи (любой релиз) и их значения
                existing = {}
                cur.execute(
                    """SELECT region_id, period_start, value FROM data.observation
                       WHERE metric_id=%s AND release_id<>%s""", (mid, release_id))
                for rid, p, v in cur.fetchall():
                    existing[(rid, p)] = float(v)
                fresh, revs = [], 0
                for rec in candidates:
                    key = (rec[1], rec[2])
                    if key in existing:
                        if abs(existing[key] - rec[4]) > 1e-9:
                            revs += 1
                        continue
                    fresh.append(rec)
                B = 4000
                ins = 0
                for i in range(0, len(fresh), B):
                    cur.executemany(
                        """INSERT INTO data.observation
                           (metric_id,region_id,period_start,frequency_id,value,
                            assessment_type,observation_status,source_id,release_id,sub_dimension)
                           VALUES (%s,%s,%s,%s,%s,'final','validated',%s,%s,'')
                           ON CONFLICT (metric_id,region_id,period_start,frequency_id,
                                        assessment_type,sub_dimension,release_id) DO NOTHING""",
                        fresh[i:i + B])
                    ins += cur.rowcount
                conn.commit()
                total_new += ins
                total_rev += revs
                total_seen += len(candidates)
                all_rej[fname] = rej
                ps = sorted({c[2] for c in candidates})
                print(f"  {fname}/{sheet}: разобрано {len(candidates):,}, новых {ins:,}, "
                      f"ревизий {revs}, период {ps[0] if ps else '—'}..{ps[-1] if ps else '—'}, "
                      f"регионов {len({c[1] for c in candidates})}", flush=True)
                if rej:
                    print(f"    неопознанные регионы: {sorted(rej)[:6]} ({len(rej)})", flush=True)
            print(f"итого: разобрано {total_seen:,}, вставлено {total_new:,}, "
                  f"ревизий {total_rev}, релиз {release_id}: {label}")


if __name__ == "__main__":
    main()