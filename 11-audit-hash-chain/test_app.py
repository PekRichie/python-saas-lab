import unittest
from app import AuditChain

class TestAudit(unittest.TestCase):
    def test_tamper_detection(self):
        c = AuditChain()
        c.append("admin", "tenant.create")
        c.append("user1", "invoice.export")
        self.assertTrue(c.verify())
        c.entries[0].action = "tampered"
        self.assertFalse(c.verify())

if __name__ == "__main__":
    unittest.main()
