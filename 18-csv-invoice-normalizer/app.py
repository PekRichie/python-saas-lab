"""CSV számlaadat-normalizáló és hibaszűrő."""
import csv
import io
from decimal import Decimal, InvalidOperation


def normalize_invoices(csv_text: str) -> tuple[list[dict], list[dict]]:
    valid, errors = [], []
    reader = csv.DictReader(io.StringIO(csv_text.strip()))
    for idx, row in enumerate(reader, start=2):
        inv_id = (row.get("invoice_id") or "").strip().upper()
        raw_amt = (row.get("amount") or "").replace(" ", "").replace(",", ".")
        try:
            amt = Decimal(raw_amt)
            if not inv_id or amt <= 0:
                raise ValueError("Hiányzó azonosító vagy nem pozitív összeg")
            valid.append({"invoice_id": inv_id, "amount": amt})
        except (InvalidOperation, ValueError) as exc:
            errors.append({"line": idx, "error": str(exc), "raw": row})
    return valid, errors
