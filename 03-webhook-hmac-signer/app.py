"""Webhook HMAC-SHA256 aláíró és replay-védett ellenőrző."""
import hashlib
import hmac
import time


class WebhookSigner:
    def __init__(self, secret: str, tolerance_sec: int = 300) -> None:
        self.secret = secret.encode("utf-8")
        self.tolerance_sec = tolerance_sec

    def sign(self, payload: bytes, timestamp: int | None = None) -> str:
        ts = int(time.time()) if timestamp is None else timestamp
        signed = f"{ts}.".encode("utf-8") + payload
        sig = hmac.new(self.secret, signed, hashlib.sha256).hexdigest()
        return f"t={ts},v1={sig}"

    def verify(self, payload: bytes, header: str, now: int | None = None) -> bool:
        parts = dict(p.split("=", 1) for p in header.split(",") if "=" in p)
        if "t" not in parts or "v1" not in parts:
            return False
        ts = int(parts["t"])
        cur = int(time.time()) if now is None else now
        if abs(cur - ts) > self.tolerance_sec:
            return False
        expected = self.sign(payload, timestamp=ts).split("v1=", 1)[1]
        return hmac.compare_digest(expected, parts["v1"])
