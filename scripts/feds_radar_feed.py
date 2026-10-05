#!/usr/bin/env python3
"""Предзагрузка свежих выпусков FEDS для недельного радара (research-radar-weekly).

Читает RSS-ленту рабочих документов ФРС (Finance and Economics Discussion
Series) и печатает выпуски за последние N дней в компактном виде — это
конкретная точка входа в канал Federal Reserve FEDS, добавленный в обход
источников 04.10.2026. Вывод попадает в промпт cron-джоба как контекст,
поэтому печатается только релевантное: заголовок, дата, ссылка, краткая
выжимка из description.

Запуск:  python3 feds_radar_feed.py [--days 14] [--max 40]
Ошибки сети не роняют джоб: печатается одна строка-предупреждение.
"""
from __future__ import annotations

import argparse
import html
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime

FEED_URL = "https://www.federalreserve.gov/feeds/feds.xml"
UA = "Mozilla/5.0 (compatible; research-radar/1.0)"


def strip_html(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text or "")
    text = html.unescape(text)
    text = text.replace("\xa0", " ")
    return re.sub(r"\s+", " ", text).strip()


def fetch(url: str = FEED_URL) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read()


def parse_items(raw: bytes) -> list[dict]:
    root = ET.fromstring(raw)
    items = []
    for it in root.iter("item"):
        def g(tag: str) -> str:
            el = it.find(tag)
            return (el.text or "").strip() if el is not None else ""
        title = strip_html(g("title"))
        link = g("link")
        pub = g("pubDate")
        desc = strip_html(g("description"))
        try:
            when = parsedate_to_datetime(pub)
            if when.tzinfo is None:
                when = when.replace(tzinfo=timezone.utc)
        except Exception:
            when = None
        items.append({"title": title, "link": link, "desc": desc, "when": when, "pub": pub})
    return items


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=14, help="окно свежести, дней")
    ap.add_argument("--max", type=int, default=40, help="максимум строк")
    ap.add_argument("--url", default=FEED_URL)
    args = ap.parse_args()

    try:
        raw = fetch(args.url)
    except Exception as exc:  # сеть недоступна — не роняем джоб
        print(f"[feds_radar_feed] лента недоступна: {type(exc).__name__}: {exc}")
        return 0

    try:
        items = parse_items(raw)
    except Exception as exc:
        print(f"[feds_radar_feed] лента не разобрана: {type(exc).__name__}: {exc}")
        return 0

    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(days=args.days)
    fresh = [i for i in items if i["when"] and i["when"] >= cutoff]

    if not fresh:
        print(
            f"[feds_radar_feed] новых выпусков FEDS за {args.days} дн. нет "
            f"(в ленте {len(items)} записей; последняя {items[0]['when'].date() if items and items[0]['when'] else '—'})"
        )
        return 0

    fresh.sort(key=lambda i: i["when"], reverse=True)
    print(f"[feds_radar_feed] свежих выпусков FEDS за {args.days} дн.: {len(fresh)}")
    for i in fresh[: args.max]:
        desc = i["desc"]
        if len(desc) > 300:
            desc = desc[:297].rstrip() + "..."
        print(f"- {i['when'].date()} | {i['title']}")
        print(f"  {i['link']}")
        if desc:
            print(f"  {desc}")
    return 0


if __name__ == "__main__":
    sys.exit(main())