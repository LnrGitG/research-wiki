#!/usr/bin/env python3
"""
Гармонизация КЭП (рубеж 7): staging.rosstat_kep__* → core.observation_v2.

Логика
------
Каждая связка (лист, раздел+подпоказатель, блок, частота) становится ОТДЕЛЬНОЙ
метрикой.

Почему блок → отдельная метрика: единица измерения в схеме привязана к метрике
(core.metric.unit_id), а блоки одного показателя измеряются по-разному —
уровень в млрд рублей или млн м², блоки yoy/mom всегда в процентах. Схлопнуть
их в одну метрику = поставить ложную единицу.

Почему идентичность ряда — это (раздел, подпоказатель, блок), а НЕ номер строки:
наивное решение «одна строка = один ряд» неверно. В 2.3 подпоказатель «до 1
года» повторяется в каждой годовой подтаблице, в 4.7 «трудоспособное» — под
каждым годом-секцией: номер строки у одного и того же ряда разный. Обратная
ловушка: одинаковые метки подпоказателей встречаются в РАЗНЫХ подтаблицах —
в 1.9 «импорт товаров» есть и по дальнему зарубежью (раздел 1.9.1), и по СНГ
(1.9.2). Поэтому в series склеены раздел и подпоказатель через « || » — это
различает оба случая. Проверено: без раздела терялось 902 строки из 3 567 в
листе 4.4 и 484 из 868 в 2.3.

Коды метрик: kep + номер листа без точки + суффикс блока
  1.7 level → kep17   |  1.7 yoy → kep17y  |  1.7 mom → kep17m

Производительность: метрики вставляются ПАЧКАМИ одним executemany, наблюдения —
COPY по таблицам. Одиночные INSERT с commit() внутри цикла не используются:
они держат транзакцию и, что важнее, уничтожают серверный курсор (грабля,
пойманная на рубеже 5) — скрипт зависает.

Запуск:
  python3 scripts/harmonize_7_kep.py
  SIMULATE=1 python3 scripts/harmonize_7_kep.py    # только план
"""
import os
import re
import sys
from datetime import date

import psycopg

os.environ.setdefault("PGPASSFILE", os.path.expanduser("~/.pgpass"))
DSN = os.environ.get("PGDSN",
                     "host=127.0.0.1 port=15432 dbname=research_wiki user=wiki")
SCHEMA = "staging"
TAG = "stage7"
SIMULATE = os.environ.get("SIMULATE") == "1"
BATCH_METRICS = 200

# методологические швы: до этого года ряд неоднороден
BREAKS = {"okved2": 2017, "income": 2013, "investment": 2016}
BREAK_SHEETS = {
    "1.2": "okved2", "1.2 (1999-2013)": "okved2", "1.2 (2014-2026)": "okved2",
    "1.4": "okved2", "1.6": "investment", "1.6.1": "investment",
    "4.4": "income", "4.6 (2007-2009)": "income", "4.6 (2010-2012)": "income",
    "4.6 (2013-2025)": "income", "4.6 (2025-2026)": "income",
    "4.7": "income",
}
BLOCK_SUFFIX = {"level": "", "yoy": "y", "mom": "m"}


def log(m):
    print(m, flush=True)


def period_start(freq, year, month, quarter):
    if freq == "M" and month:
        return date(year, month, 1)
    if freq == "Q" and quarter:
        return date(year, (quarter - 1) * 3 + 1, 1)
    return date(year, 1, 1)


def main():
    conn = psycopg.connect(DSN)
    conn.autocommit = False
    cur = conn.cursor()

    cur.execute("SELECT source_code, source_id FROM core.source")
    src_ids = dict(cur.fetchall())
    cur.execute("SELECT frequency_code, frequency_id FROM core.frequency")
    freq_ids = dict(cur.fetchall())
    cur.execute("SELECT unit_code, unit_id FROM core.unit")
    unit_ids = dict(cur.fetchall())
    cur.execute("SELECT metric_code FROM core.metric")
    taken = {r[0] for r in cur.fetchall()}

    cur.execute("""SELECT table_name FROM information_schema.tables
                   WHERE table_schema=%s AND table_name LIKE 'rosstat_kep__%%'
                   ORDER BY 1""", (SCHEMA,))
    tables = [r[0] for r in cur.fetchall()]
    if not tables:
        log("ОШИБКА: нет таблиц rosstat_kep__* в staging")
        sys.exit(1)
    sid = src_ids.get("rosstat")
    if not sid:
        log("ОШИБКА: нет источника rosstat")
        sys.exit(1)
    log("таблиц КЭП: %d" % len(tables))

    # ---------- 1. читаем ВСЁ в память (курсор закрываем до вставок) ----------
    keys, labels, rows_data = [], set(), {}
    for t in tables:
        cur.execute("""SELECT DISTINCT sheet, series, block, unit_code, unit_name,
                              frequency, release_label, row_no, col, block_name
                       FROM %s."%s" ORDER BY 1,2,3,6""" % (SCHEMA, t))
        for (sheet, series, block, ucode, uname, freq, label, rn, col,
             bname) in cur.fetchall():
            keys.append((sheet, series, block, bname, freq, ucode, uname, rn, col))
            labels.add(label)
        cur.execute("""SELECT sheet, series, block, frequency, year, month,
                              quarter, value, release_label, footnote, row_no, col,
                              block_name
                       FROM %s."%s" ORDER BY sheet""" % (SCHEMA, t))
        rows_data[t] = cur.fetchall()
    # Идентичность ряда: (лист, раздел+подпоказатель, блок, частота).
    # Номер строки для этого не годится — один ряд размазан по строкам разных
    # лет, а одинаковые метки подпоказателей встречаются в разных подтаблицах
    # листа. Поэтому в series уже склеены раздел и подпоказатель.
    seen = set()
    uniq_keys = []
    for k in keys:
        kk = (k[0], k[1], k[2], k[3], k[4], k[7], k[8])
        if kk in seen:
            continue
        seen.add(kk)
        uniq_keys.append(k)
    log("уникальных связок: %d, релизов: %d" % (len(uniq_keys), len(labels)))

    # ---------- 2. релизы ----------
    rel_cache = {}
    for label in sorted(labels):
        cur.execute("""SELECT release_id FROM core.release
                       WHERE source_id=%s AND release_label=%s""", (sid, label))
        r = cur.fetchone()
        if r:
            rel_cache[label] = r[0]
            continue
        if SIMULATE:
            rel_cache[label] = -1
            continue
        cur.execute("""INSERT INTO core.release
            (source_id, release_label, published_at, status, notes)
            VALUES (%s,%s,now(),'loaded','Рубеж 7: КЭП Росстата')
            RETURNING release_id""", (sid, str(label)[:200]))
        rel_cache[label] = cur.fetchone()[0]
    if not SIMULATE:
        conn.commit()
    log("релизов подготовлено: %d" % len(rel_cache))

    # ---------- 3. метрики пачками ----------
    metrics = {}
    batch, created = [], 0
    for sheet, series, block, bname, freq, ucode, uname, rn, col in uniq_keys:
        f_id = freq_ids.get(freq)
        u_id = unit_ids.get(ucode) if ucode else unit_ids.get("unknown")
        if not f_id:
            continue
        if not u_id:
            u_id = unit_ids.get("unknown", 18)
        base = "kep" + re.sub(r"\D", "", sheet) + BLOCK_SUFFIX.get(block, "x")
        code, i = base, 2
        while code in taken:
            code = "%s%d" % (base, i)
            i += 1
        taken.add(code)
        name = "%s — %s (КЭП %s)" % (series, block, sheet)
        batch.append((code, name[:300],
                      "Краткосрочные экономические показатели РФ, лист %s" % sheet,
                      u_id, f_id, [TAG, "kep"]))
        metrics[(sheet, series, block, bname, freq, rn, col)] = code

    if not SIMULATE:
        for i in range(0, len(batch), BATCH_METRICS):
            chunk = batch[i:i + BATCH_METRICS]
            cur.executemany("""INSERT INTO core.metric
                (metric_code, name_ru, description, unit_id, frequency_id,
                 metric_type, is_derived, status, tags)
                VALUES (%s,%s,%s,%s,%s,'primary',false,'active',%s)""", chunk)
            conn.commit()
            created += len(chunk)
            log("  метрики: %d/%d" % (created, len(batch)))
    else:
        created = len(batch)
    log("зарегистрировано метрик: %d" % created)

    # ---------- 4. карта код → metric_id ----------
    if not SIMULATE:
        cur.execute("SELECT metric_code, metric_id FROM core.metric WHERE 'kep' = ANY(tags)")
        id_by_code = dict(cur.fetchall())
    else:
        id_by_code = {c: -i for i, c in enumerate(metrics.values())}

    # ---------- 5. наблюдения ----------
    total = 0
    for t in tables:
        batch_obs = []
        for (sheet, series, block, freq, year, month, quarter, value, label,
             foot, rn, col, bname) in rows_data[t]:
            code = metrics.get((sheet, series, block, bname, freq, rn, col))
            if not code:
                continue
            mid = id_by_code.get(code)
            if not mid:
                continue
            ps = period_start(freq, year, month, quarter)
            flags = []
            bk = BREAK_SHEETS.get(sheet)
            if bk and year < BREAKS[bk]:
                flags.append("методологический_разрыв_%d" % BREAKS[bk])
            sd = "ряд: КЭП | лист: %s | блок: %s" % (sheet, str(bname)[:60])
            if foot:
                sd += " | сноска: %s" % str(foot)[:40]
            batch_obs.append((mid, 1, freq_ids[freq], ps, ps, float(value),
                              "final", "validated", sid, rel_cache[label],
                              flags, sd, None))
        if not batch_obs:
            continue
        # дедуп по полному ключу ON CONFLICT
        seen_k, uniq = set(), []
        for b in batch_obs:
            k = (b[0], b[1], b[2], b[3], b[8], b[9], b[6], b[11])
            if k in seen_k:
                continue
            seen_k.add(k)
            uniq.append(b)
        if not SIMULATE:
            with cur.copy("""COPY core.observation_v2 (metric_id, region_id,
                frequency_id, period_start, period_end, value, assessment_type,
                observation_status, source_id, release_id, quality_flags,
                sub_dimension, notes) FROM STDIN""") as cp:
                for b in uniq:
                    cp.write_row(b)
            conn.commit()
        total += len(uniq)
        log("  %-24s +%s (всего %s)" % (t.replace("rosstat_kep__", ""),
                                        format(len(uniq), ","), format(total, ",")))

    log("\n=== ИТОГ ===")
    log("наблюдений: %s" % format(total, ","))
    log("метрик: %d" % created)
    log("релизов: %d" % len(rel_cache))
    if SIMULATE:
        log("(SIMULATE — в базу ничего не записано)")
    conn.close()


if __name__ == "__main__":
    main()
