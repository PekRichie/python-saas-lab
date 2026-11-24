"""SHA-256 hash-lánccal védett vállalati audit napló."""
import hashlib
import json
from dataclasses import dataclass


@dataclass
class AuditEntry:
    index: int
    actor: str
    action: str
    prev_hash: str
    entry_hash: str


class AuditChain:
    def __init__(self) -> None:
        self.entries: list[AuditEntry] = []

    @staticmethod
    def _compute(index: int, actor: str, action: str, prev_hash: str) -> str:
        raw = json.dumps([index, actor, action, prev_hash], sort_keys=True).encode("utf-8")
        return hashlib.sha256(raw).hexdigest()

    def append(self, actor: str, action: str) -> AuditEntry:
        prev = self.entries[-1].entry_hash if self.entries else "0" * 64
        idx = len(self.entries)
        h = self._compute(idx, actor, action, prev)
        e = AuditEntry(idx, actor, action, prev, h)
        self.entries.append(e)
        return e

    def verify(self) -> bool:
        prev = "0" * 64
        for i, e in enumerate(self.entries):
            if e.index != i or e.prev_hash != prev:
                return False
            if e.entry_hash != self._compute(e.index, e.actor, e.action, e.prev_hash):
                return False
            prev = e.entry_hash
        return True
