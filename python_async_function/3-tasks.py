#!/usr/bin/env python3
"""
Write a function task_wait_random that takes an 
integer max_delay and returns a asyncio.Task
"""
import asyncio
from typing import Any

wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> Any:
    """Creates an asyncio Task for wait_random with specified max_delay"""
    return asyncio.create_task(wait_random(max_delay))
