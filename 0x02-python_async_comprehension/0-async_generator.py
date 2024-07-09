#!/usr/bin/env python3
"""I have an Async generatator function"""

import asyncio
import random
import typing


async def async_generator() -> typing.AsyncGenerator[float, None]:
    """I'm the function the module told you about"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())
