#!/usr/bin/env python3
"""Прямой загрузчик: ввод производственных мощностей по субъектам РФ → канон.

Сырьё: `raw/rosstat/data/vv-mosh-sub_Qkv-YYYY.xlsx` — тот же показатель, что в
`vv-mosh-oper`, но с разбивкой по территориям (лист на каждый накопленный
период). Устройство листа: шапка из двух-трёх строк без чисел (вид
деятельности → продукт → единица измерения), затем строки территорий, в каждой
— название и три числа («Всего», «за счёт строительства», «реконструкции»).

Метрика та же, что у `direct_mosh.py`: имя — продукт, а не строка-раздел книги
(см. урок о трёхуровневой шапке), единица измерения — в подразрезе. Регион
берётся из строки территории; неразрешённые имена (`категория: …`) и варианты
состава (`состав: …`, например «Архангельская область (кроме Ненецкого
автономного округа)») уходят в подразрез средствами `Writer.resolve_region`,
поэтому ключ строки не сталкивается с обычной территорией.

Строку «Российская Федерация» загрузчик ПРОПУСКАЕТ: она уже пришла из
`vv-mosh-oper_Qkv-YYYY.xlsx` и лежит в релизе `vv-mosh-oper_2kv-2026`; здесь её
числа служат сверкой (расхождение печатается). Региональные строки пишутся
отдельным релизом `vv-mosh-sub_2kv-2026`, поэтому одного и того же ряда под
двумя релизами не возникает.
"""

import glob
import os
import re
import sys

import openpyxl

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from direct_core import Writer, norm                      # noqa: E402
from direct_mosh import FREQ, KINDS, RAW, SOURCE, clean, months_in, num  # noqa: E402
import db_tunnel as tunnel                               # noqa: E402

RELEASE = 'vv-mosh-sub_2kv-2026'
RELEASE_RF = 'vv-mosh-oper_2kv-2026'
UNIT = 'unknown'


def latest():
    files = sorted(glob.glob(os.path.join(RAW, 'vv-mosh-sub_*.xlsx')))
    return files[-1] if files else None


def period_of(rows):
    """Период листа из подписи «в январе-июне 2026 г.» и признак накопительного."""
    for r in rows[:5]:
        for cell in r:
            if not isinstance(cell, str) or not months_in(cell):
                continue
            year = re.search(r'(20\d{2})', cell)
            months = months_in(cell)
            if year and months:
                return (int(year.group(1)), max(months)), len(months) > 1
    return None, False


def parse(path):
    """[dict(period, cum, section, product, unit, territory, vals)] из файла."""
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    out = []
    for sheet in wb.sheetnames:
        if sheet.strip().lower().startswith('содержание'):
            continue
        rows = list(wb[sheet].iter_rows(values_only=True))
        period, cum = period_of(rows)
        if not period:
            print('  лист %r: не разобран заголовок' % sheet)
            continue
        buf, head, n = [], None, 0
        for r in rows[4:]:
            name = r[0]
            if not isinstance(name, str) or not name.strip():
                continue
            vals = tuple(num(r[i]) if len(r) > i else None for i in (1, 2, 3))
            if all(v is None for v in vals):
                buf.append(clean(name))
                continue
            if buf:
                unit = buf[-1]
                product = buf[-2] if len(buf) > 1 else buf[-1]
                section = buf[-3] if len(buf) > 2 else None
                head, buf = (section, product, unit), []
            if head is None:
                print('  строка со значениями до шапки: %r' % name)
                continue
            section, product, unit = head
            out.append(dict(period=period, cum=cum, section=section, product=product,
                            unit=unit, territory=clean(name), vals=vals))
            n += 1
        print('лист %r: период %s, накопительно %s, строк территорий %d'
              % (sheet, period, cum, n))
    wb.close()
    return out


def rf_values():
    """Числа РФ из уже записанного релиза `vv-mosh-oper` — для сверки.

    Ключ включает единицу измерения: в книге есть продукты, встречающиеся дважды
    под одним названием с разными единицами (например «Скважины нефтяные
    эксплуатационного бурения» — «Единица», 1584 скважины, и «Тысяча тонн»,
    10 712,36 тыс. т добычи). Прежний путь такие пары не различал и оставлял одну
    строку; теперь у каждой своя запись с единицей в подразрезе, и сверку нужно
    вести по единице, иначе региональный файл «не совпадёт» с верной строкой.
    """
    out = {}
    for mid, nm, ps, val, sub in tunnel.query("""
            SELECT m.metric_id, m.name_ru, o.period_start, o.value::float, o.sub_dimension
            FROM data.observation o JOIN core.metric m USING(metric_id)
            JOIN core.release r USING(release_id)
            WHERE r.release_label = %s AND o.region_id = 1""", (RELEASE_RF,)):
        kind = 0 if nm.startswith('Ввод мощностей:') else (
            1 if 'новое строительство' in nm else 2)
        unit = (sub or '').split('ед.: ')[-1].strip()
        out[(norm(nm), (ps.year, ps.month), kind, unit)] = round(val, 3)
    return out


def main():
    apply = os.environ.get('APPLY') == '1'
    prune = 'period' if os.environ.get('PRUNE') == 'period' else False
    path = sys.argv[1] if len(sys.argv) > 1 else latest()
    if not path or not os.path.exists(path):
        sys.exit('нет файла vv-mosh-sub')
    print('разбираю %s' % os.path.basename(path))
    recs = parse(path)
    print('строк территорий: %d | продуктов: %d | разделов: %d'
          % (len(recs), len({(r['section'], r['product']) for r in recs}),
             len({r['section'] for r in recs if r['section']})))

    ref = rf_values()
    w = Writer(tag='direct_mosh_sub')
    payload, skipped_rf, unbound, mismatch = [], 0, set(), []
    for rec in recs:
        section = rec['section']
        unit = rec['unit']
        for kind, val in enumerate(rec['vals']):
            if val is None:
                continue
            nm = KINDS[kind] % rec['product']
            rid, parts = w.resolve_region({'region': rec['territory']}, 'region', None)
            if norm(rec['territory']) == norm('Российская Федерация') or rid == w.RU:
                key = (norm(nm), rec['period'], kind, unit)
                if key in ref and abs(ref[key] - round(val, 3)) > 0.005:
                    mismatch.append((nm, rec['period'], val, ref[key]))
                skipped_rf += 1
                continue
            if parts and parts[0].startswith('категория:'):
                unbound.add(rec['territory'])
            sub = 'section: %s | ед.: %s' % (section or rec['product'], unit)
            if parts:
                sub = '%s | %s' % (sub, ' | '.join(parts))
            payload.append(dict(metric_name=nm, value=val, ps=rec['period'], sub=sub,
                                region=rid, freq=FREQ, source=SOURCE,
                                release=RELEASE, unit=UNIT))

    print('строк к канону: %d | имён метрик: %d | пропущено строк РФ: %d'
          % (len(payload), len({p['metric_name'] for p in payload}), skipped_rf))
    if mismatch:
        print('РАСХОЖДЕНИЯ с релизом РФ: %d' % len(mismatch))
        for nm, ps, got, was in mismatch[:5]:
            print('   %s %s: %s против %s' % (nm[:60], ps, got, was))
    else:
        print('сверка РФ: значения регионального файла совпали с релизом РФ')
    if unbound:
        print('не разрешено в регион (уйдёт в подразрез как категория): %d имён, например %s'
              % (len(unbound), sorted(unbound)[:4]))
    if not apply:
        print('без записи (APPLY=1 — записать)')
        w.close()
        return
    prep, ins, conf, new = w.ingest(payload, group='', prune=prune)
    print('подготовлено %d | вставлено %d | конфликтов %d | новых метрик %d'
          % (prep, ins, conf, new))
    w.close()


if __name__ == '__main__':
    main()
