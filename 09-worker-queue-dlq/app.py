"""Háttérfeladat-sor retry és Dead-Letter Queue támogatással."""
from collections import deque
from dataclasses import dataclass
from typing import Callable


@dataclass
class Job:
    job_id: str
    payload: dict
    attempts: int = 0
    max_attempts: int = 3
    last_error: str = ""


class JobQueue:
    def __init__(self) -> None:
        self.pending: deque[Job] = deque()
        self.done: list[Job] = []
        self.dlq: list[Job] = []

    def enqueue(self, job: Job) -> None:
        self.pending.append(job)

    def process_all(self, handler: Callable[[dict], None]) -> None:
        while self.pending:
            job = self.pending.popleft()
            job.attempts += 1
            try:
                handler(job.payload)
                self.done.append(job)
            except Exception as exc:
                job.last_error = str(exc)
                if job.attempts < job.max_attempts:
                    self.pending.append(job)
                else:
                    self.dlq.append(job)
