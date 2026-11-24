"""Idempotency-Key tároló fizetési és kritikus POST API-khoz."""
from typing import Callable, TypeVar

T = TypeVar("T")


class IdempotencyStore:
    def __init__(self) -> None:
        self._results: dict[str, object] = {}

    def execute(self, key: str, fn: Callable[[], T]) -> tuple[T, bool]:
        if key in self._results:
            return self._results[key], True  # type: ignore[return-value]
        res = fn()
        self._results[key] = res
        return res, False
