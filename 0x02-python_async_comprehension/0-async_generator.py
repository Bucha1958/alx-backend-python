#!/usr/bin/env python3
import random
import asyncio
from typing import Generator
"""
Async_generator module
"""


async def async_generator() -> Generator[float, None, None]:
    """
    async generator function takes no argument
    """
    i = 0
    while i < 10:
        randint = random.randrange(1, 11)
        await asyncio.sleep(1)
        yield randint
        i += 1
