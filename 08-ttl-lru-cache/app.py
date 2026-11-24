"""TTL és LRU politikát kombináló gyorsítótár."""
import time
from collections import OrderedDict


class TtlLruCache:
    def __init__(self, max_size: int = 128, default_ttl: float = 60.0, clock=time.monotonic) -> None:
        self.max_size = max_size
        self.default_ttl = default_ttl
        self.clock = clock
        self._data: OrderedDict[str, tuple[object, float]] = OrderedDict()

    def set(self, key: str, value: object, ttl: float | None = None) -> None:
        exp = self.clock() + (self.default_ttl if ttl is None else ttl)
        if key in self._data:
            self._data.move_to_end(key)
        self._data[key] = (value, exp)
        while len(self._data) > self.max_size:
            self._data.popitem(last=False)

    def get(self, key: str, default: object = None) -> object:
        item = self._data.get(key)
        if item is None:
            return default
        val, exp = item
        if self.clock() > exp:
            del self._data[key]
            return default
        self._data.move_to_end(key)
        return val
