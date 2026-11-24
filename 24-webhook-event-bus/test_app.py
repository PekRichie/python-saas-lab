import unittest
from app import EventBus

class TestBus(unittest.TestCase):
    def test_wildcard_and_isolation(self):
        bus = EventBus()
        seen = []
        bus.subscribe("invoice.*", lambda t, p: (_ for _ in ()).throw(RuntimeError("boom")))
        bus.subscribe("invoice.*", lambda t, p: seen.append((t, p["id"])))
        res = bus.publish("invoice.paid", {"id": "INV-1"})
        self.assertEqual(res, {"delivered": 1, "failed": 1})
        self.assertEqual(seen, [("invoice.paid", "INV-1")])

if __name__ == "__main__":
    unittest.main()
