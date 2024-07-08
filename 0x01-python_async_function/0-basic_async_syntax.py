#!/usr/bin/env python3
"""wait for a random time"""

import asyncio
import random


async def wait_random(max_delay=10):
    """wait random number of seconds between 0 and max_delay"""
    t = random.uniform(0, max_delay)
    await asyncio.sleep(t)
    return t
