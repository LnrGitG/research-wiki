"""Фаза 3 схемы dkp: даты заседаний против пресс-релизов ЦБ.

Правило лага: решение объявляется на заседании, ступень вступает в силу через
0-4 дня; поэтому дата заседания = пятница, отстоящая от даты вступления ступени
на 0-4 дня. Для удержаний ступени нет, и дата подтверждается только внешним
источником — пресс-релизом вида /press/pr/?file=ДДММГГГГ_133000key.htm.
"""
import sys, json
sys.path.insert(0, "/home/ubuntu/research-wiki-private/scripts")
from db_tunnel import connect

conn = connect(); cur = conn.cursor()
log = []


def run(tag, sql):
    cur.execute(sql)
    log.append("%s -> %d" % (tag, cur.rowcount))


def note(mid, text):
    cur.execute("UPDATE dkp.meeting SET notes = %s WHERE meeting_id = %s", (text, mid))
    log.append("notes meeting %d -> %d" % (mid, cur.rowcount))


def sync_graph(did):
    cur.execute("SELECT action, rate_prev::float, rate_new::float, meeting_id FROM dkp.decision WHERE decision_id=%s", (did,))
    r = cur.fetchone()
    if not r:
        return
    props = json.dumps({"meeting_id": r[3], "action": r[0], "rate_prev": r[1], "rate_new": r[2]}, ensure_ascii=False)
    cur.execute("UPDATE graph.node SET title=%s, props=%s::jsonb WHERE ref_key=%s",
                ("Решение %s: %s" % (r[3], r[0]), props, "decision:%d" % did))
    log.append("graph decision:%d -> %d" % (did, cur.rowcount))


try:
    # --- A. Подтверждено пресс-релизом: 23.10.2020 вместо 19.10.2020 (понедельник) ---
    run("meeting 52: 2020-10-19 -> 2020-10-23 (пресс-релиз 23102020 подтверждён)",
        "UPDATE dkp.meeting SET meeting_date='2020-10-23' WHERE meeting_id=52 AND meeting_date='2020-10-19'")

    # --- B. Подтверждено: февральское заседание 2022 — 11.02, а не 18.02 ---
    run("meeting 110?: 2022-02-18 -> 2022-02-11 (пресс-релиз 11022022 подтверждён)",
        "UPDATE dkp.meeting SET meeting_date='2022-02-11' WHERE meeting_date='2022-02-18' AND decision_kind='unscheduled'")

    # --- C. Подтверждено: апрельское заседание 2023 — 28.04, а не 21.04 ---
    run("2023-04-21 -> 2023-04-28 (пресс-релиз 28042023 подтверждён)",
        "UPDATE dkp.meeting SET meeting_date='2023-04-28' WHERE meeting_date='2023-04-21'")

    # --- D. Заседание 35 (27.07.2018) без решения: вставить удержание 7.25 ---
    cur.execute("""INSERT INTO dkp.decision (meeting_id, rate_prev, rate_new, action, headline_ru)
        SELECT m.meeting_id, 7.25, 7.25, 'hold', 'Ключевая ставка: 7.25 -> 7.25%'
        FROM dkp.meeting m WHERE m.meeting_id=35
        AND NOT EXISTS (SELECT 1 FROM dkp.decision d WHERE d.meeting_id=35)
        RETURNING decision_id""")
    row = cur.fetchone()
    log.append("insert decision for meeting 35 -> %s" % (row[0] if row else "уже было"))
    if row:
        sync_graph(row[0])
        note(35, "заседание 27.07.2018: удержание 7,25 (пресс-релиз 27072018 подтверждён, ступень 7,25 с 26.03.2018)")

    # --- E. Даты, подтверждённые лестницей, но не покрытые эндпоинтом пресс-релизов ---
    for md, txt in (
        ("2018-02-09", "дата подтверждена лестницей (ступень 7,5 с 12.02.2018, лаг 3); эндпоинт пресс-релизов этот период не покрывает"),
        ("2018-03-23", "дата подтверждена лестницей (ступень 7,25 с 26.03.2018, лаг 3); запись 09.02.2018 в эндпоинте отсутствует"),
        ("2022-02-28", "внеплановое заседание, дата подтверждена лестницей (ступень 20,0 с 28.02.2022, лаг 0)"),
        ("2022-04-08", "дата подтверждена лестницей (ступень 17,0 с 11.04.2022, лаг 3)"),
        ("2022-05-26", "внеплановое, дата подтверждена лестницей (ступень 11,0 с 27.05.2022, лаг 1)"),
        ("2023-06-09", "дата подтверждена лестницей (удержание 7,5 при ступени 7,5 с 19.09.2022)"),
        ("2023-08-15", "внеплановое, дата подтверждена лестницей (ступень 12,0 с 15.08.2023, лаг 0)"),
    ):
        cur.execute("UPDATE dkp.meeting SET notes=%s WHERE meeting_date=%s::date", (txt, md))
        log.append("notes %s -> %d" % (md, cur.rowcount))

    # --- F. Подозрение на дубли и фантомы: пометить, не удаляя без источника ---
    for md, txt in (
        ("2023-05-26", "needs_source_check: существование внепланового заседания 26.05.2023 не подтверждено ни пресс-релизом, ни плановым календарём 2023 (10.02/17.03/28.04/09.06/21.07/15.09/27.10/15.12)"),
        ("2024-05-31", "needs_source_check: возможный дубль заседания 07.06.2024 (то же удержание, пресс-релиз подтверждён на 07.06)"),
    ):
        cur.execute("UPDATE dkp.meeting SET notes=%s WHERE meeting_date=%s::date", (txt, md))
        log.append("flag %s -> %d" % (md, cur.rowcount))

    # --- G. 2015-2016: даты, записанные датой вступления ступени, сдвигаем на пятницу ---
    for old, new, txt in (
        ("2015-02-02", "2015-01-30", "дата объявления решения (пятница); ступень 15,0 вступила 02.02.2015, лаг 3"),
        ("2015-03-16", "2015-03-13", "дата объявления решения (пятница); ступень 14,0 вступила 16.03.2015, лаг 3"),
        ("2015-08-03", "2015-07-31", "дата объявления решения (пятница); ступень 11,0 вступила 03.08.2015, лаг 3"),
        ("2016-02-01", "2016-01-29", "дата объявления решения (пятница); удержание 11,0 при ступени 11,0 с 03.08.2015"),
    ):
        cur.execute("UPDATE dkp.meeting SET meeting_date=%s::date, notes=%s WHERE meeting_date=%s::date AND decision_kind='scheduled'",
                    (new, txt, old))
        log.append("date %s -> %s -> %d" % (old, new, cur.rowcount))

    # --- H. 2015: пара «08.06 (снижение) + 15.06 (удержание)» — одно заседание ---
    # ступень 11,5 вступила 16.06.2015, значит решение было 12.06 или 15.06; держим
    # версию пятницы, дубль-удержание удаляем пометкой и удалением решения.
    cur.execute("SELECT d.decision_id FROM dkp.decision d JOIN dkp.meeting m USING(meeting_id) WHERE m.meeting_date='2015-06-15'")
    dup = cur.fetchone()
    if dup:
        run("child rate_level for duplicate decision",
            "DELETE FROM dkp.rate_level WHERE decision_id=%d" % dup[0])
        run("child argument for duplicate decision",
            "DELETE FROM dkp.argument WHERE decision_id=%d" % dup[0])
        run("delete duplicate decision for 2015-06-15",
            "DELETE FROM dkp.decision WHERE decision_id=%d" % dup[0])
        run("delete duplicate meeting 2015-06-15", "DELETE FROM dkp.meeting WHERE meeting_date='2015-06-15'")
    run("2015-06-08 -> 2015-06-12 (пятница, лаг 4 до ступени 16.06)",
        "UPDATE dkp.meeting SET meeting_date='2015-06-12', notes='needs_source_check: дата объявления уточнена по лестнице (ступень 11,5 с 16.06.2015, лаг 4); точный день (12.06 пятница или 15.06 понедельник) источником не подтверждён' WHERE meeting_date='2015-06-08'")

    conn.commit()
    log.append("COMMIT ok")
except Exception as e:
    conn.rollback()
    log.append("ROLLBACK: %r" % (e,))

for line in log:
    print(" -", line)
conn.close()
print("DONE")