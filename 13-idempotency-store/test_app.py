import unittest
from app import IdempotencyStore

class TestIdem(unittest.TestCase):
    def test_single_execution(self):
        store = IdempotencyStore()
        calls = [0]
        def charge():
            calls[0] += 1
            return {"status": "paid", "n": calls[0]}
        r1, cached1 = store.execute("req-1", charge)
        r2, cached2 = store.execute("req-1", charge)
        self.assertFalse(cached1)
        self.assertTrue(cached2)
        self.assertEqual(r1, r2)
        self.assertEqual(calls[0], 1)

if __name__ == "__main__":
    unittest.main()
