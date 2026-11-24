"""Mini REST API Router és Middleware lánc."""
from dataclasses import dataclass, field
from typing import Callable


@dataclass
class Request:
    method: str
    path: str
    headers: dict[str, str] = field(default_factory=dict)
    body: dict = field(default_factory=dict)


@dataclass
class Response:
    status: int
    body: dict


class MiniRouter:
    def __init__(self) -> None:
        self._routes: dict[tuple[str, str], Callable[[Request], Response]] = {}
        self._middlewares: list[Callable] = []

    def route(self, method: str, path: str):
        def deco(fn: Callable[[Request], Response]):
            self._routes[(method.upper(), path)] = fn
            return fn
        return deco

    def use(self, mw: Callable) -> None:
        self._middlewares.append(mw)

    def dispatch(self, req: Request) -> Response:
        handler = self._routes.get((req.method.upper(), req.path))
        if not handler:
            return Response(404, {"error": "Not Found"})
        chain = handler
        for mw in reversed(self._middlewares):
            nxt = chain
            chain = lambda r, m=mw, n=nxt: m(r, n)
        return chain(req)
