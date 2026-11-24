"""Stateless HMAC-SHA256 aláírt token motor lejárati ellenőrzéssel."""
import base64, hashlib, hmac, json, time


def _b64e(b: bytes) -> str:
    return base64.urlsafe_b64encode(b).rstrip(b"=").decode("ascii")


def _b64d(s: str) -> bytes:
    return base64.urlsafe_b64decode(s + "=" * (-len(s) % 4))


class TokenService:
    def __init__(self, secret: str) -> None:
        self.secret = secret.encode("utf-8")

    def issue(self, sub: str, tenant_id: str, ttl_sec: int = 3600, now: int | None = None) -> str:
        ts = int(time.time()) if now is None else now
        hdr = _b64e(json.dumps({"alg": "HS256", "typ": "JWT"}).encode())
        pay = _b64e(json.dumps({"sub": sub, "tenant": tenant_id, "exp": ts + ttl_sec}).encode())
        sig = _b64e(hmac.new(self.secret, f"{hdr}.{pay}".encode(), hashlib.sha256).digest())
        return f"{hdr}.{pay}.{sig}"

    def verify(self, token: str, now: int | None = None) -> dict | None:
        parts = token.split(".")
        if len(parts) != 3:
            return None
        hdr, pay, sig = parts
        exp_sig = _b64e(hmac.new(self.secret, f"{hdr}.{pay}".encode(), hashlib.sha256).digest())
        if not hmac.compare_digest(exp_sig, sig):
            return None
        data = json.loads(_b64d(pay).decode("utf-8"))
        cur = int(time.time()) if now is None else now
        if cur > data["exp"]:
            return None
        return data
