"""SaaS API-kulcs generátor és biztonságos ellenőrző."""
import hashlib
import hmac
import secrets
from dataclasses import dataclass, field


@dataclass
class ApiKeyRecord:
    key_id: str
    tenant_id: str
    key_hash: str
    scopes: tuple[str, ...] = ("read",)
    revoked: bool = False


class ApiKeyManager:
    def __init__(self, prefix: str = "cs_live_") -> None:
        self.prefix = prefix
        self._store: dict[str, ApiKeyRecord] = {}

    @staticmethod
    def _hash(raw_key: str) -> str:
        return hashlib.sha256(raw_key.encode("utf-8")).hexdigest()

    def issue(self, tenant_id: str, scopes: tuple[str, ...] = ("read",)) -> tuple[str, ApiKeyRecord]:
        key_id = secrets.token_hex(4)
        secret_part = secrets.token_urlsafe(24)
        raw_key = f"{self.prefix}{key_id}.{secret_part}"
        rec = ApiKeyRecord(key_id=key_id, tenant_id=tenant_id, key_hash=self._hash(raw_key), scopes=scopes)
        self._store[key_id] = rec
        return raw_key, rec

    def verify(self, raw_key: str, required_scope: str | None = None) -> ApiKeyRecord | None:
        if not raw_key.startswith(self.prefix) or "." not in raw_key:
            return None
        key_id = raw_key[len(self.prefix):].split(".", 1)[0]
        rec = self._store.get(key_id)
        if not rec or rec.revoked:
            return None
        if not hmac.compare_digest(rec.key_hash, self._hash(raw_key)):
            return None
        if required_scope and required_scope not in rec.scopes:
            return None
        return rec

    def revoke(self, key_id: str) -> bool:
        rec = self._store.get(key_id)
        if not rec:
            return False
        rec.revoked = True
        return True
