import unittest
from app import WebhookSigner

class TestWebhook(unittest.TestCase):
    def test_sign_and_replay_protection(self):
        s = WebhookSigner("whsec_test", tolerance_sec=60)
        payload = b'{"event":"invoice.paid"}'
        hdr = s.sign(payload, timestamp=1000)
        self.assertTrue(s.verify(payload, hdr, now=1030))
        self.assertFalse(s.verify(payload, hdr, now=1200))
        self.assertFalse(s.verify(b'{"tampered":true}', hdr, now=1030))

if __name__ == "__main__":
    unittest.main()
