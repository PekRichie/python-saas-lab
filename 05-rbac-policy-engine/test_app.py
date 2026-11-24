import unittest
from app import RbacEngine

class TestRbac(unittest.TestCase):
    def test_wildcard_and_tenant_isolation(self):
        rbac = RbacEngine()
        rbac.define_role("manager", {"projects:*", "invoices:read"})
        rbac.assign("t1", "u1", "manager")
        self.assertTrue(rbac.can("t1", "u1", "projects:delete"))
        self.assertFalse(rbac.can("t1", "u1", "invoices:delete"))
        self.assertFalse(rbac.can("t2", "u1", "projects:read"))

if __name__ == "__main__":
    unittest.main()
