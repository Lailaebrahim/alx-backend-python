#!/usr/bin/env python3
"""Asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random that waits for a
random delay between 0 and max_delay (included and float value) seconds and
eventually returns it.

Args:
  max_delay (int, optional): The maximum delay in seconds. Defaults to 10.

Returns:
  float: The random delay in seconds.
"""
import asyncio
import random


async def wait_random(max_delay=10):
    """Asynchronous coroutine that takes in an integer argument
    (max_delay, with a default value of 10) named wait_random that waits for a
    random delay between 0 and max_delay (included and float value) seconds and
    eventually returns it."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
