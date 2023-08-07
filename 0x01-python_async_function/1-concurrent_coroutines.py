#!/usr/bin/env python3
import asyncio
from typing import List
"""concurrent corouting"""


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    wait_n function takes two arguments
    """
    lst = []
    sorted_lst = []
    i = 0
    while i < n:
        spawn = await wait_random(max_delay)
        lst.append(spawn)
        i += 1
    y = 0
    while y < n:
        minimum = lst[0]
        for x in lst:
            if x < minimum:
                minimum = x
        sorted_lst.append(minimum)
        lst.remove(minimum)
        y += 1
    return sorted_lst
