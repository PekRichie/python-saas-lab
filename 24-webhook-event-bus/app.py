"""Wildcard eseménybusz hibaizolációval."""
import fnmatch
from typing import Callable


class EventBus:
    def __init__(self) -> None:
        self._subs: list[tuple[str, Callable[[str, dict], None]]] = []

    def subscribe(self, pattern: str, handler: Callable[[str, dict], None]) -> None:
        self._subs.append((pattern, handler))

    def publish(self, topic: str, payload: dict) -> dict[str, int]:
        delivered = failed = 0
        for pat, fn in self._subs:
            if fnmatch.fnmatch(topic, pat):
                try:
                    fn(topic, payload)
                    delivered += 1
                except Exception:
                    failed += 1
        return {"delivered": delivered, "failed": failed}
