#!/usr/bin/env python3
"""Прямой загрузчик: ввод в действие производственных мощностей (Росстат) → канон.

Сырьё: `raw/rosstat/data/vv-mosh-oper_Qkv-YYYY.xlsx` — РФ, лист на каждый
накопленный период года («январь-март», «январь-июнь»). Разметка листа
трёхуровневая: строка-вид деятельности (раздел), строка-продукт, затем строка с
единицей измерения и тремя числами — «Всего», «в том числе за счёт
строительства», «реконструкции». Единица измерения здесь часть данных, а не
оформление: у каждого продукта своя («Тысяча мест», «Квадратный метр», «Тонн»),
поэтому в каноне она уходит в подразрез, а единица метрики остаётся `unknown` —
так же, как в прежнем контуре: величины с разными единицами нельзя складывать в
одну метрику.

Прежний путь вёл группу через лендинг `rosreestr_deals.db`
(`rosstat_production_capacity_vvod`, 364 строки): 491 метрика видов
«Ввод мощностей: X» / «Ввод мощностей, новое строительство: X» /
«Ввод мощностей, реконструкция: X», релиз `vv-mosh-oper_2kv-2026`, частота Q
(6), `assessment_type = preliminary`.

ДЕФЕКТ ПРЕЖНЕГО ПУТИ (найден 16.10.2026). Прежний разбор строил имя метрики по
ПЕРВОЙ строке подряд идущих названий над строкой с числами. У продукта, который
идёт в книге сразу за строкой-разделом, таких названий два, и метрика получала
имя РАЗДЕЛА: значения продукта «Помещения для крупного рогатого скота» (11,95 за
январь-март и 46,14 за январь-июнь) стоят в каноне под именем «Растениеводство и
животноводство, охота и предоставление соответствующих услуг в этих областях», а
у самого продукта строк нет. Всего так помечены 46 первых продуктов разделов —
195 наблюдений; остальные 654 строки канона совпадают с книгой значение в
значение.

Решение владельца (16.10.2026): (1) писать имена продуктов, а строки-разделы
прежнего пути СНЯТЬ — иначе под видом деятельности висит мощность одного объекта;
(2) класть в подразрез реальную единицу измерения продукта («ед.: Тысяча мест»),
которую прежний путь терял, подставляя на её место имя продукта.

Режимы:

  MODE=fix      (по умолчанию) имена продуктов, подразрез
                `section: <раздел> | ед.: <единица>`; прежние строки-разделы
                снимаются только при `RETIRE=1` и только в границах периодов
                разбора (перед снятием пишется точка возврата в `attic/`);
  MODE=legacy   воспроизвести прежние ярлыки — только для сверки с каноном.

Запуск: [MODE=fix|legacy] APPLY=1 PRUNE=period [RETIRE=1] scripts/direct_mosh.py [файл]
"""
import os
import sys

import openpyxl

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from direct_core import Writer, norm  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(REPO, 'raw', 'rosstat', 'data')
SOURCE = 'rosstat'
RELEASE = 'vv-mosh-oper_2kv-2026'
FREQ = 'Q'
UNIT = 'unknown'
KINDS = ('Ввод мощностей: %s',
         'Ввод мощностей, новое строительство: %s',
         'Ввод мощностей, реконструкция: %s')
MONTH_STEMS = [('январ', 1), ('феврал', 2), ('март', 3), ('апрел', 4), ('май', 5),
               ('мае', 5), ('июн', 6), ('июл', 7), ('август', 8), ('сентябр', 9),
               ('октябр', 10), ('ноябр', 11), ('декабр', 12)]
FOOTNOTE = ('1)', '2)')


def num(v):
    if v is None or isinstance(v, bool):
        return None
    if isinstance(v, (int, float)):
        return float(v)
    s = str(v).strip().replace('\xa0', '').replace(' ', '').replace(',', '.')
    try:
        return float(s)
    except ValueError:
        return None


def clean(v):
    """Имя строки как в книге: внутренние переводы строк Росстата сохраняются —
    именно так они записаны в канон прежним путём; снимаются только концевые
    пробелы и сносочная метка («…1)»)."""
    s = str(v).strip()
    return s[:-2].strip() if s.endswith(FOOTNOTE) else s


def latest():
    files = [f for f in os.listdir(RAW) if f.startswith('vv-mosh-oper_')]
    return os.path.join(RAW, sorted(files)[-1]) if files else None


def months_in(text):
    low = norm(text)
    hits = [(low.find(stem), n) for stem, n in MONTH_STEMS if low.find(stem) >= 0]
    return [n for _, n in sorted(hits)]


def parse(path):
    """[{period, product, section, unit, vals}] в порядке книги.

    `section` — имя строки-раздела, если над продуктом в книге есть заголовок
    вида деятельности (тогда прежний путь назвал метрику этим заголовком).
    """
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    out = []
    for sheet in wb.sheetnames:
        if sheet.strip().lower().startswith('содержание'):
            continue
        rows = list(wb[sheet].iter_rows(values_only=True))
        head = ' '.join(str(c) for r in rows[:5] for c in r if isinstance(c, str))
        ms = months_in(head)
        yr = [t for t in head.split() if len(t) >= 4 and t[:4].isdigit()]
        if not ms or not yr:
            print('  лист %r: шапка не разобрана' % sheet)
            continue
        period = (int(yr[0][:4]), max(ms))
        names, n = [], 0
        for r in rows[6:]:
            name = r[0]
            if not isinstance(name, str) or not name.strip():
                continue
            nm = clean(name)
            if not nm or nm.startswith(FOOTNOTE):
                continue
            vals = [num(x) for x in r[1:4]]
            if all(v is None for v in vals):
                names.append(nm)                 # строка-название
                continue
            product = names[-1] if names else None
            section = names[-2] if len(names) > 1 else None
            if product is None:
                continue
            out.append(dict(period=period, product=product, section=section,
                            unit=nm, vals=tuple(vals)))
            n += 1
            names = []
        print('  лист %r: период %s, строк со значениями %d' % (sheet, period, n))
    wb.close()
    return out


def sub_of(rec, legacy):
    """Подразрез: раздел книги плюс реальная единица измерения продукта.

    Прежний путь писал на место единицы имя продукта («ед.: Помещения для
    свиней»), то есть саму единицу («Тысяча мест», «Посещение в смену») терял:
    по решению владельца от 16.10.2026 она сохраняется.
    """
    if legacy:
        if rec['section']:
            return 'section: %s | unit: %s | ед.: %s' % (rec['section'],
                                                         rec['product'],
                                                         rec['product'])
        return 'section: %s' % rec['product']
    return 'section: %s | ед.: %s' % (rec['section'] or rec['product'], rec['unit'])


def retire_targets(w, recs):
    """Метрики канона, названные строками-разделами книги (дефект прежнего пути).

    Признак: имя метрики этого релиза не совпадает ни с одним продуктом книги —
    таких строк в книге нет, потому что название стоит над продуктом, а числа
    принадлежат продукту.
    """
    products = {norm(r['product']) for r in recs}
    w.cur.execute("""SELECT m.metric_id, m.name_ru, count(o.*)
                     FROM core.metric m JOIN data.observation o USING(metric_id)
                     JOIN core.release r USING(release_id)
                     WHERE r.release_label = %s AND m.name_ru LIKE 'Ввод мощностей%%'
                     GROUP BY 1, 2 ORDER BY 1""", (RELEASE,))
    out = []
    for mid, nm, cnt in w.cur.fetchall():
        base = nm.split(': ', 1)[1] if ': ' in nm else nm
        if norm(base) not in products:
            out.append((mid, nm, cnt))
    return out


def rows_for(recs, mode):
    rows = []
    for rec in recs:
        legacy = mode == 'legacy'
        names = [rec['product']]
        subs = [sub_of(rec, legacy)]
        if legacy and rec['section']:
            # прежний путь назвал строку раздела — та же пара значений под именем
            # заголовка; имя раздела надо получить из книги, оно в `section`
            names.append(rec['section'])
            subs.append('section: %s | unit: %s | ед.: %s'
                        % (rec['section'], rec['product'], rec['product']))
        for nm, sub in zip(names, subs):
            for kind, val in zip(KINDS, rec['vals']):
                if val is None:
                    continue
                rows.append(dict(metric_name=kind % nm, value=val, ps=rec['period'],
                                 sub=sub, region=None, freq=FREQ, source=SOURCE,
                                 release=RELEASE, unit=UNIT))
    return rows


def main():
    apply = os.environ.get('APPLY') == '1'
    prune = 'period' if os.environ.get('PRUNE') == 'period' else False
    retire = os.environ.get('RETIRE') == '1'
    mode = os.environ.get('MODE', 'fix')
    path = sys.argv[1] if len(sys.argv) > 1 else latest()
    if not path or not os.path.exists(path):
        sys.exit('нет файла vv-mosh-oper')
    print('%s · режим %s' % (os.path.basename(path), mode))
    recs = parse(path)
    sections = {r['section'] for r in recs if r['section']}
    print('строк со значениями: %d | разделов книги: %d' % (len(recs), len(sections)))
    rows = rows_for(recs, mode)
    print('строк к канону: %d | имён метрик: %d'
          % (len(rows), len({r['metric_name'] for r in rows})))
    if not apply:
        print('без записи (APPLY=1 — записать)')
        return
    w = Writer(tag='direct_mosh')
    if retire:
        targets = retire_targets(w, recs)
        print('строки-разделы прежнего пути: метрик %d, наблюдений %d'
              % (len(targets), sum(t[2] for t in targets)))
        for mid, nm, cnt in targets[:5]:
            print('   %d %s (%d)' % (mid, nm[:70], cnt))
        if targets:
            dest = os.path.join(REPO, 'attic', 'mosh_sections_before.csv.gz')
            n = w.dump_group([nm for _m, nm, _c in targets], dest, delete=True)
            print('   точка возврата: %s (%d строк снято)' % (dest, n))
    prep, ins, conf, new = w.ingest(rows, group='', prune=prune)
    print('подготовлено %d | вставлено %d | конфликтов %d | новых метрик %d'
          % (prep, ins, conf, new))
    w.close()


if __name__ == '__main__':
    main()
