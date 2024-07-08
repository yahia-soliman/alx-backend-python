#!/usr/bin/env python3
"""wait it is sleep time"""

import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Wait for random time n times concurrentely"""
    return asyncio.create_task(wait_random(max_delay))
