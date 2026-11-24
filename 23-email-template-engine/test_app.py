import unittest
from app import render_template

class TestTpl(unittest.TestCase):
    def test_escape_and_missing(self):
        out = render_template("<p>Szia {{ name }}!</p>", {"name": "<b>Anna</b>"})
        self.assertIn("&lt;b&gt;Anna&lt;/b&gt;", out)
        with self.assertRaises(KeyError):
            render_template("Szia {{ name }}", {})

if __name__ == "__main__":
    unittest.main()
