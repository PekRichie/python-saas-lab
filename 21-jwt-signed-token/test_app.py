import unittest
from app import TokenService

class TestToken(unittest.TestCase):
    def test_issue_verify_expire(self):
        ts = TokenService("super-secret")
        tok = ts.issue("u1", "t1", ttl_sec=60, now=1000)
        self.assertEqual(ts.verify(tok, now=1030)["sub"], "u1")
        self.assertIsNone(ts.verify(tok, now=1100))
        self.assertIsNone(ts.verify(tok + "x", now=1030))

if __name__ == "__main__":
    unittest.main()
