"""SaaS csomagváltás időarányosító (proration) és ÁFA kalkulátor."""
from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP


@dataclass(frozen=True)
class Plan:
    code: str
    monthly_net_huf: Decimal


def calculate_proration(old_plan: Plan, new_plan: Plan, days_remaining: int, cycle_days: int = 30, vat_rate: Decimal = Decimal("0.27")) -> dict[str, Decimal]:
    if days_remaining < 0 or days_remaining > cycle_days:
        raise ValueError("Érvénytelen hátralévő napszám.")
    ratio = Decimal(days_remaining) / Decimal(cycle_days)
    credit = (old_plan.monthly_net_huf * ratio).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    charge = (new_plan.monthly_net_huf * ratio).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    net_delta = charge - credit
    vat = (net_delta * vat_rate).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    return {"credit_net": credit, "charge_net": charge, "net_delta": net_delta, "vat": vat, "gross_delta": net_delta + vat}
