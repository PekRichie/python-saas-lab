"""Konkurencia-korlátos aszinkron kötegelt feldolgozó."""
import asyncio
from typing import Awaitable, Callable, TypeVar

T = TypeVar("T")
R = TypeVar("R")


async def run_bounded(items: list[T], worker: Callable[[T], Awaitable[R]], max_concurrency: int = 4) -> list[R]:
    sem = asyncio.Semaphore(max_concurrency)

    async def _guarded(item: T) -> R:
        async with sem:
            return await worker(item)

    return await asyncio.gather(*(_guarded(it) for it in items))
