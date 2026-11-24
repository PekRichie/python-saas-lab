import unittest
from decimal import Decimal
from app import Plan, calculate_proration

class TestProration(unittest.TestCase):
    def test_mid_cycle_upgrade(self):
        starter = Plan("starter", Decimal("10000"))
        pro = Plan("pro", Decimal("30000"))
        res = calculate_proration(starter, pro, days_remaining=15, cycle_days=30)
        self.assertEqual(res["net_delta"], Decimal("10000"))
        self.assertEqual(res["gross_delta"], Decimal("12700"))

if __name__ == "__main__":
    unittest.main()
