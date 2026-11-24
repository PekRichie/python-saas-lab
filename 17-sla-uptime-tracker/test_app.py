import unittest
from app import sla_report

class TestSla(unittest.TestCase):
    def test_budget(self):
        ok = sla_report(10.0, target_sla=99.9)
        bad = sla_report(60.0, target_sla=99.9)
        self.assertTrue(ok["compliant"])
        self.assertFalse(bad["compliant"])

if __name__ == "__main__":
    unittest.main()
