import unittest
from app import Job, JobQueue

class TestQueue(unittest.TestCase):
    def test_retry_and_dlq(self):
        q = JobQueue()
        q.enqueue(Job("ok", {"fail_times": 1}))
        q.enqueue(Job("bad", {"fail_times": 5}, max_attempts=2))
        seen = {}
        def handle(p):
            k = p["fail_times"]
            seen[k] = seen.get(k, 0) + 1
            if seen[k] <= k:
                raise RuntimeError("transient")
        q.process_all(handle)
        self.assertEqual(len(q.done), 1)
        self.assertEqual(len(q.dlq), 1)

if __name__ == "__main__":
    unittest.main()
