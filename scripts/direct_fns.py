#!/usr/bin/env python3
"""Прямой загрузчик ФНС: сырьё raw/fns → канон (без SQLite-лендинга).

Заменяет группы рубежа 6: fns_profitorg_key_quarterly, fns_1nom_okved_f_quarterly,
fns_rf_annual. Разбор сырья повторяет прежние скрипты (repair_fns_profitorg.py,
fns_rf_annual_build.py) — те же кодировки, разделители, нормализация регионов, —
но запись идёт сразу в catalog.metric + data.observation.

Что исправляется по сравнению с прежним путём:

1. Кодировка. Файлы 5-П до ноября 2022 — cp1251; читались как utf-8, кириллица
   превращалась в «кракозябры», имена регионов не сопоставлялись: в каноне они
   лежат как подразрез «категория: ���������» вместо региона.
2. Частота. Рубеж 6 помечал все свои наблюдения квартальной частотой; здесь
   частота по группе (снапшоты 5-П и 1-НОМ — квартальная, РФ-итоги — годовая).
3. Дубли карточек от обрезки имени в 200 знаков (vdpotr/vdpotr_2, vrpotr/vrpot)
   уходят вместе со старыми строками: метрика ищется по обрезанному имени.

Запуск:
    python3 scripts/direct_fns.py                      # сухой прогон всех групп
    APPLY=1 python3 scripts/direct_fns.py profitorg    # запись одной группы
    APPLY=1 REPLACE=1 python3 scripts/direct_fns.py profitorg  # со снятием старых строк

Точка возврата для REPLACE: дамп снимается в attic/fns_before_<группа>.csv.gz.
"""
import csv
import glob
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from direct_core import Writer, norm  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.environ.get('FNS_RAW', os.path.join(REPO, 'raw', 'fns'))
SOURCE = 'fns'
APPLY = os.environ.get('APPLY') == '1'
REPLACE = os.environ.get('REPLACE') == '1'
SKIP_TAIL = ('_structure', '_promote', 'manifest')

# Дефекты исходников: латинская H в «Hенецкий», сокращение «Марий-Эл»,
# составное написание «Архангельская область и Ненецкий автономный округ».
FIXUPS = {
    'республика марий-эл': 'республика марий эл',
    'архангельская область и ненецкий автономный округ':
        'архангельская область (с нао)',
}
# «Российская Федерация» + составные строки источников, которые не регионы
NOT_REGION = ('российская федерация', 'россия')


def read_csv(path):
    """Читает CSV ФНС с автоопределением кодировки и разделителя."""
    raw = open(path, 'rb').read()
    txt = enc = None
    for e in ('utf-8', 'cp1251'):
        try:
            txt = raw.decode(e)
            enc = e
            break
        except UnicodeDecodeError:
            continue
    if txt is None:
        return [], None, None
    first = txt.splitlines()[0] if txt.splitlines() else ''
    delim = ';' if first.count(';') > first.count(',') else ','
    return list(csv.reader(io.StringIO(txt), delimiter=delim)), enc, delim


def num(v):
    v = (v or '').strip().strip('"').replace(' ', '').replace('\xa0', '')
    if not v:
        return None
    if v.count(',') == 1 and v.count('.') == 0:
        v = v.replace(',', '.')
    elif v.count(',') > 1:
        v = v.replace('.', '').replace(',', '.')
    try:
        return float(v)
    except ValueError:
        return None


def is_region(s):
    s = (s or '').strip()
    if len(s) < 5 or s == 'nan':
        return False
    if re.search(r'^[\d\s.,—\-Xx]+$', s):
        return False
    if 'данные по' in s:
        return False
    if not re.search(r'[А-Яа-яA-Za-z]{4,}', s):
        return False
    return True


def clean_region(name):
    s = re.sub(r'\s+', ' ', (name or '').strip().strip('"')).strip()
    s = s.replace('Hенецкий', 'Ненецкий')      # латинская H в исходнике
    s = s.replace('\xa0', ' ')
    return FIXUPS.get(s.lower(), s)


def norm_snap(s):
    """Дата съёма из имени файла. Часть старых файлов ФНС названа ДДММГГГГ
    (usn_08082017), часть — ГГГГММДД; приводим к ГГГГММДД."""
    s = str(s)
    y = int(s[:4])
    if 2000 <= y <= 2030 and 1 <= int(s[4:6]) <= 12:
        return s
    return '%s%s%s' % (s[4:], s[2:4], s[:2])


def snap_to_ps(snap):
    """Снапшот ФНС (YYYYMMDD) → (год, месяц начала квартала)."""
    m = re.match(r'^(\d{4})(\d{2})(\d{2})?', str(snap))
    if not m:
        return None
    qm = {1: 1, 2: 1, 3: 1, 4: 4, 5: 4, 6: 4,
          7: 7, 8: 7, 9: 7, 10: 10, 11: 10, 12: 10}.get(int(m.group(2)), 0)
    return (int(m.group(1)), qm) if qm else None


def region_id(w, name, stats):
    """Регион по имени сырья: точное имя, алиас, поправка дефектов."""
    for cand in (name, clean_region(name)):
        rid = w.reg.get(norm(cand))
        if rid:
            stats['matched'] += 1
            return rid
    if norm(name) in NOT_REGION or norm(clean_region(name)) in NOT_REGION:
        stats['rf_rows'] += 1
        return w.RU
    stats['unmatched'].add(name)
    return w.RU


def field_names():
    """Код поля → русское название из profitorg_structure.csv."""
    p = os.path.join(RAW, 'profitorg_structure.csv')
    if not os.path.exists(p):
        return {}
    rows, _, _ = read_csv(p)
    out = {}
    for r in rows[1:]:
        if len(r) >= 3 and r[0]:
            out[r[0].strip().strip('"')] = re.sub(r'\s+', ' ', r[2]).strip()
    return out


# --- группы ---------------------------------------------------------------
def group_profitorg(w):
    """5-П: пять полей по регионам, снапшоты 2018–2026."""
    names = field_names()
    codes = ['GB', 'G1', 'G2', 'G4', 'G6']
    files = sorted(f for f in glob.glob(os.path.join(RAW, 'profitorg_????????.csv'))
                   if not f.endswith(SKIP_TAIL))
    rows, stats, snaps = [], {'matched': 0, 'unmatched': set(), 'rf_rows': 0}, []
    for p in files:
        snap = re.search(r'_(\d{8})\.csv$', p).group(1)
        data, enc, delim = read_csv(p)
        if not data:
            print('   ПРОПУСК %s: не читается' % os.path.basename(p))
            continue
        snaps.append(snap)
        hdr = [h.strip().strip('"') for h in data[0]]
        have = [c for c in codes if c in hdr]
        for r in data[1:]:
            if not r or not is_region(r[0]):
                continue
            name = clean_region(r[0])
            rid = region_id(w, name, stats)
            for c in have:
                i = hdr.index(c)
                if len(r) <= i:
                    continue
                v = num(r[i])
                if v is None:
                    continue
                rows.append(dict(
                    metric_name=names.get(c, c), value=v, ps=snap_to_ps(snap),
                    region=rid, freq='Q', source=SOURCE,
                    release='fns_profitorg_5P_%s' % snap,
                    sub='%s: %s | снапшот: %s' % ('field', names.get(c, c), snap),
                    unit='ths_rub'))
    stats['snapshots'] = len(set(snaps))
    return rows, stats


def group_1nom_okved_f(w):
    """1-НОМ: выручка по ОКВЭД F (строительство), колонка G53."""
    files = sorted(f for f in glob.glob(os.path.join(RAW, '1nom_????????.csv'))
                   if not f.endswith(SKIP_TAIL))
    rows, stats, snaps = [], {'matched': 0, 'unmatched': set(), 'rf_rows': 0}, []
    for p in files:
        snap = re.search(r'_(\d{8})\.csv$', p).group(1)
        data, enc, delim = read_csv(p)
        if not data or 'G53' not in [h.strip().strip('"') for h in data[0]]:
            continue
        snaps.append(snap)
        hdr = [h.strip().strip('"') for h in data[0]]
        i53 = hdr.index('G53')
        for r in data[1:]:
            if not r or len(r) <= i53 or not is_region(r[0]):
                continue
            v = num(r[i53])
            if v is None:
                continue
            rows.append(dict(
                metric_name='G53_okved_F', value=v, ps=snap_to_ps(snap),
                region=region_id(w, clean_region(r[0]), stats), freq='Q',
                source=SOURCE,
                release='fns_1nom_okvedF_%s' % snap,
                sub='form: 1-НОМ | metric: G53_okved_F', unit='ths_rub'))
    stats['snapshots'] = len(set(snaps))
    return rows, stats


def _rf_sum(data, code):
    """Сумма по регионам РФ для колонки code (как в fns_rf_annual_build.py)."""
    hdr = [h.strip().strip('"') for h in data[0]]
    if code not in hdr:
        return None
    i = hdr.index(code)
    tot, n = 0.0, 0
    for r in data[1:]:
        if len(r) <= i or not is_region(r[0]):
            continue
        v = num(r[i])
        if v is not None:
            tot += v
            n += 1
    return tot if n >= 60 else None


def group_rf_annual(w):
    """РФ-итоги по формам ФНС (5-П, 5-УСН, 1-НДС, 5-НДФЛ, 5-ТН)."""
    forms = {
        'profitorg': ('5-П', {'GB': 'rev_profit', 'G1': 'rev_loss',
                              'G2': 'nonop_inc_profit', 'G4': 'exp_sales_profit',
                              'G6': 'nonop_exp_profit'}),
        'taxagent': ('5-НДФЛ', {'GB': 'income_total', 'G1': 'ndfl_withheld'}),
        '1nds': ('1-НДС', {'GB': 'nds_accrued_total'}),
        'usn': ('5-УСН', {'GB': 'usn_income', 'G1': 'usn_expense'}),
        'ttorg': ('5-ТН', {'GB': 'tnpayers'}),
    }
    rows, stats = [], {'matched': 0, 'unmatched': set(), 'rf_rows': 0}
    for code, (label, mets) in forms.items():
        best = {}
        for p in sorted(glob.glob(os.path.join(RAW, '%s_????????.csv' % code))):
            if p.endswith(SKIP_TAIL):
                continue
            snap = norm_snap(re.search(r'_(\d{8})\.csv$', p).group(1))
            data, _, _ = read_csv(p)
            if not data:
                continue
            # отчётный год: снапшот 01.01 — это итог прошлого года
            y = int(snap[:4]) - (1 if snap[4:6] == '01' else 0)
            vals = {m: _rf_sum(data, c) for c, m in mets.items()}
            if any(v is not None for v in vals.values()):
                best[y] = (snap, vals)
        for y, (snap, vals) in sorted(best.items()):
            for m, v in vals.items():
                if v is None:
                    continue
                rows.append(dict(
                    metric_name='%s (РФ)' % m, value=round(v / 1e6, 1),
                    ps=(y, 0), region=w.RU, freq='A', source=SOURCE,
                    release='fns_rf_annual_%s_%s' % (label, snap),
                    sub='form: %s | metric: %s' % (label, m), unit='bln_rub'))
    return rows, stats


GROUPS = {
    'profitorg': group_profitorg,
    '1nom_okved_f': group_1nom_okved_f,
    'rf_annual': group_rf_annual,
}


def main():
    want = [a for a in sys.argv[1:] if not a.startswith('-')] or list(GROUPS)
    w = Writer(tag='direct_fns', simulate=not APPLY)
    for g in want:
        fn = GROUPS.get(g)
        if fn is None:
            print('неизвестная группа:', g, '| доступны:', ', '.join(GROUPS))
            continue
        rows, stats = fn(w)
        un = sorted(stats['unmatched'])
        print('== %-14s строк %6d | регионов сопоставлено %6d | не найдено %3d%s'
              % (g, len(rows), stats['matched'], len(un),
                 (' | снапшотов %d' % stats['snapshots']) if 'snapshots' in stats else ''))
        if un:
            print('   не сопоставлены: %s' % ', '.join(un[:8]))
        if not APPLY:
            print('   СУХОЙ ПРОГОН (APPLY=1 — запись)')
            continue
        if REPLACE:
            nm = sorted({r['metric_name'] for r in rows})
            dump = os.path.join(REPO, 'attic', 'fns_before_%s.csv.gz' % g)
            n = w.dump_group(nm, dump)
            print('   снято старых строк: %d → %s' % (n, dump))
        prep, ins, conf, newm = w.ingest(rows, group=g)
        print('   подготовлено %d | вставлено %d | конфликтов %d | новых метрик %d'
              % (prep, ins, conf, newm))
    w.close()


if __name__ == '__main__':
    main()
