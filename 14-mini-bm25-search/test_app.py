import unittest
from app import Bm25Index

class TestBm25(unittest.TestCase):
    def test_ranking(self):
        idx = Bm25Index(["MAGMA moduláris SaaS platform", "Borostyán tudásgráf és AI memória", "Kaptár többágenses AI környezet"])
        res = idx.search("AI memória tudásgráf")
        self.assertEqual(res[0][0], 1)

if __name__ == "__main__":
    unittest.main()
