#!/usr/bin/env python3
"""Write a coroutine called async_generator"""

from asyncio import sleep
from random import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Generator that yields a random value betwen 0 - 10"""
    for i in range(10):
        await sleep(1)
        yield 10 * random()
