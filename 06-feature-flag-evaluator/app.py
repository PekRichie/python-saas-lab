"""Determinisztikus Feature Flag és fokozatos rollout kiértékelő."""
import hashlib
from dataclasses import dataclass, field


@dataclass
class FlagConfig:
    key: str
    enabled: bool = True
    rollout_percent: int = 0
    allowed_tenants: set[str] = field(default_factory=set)


class FeatureFlags:
    def __init__(self) -> None:
        self._flags: dict[str, FlagConfig] = {}

    def register(self, cfg: FlagConfig) -> None:
        self._flags[cfg.key] = cfg

    @staticmethod
    def _bucket(flag_key: str, tenant_id: str) -> int:
        digest = hashlib.sha256(f"{flag_key}:{tenant_id}".encode("utf-8")).hexdigest()
        return int(digest[:8], 16) % 100

    def is_enabled(self, flag_key: str, tenant_id: str) -> bool:
        cfg = self._flags.get(flag_key)
        if not cfg or not cfg.enabled:
            return False
        if tenant_id in cfg.allowed_tenants:
            return True
        return self._bucket(flag_key, tenant_id) < cfg.rollout_percent
