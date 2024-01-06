#!/usr/bin/env python3
"""Async Comprehensions"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine to collect 10 random numbers using async comprehension.
    Will return list of 10 random numbers
    """
    return [number async for number in async_generator()]
