import unittest
from decimal import Decimal
from app import UsageMeter

class TestMeter(unittest.TestCase):
    def test_overage(self):
        m = UsageMeter(included_units=1000, unit_price_huf=Decimal("2.5"))
        m.record("t1", 600); m.record("t1", 700)
        s = m.bill_summary("t1")
        self.assertEqual(s["billable"], 300)
        self.assertEqual(s["overage_huf"], Decimal("750.0"))

if __name__ == "__main__":
    unittest.main()
