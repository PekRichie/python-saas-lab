import unittest
from decimal import Decimal
from app import normalize_invoices

class TestCsv(unittest.TestCase):
    def test_clean_and_errors(self):
        data = 'invoice_id,amount\n inv-1 ," 12 500,50 "\n,100\ninv-2,-5'
        ok, err = normalize_invoices(data)
        self.assertEqual(len(ok), 1)
        self.assertEqual(ok[0]["amount"], Decimal("12500.50"))
        self.assertEqual(len(err), 2)

if __name__ == "__main__":
    unittest.main()
