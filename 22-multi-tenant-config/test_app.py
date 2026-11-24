import unittest
from app import TenantConfigResolver

class TestCfg(unittest.TestCase):
    def test_precedence(self):
        r = TenantConfigResolver({"max_users": 5, "ai": False})
        r.set_plan("pro", {"max_users": 50, "ai": True})
        r.set_tenant("vip", {"max_users": 500})
        cfg = r.resolve("vip", "pro")
        self.assertEqual(cfg, {"max_users": 500, "ai": True})

if __name__ == "__main__":
    unittest.main()
