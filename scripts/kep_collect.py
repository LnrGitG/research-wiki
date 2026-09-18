#!/usr/bin/env python3
"""
Сбор «Краткосрочных экономических показателей РФ» (КЭП) Росстата → staging.

Источник: https://rosstat.gov.ru/compendium/document/50802
Файл выпуска: https://rosstat.gov.ru/storage/mediabank/ind_MM-YYYY.xlsx
Выходит ежемесячно (график оперативных публикаций Росстата), 1–4 число;
содержит накопленные данные января–<месяц> текущего года.

СТРУКТУРА ВЫПУСКА (проверено 18.09.2026 на ind_07-2026.xlsx)
------------------------------------------------------------
43 листа, 39 с данными. Лист = показатель (1.6, 1.7, 1.8, 3.3, ...).
Шапка: строка 1/2 = «Год | Кварталы I–IV | Янв…Дек», строка 3 = название
показателя с единицей измерения, строка 4 = английский перевод.
Тело: строки с годом в колонке 1; по вертикали лист делится на БЛОКИ одного
показателя: уровень (в своих единицах), затем «в % к соответствующему периоду
предыдущего года», затем «в % к предыдущему периоду». У листов с
подпоказателями (1.6.1, 3.3, 3.5, 4.x) блоки названы по-своему
(«собственные средства предприятий», «продукты питания» и т.п.).

ПИТФОЛЛЫ
--------
1. Имена листов содержат ПРОБЕЛЫ в конце ('1.7 ', '1.6.1 ') — не сравнивать
   по точному имени, использовать .strip().
2. Годы приходят со сносками: '20221)', '20141)' → чистить до целого, сноску
   сохранять в footnote.
3. Нечисловые значения ('2,12)') — это не число, а указание «в разах»;
   такие ячейки пропускать, а не ронять парсер.
4. Листы 4.6 (4 штуки) — распределение населения по доходным группам, БЕЗ
   колонки года (годы = листы). Парсер их пропускает и сообщает об этом.
5. Шапка НЕ на фиксированной строке: у 3.1/3.3 это строки 1–2, у части листов
   иначе. Определять динамически — по строке с ≥8 названиями месяцев.
6. У листов 1.5 и 4.8 max_column = 16384 (артефакт форматирования) — при
   чтении ограничивать ширину, иначе openpyxl читает впустую.

ЕДИНИЦЫ
-------
Блок уровня наследует единицу из заголовка листа; блоки yoy/mom всегда «%».
Вывод в staging: unit_code + unit_name, маппинг в core.unit делает
гармонизатор (harmonize_7_kep.py).

Запуск:
  python3 scripts/kep_collect.py                 # найти свежий выпуск, загрузить
  python3 scripts/kep_collect.py --file PATH     # разобрать локальный файл
  python3 scripts/kep_collect.py --probe         # показать доступные выпуски
"""
import argparse
import hashlib
import os
import re
import ssl
import sys
import urllib.request
from datetime import datetime

import openpyxl
import psycopg

os.environ.setdefault("PGPASSFILE", os.path.expanduser("~/.pgpass"))
DSN = os.environ.get("PGDSN",
                     "host=127.0.0.1 port=15432 dbname=research_wiki user=wiki")
RAW_DIR = os.path.expanduser("~/research-wiki/raw/rosstat/kep")
BASE = "https://rosstat.gov.ru/storage/mediabank/ind_%02d-%d.xlsx"
SCHEMA = "staging"
PREFIX = "rosstat_kep__"
UA = ("Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0")

MONTHS_RU = ["Янв.", "Фев.", "Март", "Апр.", "Май", "Июнь", "Июль",
             "Август", "Сент.", "Окт.", "Нояб.", "Дек."]
QUARTERS = {"I": 1, "II": 2, "III": 3, "IV": 4}
# Кумулятивные периоды («нарастающим итогом»): листы 1.11, 2.1, 2.2 имеют
# шапку «Янв. | Янв-фев. | I квартал | Янв-апр. | …». Из них берём только
# годовую колонку — кумулятивные значения дублировали бы год в других
# единицах и путали бы временную ось.
CUMUL_MARK = re.compile(r"^(Янв|I квартал|I полугод|1st half|Jan|Q1)", re.I)
# Кумулятивные квартальные колонки: «I квартал» = фактический Q1
CUMUL_Q = {"I квартал": 1}
# Год со сноской: '19992)' = год 1999 + сноска «2)», '20221)' = 2022 + «1)»
YEAR_ANY = re.compile(r"^((?:19|20)\d\d)(\d?\)|\))?$")
# порядок важен — от специфичных к общим
UNIT_RULES = [
    (re.compile(r"млрд\s*руб", re.I), ("bln_rub", "млрд руб.")),
    (re.compile(r"млн\s*кв\.?\s*м", re.I), ("mln_sqm", "млн м²")),
    (re.compile(r"тыс\.?\s*кв\.?\s*м", re.I), ("ths_sqm", "тыс. м²")),
    (re.compile(r"млн\s*тонн", re.I), ("mln_tons", "млн тонн")),
    (re.compile(r"тыс\.?\s*тонн", re.I), ("ths_tons", "тыс. тонн")),
    (re.compile(r"млн\s*чел", re.I), ("mln_persons", "млн чел.")),
    (re.compile(r"тыс\.?\s*чел", re.I), ("ths_persons", "тыс. чел.")),
    (re.compile(r"млн\s*шт", re.I), ("mln_units", "млн шт.")),
    (re.compile(r"руб\.?\s*/\s*долл", re.I), ("rub_per_usd", "руб./долл.")),
    (re.compile(r"руб\.?\s*/\s*евро", re.I), ("rub_per_eur", "руб./евро")),
    (re.compile(r"млрд\s*долл", re.I), ("bln_usd", "млрд долл.")),
    (re.compile(r"млрд\s*пасс", re.I), ("bln_pkm", "млрд пасс-км")),
    (re.compile(r"\bрубл", re.I), ("rub", "руб.")),
    (re.compile(r"%|процент", re.I), ("pct", "%")),
]
SKIP_TEXT = re.compile(r"^(\d\)|/\s|стр\.|Примечан|Источник|Справочно)", re.I)
YEAR_FOOT = re.compile(r"^(19|20)(\d\d)\)?\s*$")


def log(msg):
    print(msg, flush=True)


# ---------------------------------------------------------------- скачивание
def fetch(url, timeout=120):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
        return r.read()


def probe_latest():
    """Свежий доступный выпуск: перебор назад от текущего месяца."""
    now = datetime.now()
    y, m = now.year, now.month
    for _ in range(18):
        url = BASE % (m, y)
        try:
            data = fetch(url, timeout=60)
            if data[:2] == b"PK" and len(data) > 100_000:
                return (m, y, url, data)
        except Exception:
            pass
        m -= 1
        if m == 0:
            m, y = 12, y - 1
    return None


def probe_all():
    now = datetime.now()
    y, m = now.year, now.month
    out = []
    for _ in range(18):
        url = BASE % (m, y)
        try:
            data = fetch(url, timeout=45)
            ok = data[:2] == b"PK" and len(data) > 100_000
            out.append((m, y, "200" if ok else "не xlsx", len(data)))
        except Exception as e:
            out.append((m, y, "404/ошибка", str(e)[:40]))
        m -= 1
        if m == 0:
            m, y = 12, y - 1
    return out


# ------------------------------------------------------------------ парсинг
def sanitize(name):
    s = re.sub(r"[^0-9a-zA-Z]+", "_", str(name).strip().lower())
    return re.sub(r"_+", "_", s).strip("_")


def resolve_unit(text, block):
    """Блок yoy/mom — всегда проценты; уровень — из заголовка."""
    if block in ("yoy", "mom"):
        return "pct", "%"
    t = text or ""
    for rx, u in UNIT_RULES:
        if rx.search(t):
            return u
    return None, None


def norm_block(text):
    """Классифицирует текстовую строку: маркер блока, служебная или имя ряда.

    Возвращает (kind, label):
      'yoy'  — в % к соответствующему периоду предыдущего года
      'mom'  — в % к предыдущему периоду
      'pct'  — прочий процентный блок («в % к концу предыдущего периода»)
      'skip' — служебная строка («в том числе:», примечания)
      'sub'  — имя ряда (продукт, категория, источник финансирования)
    """
    t = str(text).strip()
    low = t.lower()
    if "соответствующему периоду" in low:
        return "yoy", "в % к соответствующему периоду предыдущего года"
    if "предыдущему периоду" in low:
        return "mom", "в % к предыдущему периоду"
    if low.startswith("в % к") or low.startswith("в процентах"):
        return "pct", t[:110]
    # Служебная строка — только «в том числе:» БЕЗ продолжения.
    # «в том числе просроченная, млрд рублей» — это НАЗВАНИЕ РЯДА (в листе 2.4
    # под ним идёт отдельная таблица просроченной задолженности). Если считать
    # его служебным, эта таблица приписывается предыдущему ряду и данные
    # задваиваются (поймано: ровно 50% «дублей» в листе 2.4).
    # Подписи-описания методики: «в соответствии с Методикой…», «в фактически
    # действовавших ценах…» — это не ряды, а пояснения к подтаблице. Если
    # принять их за имя ряда, показатели сливаются (ловилось в 4.4).
    if re.match(r"^(в\s+соответствии|in\s+accordance)", low):
        return "skip", t
    if re.match(r"^(в\s+фактически|at\s+current|в\s+процентах\s+к|percent\s+of)", low):
        return "skip", t
    if re.match(r"^(в\s+том\s+числе|of\s+which)\s*:?\s*$", low):
        return "skip", t
    if low.startswith(("/", "1)", "2)", "3)", "4)", "5)", "6)", "7)", "8)")):
        return "skip", t
    return "sub", t


def parse_matrix_sheet(ws):
    """Листы 4.6: матрица, где ГОДЫ стоят в колонках, а периоды — во 2-й строке.

    Шапка: строка 1 = годы (2013, 2014, …), строка 2 = период ('год',
    'I квартал', 'I полугодие', 'январь-сентябрь'). Строки тела = доходные
    группы ('до 7000,0', 'свыше 100000,0') и агрегат «Численность населения».
    Возвращает наблюдения с series = имя доходной группы, а период берётся
    из пары (год, метка периода).
    """
    # годы в строке 1 (могут быть числами или текстом)
    yrow = [ws.cell(row=1, column=c).value for c in range(1, 60)]
    prow = [ws.cell(row=2, column=c).value for c in range(1, 60)]
    cols = {}
    cur_year = None
    for i, v in enumerate(yrow):
        if isinstance(v, (int, float)) and 1990 <= v <= 2030:
            cur_year = int(v)
        elif isinstance(v, str):
            m = YEAR_ANY.match(v.replace(",", "").strip())
            if m:
                cur_year = int(m.group(1))
        if cur_year is None:
            continue
        # период из строки 2 (или «год», если пусто)
        p = prow[i] if i < len(prow) else None
        per = "год"
        if isinstance(p, str):
            pl = p.strip().lower()
            if "квартал" in pl or pl.startswith("q1"):
                per = "I квартал"
            elif "полугод" in pl or "half" in pl:
                per = "I полугодие"
            elif "сентяб" in pl or "sept" in pl:
                per = "январь-сентябрь"
        cols[i + 1] = (cur_year, per)

    obs = []
    series = None
    for row_no, row in enumerate(
            ws.iter_rows(min_row=3, max_row=ws.max_row, max_col=60,
                         values_only=True), 3):
        c0 = row[0]
        if c0 is None:
            continue
        s = str(c0).strip()
        if not s:
            continue
        # служебные строки и продолжения переводов
        if s.startswith("/") or SKIP_TEXT.search(s) or re.match(r"^\d\)", s):
            continue
        low = s.lower()
        if low.startswith(("в том числе", "of which", "численность населения",
                           "population", "в  процентах", "percent o")):
            if "численность населения" in low or "population – total" in low:
                series = "Численность населения (всего)"
            continue
        nums = [v for v in row[1:] if isinstance(v, (int, float))]
        if not nums:
            continue
        if series is None:
            series = s
        name = series
        if s and not re.match(r"^\d+\.\d", s) and len(s) > 2:
            name = s
        for ci, (yr, per) in cols.items():
            if ci - 1 < len(row) and isinstance(row[ci - 1], (int, float)):
                obs.append(dict(block="level", col=ci,
                                block_name=("%s | %s" % (name, per))[:110],
                                series=("%s | %s" % (name, per))[:110],
                                frequency="A", year=yr,
                                month=None, quarter=None,
                                value=float(row[ci - 1]),
                                unit_code="pct", unit_name="%",
                                footnote=per))
    return obs


def parse_sheet(ws, sheet_name):
    """Разбирает лист → (наблюдения, заголовок, заметки)."""
    # --- шапка: строка с месяцами ИЛИ с кварталами ---
    # Листы бывают двух видов: с месяцами (1.6, 1.7, 1.8, 3.x) и только с
    # кварталами (1.1 — ВВП, 1.2 — ИПП). Требовать ≥8 месяцев нельзя:
    # квартальные листы тогда выпадают целиком.
    hrow, mcols, qcols = None, {}, {}
    for r in range(1, 8):
        vals = [ws.cell(row=r, column=c).value for c in range(1, 41)]
        nm = sum(1 for v in vals if v in MONTHS_RU)
        nq = sum(1 for v in vals if v in QUARTERS)
        ncu = sum(1 for v in vals
                  if isinstance(v, str) and CUMUL_MARK.match(v.strip()))
        # Кумулятивные листы (1.11, 2.1, 2.2): шапка «Янв. | Янв-фев. |
        # I квартал | …». Берём из них только годовую колонку и «Янв.»
        # (первый месяц кумулятивного ряда — это сам январь); остальные
        # кумулятивные ячейки пропускаем, иначе нарастающие итоги
        # смешались бы с месячными значениями.
        if nm >= 4 or nq >= 3 or ncu >= 3:
            hrow = r
            mcols = {i + 1: MONTHS_RU.index(v) + 1
                     for i, v in enumerate(vals) if v in MONTHS_RU}
            # В части листов (1.14) шапка содержит ДВА прохода месяцев:
            # «Янв…Дек | Янв…Дек» — второй блок это другой показатель
            # (например, стоимость в рублях и индекс в %). Одноимённые месяцы
            # во втором проходе нумеруем как 21..32, чтобы не схлопываться.
            seen_months = {}
            for ci, mo in list(mcols.items()):
                if mo in seen_months:
                    mcols[ci] = mo + 20
                else:
                    seen_months[mo] = ci
            for rr in (r, r + 1):
                for c in range(1, 41):
                    v = ws.cell(row=rr, column=c).value
                    if v in QUARTERS and c not in mcols:
                        qcols[c] = QUARTERS[v]
            break
    if hrow is None:
        return [], None, ["нет строки с месяцами/кварталами"]

    # --- название показателя: предпочитаем строку вида «1.7. Название» ---
    title, title_row = None, hrow
    numbered = re.compile(r"^\d+(\.\d+)*\.\s+\S")
    for r in range(hrow + 1, min(hrow + 8, ws.max_row + 1)):
        v = ws.cell(row=r, column=1).value
        if not (v and isinstance(v, str) and len(v.strip()) > 12):
            continue
        s = v.strip()
        if s.startswith("/"):
            continue
        if numbered.match(s):
            title, title_row = s, r
            break
        if title is None:
            title, title_row = s, r  # запасной вариант
    if not title:
        return [], None, ["не найден заголовок показателя"]

    maxc = max(list(mcols) + list(qcols) + [2]) + 1
    obs = []
    block, block_name = "level", "уровень"
    seen_year = False
    # ИДЕНТИЧНОСТЬ РЯДА = (раздел, имя ряда, блок, частота).
    #
    # Три вещи, которые ломали наивные варианты:
    # 1) Номер строки НЕ подходит: один ряд размазан по строкам разных лет
    #    (в 2.3 «до 1 года» повторяется под каждой годовой подтаблицей,
    #    в 4.7 «трудоспособное» — под каждым годом-секцией).
    # 2) Имя ряда задаёт СТРОКА-ПОДПИСЬ (продукт, категория, источник
    #    финансирования): в 3.1.1 это «Нефть обезвоженная…», в 4.4 —
    #    «Денежные доходы (в среднем на душу населения)», в 4.7 —
    #    «трудоспособное», «пенсионеры», «дети».
    # 3) Метки блоков («в % к концу предыдущего периода») НЕ должны затирать
    #    имя ряда — иначе блоки разных продуктов схлопываются в один ряд.
    # Плюс раздел: в 1.9 «импорт товаров» есть и по дальнему зарубежью
    # (раздел 1.9.1), и по СНГ (1.9.2) — различить можно только разделом.
    section = None       # номерной заголовок подтаблицы («1.9.1. …»)
    series_name = None   # имя ряда (строка-подпись)
    sub_idx = 0          # счётчик подтаблиц
    series_row = None    # номер строки подписи — различает одноимённые ряды
    ordinal = 0          # счётчик повторов одной подписи внутри подтаблицы
    sec_year = None      # год-заголовок секции (лист 4.7)
    for row_no, row in enumerate(
            ws.iter_rows(min_row=title_row + 1, max_row=min(ws.max_row, 3000),
                         max_col=maxc, values_only=True), title_row + 1):
        c0 = row[0] if len(row) > 0 else None
        c1 = row[1] if len(row) > 1 else None
        s = str(c0).strip() if c0 is not None else ""

        # --- маркер блока, имя ряда, служебная строка или ГОД-секция? ---
        if s and not isinstance(c0, (int, float)) and c1 is None:
            if SKIP_TEXT.search(s) or s.startswith("("):
                continue
            ysec = YEAR_ANY.match(s.replace(",", "").strip())
            if ysec:
                sec_year = int(ysec.group(1))
                continue
            if len(s) > 2:
                kind, label = norm_block(s)
                if kind == "skip":
                    continue
                if re.match(r"^\d+\.\d+(\.\d+)*\.", s):
                    section = s            # «1.9.1. Внешнеторговый оборот…»
                    sub_idx += 1
                    ordinal = 0
                    series_row = row_no
                    # Номерной заголовок ВСЕГДА становится именем ряда.
                    # Раньше он присваивался только при пустом series_name, и
                    # тогда блок 4.4.4 наследовал имя 4.4.1 — два разных
                    # показателя сливались в один (6 957 различающихся
                    # значений терялось по всему источнику).
                    series_name = s
                    # Новая подтаблица ВСЕГДА начинается с уровня: без сброса
                    # блока значения уровня наследуют метку «mom»/«yoy» от
                    # предыдущей подтаблицы и попадают не в тот ряд
                    # (поймано в 1.9: 2,7 млрд долл. шли как «% к периоду»).
                    block, block_name = "level", "уровень"
                    continue
                if kind in ("yoy", "mom"):
                    block, block_name = kind, label
                    continue
                if kind == "pct":
                    block, block_name = "pct", label
                    continue
                # kind == 'sub': это имя ряда; новый ряд начинается с уровня
                series_name = s
                series_row = row_no
                ordinal += 1
                block, block_name = "level", "уровень"
                continue

        # --- год? ---
        # Форматы: 1999 (число), '19992)' (год+сноска), '20221)' (год+сноска).
        #
        # ВАЖНО: год ищем ТОЛЬКО в колонке 2. В части листов (2.4, 2.5, 1.12)
        # колонки года нет вовсе — шапка начинается сразу с «Янв.» в колонке 2.
        # Старый код читал такую колонку и как год, и как месяц, из-за чего
        # каждое значение дублировалось (ровно 50% «дублей» в листе 2.4).
        yr = None
        foot = None
        if (isinstance(c0, (int, float)) and 1990 <= c0 <= 2030
                and 2 not in mcols and 2 not in qcols):
            yr = int(c0)
        else:
            s_clean = s.replace(",", "").strip()
            mm = YEAR_ANY.match(s_clean)
            if mm and (2 not in mcols or isinstance(c0, (int, float))):
                yr = int(mm.group(1))
                if len(s_clean) > 4:
                    foot = s
        # Листы с годом-секцией (4.7): год берём из секции, а имя ряда — ВСЕГДА
        # из строки-подписи. Здесь строки «Все население», «трудоспособное»,
        # «пенсионеры», «дети» повторяются под каждым годом (1999, 2000, …) —
        # это одна серия, растянутая по годам, поэтому имя ряда обязано
        # обновляться на каждой строке, а не запоминаться один раз.
        if yr is None and sec_year and s and c1 is not None:
            yr = sec_year
            series_name = s
            series_row = row_no
        # Листы с годами в колонке 1 и месяцами без годовой колонки (2.4):
        # строка всё равно начинается с года — он уже разобран выше.
        if yr is None:
            continue
        seen_year = True

        unit_code, unit_name = resolve_unit(title, block)
        # Номер подтаблицы обязателен: в листах 4.4, 3.2, 1.9 под одним и тем же
        # номером идут несколько таблиц (месячная, квартальная, годовая) с
        # одинаковыми подписями рядов — без счётчика они схлопываются.
        cur_series = " || ".join(p for p in (section, series_name) if p) or title
        if sub_idx:
            cur_series += " [подтаблица %d]" % sub_idx
        if ordinal > 1:
            cur_series += " [повтор %d]" % ordinal
        # Страховка: если подпись ряда так и не встретилась (например, данные
        # идут до первого заголовка), берём текущую строку — иначе row_no
        # окажется None и такие строки схлопнутся между собой.
        eff_row = series_row if series_row is not None else row_no
        for ci, mo in mcols.items():
            if ci - 1 < len(row):
                v = row[ci - 1]
                if isinstance(v, (int, float)):
                    obs.append(dict(block=block, block_name=block_name,
                                    series=cur_series, row_no=eff_row, col=ci,
                                    frequency="M", year=yr, month=mo, quarter=None,
                                    value=float(v), unit_code=unit_code,
                                    unit_name=unit_name, footnote=foot))
        for ci, q in qcols.items():
            if ci - 1 < len(row):
                v = row[ci - 1]
                if isinstance(v, (int, float)):
                    obs.append(dict(block=block, block_name=block_name,
                                    series=cur_series, row_no=eff_row, col=ci,
                                    frequency="Q", year=yr, month=None, quarter=q,
                                    value=float(v), unit_code=unit_code,
                                    unit_name=unit_name, footnote=foot))
        # Годовое значение берём из колонки 2 ТОЛЬКО если она не занята месяцем
        # или кварталом. В части листов (1.14, 2.4, 2.5) годовой колонки нет
        # вовсе, и колонка 2 — это «Янв.»: без проверки одно и то же число
        # попадало и как январь, и как год (в 1.14 так задваивались 573
        # значения, причём с разными метками периодов).
        if (isinstance(c1, (int, float))
                and 2 not in mcols and 2 not in qcols):
            obs.append(dict(block=block, block_name=block_name, series=cur_series,
                            row_no=eff_row, col=2,
                            frequency="A", year=yr, month=None, quarter=None,
                            value=float(c1), unit_code=unit_code,
                            unit_name=unit_name, footnote=foot))

    notes = [] if seen_year else ["нет строк с годами"]
    return obs, title, notes


# ------------------------------------------------------------------- запись
def ensure_table(cur, table):
    cur.execute("""SELECT 1 FROM information_schema.tables
                   WHERE table_schema=%s AND table_name=%s""", (SCHEMA, table))
    if cur.fetchone():
        cur.execute('DROP TABLE %s."%s"' % (SCHEMA, table))
    cur.execute(f"""
        CREATE TABLE {SCHEMA}."{table}" (
            sheet         text,
            block         text,
            block_name    text,
            series        text,
            row_no        int,
            col           int,
            frequency     text,
            year          int,
            month         int,
            quarter       int,
            value         numeric,
            unit_code     text,
            unit_name     text,
            footnote      text,
            release_label text
        )""")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", help="локальный XLSX вместо скачивания")
    ap.add_argument("--probe", action="store_true", help="только показать выпуски")
    ap.add_argument("--limit-sheets", type=int, default=0)
    args = ap.parse_args()

    if args.probe:
        log("доступные выпуски ind_MM-YYYY.xlsx:")
        for m, y, st, extra in probe_all():
            log("  %02d-%d: %s %s" % (m, y, st, extra if st != "200" else "%s байт" % extra))
        return

    os.makedirs(RAW_DIR, exist_ok=True)
    if args.file:
        path = args.file
        label_period = None
        log("файл: %s" % path)
    else:
        log("ищу свежий выпуск…")
        found = probe_latest()
        if not found:
            log("ОШИБКА: доступных выпусков не найдено")
            sys.exit(1)
        m, y, url, data = found
        path = os.path.join(RAW_DIR, "ind_%02d-%d.xlsx" % (m, y))
        log("выпуск: ind_%02d-%d.xlsx (%s байт)" % (m, y, format(len(data), ",")))
        old = None
        if os.path.exists(path):
            old = hashlib.sha256(open(path, "rb").read()).hexdigest()
        new = hashlib.sha256(data).hexdigest()
        if old == new:
            log("хеш совпал с локальной копией — перезаписи не требуется")
        else:
            with open(path, "wb") as f:
                f.write(data)
            log("сохранён: %s" % path)
        label_period = (m, y)

    # метка релиза
    if label_period:
        m, y = label_period
        prev_m = 12 if m == 1 else m - 1
        prev_y = y - 1 if m == 1 else y
        label = "КЭП, выпуск январь–%s %d" % (
            ["", "январь", "февраль", "март", "апрель", "май", "июнь", "июль",
             "август", "сентябрь", "октябрь", "ноябрь", "декабрь"][m], y)
        pub = "20%02d-%02d" % (y % 100, m)
    else:
        label = "КЭП, локальный файл %s" % os.path.basename(path)
        pub = None

    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    conn = psycopg.connect(DSN)
    cur = conn.cursor()

    total = 0
    sheets_done, sheets_skip = [], []
    names = [n for n in wb.sheetnames
             if n.strip() not in ("Титульный", "Содержание", "The Contens")]
    if args.limit_sheets:
        names = names[:args.limit_sheets]

    for name in names:
        ws = wb[name]
        # листы 4.6 — матрица «годы в колонках»: свой парсер
        if name.strip().startswith("4.6"):
            obs = parse_matrix_sheet(ws)
            if obs:
                title = "4.6. Распределение населения по величине доходов (%% к итогу)"
                notes = []
            else:
                title, notes = None, ["матрица не разобрана"]
        else:
            obs, title, notes = parse_sheet(ws, name)
        table = PREFIX + sanitize(name)
        if not obs:
            sheets_skip.append((name.strip(), notes[0] if notes else "нет данных"))
            continue
        ensure_table(cur, table)
        with cur.copy('COPY %s."%s" (sheet, block, block_name, series, row_no, col, frequency, '
                      'year, month, quarter, value, unit_code, unit_name, '
                      'footnote, release_label) FROM STDIN' % (SCHEMA, table)) as cp:
            for o in obs:
                cp.write_row((name.strip(), o["block"], o["block_name"],
                              o["series"], o.get("row_no"), o.get("col"),
                              o["frequency"], o["year"], o["month"],
                              o["quarter"], o["value"], o["unit_code"],
                              o["unit_name"], o["footnote"], label))
        conn.commit()
        sheets_done.append((name.strip(), title[:60] if title else "?", len(obs)))
        total += len(obs)
    conn.close()

    log("\n=== загружено в staging ===")
    for n, t, c in sheets_done:
        log("  %-9s %-58s %s" % (n, t, format(c, ",")))
    log("\nлистов с данными: %d, наблюдений: %s" % (len(sheets_done), format(total, ",")))
    if sheets_skip:
        log("\nпропущено (нет табличной структуры с годами): %d" % len(sheets_skip))
        for n, why in sheets_skip:
            log("  %-20s %s" % (n, why))
    log("\nrelease_label: %s" % label)


if __name__ == "__main__":
    main()
