#!/usr/bin/env python3
"""Слушатель изменений наблюдений: обновляет витрину при вставке данных.

Слушает канал `observation_changed`, который поднимает триггер
`trg_observation_change` на data.observation. На уведомление выполняет
REFRESH MATERIALIZED VIEW CONCURRENTLY derived.metric_card.

Драйвер — psycopg 3 (его возвращает db_tunnel.connect). У соединения psycopg3
нет метода poll(), поэтому ожидание уведомлений идёт через генератор
conn.notifies(timeout=...); при обрыве связи цикл переподключается.

Оговорка: pg_notify не переживает разрыв связи — уведомления, отправленные
пока слушатель отключён, теряются. Поэтому при каждом подключении витрина
обновляется сразу, а в дополнение к слушателю ставится страховочное
периодическое обновление заданием pg_cron.
"""
import sys
import time

sys.path.insert(0, "/home/lnr/research-wiki-private")
from scripts import db_tunnel  # noqa: E402

CHANNEL = "observation_changed"
REFRESH = "REFRESH MATERIALIZED VIEW CONCURRENTLY derived.metric_card"
RECONNECT_DELAY = 10
WAIT_SECONDS = 30


def log(msg):
    print(f"[listener] {time.strftime('%Y-%m-%d %H:%M:%S')} {msg}", flush=True)


def refresh(cur):
    try:
        cur.execute(REFRESH)
        log("витрина обновлена")
    except Exception as e:
        log(f"ошибка обновления витрины: {str(e)[:200]}")


def run_once():
    conn = db_tunnel.connect()
    conn.autocommit = True          # нужно для LISTEN
    cur = conn.cursor()
    cur.execute(f"LISTEN {CHANNEL};")
    log(f"подключён, слушаю канал {CHANNEL}")

    # при подключении обновляем сразу: пока слушателя не было, уведомления
    # могли потеряться
    refresh(cur)

    while True:
        got = False
        try:
            # генератор отдаёт уведомления; по истечении таймаута завершается
            for n in conn.notifies(timeout=WAIT_SECONDS):
                log(f"уведомление: {n.payload}")
                got = True
        except Exception as e:
            log(f"связь потеряна: {str(e)[:150]}")
            try:
                conn.close()
            except Exception:
                pass
            return
        if got:
            refresh(cur)


def main():
    while True:
        try:
            run_once()
        except Exception as e:
            log(f"не удалось подключиться: {str(e)[:200]}")
        time.sleep(RECONNECT_DELAY)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log("остановлен")
        sys.exit(0)