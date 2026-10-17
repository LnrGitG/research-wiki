#!/usr/bin/env python3
"""Слушатель изменений наблюдений: обновляет витрину свежести при вставке данных.

Слушает канал `observation_changed`, который поднимает триггер
`trg_observation_change` на data.observation (statement-level, FOR EACH
STATEMENT — одно уведомление на команду, а не на строку). На уведомление
выполняет REFRESH MATERIALIZED VIEW CONCURRENTLY derived.v_metric_card.

Драйвер — psycopg 3 (его возвращает db_tunnel.connect). У соединения psycopg3
нет метода poll(), поэтому ожидание уведомлений идёт через генератор
conn.notifies(timeout=...); при обрыве связи цикл переподключается.

Оговорка: pg_notify не переживает разрыв связи — уведомления, отправленные
пока слушатель отключён, теряются. Поэтому при каждом подключении витрина
обновляется сразу, а в дополнение к слушателю идёт страховочное периодическое
обновление прямо в этом цикле (PERIODIC_REFRESH секунд), а не заданием
pg_cron: расширения pg_cron на сервере нет, и расчёт на него был ошибкой
(исправлено 17.10.2026).

Исправление 17.10.2026: обновлялся объект `derived.metric_card`, но это
таблица семантических карточек, а не материализованное представление;
представление называется `derived.v_metric_card`. До правки каждое
подключение писало в журнал «"metric_card" is not a materialized view»,
витрину обновлял только ингест, и доска свежести могла показывать «свежие»
по ряду, которого в data.observation уже нет.
"""
import sys
import time

sys.path.insert(0, "/home/lnr/research-wiki-private")
from scripts import db_tunnel  # noqa: E402

CHANNEL = "observation_changed"
REFRESH = "REFRESH MATERIALIZED VIEW CONCURRENTLY derived.v_metric_card"
RECONNECT_DELAY = 10
WAIT_SECONDS = 30
PERIODIC_REFRESH = 600       # страховка: полный пересчёт раз в 10 минут
                             # (замер 17.10.2026: 1,9 с на 17 077 карточек)


def log(msg):
    print(f"[listener] {time.strftime('%Y-%m-%d %H:%M:%S')} {msg}", flush=True)


def refresh(cur, why):
    try:
        t0 = time.monotonic()
        cur.execute(REFRESH)
        log(f"витрина обновлена ({why}, {time.monotonic() - t0:.1f} с)")
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
    refresh(cur, "подключение")
    last_refresh = time.monotonic()

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
            refresh(cur, "уведомление")
            last_refresh = time.monotonic()
        elif time.monotonic() - last_refresh >= PERIODIC_REFRESH:
            # страховка на случай потерянных уведомлений
            refresh(cur, "периодическая")
            last_refresh = time.monotonic()


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
