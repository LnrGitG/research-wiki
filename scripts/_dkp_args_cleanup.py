#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Очистка частично вставленных аргументов и перезапуск полной загрузки."""
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from db_tunnel import execute, query  # noqa: E402

n = query("SELECT count(*) FROM dkp.argument")[0][0]
print("before:", n)
execute("DELETE FROM dkp.argument WHERE classifier_version='manual_v1'")
print("after delete:", query("SELECT count(*) FROM dkp.argument")[0][0])