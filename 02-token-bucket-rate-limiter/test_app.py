import unittest
from app import TokenBucketLimiter

class TestLimiter(unittest.TestCase):
    def test_refill_and_limit(self):
        t = [0.0]
        lim = TokenBucketLimiter(capacity=2, refill_per_sec=1.0, clock=lambda: t[0])
        self.assertTrue(lim.allow("t1"))
        self.assertTrue(lim.allow("t1"))
        self.assertFalse(lim.allow("t1"))
        t[0] += 1.0
        self.assertTrue(lim.allow("t1"))

if __name__ == "__main__":
    unittest.main()
