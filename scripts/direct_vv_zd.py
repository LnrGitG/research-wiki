#!/usr/bin/env python3
"""Прямой загрузчик: ввод в действие зданий (Росстат) → канон.

Два источника, обе публикации оперативные:
  1) raw/rosstat/data/vv-zd-oper_QQ-YYYY.xlsx — РФ по типам зданий, накопительно
     с начала года (листы «январь-март», «январь-июнь», …): 12 категорий ×
     2 меры (количество зданий, ед.; общая площадь, тыс. м²). Соответствует
     прежним метрикам `rosstat_c1_*` (24 метрики, релиз
     `rosstat_housing_types_2026-09`), которые до сих пор писались из лендинга
     `rosreestr_deals.db` → таблица `rosstat_buildings_vvod`; тот лендинг, в свою
     очередь, наполнялся из ЭТОГО же файла. Теперь файл читается напрямую.
  2) raw/rosstat/data/vv-zd-sub_MM-YYYY.xlsx — то же «введено в действие
     зданий», но по субъектам РФ: по листу на месяц («январь 2026») и на
     накопленный период («январь-июль 2026»), в каждом — Российская Федерация,
     федеральные округа и субъекты, 2 меры. Раньше этот файл не разбирался
     вовсе; заводится четырьмя метриками (количество и площадь × месяц и
     накопительно), релиз `rosstat_vv_zd_sub_2026-10`.

Обе публикации — кумулятивные и ревизуемые, а файл vv-zd-sub к тому же
скользящий внутри года, поэтому месячный прогон идёт с `PRUNE=period`:
снимаются ровно периоды из разбора и пишутся заново; периоды вне окна не
теряются.

Имена категорий, коды и русские имена метрик С-1 берутся из
`ingest_housing_types.py` (`CAT_MAP`, `NAME_RU`): так загрузчик попадает в уже
существующие метрики, а не плодит дубликаты.

Запуск: APPLY=1 [PRUNE=period] scripts/direct_vv_zd.py
"""
import os
import re
import sys

import openpyxl

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from direct_core import Writer, norm  # noqa: E402
from ingest_housing_types import CAT_MAP, NAME_RU  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(REPO, 'raw', 'rosstat', 'data')
SOURCE = 'rosstat'
RELEASE_C1 = 'rosstat_housing_types_2026-09'
RELEASE_SUB = 'rosstat_vv_zd_sub_2026-10'
FREQ = 'M'
UNIT_AREA = 'ths_sqm'
UNIT_COUNT = 'count'
# блоки таблицы vv-zd-sub: подпись строки → разрез в имени метрики
DEFAULT_BLOCK = 'Жилые и нежилые здания'
BLOCKS = {'Жилые и нежилые здания': 'жилые и нежилые',
          'Жилые здания': 'жилые',
          'Нежилые здания': 'нежилые'}

# основы месяцев: в шапке Росстат пишет и «январь», и «январе», и «январе-июле»
MONTH_STEMS = [('январ', 1), ('феврал', 2), ('март', 3), ('апрел', 4), ('май', 5),
               ('мае', 5), ('июн', 6), ('июл', 7), ('август', 8), ('сентябр', 9),
               ('октябр', 10), ('ноябр', 11), ('декабр', 12)]
# служебные строки: заголовки «в том числе» и сноски внизу таблицы
SKIP = re.compile(r'^(в том числе|\d+\))', re.I)


def num(v):
    """Число из ячейки; пустое, прочерк и текст → None."""
    if v is None or isinstance(v, bool):
        return None
    if isinstance(v, (int, float)):
        return float(v)
    s = str(v).strip().replace('\xa0', '').replace(' ', '').replace(',', '.')
    return float(s) if re.match(r'^[-+]?\d*\.?\d+$', s) else None


def clean_name(v):
    """Имя строки: снять пробелы и сносочную метку («Российская Федерация1)»).

    Цифра перед скобкой обязательна: у «Архангельская область (кроме Ненецкого
    автономного округа)» скобка своя, и снимать её нельзя.
    """
    s = re.sub(r'\s+', ' ', str(v)).strip()          # снять двойные пробелы
    return re.sub(r'\s*\d+\)\s*$', '', s).strip()


def months_in(text):
    """Номера месяцев, упомянутых в тексте шапки (в порядке появления)."""
    low = norm(text)
    hits = []
    for i, (stem, num) in enumerate(MONTH_STEMS):
        pos = low.find(stem)
        if pos >= 0:
            hits.append((pos, num))
    return [num for _, num in sorted(hits)]


def latest(pattern):
    if not os.path.isdir(RAW):
        return None
    files = [f for f in os.listdir(RAW) if re.match(pattern, f)]
    return os.path.join(RAW, sorted(files)[-1]) if files else None


def parse_oper(path):
    """[(период (год, месяц), категория, количество, площадь)] из vv-zd-oper."""
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    out = []
    for sheet in wb.sheetnames:
        if sheet.strip().lower() in ('содержание', 'содержание '):
            continue
        rows = list(wb[sheet].iter_rows(values_only=True))
        head = ' '.join(str(c) for r in rows[:4] for c in r if isinstance(c, str))
        year = re.search(r'(20\d{2})', head)
        months = months_in(head)
        if not year or not months:
            print('  лист %r: не разобран заголовок' % sheet)
            continue
        ps = (int(year.group(1)), max(months))     # конец накопленного периода
        for r in rows[4:]:
            name = r[0]
            if not isinstance(name, str) or not name.strip():
                continue
            nm = clean_name(name)
            if SKIP.match(nm) or not nm:
                continue
            out.append((ps, nm, num(r[1]) if len(r) > 1 else None,
                        num(r[2]) if len(r) > 2 else None))
    wb.close()
    return out


def parse_sub(path):
    """[(период, накопительно, блок, имя строки, количество, площадь)] из vv-zd-sub.

    Лист устроен тремя блоками с одинаковым списком территорий: «Жилые и
    нежилые здания», «Жилые здания», «Нежилые здания»; подпись блока — строка
    без значений, она задаёт разрез, а не территорию.
    """
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    out = []
    block = BLOCKS[DEFAULT_BLOCK]
    for sheet in wb.sheetnames:
        if sheet.strip().lower().startswith('содержание'):
            continue
        rows = list(wb[sheet].iter_rows(values_only=True))
        title = sheet
        for r in rows[:4]:
            found = [c for c in r if isinstance(c, str) and months_in(c)]
            if found:
                title = found[0]
                break
        year = re.search(r'(20\d{2})', str(title))
        months = months_in(str(title))
        if not year or not months:
            print('  лист %r: не разобран заголовок' % sheet)
            continue
        ps = (int(year.group(1)), max(months))
        # «в январе 2026 года» — месяц; «в январе-июле 2026 года» — накопительно
        cum = len(months) > 1
        for r in rows[4:]:
            name = r[0]
            if not isinstance(name, str) or not name.strip():
                continue
            nm = clean_name(name)
            if SKIP.match(nm) or not nm:
                continue
            if nm in BLOCKS:
                block = BLOCKS[nm]
                continue
            out.append((ps, cum, block, nm, num(r[1]) if len(r) > 1 else None,
                        num(r[2]) if len(r) > 2 else None))
    wb.close()
    return out


def main():
    apply = os.environ.get('APPLY') == '1'
    prune = 'period' if os.environ.get('PRUNE') == 'period' else False
    oper = sys.argv[1] if len(sys.argv) > 1 else latest(r'^vv-zd-oper_\d+kv-20\d\d\.xlsx$')
    sub = sys.argv[2] if len(sys.argv) > 2 else latest(r'^vv-zd-sub_\d\d-20\d\d\.xlsx$')

    rows = []
    if oper and os.path.exists(oper):
        recs = parse_oper(oper)
        periods = sorted({r[0] for r in recs})
        cats = sorted({r[1] for r in recs})
        print('%s: %d строк, периодов %d, категорий %d'
              % (os.path.basename(oper), len(recs), len(periods), len(cats)))
        for ps, cat, cnt, area in recs:
            key = CAT_MAP.get(cat)
            if not key:
                print('   категория вне карты: %r' % cat)
                continue
            slug, _ = key
            if area is not None:
                rows.append(dict(metric_name=NAME_RU[slug], value=area, ps=ps,
                                 region=None, sub=None, freq=FREQ, source=SOURCE,
                                 release=RELEASE_C1, unit=UNIT_AREA))
            if cnt is not None:
                rows.append(dict(metric_name=NAME_RU[slug] + ' — количество зданий',
                                 value=cnt, ps=ps, region=None, sub=None, freq=FREQ,
                                 source=SOURCE, release=RELEASE_C1, unit=UNIT_COUNT))
    else:
        print('предупреждение: файла vv-zd-oper нет — разрез по типам пропущен')

    if sub and os.path.exists(sub):
        recs = parse_sub(sub)
        periods = sorted({r[0] for r in recs})
        print('%s: %d строк, периодов %d (%s .. %s), накопительных листов %d'
              % (os.path.basename(sub), len(recs), len(periods), periods[0], periods[-1],
                 len({r[0] for r in recs if r[1]})))
        for ps, cum, block, nm, cnt, area in recs:
            # накопительный лист задаёт только накопленный ряд; лист января —
            # единственный, где месячный итог и накопленный совпадают
            if ps[1] == 1:
                tags = ['месяц', 'накопительно с начала года']
            else:
                tags = ['накопительно с начала года' if cum else 'месяц']
            for tag in tags:
                for measure, val, unit in (('общая площадь', area, UNIT_AREA),
                                           ('количество', cnt, UNIT_COUNT)):
                    if val is None:
                        continue
                    rows.append(dict(
                        metric_name=('Ввод зданий по субъектам: %s, %s, %s '
                                     '(Росстат, vv-zd-sub)' % (block, measure, tag)),
                        value=val, ps=ps, name=nm, freq=FREQ, source=SOURCE,
                        release=RELEASE_SUB, unit=unit))
    else:
        print('предупреждение: файла vv-zd-sub нет — региональный разрез пропущен')

    if not rows:
        sys.exit('нечего писать: сырья нет')

    w = Writer(tag='direct_vv_zd')
    payload = []
    for r in rows:
        nm = r.pop('name', None)
        sub = None
        if nm is not None:
            rid, parts = w.resolve_region({'region': nm}, 'region', None)
            sub = ' | '.join(parts) or None
            if parts and parts[0].startswith('категория:'):
                print('   не разрешено в регион: %r' % nm)
            r['region'] = rid
        r['sub'] = sub
        payload.append(r)
    print('строк к канону: %d | метрик-имён: %d'
          % (len(payload), len({p['metric_name'] for p in payload})))
    if not apply:
        print('без записи (APPLY=1 — записать)')
        w.close()
        return

    prep_n, ins, conf, new = w.ingest(payload, group='', prune=prune)
    print('подготовлено %d | вставлено %d | конфликтов %d | новых метрик %d'
          % (prep_n, ins, conf, new))
    w.close()


if __name__ == '__main__':
    main()
