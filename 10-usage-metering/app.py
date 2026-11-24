"""Használatalapú SaaS fogyasztásmérő és számlázási aggregátor."""
from collections import defaultdict
from decimal import Decimal


class UsageMeter:
    def __init__(self, included_units: int, unit_price_huf: Decimal) -> None:
        self.included_units = included_units
        self.unit_price_huf = unit_price_huf
        self._usage: dict[str, int] = defaultdict(int)

    def record(self, tenant_id: str, units: int) -> None:
        if units < 0:
            raise ValueError("Negatív fogyasztás nem rögzíthető.")
        self._usage[tenant_id] += units

    def bill_summary(self, tenant_id: str) -> dict[str, object]:
        used = self._usage.get(tenant_id, 0)
        billable = max(0, used - self.included_units)
        return {"tenant_id": tenant_id, "used": used, "billable": billable, "overage_huf": Decimal(billable) * self.unit_price_huf}
