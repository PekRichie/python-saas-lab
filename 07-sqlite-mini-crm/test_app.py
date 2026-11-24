import unittest
from app import CrmRepository

class TestCrm(unittest.TestCase):
    def test_tenant_isolation(self):
        repo = CrmRepository()
        repo.create("t1", "Anna", "anna@a.hu", "lead")
        repo.create("t2", "Béla", "bela@b.hu", "won")
        self.assertEqual(len(repo.list_by_tenant("t1")), 1)
        self.assertEqual(repo.list_by_tenant("t1")[0].name, "Anna")

if __name__ == "__main__":
    unittest.main()
