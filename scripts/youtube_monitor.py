#!/usr/bin/env python3
"""Регулярный обход YouTube-каналов через публичные RSS-фиды (без API-ключа и квоты).

Зачем: YouTube Data API v3 требует ключ формата AIza… (наш GCP_API_KEY — OAuth-токен,
Data API его не принимает), а RSS-фид канала отдаёт последние 15 видео с датами и
работает бесплатно и без лимитов. Для «что нового» этого достаточно.

Использование:
  python3 scripts/youtube_monitor.py                 # показать последние видео по всем каналам
  python3 scripts/youtube_monitor.py --new-only      # только то, чего нет в state-файле
  python3 scripts/youtube_monitor.py --stale-days 60 # плюс пометить каналы без публикаций N дней

Файлы: data/yt_channels.csv (name,channel_id,tier,comment), state — data/yt_state.json
"""
import argparse
import csv
import datetime
import json
import os
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHANNELS = os.path.join(ROOT, 'data', 'yt_channels.csv')
STATE = os.path.join(ROOT, 'data', 'yt_state.json')
FEED = 'https://www.youtube.com/feeds/videos.xml?channel_id={}'
NS = {'a': 'http://www.w3.org/2005/Atom', 'm': 'http://search.yahoo.com/mrss/'}


def load_channels():
    rows = []
    with open(CHANNELS, encoding='utf-8') as f:
        for r in csv.DictReader(f):
            if r.get('channel_id'):
                rows.append(r)
    return rows


def fetch_feed(channel_id, timeout=25):
    req = urllib.request.Request(FEED.format(channel_id),
                                 headers={'User-Agent': 'Mozilla/5.0 (hermes-research)'})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def parse_feed(xml_bytes):
    root = ET.fromstring(xml_bytes)
    out = []
    for e in root.findall('a:entry', NS):
        vid = (e.findtext('a:id', default='', namespaces=NS) or '').split(':')[-1]
        out.append({
            'video_id': vid,
            'title': e.findtext('a:title', default='', namespaces=NS).strip(),
            'published': (e.findtext('a:published', default='', namespaces=NS) or '')[:10],
        })
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--new-only', action='store_true')
    ap.add_argument('--stale-days', type=int, default=0)
    ap.add_argument('--limit', type=int, default=5)
    args = ap.parse_args()

    now = datetime.datetime.now(datetime.timezone.utc)
    state = json.load(open(STATE, encoding='utf-8')) if os.path.exists(STATE) else {}
    total_new = 0
    problems = []

    for ch in load_channels():
        try:
            entries = parse_feed(fetch_feed(ch['channel_id']))
        except Exception as e:
            problems.append(f"{ch['name']}: {type(e).__name__}")
            continue
        if not entries:
            problems.append(f"{ch['name']}: фид пуст")
            continue
        seen = set(state.get(ch['channel_id'], []))
        fresh = [e for e in entries if e['video_id'] not in seen]
        last = entries[0]['published']
        days = (now - datetime.datetime.fromisoformat(last + 'T00:00:00+00:00')).days
        if args.new_only and not fresh:
            continue
        head = f"{ch['name']} (тир {ch.get('tier', '?')}) — последняя {last}, {days} дн назад"
        if args.stale_days and days > args.stale_days:
            head += f"  [ПРОСРОЧЕН > {args.stale_days} дн]"
        print(head)
        for e in (fresh if args.new_only else entries)[:args.limit]:
            print(f"    {e['published']}  {e['title'][:88]}")
        total_new += len(fresh)
        state[ch['channel_id']] = [e['video_id'] for e in entries]

    if problems:
        print('\nпроблемы:', '; '.join(problems))
    if args.new_only:
        print(f'\nновых видео: {total_new}')
    json.dump(state, open(STATE, 'w', encoding='utf-8'), ensure_ascii=False)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())