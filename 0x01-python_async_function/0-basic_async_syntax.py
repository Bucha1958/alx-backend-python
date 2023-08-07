#!/usr/bin/env python3
import asyncio
import random
"""Basic async syntax"""


async def wait_random(max_delay: int = 10) -> float:
    """
    wait_function is a coroutine with an int parameter
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
