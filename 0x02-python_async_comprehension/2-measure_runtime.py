#!/usr/bin/env python3
'''
Import async_comprehension from the previous file and write a
measure_runtime coroutine that will execute async_comprehension
four times in parallel using asyncio.gather.
measure_runtime should measure the total runtime and return it.
'''
import time
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''measures time taken to run concurrent operation four times'''
    begin = time.perf_counter()
    aws = [async_comprehension() for i in range(4)]
    await asyncio.gather(*aws)
    end = time.perf_counter()
    return (end - begin)
