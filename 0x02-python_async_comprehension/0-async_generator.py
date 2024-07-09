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
