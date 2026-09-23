#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Дозагрузка: решение 19.06.2026 не обновилось (проверить), statement rows=0."""
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from db_tunnel import execute, query  # noqa: E402

# 19.06: URL должен быть; проверить и вставить при отсутствии
r = query("SELECT meeting_id, press_release_url FROM dkp.meeting "
          "WHERE meeting_date='2026-06-19'")
print("meeting 19.06:", r)
if r and not r[0][1]:
    execute("UPDATE dkp.meeting SET press_release_url=%s WHERE meeting_date='2026-06-19'",
            ("https://www.cbr.ru/press/pr/?file=19062026_133000key.htm",))
    print("19.06 url set")

# statement: почему 0? Проверить
print("statement count:", query("SELECT count(*) FROM dkp.statement")[0][0])
r = query("SELECT meeting_id FROM dkp.meeting WHERE meeting_date='2026-06-19'")
print("meeting id 19.06:", r)