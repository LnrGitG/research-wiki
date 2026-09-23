#!/usr/bin/env python3
"""Микромиграция: dkp.meeting.notes (не вошло в v1 DDL)."""
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from db_tunnel import execute, query  # noqa: E402

cols = query(
    "SELECT column_name FROM information_schema.columns "
    "WHERE table_schema='dkp' AND table_name='meeting'")
names = {r[0] for r in cols}
if "notes" not in names:
    execute("ALTER TABLE dkp.meeting ADD COLUMN notes text")
    print("added dkp.meeting.notes")
else:
    print("notes exists")
print("meeting cols:", query(
    "SELECT column_name FROM information_schema.columns "
    "WHERE table_schema='dkp' AND table_name='meeting' ORDER BY ordinal_position"))