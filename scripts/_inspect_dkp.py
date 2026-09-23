#!/usr/bin/env python3
"""Инспекция: сигнатура db_tunnel.execute + колонки v2.dataset."""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from db_tunnel import query  # noqa: E402

print("v2.dataset:", query(
    "SELECT column_name, data_type, is_nullable FROM information_schema.columns "
    "WHERE table_schema='v2' AND table_name='dataset' ORDER BY ordinal_position"))
print("dataset rows:", query("SELECT count(*) FROM v2.dataset"))
print("datasets sample:", query("SELECT * FROM v2.dataset LIMIT 3"))