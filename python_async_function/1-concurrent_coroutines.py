#!/usr/bin/env python3
"""The list of the delays should be in ascending order without using sort() because of concurrency"""
from typing import List
import asyncio
wait_random = __impor('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """Async routine to spawn wait_random n times with specified max_delay"""
    delay_list = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await delay_list for delay_list in asyncio.as_completed(delay_list)]