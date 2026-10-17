#!/usr/bin/env python3
"""Проверка триггера уведомлений: поднимается ли канал observation_changed.

Тест не меняет канон: выполняется `UPDATE ... WHERE false` — statement-level
триггер срабатывает, ни одна строка не затронута. Уведомление приходит на
соединение, которое слушает канал.

Запуск: ~/.hermes/hermes-agent/venv/bin/python3 scripts/test_observation_trigger.py
"""
import sys
import time

sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import connect  # noqa: E402

CHANNEL = "observation_changed"

# 1. Предохранитель: триггер существует и statement-level
c0 = connect()
c0.autocommit = True
cur0 = c0.cursor()
cur0.execute("""
    SELECT t.tgname, t.tgtype::int & 1 AS row_level, pg_get_triggerdef(t.oid)
    FROM pg_trigger t
    WHERE t.tgrelid = 'data.observation'::regclass AND NOT t.tgisinternal
""")
trigs = cur0.fetchall()
print("Триггеры на data.observation:", len(trigs))
for name, row_level, ddl in trigs:
    print(f"  {name}: row_level={bool(row_level)}")
    print(f"    {ddl}")

# 2. Слушаем канал
listener = connect()
listener.autocommit = True
lcur = listener.cursor()
lcur.execute(f"LISTEN {CHANNEL};")
print(f"Слушаю {CHANNEL}...")

# 3. Пустая команда: срабатывает триггер, строки не меняются
writer = connect()
writer.autocommit = True
wcur = writer.cursor()
wcur.execute("UPDATE data.observation SET notes = notes WHERE false")
wcur.execute("SELECT count(*) FROM data.observation")
print("Строк в data.observation после пустой команды:", wcur.fetchone()[0])

# 4. Ждём уведомление
got = []
deadline = time.monotonic() + 10
for n in listener.notifies(timeout=8):
    got.append((n.channel, n.payload))
    if time.monotonic() > deadline:
        break
print("Получено уведомлений:", len(got), got)

for c in (c0, listener, writer):
    try:
        c.close()
    except Exception:
        pass

sys.exit(0 if got else 1)
