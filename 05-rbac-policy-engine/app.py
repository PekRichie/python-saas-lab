"""Multi-tenant RBAC jogosultságkezelő motor."""
from dataclasses import dataclass, field


@dataclass
class Role:
    name: str
    permissions: set[str] = field(default_factory=set)


class RbacEngine:
    def __init__(self) -> None:
        self._roles: dict[str, Role] = {}
        self._assignments: dict[tuple[str, str], set[str]] = {}

    def define_role(self, name: str, permissions: set[str]) -> None:
        self._roles[name] = Role(name=name, permissions=set(permissions))

    def assign(self, tenant_id: str, user_id: str, role_name: str) -> None:
        if role_name not in self._roles:
            raise KeyError(f"Ismeretlen szerepkör: {role_name}")
        self._assignments.setdefault((tenant_id, user_id), set()).add(role_name)

    def can(self, tenant_id: str, user_id: str, permission: str) -> bool:
        resource = permission.split(":", 1)[0]
        for rname in self._assignments.get((tenant_id, user_id), set()):
            perms = self._roles[rname].permissions
            if "*" in perms or permission in perms or f"{resource}:*" in perms:
                return True
        return False
