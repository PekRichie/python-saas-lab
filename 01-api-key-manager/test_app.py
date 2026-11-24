import unittest
from app import ApiKeyManager

class TestApiKeyManager(unittest.TestCase):
    def test_issue_verify_revoke(self):
        mgr = ApiKeyManager()
        raw, rec = mgr.issue("tenant-1", ("read", "write"))
        self.assertIsNotNone(mgr.verify(raw, "write"))
        self.assertIsNone(mgr.verify(raw, "admin"))
        self.assertTrue(mgr.revoke(rec.key_id))
        self.assertIsNone(mgr.verify(raw))

if __name__ == "__main__":
    unittest.main()
