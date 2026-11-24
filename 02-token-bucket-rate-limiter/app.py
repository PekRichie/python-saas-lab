"""Token Bucket alapú per-tenant API rate limiter."""
import time
from dataclasses import dataclass


@dataclass
class Bucket:
    tokens: float
    last_refill: float


class TokenBucketLimiter:
    def __init__(self, capacity: int, refill_per_sec: float, clock=time.monotonic) -> None:
        self.capacity = float(capacity)
        self.refill_per_sec = float(refill_per_sec)
        self.clock = clock
        self._buckets: dict[str, Bucket] = {}

    def allow(self, tenant_id: str, cost: float = 1.0) -> bool:
        now = self.clock()
        b = self._buckets.get(tenant_id)
        if b is None:
            b = Bucket(tokens=self.capacity, last_refill=now)
            self._buckets[tenant_id] = b
        elapsed = max(0.0, now - b.last_refill)
        b.tokens = min(self.capacity, b.tokens + elapsed * self.refill_per_sec)
        b.last_refill = now
        if b.tokens >= cost:
            b.tokens -= cost
            return True
        return False
