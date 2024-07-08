#!/usr/bin/env python3
"""wait it is sleep time"""

import asyncio
import typing

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """Wait for random time n times concurrentely"""
    coros = [wait_random(max_delay) for _ in range(n)]
    results = []
    for coro in asyncio.as_completed(coros):
        results.append(await coro)
    return results
