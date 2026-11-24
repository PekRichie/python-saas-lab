import unittest
from app import ModelPricing, render_and_price

class TestPrompt(unittest.TestCase):
    def test_render_and_cost(self):
        p = ModelPricing("gemini-flash", 0.15, 0.60)
        res = render_and_price("Összegezd: {topic}", {"topic": "MAGMA SaaS"}, p, expected_output_tokens=500)
        self.assertIn("MAGMA SaaS", res["prompt"])
        self.assertGreater(res["estimated_usd"], 0)

if __name__ == "__main__":
    unittest.main()
