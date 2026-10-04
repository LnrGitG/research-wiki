#!/usr/bin/env python3
"""Проверка логики очереди: постановка, захват, закрытие, повтор."""
import sys
sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import execute, query

ep = query("SELECT endpoint_id, url FROM catalog.source_endpoint ORDER BY endpoint_id LIMIT 1")
ep_id, url = ep[0][0], ep[0][1]
print(f"точка: {ep_id} {url}")

print("\n1. постановка новой версии")
q1 = query("SELECT ops.enqueue_release(%s, 'test-hash-aaa', '2026-10-04', %s) AS q",
           (ep_id, url))
print("   первая постановка ->", q1[0][0], "(ожидается номер задачи)")

print("\n2. повтор той же версии (должен быть отказ)")
q2 = query("SELECT ops.enqueue_release(%s, 'test-hash-aaa', '2026-10-04', %s) AS q",
           (ep_id, url))
print("   повтор ->", q2[0][0], "(ожидается None: версия уже видна)")

print("\n3. другая версия (новая задача)")
q3 = query("SELECT ops.enqueue_release(%s, 'test-hash-bbb', '2026-10-05', %s) AS q",
           (ep_id, url))
print("   новая версия ->", q3[0][0])

print("\n4. захват пачки")
claimed = query("SELECT queue_id, endpoint_id, parser_script, attempts FROM ops.claim_ingest(5)")
for c in claimed:
    print("   взято:", c)

print("\n5. захват повторно (очередь уже пуста от pending)")
print("   взято:", len(query("SELECT * FROM ops.claim_ingest(5)")))

print("\n6. закрытие задач")
for c in claimed:
    execute("SELECT ops.finish_ingest(%s, 'done', 123, 0, NULL, 'тестовый прогон')", (c[0],))
print("   закрыто:", len(claimed))

print("\n7. журнал прогонов")
for r in query("SELECT run_id, queue_id, status, rows_written, exit_code "
               "FROM ops.ingest_run ORDER BY run_id DESC LIMIT 4"):
    print("  ", r)

print("\n8. витрина очереди")
for r in query("SELECT source_code, в_очереди, разобрано, сбоев, последний_разбор "
               "FROM ops.v_ingest_board WHERE разобрано > 0"):
    print("  ", r)

print("\n9. уборка тестовых записей")
execute("DELETE FROM ops.ingest_run WHERE output_tail = 'тестовый прогон'")
execute("DELETE FROM ops.ingest_queue WHERE content_hash LIKE 'test-hash-%'")
execute("DELETE FROM ops.release_seen WHERE content_hash LIKE 'test-hash-%'")
print("   очередь:", query("SELECT count(*) FROM ops.ingest_queue")[0][0],
      "| релизов:", query("SELECT count(*) FROM ops.release_seen")[0][0],
      "| прогонов:", query("SELECT count(*) FROM ops.ingest_run")[0][0])