import unittest
from app import CircuitBreaker, CircuitOpenError

class TestBreaker(unittest.TestCase):
    def test_open_and_recover(self):
        t = [0.0]
        cb = CircuitBreaker(failure_threshold=2, recovery_sec=10.0, clock=lambda: t[0])
        for _ in range(2):
            with self.assertRaises(ValueError):
                cb.call(lambda: (_ for _ in ()).throw(ValueError("down")))
        with self.assertRaises(CircuitOpenError):
            cb.call(lambda: "ok")
        t[0] += 11.0
        self.assertEqual(cb.call(lambda: "recovered"), "recovered")

if __name__ == "__main__":
    unittest.main()
