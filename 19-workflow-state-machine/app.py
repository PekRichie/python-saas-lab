"""Szigorú átmenet-ellenőrzéssel védett jóváhagyási állapotgép."""
from dataclasses import dataclass, field


ALLOWED_TRANSITIONS = {
    "draft": {"review"},
    "review": {"approved", "rejected"},
    "rejected": {"draft"},
    "approved": {"archived"},
    "archived": set(),
}


@dataclass
class DocumentWorkflow:
    doc_id: str
    state: str = "draft"
    history: list[tuple[str, str]] = field(default_factory=list)

    def transition(self, target: str) -> None:
        if target not in ALLOWED_TRANSITIONS.get(self.state, set()):
            raise ValueError(f"Tiltott átmenet: {self.state} -> {target}")
        self.history.append((self.state, target))
        self.state = target
