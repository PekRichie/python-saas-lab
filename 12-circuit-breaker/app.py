"""Circuit Breaker minta külső API-k védelmére."""
import time
from typing import Callable, TypeVar

T = TypeVar("T")


class CircuitOpenError(RuntimeError):
    pass


class CircuitBreaker:
    def __init__(self, failure_threshold: int = 3, recovery_sec: float = 30.0, clock=time.monotonic) -> None:
        self.failure_threshold = failure_threshold
        self.recovery_sec = recovery_sec
        self.clock = clock
        self.failures = 0
        self.state = "CLOSED"
        self.opened_at = 0.0

    def call(self, fn: Callable[[], T]) -> T:
        if self.state == "OPEN":
            if self.clock() - self.opened_at >= self.recovery_sec:
                self.state = "HALF_OPEN"
            else:
                raise CircuitOpenError("A megszakító nyitva van.")
        try:
            res = fn()
        except Exception:
            self.failures += 1
            if self.failures >= self.failure_threshold:
                self.state = "OPEN"
                self.opened_at = self.clock()
            raise
        self.failures = 0
        self.state = "CLOSED"
        return res
