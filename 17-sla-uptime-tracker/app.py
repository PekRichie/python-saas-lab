"""SLA rendelkezésre állás és Error Budget kalkulátor."""


def sla_report(downtime_minutes: float, target_sla: float = 99.9, period_days: int = 30) -> dict[str, float | bool]:
    total_min = period_days * 24 * 60
    allowed_min = total_min * (1.0 - target_sla / 100.0)
    achieved = max(0.0, (1.0 - downtime_minutes / total_min) * 100.0)
    return {
        "achieved_sla": round(achieved, 4),
        "allowed_downtime_min": round(allowed_min, 2),
        "remaining_budget_min": round(allowed_min - downtime_minutes, 2),
        "compliant": achieved >= target_sla,
    }
