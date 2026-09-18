"""Подготовка core.observation_v3: структура + уникальный индекс (как у v2)."""
import psycopg, os
os.environ.setdefault('PGPASSFILE', os.path.expanduser('~/.pgpass'))
conn = psycopg.connect("host=localhost port=5432 dbname=research_wiki user=wiki")
conn.autocommit = True
cur = conn.cursor()

V3 = 'core.observation_v3'

print("=== 1. Индексы observation_v2 (образец) ===")
cur.execute("""SELECT indexname, indexdef FROM pg_indexes
               WHERE schemaname='core' AND tablename='observation_v2'""")
for n, d in cur.fetchall():
    print(f"  {n}")
    print(f"    {d[:150]}")

print("\n=== 2. Создаю observation_v3 по образцу v2 ===")
cur.execute(f"DROP TABLE IF EXISTS {V3}")
cur.execute(f"CREATE TABLE {V3} (LIKE core.observation_v2 INCLUDING ALL)")
cur.execute(f"""SELECT count(*) FROM information_schema.columns
                WHERE table_schema='core' AND table_name='observation_v3'""")
print(f"  колонок: {cur.fetchone()[0]}")

# уникальное ограничение нужно для ON CONFLICT
cur.execute(f"""SELECT conname FROM pg_constraint
                WHERE conrelid='{V3}'::regclass AND contype='u'""")
u = cur.fetchall()
print(f"  уникальных ограничений: {len(u)} — {[x[0] for x in u]}")

cur.execute(f"""SELECT count(*) FROM pg_indexes
                WHERE schemaname='core' AND tablename='observation_v3'""")
print(f"  индексов: {cur.fetchone()[0]}")

print("\n=== 3. Проверка: ON CONFLICT сработает ===")
try:
    cur.execute(f"""INSERT INTO {V3}
        (metric_id, region_id, frequency_id, period_start, period_end, value,
         assessment_type, observation_status, source_id, release_id, sub_dimension)
        VALUES (1,1,1,'2020-01-01','2020-12-31',1,'final','validated',1,1,'test')
        ON CONFLICT (metric_id, region_id, frequency_id, period_start, source_id,
                     release_id, assessment_type, sub_dimension) DO NOTHING""")
    print("  ✓ ON CONFLICT принимается")
except Exception as e:
    print(f"  ✗ ошибка: {str(e)[:120]}")
    conn.rollback()
cur.execute(f"DELETE FROM {V3} WHERE sub_dimension='test'")
conn.close()
