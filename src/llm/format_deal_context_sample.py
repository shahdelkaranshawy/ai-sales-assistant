"""
Format deal + customer blocks for the simulator LLM prompt (readable context string).

Production takes a rich `SimulatorContext`; here we use plain dataclasses so the
sample runs without the private API package.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class DealInputs:
    rate_plan_code: str
    rate_plan_desc: str | None
    term_months: int
    discount_pct: float
    quantity: int
    payment_terms: str


@dataclass
class CustomerSummary:
    segment: str
    annual_arpu: float
    tenure_months: int | None
    churn_score: float


def format_context_blocks(
    deal: DealInputs,
    customer: CustomerSummary,
    revenue: float,
    margin_pct: float,
    monthly_price: float,
    budget_ok: str,
) -> str:
    rp = deal.rate_plan_code
    if deal.rate_plan_desc and str(deal.rate_plan_desc).strip():
        rp = f"{deal.rate_plan_code} – {deal.rate_plan_desc.strip()}"
    ten = customer.tenure_months if customer.tenure_months is not None else "unknown"
    return f"""--- Deal (inputs) ---
- Product / rate plan: {rp}
- Term: {deal.term_months} months
- Discount: {deal.discount_pct}%
- Quantity: {deal.quantity}
- Payment terms: {deal.payment_terms}

--- Customer context ---
- Segment: {customer.segment}
- Annual ARPU: {customer.annual_arpu:.0f}
- Tenure (months): {ten}
- Churn score (0-1): {customer.churn_score:.2f}

--- Derived metrics ---
- Revenue (OTC + MRC×term): {revenue:.0f}
- Margin (0-1): {margin_pct:.2f}
- Monthly price: {monthly_price:.2f}
- Budget: {budget_ok}
"""


def build_deal_prediction_prompt_sample(context_blocks: str, revenue: float) -> str:
    """Fill `deal_simulator_llm_prompt_sample.md` placeholders (inline for simplicity)."""
    return f"""You are a sales deal analyst. Use only the facts below.

{context_blocks}

Predict win probability, revenue, margin, churn impact, NPS impact, and risk flags.
Use computed revenue ({revenue:.0f}) unless you have a strong reason to adjust.
Respond with ONLY valid JSON with keys: win_probability, revenue, margin_pct, churn_impact, nps_impact, risk_flags.
"""


if __name__ == "__main__":
    d = DealInputs("ENT_5G", "Enterprise 5G", 24, 12.0, 1, "monthly")
    c = CustomerSummary("Gold", 480_000.0, 18, 0.35)
    blocks = format_context_blocks(d, c, revenue=920_000.0, margin_pct=0.29, monthly_price=38_000.0, budget_ok="within budget")
    print(blocks)
    print("---")
    print(build_deal_prediction_prompt_sample(blocks, 920_000.0)[:800])
