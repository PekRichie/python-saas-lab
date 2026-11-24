import unittest
from app import DocumentWorkflow

class TestWf(unittest.TestCase):
    def test_transitions(self):
        wf = DocumentWorkflow("doc-1")
        wf.transition("review")
        wf.transition("approved")
        with self.assertRaises(ValueError):
            wf.transition("draft")

if __name__ == "__main__":
    unittest.main()
