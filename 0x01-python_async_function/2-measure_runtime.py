#!/usr/bin/env python3
"""Asynchronous coroutine that takes in an int argument"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the runtime of the wait_n function.

    Args:
        n (int): The number of times to call the wait_n function.
        max_delay (int): The maximum delay for each call to the wait_n function.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    return end_time - start_time
