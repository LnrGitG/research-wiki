import sys
sys.path.insert(0, "/home/ubuntu/research-wiki-private/scripts")
from db_tunnel import connect
conn = connect(); cur = conn.cursor()
log = []

def upd(tag, sql):
    cur.execute(sql)
    log.append("%s -> %d" % (tag, cur.rowcount))

# 1) 2017-03-27 (понедельник) -> 24.03.2017 (пятница): ступень 9,75 вступила
#    27.03.2017, лаг 3 дня; объявление решения — пятница.
upd("2017-03-27 -> 2017-03-24 (лаг 3 до ступени 9,75)",
    "UPDATE dkp.meeting SET meeting_date='2017-03-24', notes='дата объявления решения (пятница); ступень 9,75 вступила 27.03.2017, лаг 3' WHERE meeting_date='2017-03-27'")

# 2) Удержания 2015 года с датами вне пятницы: помечаем, не меняя без источника.
for md, txt in (
    ("2015-11-10", "needs_source_check: дата вне пятницы (вторник). Плановый календарь 2015 года предполагает заседание 30.10.2015; точная дата источником не подтверждена (эндпоинт пресс-релизов период 2015 года не покрывает)"),
    ("2015-12-03", "needs_source_check: дата вне пятницы (четверг). Плановый календарь 2015 года предполагает заседание 11.12.2015; точная дата источником не подтверждена"),
    ("2014-10-25", "needs_source_check: суббота; до перехода на пятничный график даты заседаний 2014 года не сверены по первоисточнику"),
    ("2013-11-13", "needs_source_check: период до введения пятничного графика; даты 2013 года по первоисточнику не сверялись"),
    ("2013-12-12", "needs_source_check: период до введения пятничного графика; даты 2013 года по первоисточнику не сверялись"),
    ("2014-03-03", "needs_source_check: понедельник; дата совпадает с датой вступления ступени 7,0 (лаг 0), объявление могло быть 28.02.2014 — источником не подтверждено"),
):
    upd("notes %s" % md, "UPDATE dkp.meeting SET notes=%s WHERE meeting_date='%s'::date" % ("'" + txt.replace("'", "''") + "'", md))

conn.commit()
log.append("COMMIT ok")
cur.execute("SELECT count(*) FROM dkp.meeting WHERE extract(dow FROM meeting_date) <> 5")
log.append("заседаний вне пятницы: %d" % cur.fetchone()[0])
cur.execute("SELECT count(*) FROM dkp.meeting"); log.append("заседаний: %d" % cur.fetchone()[0])
for line in log:
    print(" -", line)
conn.close()