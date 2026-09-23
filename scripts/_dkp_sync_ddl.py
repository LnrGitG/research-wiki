#!/usr/bin/env python3
"""Синхронизация DDL: dkp.meeting.notes + dkp.forecast.unit_code расширения."""
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from db_tunnel import execute  # noqa: E402

# Обновляем DDL-файл: добавляем notes в dkp.meeting
import re
path = os.path.join(HERE, "cbr_decision_ddl.sql")
with open(path, encoding="utf-8") as fh:
    sql = fh.read()

if "notes text" not in sql:
    sql = sql.replace(
        "    published_at      timestamptz,",
        "    published_at      timestamptz,\n"
        "    notes             text,                    -- источник, needs_source_check и пр.")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(sql)
    print("DDL updated: meeting.notes")
else:
    print("DDL already has notes")