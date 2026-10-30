#!/usr/bin/env python3
"""Резидентный канал: HTTP-прокси на ноутбуке, доступный только на VPS.

Зачем. Часть источников закрыта для датацентр-IP: `api.hh.ru` отдаёт 403 и с
VPS, и с ВМ; `fedstat.ru` (ЕМИСС) — тоже. Проверять такие ряды можно только
через канал с резидентным адресом. Ноутбук владельца (Уфанет) годится, но у него
нет публичного адреса, поэтому порядок обратный обычному: прокси слушает
127.0.0.1 на ноутбуке, а SSH-соединение *с ноутбука на VPS* пробрасывает этот
порт назад (`ssh -N -R 127.0.0.1:18080:127.0.0.1:18080 vps`). На VPS прокси
виден как `127.0.0.1:18080` и недоступен снаружи — снаружи его нет вовсе.

Ограничения сделаны намеренно:
  * bind только 127.0.0.1 (обратный проброс по умолчанию тоже loopback);
  * allowlist хостов — прокси не станет открытым релеем, если порт всё же
    окажется доступен кому-то ещё;
  * токен в `Proxy-Authorization` (Basic), сравнение постоянного времени;
  * заготовка под `--once N`: прокси сам завершится после N запросов, чтобы
    забытый канал не жил сутками.

Запуск на ноутбуке (WSL или любой Linux/macOS с python3):

    python3 resident_proxy.py --token <TOKEN> --port 18080

Проверка с VPS:

    curl -x http://127.0.0.1:18080 -U <TOKEN>: https://api.hh.ru/vacancies?text=test

Скрипт ничего не пишет на диск и не требует зависимостей — только stdlib.
"""
import argparse
import base64
import hmac
import select
import socket
import socketserver
import sys
import threading
import time

DEFAULT_ALLOW = (
    'api.hh.ru',
    'hh.ru',
    'fedstat.ru',
    'www.fedstat.ru',
    'rosstat.gov.ru',
    'дом.рф',
    'xn--d1aqf.xn--p1ai',
    'наш.дом.рф',
    'roschart.ru',
    'www.roschart.ru',
    'cbr.ru',
    'www.cbr.ru',
    'ipinfo.io',
    'ifconfig.me',
    'api.ipify.org',
)

BUF = 65536


def host_allowed(host, allow):
    host = host.lower().strip('.')
    for a in allow:
        a = a.lower().strip('.')
        if host == a or host.endswith('.' + a):
            return True
    return False


def split_hostport(netloc, default_port):
    if netloc.startswith('['):                       # [::1]:443
        host, _, rest = netloc[1:].partition(']')
        port = int(rest.lstrip(':') or default_port)
        return host, port
    if ':' in netloc:
        host, _, p = netloc.rpartition(':')
        return host, int(p or default_port)
    return netloc, default_port


def pump(a, b):
    try:
        while True:
            r, _, _ = select.select([a, b], [], [], 300)
            if not r:
                return
            for s in r:
                data = s.recv(BUF)
                if not data:
                    return
                (b if s is a else a).sendall(data)
    except OSError:
        return


class Handler(socketserver.StreamRequestHandler):
    timeout = 300
    server_version = 'resident/1.0'

    def log(self, msg):
        sys.stderr.write(f'[{time.strftime("%H:%M:%S")}] {msg}\n')
        sys.stderr.flush()

    def _authorized(self, headers):
        tok = self.server.token
        if not tok:
            return True
        got = ''
        for line in headers:
            if line.lower().startswith('proxy-authorization:'):
                raw = line.split(':', 1)[1].strip()
                if raw.lower().startswith('basic '):
                    try:
                        dec = base64.b64decode(raw[6:].strip()).decode('utf-8', 'ignore')
                        got = dec.split(':', 1)[0]
                    except Exception:
                        got = ''
        return hmac.compare_digest(got, tok)

    def handle(self):
        try:
            request_line = self.rfile.readline(65536).decode('latin-1').strip()
        except OSError:
            return
        if not request_line:
            return
        parts = request_line.split()
        if len(parts) < 3:
            return
        method, target, _version = parts[0], parts[1], parts[2]

        headers = []
        while True:
            line = self.rfile.readline(65536).decode('latin-1')
            if line in ('\r\n', '\n', ''):
                break
            headers.append(line.strip())

        if not self._authorized(headers):
            self.wfile.write(b'HTTP/1.1 407 Proxy Authentication Required\r\n'
                             b'Proxy-Authenticate: Basic realm="resident"\r\n'
                             b'Content-Length: 0\r\n\r\n')
            self.log('407 ' + target)
            return

        if method.upper() == 'CONNECT':
            host, port = split_hostport(target, 443)
            if not host_allowed(host, self.server.allow):
                self.wfile.write(b'HTTP/1.1 403 Forbidden\r\nContent-Length: 0\r\n\r\n')
                self.log('403 (allowlist) ' + host)
                return
            try:
                upstream = socket.create_connection((host, port), timeout=20)
            except OSError as exc:
                self.wfile.write(b'HTTP/1.1 502 Bad Gateway\r\nContent-Length: 0\r\n\r\n')
                self.log(f'502 {host}:{port} {exc}')
                return
            self.wfile.write(b'HTTP/1.1 200 Connection established\r\n\r\n')
            self.wfile.flush()
            self.log(f'CONNECT {host}:{port}')
            with upstream:
                self.server.count_request()
                pump(self.connection, upstream)
            return

        # обычный HTTP без CONNECT: цель — абсолютный URL
        if not target.lower().startswith('http://'):
            self.wfile.write(b'HTTP/1.1 400 Bad Request\r\nContent-Length: 0\r\n\r\n')
            return
        rest = target[7:]
        netloc, _, path = rest.partition('/')
        host, port = split_hostport(netloc, 80)
        if not host_allowed(host, self.server.allow):
            self.wfile.write(b'HTTP/1.1 403 Forbidden\r\nContent-Length: 0\r\n\r\n')
            self.log('403 (allowlist) ' + host)
            return
        try:
            upstream = socket.create_connection((host, port), timeout=20)
        except OSError as exc:
            self.wfile.write(b'HTTP/1.1 502 Bad Gateway\r\nContent-Length: 0\r\n\r\n')
            self.log(f'502 {host}:{port} {exc}')
            return
        keep = [h for h in headers
                if not h.lower().startswith(('proxy-authorization:', 'proxy-connection:'))]
        req = f'{method} /{path} HTTP/1.1\r\n' + '\r\n'.join(keep) + '\r\n\r\n'
        self.log(f'{method} {host}/{path[:40]}')
        self.server.count_request()
        with upstream:
            upstream.sendall(req.encode('latin-1'))
            pump(self.connection, upstream)


class Proxy(socketserver.ThreadingTCPServer):
    daemon_threads = True
    allow_reuse_address = True

    def __init__(self, addr, handler, token='', allow=DEFAULT_ALLOW, once=0):
        super().__init__(addr, handler)
        self.token = token
        self.allow = tuple(allow)
        self.once = once
        self.n = 0
        self._lock = threading.Lock()

    def count_request(self):
        if not self.once:
            return
        with self._lock:
            self.n += 1
            if self.n >= self.once:
                threading.Thread(target=self._shutdown_later, daemon=True).start()

    def _shutdown_later(self):
        time.sleep(2)
        self.shutdown()


def main():
    ap = argparse.ArgumentParser(description='HTTP-прокси для резидентного канала')
    ap.add_argument('--host', default='127.0.0.1')
    ap.add_argument('--port', type=int, default=18080)
    ap.add_argument('--token', default='')
    ap.add_argument('--allow', nargs='*', default=list(DEFAULT_ALLOW))
    ap.add_argument('--once', type=int, default=0,
                    help='завершиться после N запросов (0 — работать до остановки)')
    args = ap.parse_args()

    srv = Proxy((args.host, args.port), Handler, token=args.token,
                allow=args.allow, once=args.once)
    sys.stderr.write(f'resident proxy на {args.host}:{args.port}, '
                     f'хостов в allowlist: {len(args.allow)}, токен: '
                     f'{"есть" if args.token else "нет (только loopback)"}\n')
    sys.stderr.flush()
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        srv.server_close()


if __name__ == '__main__':
    main()
