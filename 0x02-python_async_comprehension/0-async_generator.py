#!/usr/bin/env python3
import random
import asyncio
"""
Async_generator module
"""


async def async_generator() -> int:
    """
    async generator function takes no argument
    """
    i = 0
    while i < 10:
        randint = random.randrange(1, 11)
        await asyncio.sleep(1)
        yield randint
        i += 1
