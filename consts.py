import os
from classes.functions import filter_proc, map_proc, unique_proc, sort_proc, limit_proc, regex_proc
from typing import Dict, Callable

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

DEF_TYPE_COMMAND: Dict[str, Callable] = {'filter': filter_proc,
                                         'map': map_proc,
                                         'unique': unique_proc,
                                         'sort': sort_proc,
                                         'limit': limit_proc,
                                         'regex': regex_proc}

