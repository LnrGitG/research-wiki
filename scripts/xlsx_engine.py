#!/usr/bin/env python3
"""Единый читатель табличных выгрузок (xlsx/xlsb/ods) с выбором движка.

Зачем: `openpyxl` в режиме read_only разбирает XML на чистом Python и на
больших листах упирается в минуты (200 тыс. строк × 8 колонок — 92,5 с).
`fastexcel` 0.21 (Rust, движок calamine — тот же, что у Polars и undatum)
читает тот же файл за 4,1 с, значения совпадают побайтно после приведения
к канонической текстовой форме.

Контракт намеренно повторяет то подмножество openpyxl, которым пользуются
парсеры репозитория:

    wb = open_workbook(path, engine="fastexcel")   # по умолчанию fastexcel
    for name in wb.sheetnames:
        for row in wb[name].iter_rows(min_row=9, values_only=True):
            ...
    wb.close()

Значения приводятся к тем же типам Python, что отдаёт openpyxl:
строка -> str, число -> int/float, дата -> datetime.datetime.
Ключевое отличие fastexcel — он типизирует колонки по образцу первых
строк (Arrow), поэтому длинная текстовая колонка с ведущими нулями может
прийти как int64. Для таких листов используйте `dtypes`, например
`wb[name].iter_rows(dtypes={"col": "string"})` или параметр `text_columns`
в `open_workbook`; в отчёте о пилоте это зафиксировано.

Выбор движка: аргумент `--xlsx-engine openpyxl|fastexcel` (см.
`add_engine_arg`), переменная окружения `XLSX_ENGINE` как резервный
канал отката без правки командных строк.
"""
from __future__ import annotations

import datetime as _dt
import decimal
import os
import re
import sys

ENGINES = ("fastexcel", "openpyxl")
DEFAULT_ENGINE = os.environ.get("XLSX_ENGINE", "fastexcel")
_NUMERIC_TEXT = re.compile(r"-?\d+(?:\.\d+)?")

_HAS_FASTEXCEL = None


def has_fastexcel() -> bool:
    global _HAS_FASTEXCEL
    if _HAS_FASTEXCEL is None:
        try:
            import fastexcel  # noqa: F401
            _HAS_FASTEXCEL = True
        except Exception:
            _HAS_FASTEXCEL = False
    return _HAS_FASTEXCEL


def add_engine_arg(parser, default: str | None = None):
    """Добавить в argparse-парсер выбор движка чтения xlsx."""
    parser.add_argument(
        "--xlsx-engine",
        choices=ENGINES,
        default=default or DEFAULT_ENGINE,
        help="движок чтения xlsx (по умолчанию fastexcel; откат — openpyxl "
             "или переменная окружения XLSX_ENGINE)",
    )
    return parser


def resolve_engine(engine: str | None = None) -> str:
    eng = (engine or DEFAULT_ENGINE or "fastexcel").lower()
    if eng not in ENGINES:
        raise ValueError(f"неизвестный движок xlsx: {engine!r}; допустимо {ENGINES}")
    if eng == "fastexcel" and not has_fastexcel():
        print("WARN: fastexcel не установлен, откат на openpyxl", file=sys.stderr)
        return "openpyxl"
    return eng


def to_python(value):
    """Значение Arrow/calamine -> тип, который отдаёт openpyxl."""
    if value is None:
        return None
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value if value != "" else None
    if isinstance(value, decimal.Decimal):
        f = float(value)
        return int(f) if f.is_integer() else f
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return value
    if isinstance(value, _dt.datetime):
        return value
    if isinstance(value, _dt.date):
        return _dt.datetime(value.year, value.month, value.day)
    if isinstance(value, _dt.time):
        return _dt.datetime(1899, 12, 30, value.hour, value.minute, value.second,
                            value.microsecond)
    return value


def cell_text(value) -> str:
    """Каноническая текстовая форма ячейки для сверки хешей.

    Числа приводятся к целому виду без хвоста `.0`, даты — к ISO с пробелом
    (как str() от datetime у openpyxl), None — к пустой строке.
    """
    v = to_python(value) if not isinstance(value, (str, int, float, bool)) else value
    if v is None:
        return ""
    if isinstance(v, bool):
        return "TRUE" if v else "FALSE"
    if isinstance(v, float):
        if v.is_integer():
            return str(int(v))
        return repr(v)
    if isinstance(v, _dt.datetime):
        if v.microsecond:
            return v.isoformat(sep=" ")
        return v.strftime("%Y-%m-%d %H:%M:%S")
    if isinstance(v, _dt.date):
        return v.strftime("%Y-%m-%d")
    return str(v)


def _is_plain_number(text: str) -> bool:
    """Текст — обычное десятичное число без ведущих нулей («1010», «-3.5»).

    Ведущие нули — признак кода или идентификатора (ОКТМО, артикул): такой
    текст остаётся строкой, иначе значение «007» превратится в 7.
    """
    s = text.strip()
    if not _NUMERIC_TEXT.fullmatch(s):
        return False
    body = s.lstrip("+-")
    return not (len(body) > 1 and body[0] == "0" and body[1].isdigit())


class Sheet:
    """Лист с интерфейсом openpyxl: iter_rows(min_row, max_row, values_only)."""

    def __init__(self, name, loader, dtypes=None):
        self.name = name
        self._loader = loader
        self._rows = None
        self._dtypes = dtypes

    @property
    def rows(self):
        if self._rows is None:
            self._rows = self._loader(self._dtypes)
        return self._rows

    def iter_rows(self, min_row: int = 1, max_row=None, values_only: bool = True):
        rows = self.rows
        hi = len(rows) if max_row is None else min(max_row, len(rows))
        for i in range(max(1, min_row) - 1, hi):
            row = rows[i]
            yield tuple(row) if values_only else row

    def close(self):
        self._rows = None


def _col_index(ref: str) -> int:
    """'BX12' -> 75 (0-based)."""
    n = 0
    for ch in ref:
        if ch.isalpha():
            n = n * 26 + (ord(ch.upper()) - 64)
        else:
            break
    return n - 1


def _col_letters(idx: int) -> str:
    s = ""
    idx += 1
    while idx:
        idx, r = divmod(idx - 1, 26)
        s = chr(65 + r) + s
    return s


def _attrs(fragment: str) -> dict:
    """Атрибуты элемента XML -> словарь (порядок атрибутов не важен)."""
    return dict(re.findall(r'([A-Za-z_:][-A-Za-z0-9_:.]*)\s*=\s*"([^"]*)"', fragment))


def _sheet_xml_names(zf) -> dict:
    """Имя листа -> путь XML внутри архива."""
    wbxml = zf.read("xl/workbook.xml").decode("utf-8", "replace")
    rels = zf.read("xl/_rels/workbook.xml.rels").decode("utf-8", "replace")
    relmap = {}
    for frag in re.findall(r"<Relationship\b([^>]*?)/?>", rels):
        a = _attrs(frag)
        if a.get("Id"):
            relmap[a["Id"]] = a.get("Target", "")
    out = {}
    for frag in re.findall(r"<sheet\b([^>]*?)/?>", wbxml):
        a = _attrs(frag)
        name = a.get("name")
        rid = a.get("r:id")
        target = relmap.get(rid or "", "")
        if not name or not target:
            continue
        target = target.lstrip("/")
        out[name] = target if target.startswith("xl/") else "xl/" + target
    return out


def xml_sheet_offsets(path, sheet_name: str, name_map=None):
    """Сдвиги листа в разметке: (пустые строки сверху, пустые колонки слева).

    openpyxl нумерует и строки, и колонки от A1, fastexcel (calamine) — от
    первой строки и первой колонки со значениями: без поправки значения
    съезжают и по строкам (ФНС: лист начинается с 9-й строки), и по колонкам
    (лист, заведённый с C1). Считаем по разметке: первая строка и первая
    колонка, где есть <v> или <is>; атрибут dimension файла — только нижняя
    граница, он бывает устаревшим.
    """
    import zipfile
    try:
        with zipfile.ZipFile(path) as zf:
            names = name_map if name_map is not None else _sheet_xml_names(zf)
            xml_name = names.get(sheet_name)
            if not xml_name or xml_name not in zf.namelist():
                return 0, 0
            with zf.open(xml_name) as fh:
                head = fh.read(400000)
    except (OSError, KeyError):
        return 0, 0
    m = re.search(rb'<dimension ref="([A-Z]*)(\d+)', head)
    row_lead = max(0, int(m.group(2)) - 1) if m else 0
    col_lead = _col_index(m.group(1).decode()) if m and m.group(1) else 0
    row_pat = re.compile(rb'<row r="(\d+)"[^>]*>(.*?)</row>', re.S)
    cell_pat = re.compile(rb'<c r="([A-Z]+)\d+"[^>]*>(?:<f[^>]*>[^<]*</f>)?<(?:v|is)>')
    first_row = None
    seen = 0
    for mrow in row_pat.finditer(head):
        inner = mrow.group(2)
        if b"<v>" not in inner and b"<is>" not in inner:
            continue
        if first_row is None:
            first_row = int(mrow.group(1))
        # колонка отсчёта calamine — минимальная колонка со значением;
        # смотрим первые строки, дальше диапазон листа уже определён
        cols = [_col_index(mc.group(1).decode())
                for mc in cell_pat.finditer(inner)]
        if cols:
            col_lead = min(cols) if first_row is None or seen == 0 else min(col_lead, min(cols))
        seen += 1
        if seen >= 20:
            break
    if first_row:
        return max(row_lead, first_row - 1), max(0, col_lead)
    return row_lead, max(0, col_lead)


class _OpenpyxlWorkbook:
    engine = "openpyxl"

    def __init__(self, path, text_columns=None):
        import openpyxl
        self._wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
        self.sheetnames = list(self._wb.sheetnames)

    def __getitem__(self, name):
        ws = self._wb[name]
        return Sheet(name, lambda dtypes=None: self._materialize(ws))

    @staticmethod
    def _materialize(ws):
        return [list(r) for r in ws.iter_rows(values_only=True)]

    def close(self):
        try:
            self._wb.close()
        except Exception:
            pass


class _FastexcelWorkbook:
    engine = "fastexcel"

    def __init__(self, path, text_columns=None, exact=True):
        import fastexcel
        self._path = path
        self._reader = fastexcel.read_excel(path)
        self.sheetnames = list(self._reader.sheet_names)
        self._text_columns = text_columns or {}
        self._exact = exact
        self._cache = {}
        self._xml_meta = {}
        self._xml_names = None

    # --- сверка с разметкой исходного XLSX ---------------------------------
    def _load(self, name, dtypes=None):
        key = (name, tuple(sorted(dtypes.items())) if dtypes else None)
        if key in self._cache:
            return self._cache[key]
        dtypes = dict(dtypes or {})
        dtypes.update(self._text_columns.get(name, {}))
        sheet = self._reader.load_sheet_by_name(
            name, header_row=None, dtype_coercion="strict" if dtypes else "coerce",
            dtypes=dtypes or None,
        )
        table = sheet.to_arrow()
        cols = [table.column(i).to_pylist() for i in range(table.num_columns)]
        height = max((len(c) for c in cols), default=0)
        rows = [
            [to_python(c[i]) if i < len(c) else None for c in cols]
            for i in range(height)
        ]
        if self._exact:
            str_cols = {i for i in range(table.num_columns)
                        if str(table.schema.field(i).type) == "string"}
            row_lead, col_lead = self._sheet_offsets(name) if str_cols else (0, 0)
            if str_cols:
                self._repair_precision(name, rows, table, str_cols,
                                       row_lead, col_lead)
            if row_lead or col_lead:
                width = max((len(r) for r in rows), default=0) + col_lead
                if row_lead:
                    rows = [[None] * width for _ in range(row_lead)] + rows
                if col_lead:
                    rows = [[None] * col_lead + list(r) for r in rows]
        self._cache[key] = rows
        return rows

    def _sheet_offsets(self, name):
        """Пустые строки сверху и колонки слева, которые calamine отбросил."""
        if name not in self._xml_meta:
            if self._xml_names is None:
                try:
                    import zipfile
                    with zipfile.ZipFile(self._path) as zf:
                        self._xml_names = _sheet_xml_names(zf)
                except (OSError, KeyError):
                    self._xml_names = {}
            self._xml_meta[name] = xml_sheet_offsets(self._path, name,
                                                     name_map=self._xml_names)
        return self._xml_meta[name]

    def _repair_precision(self, name, rows, table, str_cols, lead=0, col_lead=0):
        """Вернуть числам полную точность в колонках, типизированных строкой.

        calamine печатает число в смешанной колонке строкой с 12 значащими
        цифрами. Колонка перечитывается одним проходом с dtypes=«float», и
        значение подменяется только там, где исходный текст не воспроизводит
        число: то есть только при реальной потере точности. Текст, который
        сам по себе является числом («1010», «007»), остаётся строкой —
        открытый текст не подменяется и ведущие нули не теряются.
        """
        if not str_cols:
            return
        cand = []
        for ci in sorted(str_cols):
            sample = 0
            for v in table.column(ci).to_pylist():
                if isinstance(v, str) and _is_plain_number(v):
                    sample += 1
                    if sample >= 3:
                        cand.append(ci)
                        break
        if not cand:
            return
        # dtypes адресуются по именам колонок всего листа; без use_columns
        # fastexcel отдаёт таблицу со всеми колонками, лишние не читаем в Python
        probe = self._reader.load_sheet_by_name(
            name, header_row=None,
            dtypes={f"__UNNAMED__{c + col_lead}": "float" for c in cand},
        )
        ptab = probe.to_arrow()
        for k, ci in enumerate(cand):
            vals = ptab.column(ci + col_lead).to_pylist()
            main_col = rows_column = [r[ci] if ci < len(r) else None for r in rows]
            # второй проход может начать лист на другую строку (dtypes меняют
            # то, какие строки считаются непустыми), поэтому выравниваем по
            # совпадению текста, а не по номеру строки
            probe_text = [cell_text(v) for v in vals[:120]]
            main_text = [cell_text(v) for v in main_col[:120]]
            best, best_hits = 0, -1
            for shift in range(0, 4):
                hits = 0
                for idx, t in enumerate(probe_text):
                    j = idx + shift
                    if j >= len(main_text) or not t:
                        continue
                    mt = main_text[j]
                    if mt == t:
                        hits += 1
                    elif _is_plain_number(t) and _is_plain_number(mt):
                        a, b = float(t), float(mt)
                        if abs(a - b) <= 1e-9 * max(1.0, abs(a)):
                            hits += 1
                if hits > best_hits:
                    best, best_hits = shift, hits
                if best_hits >= 0.8 * len(probe_text):
                    break
            if best_hits <= 0:
                continue
            for idx, v in enumerate(vals):
                i = idx + best
                if v is None or i >= len(rows) or ci >= len(rows[i]):
                    continue
                cur = rows[i][ci]
                if (isinstance(cur, str) and _is_plain_number(cur)
                        and cell_text(cur) != cell_text(v)):
                    rows[i][ci] = to_python(v)

    def __getitem__(self, name):
        if name not in self.sheetnames:
            raise KeyError(f"нет листа {name!r}")
        return Sheet(name, lambda dtypes=None: self._load(name, dtypes))

    def close(self):
        self._cache.clear()


def open_workbook(path, engine: str | None = None, text_columns=None, exact=True):
    """Открыть книгу; text_columns — {лист: {колонка: 'string'}} для колонок,
    где важны ведущие нули или текстовый тип. exact=False отключает сверку
    типов с разметкой XLSX (быстрее, но числа в смешанных колонках придут
    строками с 12 значащими цифрами)."""
    eng = resolve_engine(engine)
    if eng == "fastexcel":
        return _FastexcelWorkbook(path, text_columns, exact=exact)
    return _OpenpyxlWorkbook(path, text_columns)


def read_sheet_rows(path, sheet=None, engine=None, min_row=1, text_columns=None,
                    exact=True):
    """Плоское чтение одного листа (первого, если имя не задано)."""
    wb = open_workbook(path, engine=engine, text_columns=text_columns, exact=exact)
    try:
        name = sheet if sheet is not None else wb.sheetnames[0]
        return [r for r in wb[name].iter_rows(min_row=min_row, values_only=True)]
    finally:
        wb.close()
