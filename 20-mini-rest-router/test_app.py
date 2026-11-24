import unittest
from app import MiniRouter, Request, Response

class TestRouter(unittest.TestCase):
    def test_dispatch_and_middleware(self):
        r = MiniRouter()
        r.use(lambda req, nxt: Response(nxt(req).status, {**nxt(req).body, "mw": True}))
        @r.route("GET", "/health")
        def health(_req):
            return Response(200, {"ok": True})
        res = r.dispatch(Request("GET", "/health"))
        self.assertEqual(res.status, 200)
        self.assertTrue(res.body["mw"])
        self.assertEqual(r.dispatch(Request("GET", "/missing")).status, 404)

if __name__ == "__main__":
    unittest.main()
