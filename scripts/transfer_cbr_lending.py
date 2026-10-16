#!/usr/bin/env python3
"""Мост cbr_lending.db (landing) → канон catalog/data.

Сверка 16.10.2026 показала, что landing `data/cbr_lending.db` (три таблицы:
mortgage_monthly, escrow_monthly, corporate_monthly) на ~95 % дублирует уже
канонические ряды, наполняемые параллельным путём из тех же сырых xlsx
(raw/cbr/vfs → transfer_cbr_vfs.py). Дубликаты НЕ переносятся.

Уникальный остаток (в каноне отсутствует) — 4 показателя, они и переносятся:

  mortgage_monthly  avg_price_sqm_первичный_рынок  → cbr_housing_price_primary_reg_m
  mortgage_monthly  avg_price_sqm_вторичный_рынок → cbr_housing_price_secondary_reg_m
  escrow_monthly    debt                          → cbr_pf_debt_reg_m
  escrow_monthly    credit_rate                   → cbr_pf_rate_reg_m

Разрешение регионов: точное совпадение с catalog.region.name_ru (без регистра),
затем meta.region_alias (приоритет confidence='exact'). Агрегаты
(РФ, федеральные округа, «Итого») пропускаются: канонические рег. ряды их не содержат.

Идемпотентно: ON CONFLICT DO NOTHING по бизнес-ключу наблюдения.
Точка возврата: DELETE FROM data.observation WHERE release_id=<новый>.
"""
import os
import re
import sqlite3
import sys
import datetime as dt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import db_tunnel  # noqa: E402

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANDING = os.path.join(BASE, 'data', 'cbr_lending.db')
RELEASE_LABEL = os.environ.get(
    'CBR_LENDING_RELEASE',
    'cbr-lending residue 2026-10-16 (цены ЦБ рег., ставка/задолженность ПФ)')

# код канона → (имя, unit_id, таблица landing, indicator)
RESIDUE = {
    'cbr_housing_price_primary_reg_m': (
        'ЦБ: средняя цена 1 кв.м жилья, первичный рынок (рег.)', 14,
        'mortgage_monthly', 'avg_price_sqm_первичный_рынок'),
    'cbr_housing_price_secondary_reg_m': (
        'ЦБ: средняя цена 1 кв.м жилья, вторичный рынок (рег.)', 14,
        'mortgage_monthly', 'avg_price_sqm_вторичный_рынок'),
    'cbr_pf_debt_reg_m': (
        'ЦБ: задолженность по действующим кредитным договорам проектного '
        'финансирования (рег.)', 11, 'escrow_monthly', 'debt'),
    'cbr_pf_rate_reg_m': (
        'ЦБ: средневзвешенная ставка по кредитным договорам проектного '
        'финансирования (рег.)', 12, 'escrow_monthly', 'credit_rate'),
}


def norm(s):
    return (s or '').strip().lower().replace('ё', 'е')


def main():
    assert os.path.exists(LANDING), 'нет %s' % LANDING
    con = sqlite3.connect(LANDING)

    with db_tunnel.connect() as conn:
        with conn.cursor() as cur:
            src_id = cur.execute(
                "SELECT source_id FROM catalog.source WHERE source_code='cbr'").fetchone()[0]
            freq_m = cur.execute(
                "SELECT frequency_id FROM catalog.frequency WHERE freq_code='M'").fetchone()[0]

            # --- регионы: имя + алиасы ---
            rmap = {}
            for rid, nm, lvl in cur.execute(
                    'SELECT region_id, name_ru, level FROM catalog.region').fetchall():
                rmap[norm(nm)] = (rid, lvl)
            amap = {}
            for al, rid, conf in cur.execute(
                    'SELECT alias, region_id, confidence FROM meta.region_alias').fetchall():
                k = norm(al)
                if k not in amap or conf == 'exact':
                    amap[k] = rid
            rf_id = cur.execute(
                "SELECT region_id FROM catalog.region WHERE name_ru='Российская Федерация'").fetchone()
            fo_ids = {r[0] for r in cur.execute(
                "SELECT region_id FROM catalog.region WHERE level <> 'region'").fetchall()}

            def resolve(name):
                n = norm(name)
                if not n or 'итого' in n or 'федерация' in n:
                    return None
                # снять служебные префиксы строк-расшифровок («в том числе …»)
                n = re.sub(r'^в том числе[:\s]*', '', n).strip()
                n = re.sub(r'^в т\.\s?ч\.\s*', '', n).strip()
                if n in rmap:
                    rid, lvl = rmap[n]
                    return rid if lvl == 'region' else None
                if n in amap:
                    rid = amap[n]
                    return None if (rf_id and rid == rf_id[0]) or rid in fo_ids else rid
                # служебные хвосты-опечатки вида «Воронежская область7»
                stripped = ''.join(ch for ch in n if not ch.isdigit()).strip()
                if stripped != n and stripped in rmap:
                    rid, lvl = rmap[stripped]
                    return rid if lvl == 'region' else None
                return None

            # --- release ---
            rel = cur.execute('SELECT release_id FROM catalog.release WHERE label=%s',
                              (RELEASE_LABEL,)).fetchone()
            if rel:
                release_id = rel[0]
            else:
                release_id = cur.execute(
                    """INSERT INTO catalog.release (source_id,label,published_at,status,notes)
                       VALUES (%s,%s,%s,'loaded',
                       'остаток cbr_lending.db: цены ЦБ рег., ставка/задолженность проектного финансирования')
                       RETURNING release_id""",
                    (src_id, RELEASE_LABEL, dt.date(2026, 10, 16))).fetchone()[0]
                conn.commit()

            def ensure_metric(code):
                r = cur.execute('SELECT metric_id FROM catalog.metric WHERE metric_code=%s',
                                (code,)).fetchone()
                if r:
                    return r[0]
                name, unit_id = RESIDUE[code][0], RESIDUE[code][1]
                mid = cur.execute(
                    """INSERT INTO catalog.metric
                       (metric_code,name_ru,unit_id,source_id,frequency_id,metric_type,status,is_active)
                       VALUES (%s,%s,%s,%s,%s,'primary','active',true) RETURNING metric_id""",
                    (code, name, unit_id, src_id, freq_m)).fetchone()[0]
                conn.commit()
                return mid

            metrics = {c: ensure_metric(c) for c in RESIDUE}
            conn.commit()

            # --- сбор строк ---
            rows = []
            stat = {c: {'parsed': 0, 'skip': 0} for c in RESIDUE}
            rejects = {}
            for code, (_n, _u, table, indicator) in RESIDUE.items():
                for region, rdate, val in con.execute(
                        'SELECT region_name, report_date, value FROM "%s" WHERE indicator=?'
                        % table, (indicator,)):
                    if val is None:
                        continue
                    rid = resolve(region)
                    if rid is None:
                        stat[code]['skip'] += 1
                        rejects[region] = rejects.get(region, 0) + 1
                        continue
                    stat[code]['parsed'] += 1
                    rows.append((metrics[code], rid, rdate[:10], float(val)))

            # --- пакетная вставка ---
            inserted = 0
            B = 2000
            for i in range(0, len(rows), B):
                chunk = rows[i:i + B]
                cur.executemany(
                    """INSERT INTO data.observation
                       (metric_id,region_id,period_start,frequency_id,value,
                        assessment_type,observation_status,source_id,release_id,sub_dimension)
                       VALUES (%s,%s,%s,%s,%s,'final','validated',%s,%s,'')
                       ON CONFLICT (metric_id,region_id,period_start,frequency_id,
                                    assessment_type,sub_dimension,release_id) DO NOTHING""",
                    [(m, rid, per, freq_m, v, src_id, release_id)
                     for m, rid, per, v in chunk])
                inserted += cur.rowcount
            conn.commit()

            # --- отчёт ---
            print('release_id=%s label=%r' % (release_id, RELEASE_LABEL))
            print('source=cbr id=%s freq_M=%s' % (src_id, freq_m))
            for code, mid in metrics.items():
                got = cur.execute('SELECT count(*) FROM data.observation WHERE metric_id=%s',
                                  (mid,)).fetchone()[0]
                regs = cur.execute('SELECT count(DISTINCT region_id) FROM data.observation '
                                   'WHERE metric_id=%s', (mid,)).fetchone()[0]
                lp = cur.execute('SELECT max(period_start) FROM data.observation '
                                 'WHERE metric_id=%s', (mid,)).fetchone()[0]
                print('  %-34s canon=%-6d рег.=%-3d до %s  (parsed=%d skip=%d)'
                      % (code, got, regs, lp, stat[code]['parsed'], stat[code]['skip']))
            print('всего вставлено (новых):', inserted, '| строк-кандидатов:', len(rows))
            if rejects:
                print('регионы-отказы:', sorted(rejects.items(), key=lambda x: -x[1])[:10])


if __name__ == '__main__':
    main()
