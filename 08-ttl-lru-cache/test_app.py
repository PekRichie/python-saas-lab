import unittest
from app import TtlLruCache

class TestCache(unittest.TestCase):
    def test_lru_and_ttl(self):
        now = [0.0]
        c = TtlLruCache(max_size=2, default_ttl=10.0, clock=lambda: now[0])
        c.set("a", 1); c.set("b", 2); c.get("a"); c.set("c", 3)
        self.assertIsNone(c.get("b"))
        self.assertEqual(c.get("a"), 1)
        now[0] += 11.0
        self.assertIsNone(c.get("a"))

if __name__ == "__main__":
    unittest.main()
