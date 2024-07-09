#!/usr/bin/env python3
"""this is some one liners from Python"""

import typing

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """learn how to use this"""
    return [n async for n in async_generator()]
