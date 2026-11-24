import unittest
from app import FeatureFlags, FlagConfig

class TestFlags(unittest.TestCase):
    def test_whitelist_and_determinism(self):
        ff = FeatureFlags()
        ff.register(FlagConfig("ai_v2", enabled=True, rollout_percent=20, allowed_tenants={"vip"}))
        self.assertTrue(ff.is_enabled("ai_v2", "vip"))
        first = ff.is_enabled("ai_v2", "tenant-42")
        self.assertEqual(first, ff.is_enabled("ai_v2", "tenant-42"))

if __name__ == "__main__":
    unittest.main()
