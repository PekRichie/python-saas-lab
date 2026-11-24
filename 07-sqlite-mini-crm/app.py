"""Multi-tenant SQLite Mini-CRM adattár."""
import sqlite3
from dataclasses import dataclass


@dataclass
class Contact:
    id: int
    tenant_id: str
    name: str
    email: str
    stage: str


class CrmRepository:
    def __init__(self, db_path: str = ":memory:") -> None:
        self.conn = sqlite3.connect(db_path)
        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY AUTOINCREMENT, tenant_id TEXT NOT NULL, name TEXT NOT NULL, email TEXT NOT NULL, stage TEXT NOT NULL)"
        )
        self.conn.commit()

    def create(self, tenant_id: str, name: str, email: str, stage: str = "lead") -> Contact:
        cur = self.conn.execute(
            "INSERT INTO contacts (tenant_id, name, email, stage) VALUES (?, ?, ?, ?)",
            (tenant_id, name, email, stage),
        )
        self.conn.commit()
        return Contact(cur.lastrowid, tenant_id, name, email, stage)

    def list_by_tenant(self, tenant_id: str, stage: str | None = None) -> list[Contact]:
        if stage:
            rows = self.conn.execute(
                "SELECT id, tenant_id, name, email, stage FROM contacts WHERE tenant_id = ? AND stage = ?",
                (tenant_id, stage),
            ).fetchall()
        else:
            rows = self.conn.execute(
                "SELECT id, tenant_id, name, email, stage FROM contacts WHERE tenant_id = ?",
                (tenant_id,),
            ).fetchall()
        return [Contact(*r) for r in rows]
