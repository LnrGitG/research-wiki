#!/usr/bin/env python3
"""Прямой загрузчик: файл СС-индексов промпроизводства Росстата → канон.

Путь «сырьё → канон» вместо прежнего «парсер (rosstat_sezon_parse.py) →
SQLite-лендинг (rosreestr_deals.db, таблица rosstat_ind_prod_saar) → гармонайзер 6
→ канон». Разбор повторяет осиротевший парсер, чтобы попадать в те же ключи.

Сырьё: raw/rosstat/data/sezon_2023_MM-YYYY.xlsx (первый лист, если первый —
«Содержание»). Колонки: Месяц | IPP (м/м факт, м/м СС, к базовому факт, к базовому
СС) | B Добыча | C Обрабатывающие | D Энергетика | E Водоснабжение — по 4 колонки
на секцию, то есть столбцы 1..4, 5..8, 9..12, 13..16, 17..20. Строка года —
маркер 'YYYY' (встречается как '20262' со сноской 2: без ДНР/ЛНР/Запорожья и
Херсона).

В канон идут ДВЕ серии из четырёх (имена совпадают с рубежом 6):
    Промпроизводство, % к предыдущему месяцу (SAAR)   ← mom_saar
    Промпроизводство, % к базовому периоду (SAAR)     ← base_saar
Колонки «факт» (mom_fact, base_fact) в канон отсюда не пишутся: рубеж 6 их в этой
группе не заводил, их ряды приходят из файлов ind_baza/ind_sub.

Частота — M. Рубеж 6 помечал эти месячные ряды квартальной частотой 'Q' (тот же
дефект, что исправлен в транше 1); частота входит в уникальный ключ наблюдения,
поэтому перевод делается снятием прежних строк (REPLACE=1) — иначе рядом
остались бы квартально помеченные близнецы.

Подразрез — 'section: <SEC>' (IPP, B_mining, C_manufacturing, D_energy, E_water),
регион — РФ, релиз — 'rosstat_sezon_2023' (метка прежней дороги: релиз входит в
уникальный ключ).

Запуск:
    python3 scripts/direct_sezon.py                      # разбор и отчёт (без записи)
    APPLY=1 python3 scripts/direct_sezon.py              # дописать без снятия
    APPLY=1 PRUNE=period python3 scripts/direct_sezon.py # месячный прогон (режим cron)
    APPLY=1 REPLACE=1 python3 scripts/direct_sezon.py    # разовая миграция: точка возврата плюс снятие
"""
try:
    from xlsx_engine import open_workbook  # noqa: E402
except ImportError:  # запуск из другого каталога
    import os as _os
    import sys as _sys
    _sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
    from xlsx_engine import open_workbook  # noqa: E402

import glob
import os
import re
import sys

try:
    from xlsx_engine import engine_from_argv, open_workbook  # noqa: E402
except ImportError:  # запуск из другого каталога
    import os as _os
    import sys as _sys
    _sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
    from xlsx_engine import engine_from_argv, open_workbook  # noqa: E402
ENGINE = engine_from_argv()  # --xlsx-engine openpyxl|fastexcel, резерв — XLSX_ENGINE


sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from direct_core import Writer  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(REPO, 'raw', 'rosstat', 'data')
ATTIC = os.path.join(REPO, 'attic')

MONTHS = {'январь': 1, 'февраль': 2, 'март': 3, 'апрель': 4, 'май': 5, 'июнь': 6,
          'июль': 7, 'август': 8, 'сентябрь': 9, 'октябрь': 10, 'ноябрь': 11,
          'декабрь': 12}
# (подразрез, индекс колонки «м/м СС», «к базовому СС») — столбцы считаем по номерам
SECTIONS = [('IPP', 2, 4), ('B_mining', 6, 8), ('C_manufacturing', 10, 12),
            ('D_energy', 14, 16), ('E_water', 18, 20)]
SOURCE = 'rosstat'
RELEASE = 'rosstat_sezon_2023'
FREQ = 'M'
METRICS = ['Промпроизводство, % к предыдущему месяцу (SAAR)',
           'Промпроизводство, % к базовому периоду (SAAR)']


def latest_file():
    files = sorted(glob.glob(os.path.join(RAW_DIR, 'sezon_*.xlsx')))
    if not files:
        return None
    # имя sezon_2023_MM-YYYY.xlsx: свежий — по (год, месяц)
    def key(p):
        m = re.search(r'sezon_\d{4}_(\d{2})-(\d{4})', os.path.basename(p))
        return (int(m.group(2)), int(m.group(1))) if m else (0, 0)
    return max(files, key=key)


def num(v):
    if isinstance(v, (int, float)):
        return float(v)
    if isinstance(v, str):
        try:
            return float(v.strip().replace(' ', '').replace(',', '.'))
        except ValueError:
            return None
    return None


def parse(path):
    """[(год, месяц, секция, mom_saar, base_saar)] из листа с данными."""
    wb = open_workbook(path, engine=ENGINE)
    name = wb.sheetnames[1] if wb.sheetnames[0] == 'Содержание' else wb.sheetnames[0]
    ws = wb[name]
    year, out = None, []
    for row in ws.iter_rows(values_only=True):
        c0 = str(row[0]).strip() if row and row[0] is not None else ''
        if c0[:4].isdigit():
            year = int(c0[:4])
        if year and c0 in MONTHS:
            m = MONTHS[c0]
            for sec, i_saar, i_base in SECTIONS:
                v1 = num(row[i_saar]) if len(row) > i_saar else None
                v2 = num(row[i_base]) if len(row) > i_base else None
                if v1 is not None or v2 is not None:
                    out.append((year, m, sec, v1, v2))
    wb.close()
    return out, os.path.basename(path)


def main():
    apply = os.environ.get('APPLY') == '1'
    replace = os.environ.get('REPLACE') == '1'
    path = sys.argv[1] if len(sys.argv) > 1 else latest_file()
    if not path or not os.path.exists(path):
        sys.exit('не найдено raw/rosstat/data/sezon_*.xlsx')
    recs, base = parse(path)
    months = sorted({(y, m) for y, m, *_ in recs})
    print('файл: %s' % base)
    print('разобрано: %d строк (периодов %d, секций %d)'
          % (len(recs), len(months), len({s for *_, s, _, _ in recs})))
    print('окно периодов: %04d-%02d .. %04d-%02d'
          % (months[0][0], months[0][1], months[-1][0], months[-1][1]))

    rows = []
    for y, m, sec, v_saar, v_base in recs:
        for tmpl, val in ((METRICS[0], v_saar), (METRICS[1], v_base)):
            rows.append(dict(metric_name=tmpl, value=val, ps=(y, m),
                             region=None, sub='section: %s' % sec, freq=FREQ,
                             source=SOURCE, release=RELEASE, unit='unknown'))
    if not apply:
        print('без записи (APPLY=1 — записать): строк к канону %d' % len(rows))
        return

    w = Writer(tag='direct_sezon')
    # Режимы снятия:
    #   PRUNE=period — снять ровно те (метрика, релиз, период), что есть в разборе,
    #                  и записать заново. Нужен для ежемесячного прогона: файл
    #                  Росстата кумулятивный и ревизуемый, а ON CONFLICT DO NOTHING
    #                  правку исторических значений не подхватил бы.
    #   REPLACE=1    — снять пару «метрика — релиз» целиком с точкой возврата в attic.
    #                  Для разовой миграции (перевод частоты Q → M и подобное).
    prune = 'period' if os.environ.get('PRUNE') == 'period' else replace
    if replace:
        os.makedirs(ATTIC, exist_ok=True)
        n = w.dump_group(METRICS, os.path.join(ATTIC, 'sezon_saar_before.csv.gz'))
        print('точка возврата: attic/sezon_saar_before.csv.gz — снято %d строк' % n)
    prep, ins, conf, nm = w.ingest(rows, group=RELEASE, prune=prune)
    print('подготовлено %d | вставлено %d | конфликтов %d | новых метрик %d'
          % (prep, ins, conf, nm))
    w.close()


if __name__ == '__main__':
    main()
