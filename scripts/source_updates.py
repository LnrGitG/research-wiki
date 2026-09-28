#!/usr/bin/env python3
"""Планировщик обновления источников: что просрочено и что обновилось.

Читает реестр data/source_updates.yaml, состояние авто-джобов — из ~/.hermes/cron/jobs.json,
и считает по каждой позиции: ожидаемую дату следующего обновления, фактическую дату последнего
успешного прогона и просрочку.

Запуск:
  python3 scripts/source_updates.py                 # статус всех позиций
  python3 scripts/source_updates.py --due           # только просроченные
  python3 scripts/source_updates.py --coverage      # покрытие реестра источников владельца
  python3 scripts/source_updates.py --run <code>    # показать команду обновления (без запуска)

Скрипт ничего не запускает сам: сначала реестр должен быть проверен владельцем.
"""
import argparse
import csv
import datetime as dt
import json
import os
import re
import sys

import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGISTRY = os.path.join(REPO, 'data', 'source_updates.yaml')
JOBS = os.path.expanduser('~/.hermes/cron/jobs.json')
USER_REGISTRY = os.path.join(REPO, 'data', 'sources_registry_user.csv')

CADENCE_DAYS = {'daily': 1, 'weekly': 7, 'monthly': 30, 'quarterly': 91, 'annual': 365}


def load_registry():
    with open(REGISTRY, encoding='utf-8') as f:
        return yaml.safe_load(f)


def load_jobs():
    if not os.path.exists(JOBS):
        return {}
    d = json.load(open(JOBS, encoding='utf-8'))
    jobs = d if isinstance(d, list) else d.get('jobs', d)
    if isinstance(jobs, dict):
        jobs = list(jobs.values())
    return {j.get('id'): j for j in jobs}


def parse_date(s):
    if not s:
        return None
    m = re.match(r'^(\d{4})-(\d{2})-(\d{2})', str(s))
    return dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3))) if m else None


def status_of(entry, jobs, today):
    """(последняя дата, источник даты, дней просрочки, состояние)."""
    last = parse_date(entry.get('last_ok'))
    origin = 'реестр'
    jid = entry.get('cron_job_id')
    job = jobs.get(jid) if jid else None
    if job and job.get('last_run_at'):
        d = parse_date(job['last_run_at'])
        if d and (last is None or d > last):
            last, origin = d, f"джоб {jid}"
        if job.get('last_status') not in (None, 'ok'):
            return last, origin, None, f"ошибка прогона ({job.get('last_status')})"
    cad = CADENCE_DAYS.get(entry.get('cadence'), 30)
    if last is None:
        return None, '—', None, 'нет данных о прогоне'
    overdue = (today - last).days - cad
    state = 'ок' if overdue <= 3 else ('просрочка' if overdue > 0 else 'ок')
    return last, origin, max(overdue, 0), state


def cmd_status(entries, jobs, today, due_only=False):
    rows = []
    for e in entries:
        last, origin, over, state = status_of(e, jobs, today)
        due = over is not None and over > 3
        rows.append((due, over or 0, e, last, origin, state))
        if due_only and not due:
            continue
        last_s = last.isoformat() if last else '—'
        over_s = f'{over} дн' if (over is not None and over > 0) else '—'
        print(f"  {e['code']:24} {e.get('kind','?'):7} {e.get('cadence','?'):9} последнее {last_s:10} "
              f"просрочка {over_s:7} {state}")
    n_due = sum(1 for r in rows if r[0])
    print(f'\nпозиций: {len(rows)}, просрочено: {n_due}')
    return n_due


def cmd_coverage(today):
    """Насколько реестр обновлений покрывает пользовательский реестр источников."""
    if not os.path.exists(USER_REGISTRY):
        print('реестр источников владельца не найден:', USER_REGISTRY)
        return
    rows = list(csv.DictReader(open(USER_REGISTRY, encoding='utf-8')))
    monthly = [r for r in rows if (r.get('freq') or '').strip().lower().startswith('ежемес')]
    reg = load_registry()['sources']
    covered_kw = {
        'cbr': ['банк россии', 'цб'],
        'rosstat_operational': ['росстат'],
        'fns_1nom': ['фнс'],
        'domrf_price_index': ['дом.рф', 'дом рф'],
        'emiss_regional_batch': ['емисс', 'fedstat'],
    }
    covered, uncovered = [], []
    for r in monthly:
        src = (r.get('source') or '').lower()
        hit = None
        for code, kws in covered_kw.items():
            if any(k in src for k in kws) and any(e['code'] == code for e in reg):
                hit = code
                break
        (covered if hit else uncovered).append((r.get('indicator', '')[:60], r.get('source', ''), hit))
    print(f'ежемесячных позиций в реестре владельца: {len(monthly)}')
    print(f'  с зарегистрированным обновлением: {len(covered)}')
    print(f'  без обновления: {len(uncovered)}')
    print('\nпозиции без механизма обновления (первые 20):')
    for ind, src, _ in uncovered[:20]:
        print(f'    {ind:62} [{src}]')
    print(f'\nреестр обновлений содержит записей: {len(reg)}')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--due', action='store_true', help='только просроченные позиции')
    ap.add_argument('--coverage', action='store_true', help='сопоставление с реестром источников владельца')
    ap.add_argument('--run', metavar='CODE', help='показать команду обновления позиции')
    args = ap.parse_args()

    today = dt.date.today()
    reg = load_registry()
    entries = reg['sources']
    jobs = load_jobs()

    if args.coverage:
        cmd_coverage(today)
        return 0
    if args.run:
        e = next((x for x in entries if x['code'] == args.run), None)
        if not e:
            print('нет такой позиции:', args.run)
            return 1
        print(f"{e['code']}: {e['title']}")
        print(f"  тип: {e.get('kind')} | периодичность: {e.get('cadence')} | скрипт: {e.get('script')}")
        if e.get('cron_job_id'):
            print(f"  джоб: {e['cron_job_id']} ({e.get('cron')})")
        if e.get('url'):
            print(f"  источник: {e['url']}")
        if e.get('notes'):
            print(f"  заметка: {e['notes']}")
        return 0

    print(f"реестр обновлений на {reg.get('updated')} (сегодня {today}), позиций {len(entries)}\n")
    return 1 if cmd_status(entries, jobs, today, due_only=args.due) else 0


if __name__ == '__main__':
    raise SystemExit(main())