"""AI Prompt sablonmotor és modell-költségbecslő."""
from dataclasses import dataclass


@dataclass(frozen=True)
class ModelPricing:
    name: str
    input_per_1m_usd: float
    output_per_1m_usd: float


def estimate_tokens(text: str) -> int:
    return max(1, (len(text) + 3) // 4)


def render_and_price(template: str, variables: dict[str, str], pricing: ModelPricing, expected_output_tokens: int = 300) -> dict[str, object]:
    prompt = template.format(**variables)
    in_tok = estimate_tokens(prompt)
    cost = (in_tok / 1_000_000) * pricing.input_per_1m_usd + (expected_output_tokens / 1_000_000) * pricing.output_per_1m_usd
    return {"prompt": prompt, "input_tokens": in_tok, "output_tokens": expected_output_tokens, "estimated_usd": round(cost, 6)}
