#!/usr/bin/env python3
"""Прямой загрузчик: ИКВ по регионам, квартальные публикации Росстата → канон.

Сырьё: `raw/rosstat/data/Inv_reg_kv_2020-2026.xlsx`, два листа —
«млн. рублей» (объём инвестиций в основной капитал) и «к соотв.периоду»
(в % к соответствующему периоду). Оба листа устроены одинаково: строка с годами,
под ней четыре ПЕРИОДА НАКОПЛЕНИЯ («I квартал», «I полугодие»,
«январь-сентябрь», «год»), затем строки территорий.

Важное свойство источника: подписи периодов — накопительные, а не квартальные.
«I полугодие 2020» — это 7 111 774,7 млн руб., то есть январь-июнь целиком, а
не II квартал (3 246 620,1 млн руб. + 2 986 759,7 млн руб. — сумма двух кварталов
даёт 6 233 379,8, но публикация даёт 7 111 774,7; ряд не сводится к покварталке).
Прежний контур переносил эти же числа в поля «квартал», поэтому ряд в каноне
выглядит квартальным, оставаясь накопительным: `iokmrrk`, запись `2020Q2` равна
первому полугодию. Загрузчик это свойство не правит (значения те же), но пишет в
подразрез метку накопления («накопительно: I полугодие»), чтобы ряд нельзя было
прочитать как квартальный.

Метрики: `iokmrrk` — млн руб. (все четыре накопленных периода каждого года,
2 400 строк), `iokspr` — % к соответствующему периоду. Прежний контур брал из
листа процентов ТОЛЬКО колонку «I квартал» (672 строки = 96 территорий × 7 лет);
по решению владельца от 16.10.2026 ряд дополнен остальными тремя периодами
(2 688 строк). Отключить расширение — `ALL_PCT=0`.

Релизы: группа пришла в канон тремя наборами — перенос из SQLite (релиз 1)
и два релиза рубежа 6 (76, 77), — а `iokmrrkri` дублировала `iokmrrk` по всем
2 400 значениям. Решением владельца от 17.10.2026 группа сведена к одному
релизу `rosstat_inv_reg_kv_2020-2026` (id 76), карточка-дубль снята, релиз 77
удалён (скрипт `merge_ikv_releases.py`). Теперь обе метрики лежат под одним
релизом, и загрузчик пишет туда же.
"""

import os
import re
import sys

import openpyxl

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from direct_core import Writer, norm                    # noqa: E402
import db_tunnel as tunnel                              # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(REPO, 'raw', 'rosstat', 'data')
SOURCE = 'rosstat'
FREQ = 'Q'
UNIT_MLN = 'mln_rub'
UNIT_PCT = 'pct'
CODE_MLN = 'iokmrrk'
CODE_PCT = 'iokspr'
NAME_MLN = 'Инвестиции в основной капитал, млн руб., регион, квартал'
NAME_PCT = 'Инвестиции в основной капитал, % к соотв. периоду, регион'
# подпись периода в источнике → месяц начала квартала и метка накопления
PERIODS = {'I квартал': (1, 'I квартал'),
           'I полугодие': (4, 'I полугодие'),
           'январь-сентябрь': (7, 'январь-сентябрь'),
           'январь-декабрь': (10, 'январь-декабрь'),
           'год': (10, 'год')}


def file_path():
    files = sorted(f for f in os.listdir(RAW)
                   if re.match(r'Inv_reg_kv_\d{4}-\d{4}\.xlsx$', f))
    return os.path.join(RAW, files[-1]) if files else None


def grid(ws):
    """[(year, label, col, month, cum)] — шапка ищется по подписям периодов.

    Листы отличаются числом строк над шапкой, поэтому строку с подписями
    («I квартал», «I полугодие», …) находим по тексту, а год берём из строки
    выше и переносим вправо (в исходнике годы в объединённых ячейках).
    """
    rows = list(ws.iter_rows(values_only=True))
    hdr = next((i for i, r in enumerate(rows[:10])
                if r and any(isinstance(c, str) and c.strip() in PERIODS for c in r)), None)
    if hdr is None or hdr == 0:
        return [], []
    years, labels = rows[hdr - 1], rows[hdr]
    out, year = [], None
    for col in range(1, max(len(years), len(labels))):
        y = years[col] if col < len(years) else None
        if y is not None:
            m = re.search(r'(20\d{2})', str(y))   # год бывает и числом (2026)
            if m:
                year = int(m.group(1))
        lab = labels[col] if col < len(labels) else None
        lab = str(lab).strip() if isinstance(lab, str) else None
        if year and lab in PERIODS:
            month, cum = PERIODS[lab]
            out.append((year, lab, col, month, cum))
    return out, rows[hdr + 1:]


def parse(path, all_pct=False):
    """[(ps, cum_label, territory, value_mln, pct)] из двух листов файла."""
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    by_name = wb.sheetnames
    mln = next((s for s in by_name if 'млн' in s.lower()), None)
    pct = next((s for s in by_name if 'соотв' in s.lower()), None)
    print('  листы: %r (млн руб.), %r (%% к периоду)' % (mln, pct))
    out = {}
    cols, rows = grid(wb[mln])
    print('  лист млн руб.: периодов %d (%s..%s)'
          % (len(cols), cols[0][0], cols[-1][0]))
    for r in rows:
        name = r[0]
        if not isinstance(name, str) or not name.strip():
            continue
        for year, lab, col, month, cum in cols:
            val = r[col] if col < len(r) else None
            if val is None or month is None:
                continue
            key = ((year, month), (name.strip(),))
            out.setdefault((year, month, name.strip()), {})['mln'] = float(val)
            out[(year, month, name.strip())]['cum'] = cum
    cols, rows = grid(wb[pct])
    keep = None if all_pct else {'I квартал'}
    for r in rows:
        name = r[0]
        if not isinstance(name, str) or not name.strip():
            continue
        for year, lab, col, month, cum in cols:
            if keep and lab not in keep:
                continue
            val = r[col] if col < len(r) else None
            if val is None or month is None:
                continue
            rec = out.setdefault((year, month, name.strip()), {})
            rec['pct'] = float(val)
            rec.setdefault('cum', cum)
    wb.close()
    return [dict(ps=(k[0], k[1]), territory=k[2], cum=v.get('cum', ''),
                 mln=v.get('mln'), pct=v.get('pct'))
            for k, v in sorted(out.items())]


def landing():
    """Прежние строки из лендинга `rosreestr_deals.db` — эталон сверки."""
    import sqlite3
    p = os.path.join(REPO, 'data', 'rosreestr_deals.db')
    if not os.path.exists(p):
        return {}, {}
    c = sqlite3.connect('file:%s?mode=ro' % p, uri=True)
    mln = {(r[1], r[2], r[0]): round(r[3], 3)
           for r in c.execute('SELECT region, year, q, value_mln FROM ikv_region_quarter')}
    pct = {(r[1], r[2], r[0]): round(r[3], 3)
           for r in c.execute('SELECT region, year, q, pct FROM ikv_region_quarter_pct')}
    c.close()
    return mln, pct


def releases_of(w):
    """Релиз группы, в котором строки этих метрик лежат сейчас (по коду карточки).

    До 17.10.2026 группа приходила тремя наборами (релизы 1, 76, 77), причём
    `iokmrrkri` была полным дублем `iokmrrk`. Решением владельца наборы сведены
    к одному релизу `rosstat_inv_reg_kv_2020-2026`, поэтому обе метрики должны
    находиться ровно в одном релизе; иначе запись остановится.
    """
    out = {}
    for code in (CODE_MLN, CODE_PCT):
        rows = tunnel.query("""SELECT DISTINCT r.release_label, count(o.*)
            FROM core.metric m JOIN data.observation o USING(metric_id)
            JOIN core.release r USING(release_id) WHERE m.metric_code = %s
            GROUP BY 1 ORDER BY 2 DESC""", (code,))
        if len(rows) != 1:
            sys.exit('у метрики %s релизов %d (%s) — нужно решение до записи'
                     % (code, len(rows), [r[0] for r in rows]))
        out[code] = rows[0][0]
    return out


def main():
    apply = os.environ.get('APPLY') == '1'
    prune = 'period' if os.environ.get('PRUNE') == 'period' else False
    all_pct = os.environ.get('ALL_PCT', '1') != '0'   # решение владельца: все четыре периода
    path = sys.argv[1] if len(sys.argv) > 1 else file_path()
    if not path or not os.path.exists(path):
        sys.exit('нет файла Inv_reg_kv')
    print('разбираю %s' % os.path.basename(path))
    recs = parse(path, all_pct=all_pct)
    print('записей (период × территория): %d, территорий %d, периодов %d'
          % (len(recs), len({r['territory'] for r in recs}),
             len({r['ps'] for r in recs})))

    ref_mln, ref_pct = landing()
    ok = bad = miss = 0
    for rec in recs:
        q = (rec['ps'][1] - 1) // 3 + 1
        for key, val, ref in ((('mln', ), rec['mln'], ref_mln), (('pct', ), rec['pct'], ref_pct)):
            if val is None:
                continue
            e = ref.get((rec['ps'][0], q, rec['territory']))
            if e is None:
                miss += 1
            elif abs(e - round(val, 3)) < 0.005:
                ok += 1
            else:
                bad += 1
                if bad <= 4:
                    print('   РАСХОЖДЕНИЕ %s %s %sQ%s: %s против %s'
                          % (rec['territory'][:34], rec['ps'], rec['ps'][0], q, val, e))
    print('лендинг: совпало %d | расхождений %d | нет в лендинге %d' % (ok, bad, miss))

    w = Writer(tag='direct_ikv_reg')
    rel_by_code = releases_of(w)
    print('релизы карточек: ' + ', '.join('%s → %r' % (c, r) for c, r in rel_by_code.items()))
    payload = []
    for rec in recs:
        rid, parts = w.resolve_region({'region': rec['territory']}, 'region', None)
        if parts and parts[0].startswith('категория:'):
            print('   не разрешено в регион: %r' % rec['territory'])
        base = 'накопительно: %s' % rec['cum']
        sub = base if not parts else '%s | %s' % (base, ' | '.join(parts))
        for field, code, name, unit in (('mln', CODE_MLN, NAME_MLN, UNIT_MLN),
                                        ('pct', CODE_PCT, NAME_PCT, UNIT_PCT)):
            val = rec[field]
            if val is None:
                continue
            payload.append(dict(metric_name=name, value=val, ps=rec['ps'], sub=sub,
                                region=rid, freq=FREQ, source=SOURCE,
                                release=rel_by_code[code], unit=unit))
    print('строк к канону: %d (млн руб. %d, %% %d)'
          % (len(payload), sum(1 for p in payload if p['metric_name'] == NAME_MLN),
             sum(1 for p in payload if p['metric_name'] == NAME_PCT)))
    print('коды метрик: %s — %s, %s — %s' % (CODE_MLN, NAME_MLN[:44], CODE_PCT, NAME_PCT[:44]))
    if not apply:
        print('без записи (APPLY=1 — записать)')
        w.close()
        return
    if prune:
        # точка возврата пишется один раз: повторный прогон не должен затирать
        # состояние ДО переноса состоянием после него (первый прогон 16.10.2026
        # засел 3 072 строки прежнего вида, второй перезаписал файл — прежнее
        # состояние восстановимо из лендинга `rosreestr_deals.db`, сверка с ним
        # даёт 3 072 из 3 072).
        dest = os.path.join(REPO, 'attic', 'ikv_reg_before.csv.gz')
        if os.path.exists(dest):
            print('точка возврата уже есть: %s' % dest)
        else:
            n = w.dump_group([NAME_MLN, NAME_PCT], dest, delete=False)
            print('точка возврата: %s (%d строк)' % (dest, n))
    prep, ins, conf, new = w.ingest(payload, group='', prune=prune)
    print('подготовлено %d | вставлено %d | конфликтов %d | новых метрик %d'
          % (prep, ins, conf, new))
    w.close()


if __name__ == '__main__':
    main()
