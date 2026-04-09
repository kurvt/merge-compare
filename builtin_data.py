"""BSP merge records - loaded from data.json"""
import json
import os

_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(_dir, "data.json"), encoding="utf-8") as _f:
    BSP_DATA = json.load(_f)
