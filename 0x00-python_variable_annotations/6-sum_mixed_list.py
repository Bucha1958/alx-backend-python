#!/usr/bin/env python3
from typing import Union
"""6-sum_mixed_list module"""
Vector = Union[float, int]


def sum_mixed_list(mxd_lst: Vector) -> float:
    """
    sum_mixed_list function takes list as argument
    """
    sum : float = 0.0
    for n in mxd_lst:
        sum += n
    return sum

