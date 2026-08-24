#!/usr/bin/env python3
"""
P6b: VACUUM через VACUUM INTO (безопаснее при малом месте: пишет новый файл,
потом переименование). Если места не хватит — упадёт, не повредив исходник.
"""
import sqlite3, os, time

DB = '/home/lnr/research-wiki/data/rosstat_construction.db'
TMP = '/home/lnr/research-wiki/data/rosstat_construction_vacuumed.db'

size_before = os.path.getsize(DB)
print(f"До: {size_before/1024/1024:.0f} МБ")

t0 = time.time()
src = sqlite3.connect(DB)
src.execute("PRAGMA journal_mode=DELETE")
print("VACUUM INTO ...")
src.execute(f"VACUUM INTO '{TMP}'")
src.close()
print(f"Готово за {time.time()-t0:.1f}s")

size_new = os.path.getsize(TMP)
print(f"Новый файл: {size_new/1024/1024:.0f} МБ")

# Integrity check нового файла
chk = sqlite3.connect(TMP)
res = chk.execute("PRAGMA integrity_check").fetchone()[0]
tables = chk.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table'").fetchone()[0]
rows_domrf = chk.execute("SELECT COUNT(*) FROM domrf_indicators").fetchone()[0]
chk.close()
print(f"integrity_check: {res}, tables: {tables}, domrf rows: {rows_domrf:,}")

if res == 'ok':
    os.replace(TMP, DB)
    print("Заменено. Финальный размер:")
    os.system(f"ls -lh {DB}")
else:
    print("INTEGRITY FAILED — исходник не тронут")
