#!/usr/bin/env python3
"""Докачка и загрузка регионального монитора Росстата (info-stat-MM-YYYY.zip).

Страница: https://rosstat.gov.ru/folder/11109 — «Информация для ведения
мониторинга социально-экономического положения субъектов РФ». Архив лежит по
шаблону https://rosstat.gov.ru/storage/mediabank/info-stat-MM-YYYY.zip
(проверено 29.10.2026: 09-2026 — 8,6 МБ, Last-Modified 28.10.2026 09:48 GMT;
08-2026 — 8,4 МБ, 06.10.2026; 07-2026 по шаблону отдаёт 404).

Логика: для текущего и двух предыдущих месяцев проверяем наличие архива; если
он новее уже распакованного — скачиваем, распаковываем и запускаем
`direct_rosstat_monitoring.py`. Когда нового нет, скрипт молчит и выходит с 0,
чтобы ежедневный прогон в окне публикации не давал ежедневный отчёт.

Запуск: APPLY=1 python3 scripts/rosstat_monitoring_files_update.py
"""
import os
import sys
import io
import zipfile
import datetime as dt

import requests
import urllib3

urllib3.disable_warnings()

BASE = 'https://rosstat.gov.ru/storage/mediabank/info-stat-%02d-%04d.zip'
HDRS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/120 Safari/537.36'}
ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    'raw', 'rosstat', 'monitoring')
MARKER = os.path.join(ROOT, '.last_release')


def fetch(url, path, timeout=180):
    """Скачивание с verify=False: CA-бандл VPS не проверяет цепочку Росстата."""
    r = requests.get(url, headers=HDRS, verify=False, timeout=timeout, stream=True)
    if r.status_code != 200:
        return None
    tmp = path + '.part'
    with open(tmp, 'wb') as f:
        for chunk in r.iter_content(1 << 16):
            f.write(chunk)
    os.replace(tmp, path)
    return r.headers.get('Last-Modified', '')


def candidates(today=None):
    today = today or dt.date.today()
    out = []
    y, m = today.year, today.month
    for _ in range(3):
        out.append((y, m))
        m -= 1
        if m == 0:
            y, m = y - 1, 12
    return out


def unpack(zpath, dest):
    with zipfile.ZipFile(zpath) as z:
        names = z.namelist()
        # имена внутри архива в cp866 — декодируем, иначе каталоги «кракозябры»
        for info in z.infolist():
            raw = info.filename
            try:
                name = raw.encode('cp437').decode('cp866')
            except (UnicodeEncodeError, UnicodeDecodeError):
                name = raw
            target = os.path.join(dest, name)
            if info.is_dir():
                os.makedirs(target, exist_ok=True)
                continue
            os.makedirs(os.path.dirname(target), exist_ok=True)
            with z.open(info) as src, open(target, 'wb') as dst:
                dst.write(src.read())
    return len(names)


def main():
    apply = os.environ.get('APPLY') == '1'
    os.makedirs(ROOT, exist_ok=True)
    last = ''
    if os.path.exists(MARKER):
        last = open(MARKER).read().strip()

    for y, m in candidates():
        url = BASE % (m, y)
        try:
            head = requests.get(url, headers=HDRS, verify=False, timeout=60,
                                stream=True)
        except requests.RequestException as e:
            print('сеть: %s (%s)' % (url, e), file=sys.stderr)
            return 1
        if head.status_code != 200:
            head.close()
            continue
        stamp = head.headers.get('Last-Modified', '')
        head.close()
        if stamp and stamp == last:
            return 0                     # новее ничего нет — молчим
        rel = '%04d-%02d' % (y, m)
        zpath = os.path.join(ROOT, 'info-stat-%s.zip' % rel)
        got = fetch(url, zpath)
        if got is None:
            continue
        dest = os.path.join(ROOT, 'rel-%s' % rel)
        n = unpack(zpath, dest)
        print('Росстат. Региональный монитор %s: архив %d файлов, %.1f МБ, '
              'опубликован %s' % (rel, n, os.path.getsize(zpath) / 1e6, got))
        if not apply:
            print('  dry-run: распаковано в %s, загрузка не запускалась' % dest)
            return 0
        rc = os.system('%s %s --dir %s' % (
            sys.executable,
            os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         'direct_rosstat_monitoring.py'), dest))
        if rc != 0:
            print('  загрузка вернула код %d' % rc, file=sys.stderr)
            return rc
        with open(MARKER, 'w') as f:
            f.write(got)
        return 0
    return 0


if __name__ == '__main__':
    sys.exit(main())
