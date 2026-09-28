#!/usr/bin/env python3
"""Универсальный загрузчик данных с ЕМИСС (fedstat.ru).

Зачем: прежний `emiss_client.py` был незавершённым портом R-пакета
fedstatAPIr под старый шаблон страницы и не работал на текущей разметке.
Здесь протокол собран заново и проверен на живом источнике.

Как устроен источник (проверено 28.09.2026 на показателе 43062):
  1. GET /indicator/<id> отдаёт страницу; в ней в JS-блоке лежит структура
     фильтров (`filters: {...}`), раскладка (`left_columns`, `top_columns`,
     `filterObjectIds`) и в div#downloadTokenHolder — CSRF-токен.
  2. POST /indicator/downloadData.do?format=sdmx|excel принимает тело:
     title, struts.token.name, <имя токена>=<токен>, id, затем по одному
     lineObjectIds/columnObjectIds на поле раскладки и по одному
     selectedFilterIds=<поле>_<значение> на каждое выбранное значение.
  3. Токен одноразовый и привязан к сессии (cookie), поэтому GET и POST
     делаются одним opener'ом с cookie-jar.

Ответ sdmx разбирается средствами стандартной библиотеки: каждый Series —
это одна точка, в SeriesKey лежат измерения (s_OKATO — территория,
s_vozr — возраст), в Attributes — единица измерения (EI) и период
(PERIOD), в Obs — Time (год) и ObsValue (значение). Excel отдаётся в
устаревшем формате .xls и требует xlrd, поэтому по умолчанию sdmx.

Использование:
    python3 emiss_loader.py 43062 --list
    python3 emiss_loader.py 43062 --filter "Классификатор объектов админ...=Свердловская область" \
        --filter "Год=2025,2026" --out /tmp/43062.csv

Питфоллы источника (проверены на практике):
  * Сужение полей из top_columns (обычно Год и Период) ЕМИСС не принимает:
    вместо таблицы приходит HTML-страница. Сужение полей из left_columns
    (территория, товар, возраст) работает. Отбор по годам и периодам делайте
    после загрузки — по колонкам time и PERIOD.
  * У показателя могут быть варианты размерности с разным охватом лет. Пример:
    43062 «15 лет и старше» покрыт 2017–2026, а «15-72 лет» — только 2000–2021.
    Поэтому при сверке ряда сначала проверьте, какая градация свежая.
  * Выгрузка «всё по показателю» может быть очень большой: 31074 по одной
    территории дал 914 848 точек и 470 МБ xml. Для тяжёлых показателей
    сужайте left_columns и сохраняйте сырой ответ в файл (save_raw).
"""

import argparse
import csv
import http.cookiejar
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

BASE = "https://www.fedstat.ru"
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/126.0 Safari/537.36")
SDMX_NS = "{http://www.SDMX.org/resources/SDMXML/schemas/v1_0/message}"


# ---------------------------------------------------------------- разбор JS

def js_to_json(src):
    """Переводит фрагмент JS-объекта в JSON: строки, ключи, висячие запятые.

    Разметка ЕМИСС — это JS-литерал (одинарные кавычки, голые ключи, в том
    числе числовые, комментарии), который json.loads не принимает напрямую.
    """
    out, i, n = [], 0, len(src)
    while i < n:
        ch = src[i]
        if src[i:i + 2] == "//":
            j = src.find("\n", i)
            i = n if j < 0 else j + 1
            continue
        if src[i:i + 2] == "/*":
            j = src.find("*/", i + 2)
            i = n if j < 0 else j + 2
            continue
        if ch in ("'", '"'):
            q, j, buf = ch, i + 1, []
            while j < n:
                c = src[j]
                if c == "\\":
                    nxt = src[j + 1] if j + 1 < n else ""
                    if nxt == "u":
                        try:
                            buf.append(chr(int(src[j + 2:j + 6], 16)))
                        except ValueError:
                            pass
                        j += 6
                        continue
                    buf.append({"n": "\n", "t": "\t", "r": "\r",
                                "b": "\b", "f": "\f"}.get(nxt, nxt))
                    j += 2
                    continue
                if c == q:
                    j += 1
                    break
                buf.append(c)
                j += 1
            out.append(json.dumps("".join(buf), ensure_ascii=False))
            i = j
            continue
        out.append(ch)
        i += 1
    s = "".join(out)
    s = re.sub(r"([{,])\s*([A-Za-z_][A-Za-z0-9_]*)\s*:", r'\1"\2":', s)
    s = re.sub(r"([{,])\s*(\d+)\s*:", r'\1"\2":', s)
    s = re.sub(r",\s*([}\]])", r"\1", s)
    return json.loads(s)


def _slice_braced(text, key):
    """Вырезает объект {...} , начинающийся после ключа, с учётом скобок и кавычек."""
    i = text.find(key)
    if i < 0:
        return None
    start = text.find("{", i)
    if start < 0:
        return None
    depth, j, in_q, esc = 0, start, None, False
    while j < len(text):
        c = text[j]
        if esc:
            esc = False
        elif c == "\\":
            esc = True
        elif in_q:
            if c == in_q:
                in_q = None
        elif c in ("'", '"'):
            in_q = c
        elif c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return text[start:j + 1]
        j += 1
    return None


def _arr_ints(text, key):
    i = text.find(key)
    if i < 0:
        return []
    seg = text[i:text.find("]", i) + 1]
    return [int(x) for x in re.findall(r"\d+", seg)]


# ------------------------------------------------------------------- сессия

class Emiss:
    """Сессия с ЕМИСС: одна cookie-банка на все запросы, токен одноразовый."""

    def __init__(self, base=BASE, timeout=180, retries=3):
        self.base = base
        self.timeout = timeout
        self.retries = retries
        self.cj = http.cookiejar.CookieJar()
        self.opener = urllib.request.build_opener(
            urllib.request.HTTPCookieProcessor(self.cj))
        self.opener.addheaders = [("User-Agent", UA),
                                  ("Accept-Language", "ru,en;q=0.9")]

    # --- шаг 1: страница показателя
    def page(self, indicator_id):
        url = "%s/indicator/%s" % (self.base, indicator_id)
        last = None
        for attempt in range(1, self.retries + 1):
            try:
                with self.opener.open(url, timeout=self.timeout) as r:
                    return r.read().decode("utf-8", "replace")
            except (urllib.error.URLError, urllib.error.HTTPError) as e:
                last = e
                time.sleep(5 * attempt)
        raise RuntimeError("страница показателя %s недоступна: %r" % (indicator_id, last))

    @staticmethod
    def _csrf(html):
        m = re.search(r"id=['\"]downloadTokenHolder['\"](.{0,2000}?)</div>", html, re.S)
        if not m:
            return None, None
        holder = m.group(1)
        mn = re.search(r"name=['\"]struts\.token\.name['\"]\s+value=['\"]([^'\"]+)['\"]", holder)
        if not mn:
            return None, None
        name = mn.group(1)
        mt = re.search(r"name=['\"]%s['\"]\s+value=['\"]([^'\"]+)['\"]" % re.escape(name), holder)
        return name, (mt.group(1) if mt else None)

    def meta(self, indicator_id):
        """Структура показателя: поля фильтров, раскладка, токен."""
        html = self.page(indicator_id)
        filters = js_to_json(_slice_braced(html, "filters:"))
        name, token = self._csrf(html)
        return {
            "indicator_id": str(indicator_id),
            "filters": filters,
            "left": _arr_ints(html, "left_columns:"),
            "top": _arr_ints(html, "top_columns:"),
            "filter_object_ids": _arr_ints(html, "filterObjectIds:"),
            "token_name": name,
            "token": token,
        }

    # --- шаг 2: выбор значений
    @staticmethod
    def select(meta, wanted=None):
        """wanted: {название поля: [названия значений] | '*'}.

        Возвращает список пар (код поля, код значения) для selectedFilterIds.
        Если wanted пуст — берутся все значения всех полей. Одиночный ['*']
        трактуется так же, как '*'.

        Питфолл источника: сужение полей, стоящих в top_columns (обычно Год и
        Период), ЕМИСС не принимает — на такой запрос приходит HTML-страница
        вместо таблицы, а не ошибка. Сужение полей из left_columns (территория,
        товар, возраст) работает. Поэтому отбор по годам и периодам делается
        уже после загрузки, на стороне разбора.
        """
        f = meta["filters"]
        if wanted:
            known = {t.strip().lower() for t in
                     (field.get("title", "") for field in f.values())}
            unknown = [k for k in wanted
                       if k.strip().lower() not in known]
            if unknown:
                raise ValueError(
                    "поля не найдены в показателе: %s; доступные поля: %s"
                    % (unknown, sorted(field.get("title", "") for field in f.values())))
        out = []
        for fid, field in f.items():
            title = field.get("title", "")
            values = field.get("values", {}) or {}
            want = None
            if wanted:
                for k, v in wanted.items():
                    if k.strip().lower() == title.strip().lower():
                        want = v
                        break
            if want is None:
                out += [(fid, vid) for vid in values]
            elif want == "*" or (isinstance(want, (list, tuple)) and list(want) == ["*"]):
                out += [(fid, vid) for vid in values]
            else:
                titles = [w.strip().lower() for w in want]
                chosen = [(fid, vid) for vid, v in values.items()
                          if (v.get("title") or "").strip().lower() in titles]
                if not chosen:
                    raise ValueError("значения не найдены в поле «%s»: %s" % (title, want))
                out += chosen
        return out

    # --- шаг 3: загрузка
    def download(self, meta, selected, fmt="sdmx"):
        f = meta["filters"]
        ind_field = next((k for k, v in f.items() if v.get("indicator")), "0")
        ind_title = list(f[ind_field]["values"].values())[0].get("title", "")
        parts = [("title", ind_title),
                 ("struts.token.name", meta["token_name"] or ""),
                 (meta["token_name"] or "", meta["token"] or ""),
                 ("id", meta["indicator_id"])]
        parts += [("lineObjectIds", str(x)) for x in meta["left"]]
        parts += [("columnObjectIds", str(x)) for x in meta["top"]]
        parts += [("filterObjectIds", str(x)) for x in meta["filter_object_ids"]]
        parts += [("selectedFilterIds", "%s_%s" % (fid, vid)) for fid, vid in selected]
        body = urllib.parse.urlencode(parts).encode()
        url = "%s/indicator/downloadData.do?format=%s" % (self.base, fmt)
        req = urllib.request.Request(url, data=body, headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer": "%s/indicator/%s" % (self.base, meta["indicator_id"]),
            "Origin": self.base, "User-Agent": UA})
        with self.opener.open(req, timeout=max(self.timeout, 300)) as r:
            ctype = r.headers.get("Content-Type", "")
            blob = r.read()
        if fmt == "excel" and "ms-excel" not in ctype:
            raise RuntimeError("ЕМИСС вернул %s вместо таблицы; вероятно, пустая выборка" % ctype)
        if fmt == "sdmx" and "xml" not in ctype:
            raise RuntimeError("ЕМИСС вернул %s вместо xml; вероятно, пустая выборка" % ctype)
        return blob

    # --- шаг 4: разбор ответа
    @staticmethod
    def parse_sdmx(blob):
        """Из sdmx делает список словарей: одна строка на точку.

        Разбор идёт по локальным именам тегов без учёта пространств имён:
        в ответе ЕМИСС часть элементов (Series, Obs и другие) идёт вообще
        без namespace, поэтому поиск по полному имени с namespace не находит
        ни одного ряда. Это была первая ошибка разбора — учитывать её при
        правках.
        """
        def local(el):
            return el.tag.split("}")[-1]

        root = ET.fromstring(blob)
        # справочники: код -> название
        names = {}
        for el in root.iter():
            if local(el) != "Code":
                continue
            desc = next((c for c in el if local(c) == "Description"), None)
            names[str(el.attrib.get("value"))] = (desc.text or "").strip() if desc is not None else ""
        rows = []
        for el in root.iter():
            if local(el) != "Series":
                continue
            row = {}
            for child in el:
                tag = local(child)
                if tag == "SeriesKey":
                    for v in child:
                        if local(v) == "Value":
                            row[v.attrib.get("concept")] = v.attrib.get("value")
                elif tag == "Attributes":
                    for v in child:
                        if local(v) == "Value":
                            c = v.attrib.get("concept")
                            row[c] = v.attrib.get("value") or (v.text or "").strip()
                elif tag == "Obs":
                    t = next((x for x in child if local(x) == "Time"), None)
                    val = next((x for x in child if local(x) == "ObsValue"), None)
                    row["time"] = (t.text or "").strip() if t is not None else ""
                    raw = (val.attrib.get("value") if val is not None else "") or ""
                    row["value_raw"] = raw
                    try:
                        row["value"] = float(raw.replace(",", ".").replace(" ", ""))
                    except ValueError:
                        row["value"] = None
            if not row:
                continue
            for code_key in ("s_OKATO", "s_vozr"):
                if code_key in row:
                    row[code_key + "_name"] = names.get(str(row[code_key]), "")
            rows.append(row)
        return {"rows": rows, "names": names}

    def load(self, indicator_id, wanted=None, fmt="sdmx", retries=3, pause=20, save_raw=None):
        """Загрузка с повторами: токен одноразовый, сервер отдаёт 503 при нагрузке.

        Поэтому на каждой попытке берётся свежая страница (новый токен и сессия),
        а между попытками выдерживается пауза.
        """
        last = None
        for attempt in range(1, retries + 1):
            try:
                meta = self.meta(indicator_id)
                selected = self.select(meta, wanted)
                blob = self.download(meta, selected, fmt=fmt)
                if fmt == "sdmx":
                    if save_raw:
                        with open(save_raw, "wb") as fh:
                            fh.write(blob)
                    data = self.parse_sdmx(blob)
                    data.update({"meta": meta, "selected": selected,
                                 "bytes": len(blob), "attempts": attempt})
                    return data
                return {"blob": blob, "meta": meta, "selected": selected,
                        "bytes": len(blob), "attempts": attempt}
            except (urllib.error.HTTPError, urllib.error.URLError, RuntimeError) as e:
                last = e
                if attempt < retries:
                    time.sleep(pause)
        raise RuntimeError("загрузка показателя %s не удалась за %d попыток: %r"
                           % (indicator_id, retries, last))


# ---------------------------------------------------------------------- CLI

def _print_meta(meta):
    f = meta["filters"]
    print("показатель %s | полей фильтров: %d" % (meta["indicator_id"], len(f)))
    for fid, field in f.items():
        vals = field.get("values", {}) or {}
        print("  %-8s %-34s значений %4d %s" % (
            fid, (field.get("title") or "")[:34], len(vals),
            "индикатор" if field.get("indicator") else ""))
    print("  раскладка: line=%s column=%s filter=%s | токен: %s" % (
        meta["left"], meta["top"], meta["filter_object_ids"], "есть" if meta["token"] else "НЕТ"))


def main():
    ap = argparse.ArgumentParser(description="Загрузка данных ЕМИСС (fedstat.ru)")
    ap.add_argument("indicator_id")
    ap.add_argument("--list", action="store_true", help="показать поля фильтров и выйти")
    ap.add_argument("--filter", action="append", default=[],
                    help="отбор вида \"Поле=значение1,значение2\" или \"Поле=*\"")
    ap.add_argument("--format", default="sdmx", choices=["sdmx", "excel"])
    ap.add_argument("--out", default=None, help="куда записать csv")
    ap.add_argument("--limit", type=int, default=0, help="сколько строк напечатать")
    args = ap.parse_args()

    wanted = {}
    for flt in args.filter:
        if "=" not in flt:
            raise SystemExit("фильтр должен быть вида Поле=значение: %s" % flt)
        k, v = flt.split("=", 1)
        wanted[k.strip()] = "*" if v.strip() == "*" else [x for x in v.split(",")]

    e = Emiss()
    meta = e.meta(args.indicator_id)
    _print_meta(meta)
    if args.list:
        for fid, field in meta["filters"].items():
            print("\n[%s] %s" % (fid, field.get("title")))
            for vid, v in (field.get("values") or {}).items():
                print("   %-9s %s" % (vid, v.get("title")))
        return

    data = e.load(args.indicator_id, wanted=wanted, fmt=args.format)
    if args.format != "sdmx":
        with open(args.out or "/tmp/emiss_download.xls", "wb") as fh:
            fh.write(data["blob"])
        print("записано %d байт (excel)" % data["bytes"])
        return

    rows = data["rows"]
    print("\nвыбрано значений: %d | получено точек: %d | байт: %d"
          % (len(data["selected"]), len(rows), data["bytes"]))
    keys = sorted({k for r in rows for k in r if k not in ("value_raw",)})
    print("колонки:", keys)
    if args.out:
        with open(args.out, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=keys)
            w.writeheader()
            w.writerows(rows)
        print("записано:", args.out)
    shown = rows[:args.limit] if args.limit else rows[:12]
    for r in shown:
        print("   ", {k: r[k] for k in keys if k in r})


if __name__ == "__main__":
    main()