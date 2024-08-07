#!/usr/bin/env python3
"""Asynchronous coroutine called wait_n that takes in 2
int arguments (in this order): n and max_delay.
You will spawn wait_random n times with the specified max_delay..

Args:
    max_delay (int, optional): The maximum delay in seconds. Defaults to 10.

Returns:
    float: The random delay in seconds.
"""
import asyncio
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine called wait_n that takes in 2
    int arguments (in this order): n and max_delay.
    You will spawn wait_random n times with the specified max_delay.
    spawned tasks will run concurrantly and will return a list of the
    delays in ascending order.
    """
    wait_random = __import__('0-basic_async_syntax').wait_random
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
