"""Hierarchikus multi-tenant konfiguráció-kezelő."""


class TenantConfigResolver:
    def __init__(self, defaults: dict) -> None:
        self.defaults = dict(defaults)
        self.plan_overrides: dict[str, dict] = {}
        self.tenant_overrides: dict[str, dict] = {}

    def set_plan(self, plan: str, values: dict) -> None:
        self.plan_overrides[plan] = dict(values)

    def set_tenant(self, tenant_id: str, values: dict) -> None:
        self.tenant_overrides[tenant_id] = dict(values)

    def resolve(self, tenant_id: str, plan: str) -> dict:
        out = dict(self.defaults)
        out.update(self.plan_overrides.get(plan, {}))
        out.update(self.tenant_overrides.get(tenant_id, {}))
        return out
