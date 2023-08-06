#!/usr/bin/env python3
"""
7-to_kv
"""

from typing import Union
from typing import Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    return k and v as a tuple
    """
    rv: Tuple[str, float] = (k, v ** 2)
    return rv
