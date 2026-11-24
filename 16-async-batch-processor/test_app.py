import asyncio
import unittest
from app import run_bounded

class TestAsync(unittest.TestCase):
    def test_concurrency_limit(self):
        active = [0]; peak = [0]
        async def work(x):
            active[0] += 1; peak[0] = max(peak[0], active[0])
            await asyncio.sleep(0.01)
            active[0] -= 1
            return x * 2
        res = asyncio.run(run_bounded([1, 2, 3, 4, 5, 6], work, max_concurrency=2))
        self.assertEqual(res, [2, 4, 6, 8, 10, 12])
        self.assertLessEqual(peak[0], 2)

if __name__ == "__main__":
    unittest.main()
