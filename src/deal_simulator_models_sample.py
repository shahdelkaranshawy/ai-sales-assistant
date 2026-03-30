"""
Pydantic models for deal simulation & AI suggestions — condensed from production.
Requires: pip install pydantic>=2
"""

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field, model_validator


class PaymentTermsEnum(str, Enum):
    MONTHLY = "monthly"
    QUARTERLY = "quarterly"
    UPFRONT = "upfront"


class CustomerConstraintsInput(BaseModel):
    model_config = ConfigDict(extra="allow")

    max_budget_monthly: Optional[float] = Field(None, ge=0)
    hardware_allowed: Optional[bool] = Field(True)
    notes: Optional[str] = None


class DealSimulateRequest(BaseModel):
    customer_id: str
    rate_plan_code: Optional[str] = None
    product_id: Optional[str] = None
    rate_plan_codes: Optional[List[str]] = None
    term_months: int = Field(..., ge=1, le=120)
    discount_pct: float = Field(..., ge=0, le=100)
    quantity: int = Field(1, ge=1)
    payment_terms: PaymentTermsEnum = PaymentTermsEnum.MONTHLY
    customer_constraints: Optional[CustomerConstraintsInput] = None

    @model_validator(mode="after")
    def require_rate_plan_or_product(self):
        codes = self.rate_plan_codes or []
        if not (
            self.rate_plan_code
            or self.product_id
            or (codes and any(c and str(c).strip() for c in codes))
        ):
            raise ValueError(
                "At least one of rate_plan_code, product_id, or rate_plan_codes is required"
            )
        return self


class DealSimulateResponse(BaseModel):
    win_probability: float = Field(..., ge=0, le=1)
    revenue: float = Field(..., ge=0)
    margin_pct: float = Field(..., ge=0, le=1)
    churn_impact: float
    nps_impact: int
    approval_required: Optional[str] = None
    risk_flags: List[str] = Field(default_factory=list)
    budget_fit: str
    otc: Optional[float] = Field(None, ge=0)
    monthly_recurring: Optional[float] = Field(None, ge=0)


class DealSuggestionItem(BaseModel):
    title: str
    reason: str
    apply_payload: Dict[str, Any] = Field(
        ...,
        description='e.g. {"change_discount": 12} or {"add_product": "PLAN_X"}',
    )
    delta_win_probability: float
    delta_revenue_aed_per_year: float
    rate_plan_desc: Optional[str] = None


if __name__ == "__main__":
    req = DealSimulateRequest(
        customer_id="ACC-42",
        rate_plan_code="ENTERPRISE_5G",
        term_months=24,
        discount_pct=10,
        quantity=2,
    )
    print("request:", req.model_dump(mode="json"))
    out = DealSimulateResponse(
        win_probability=0.62,
        revenue=480_000.0,
        margin_pct=0.28,
        churn_impact=-0.03,
        nps_impact=5,
        budget_fit="Good",
        risk_flags=[],
    )
    print("response:", out.model_dump(mode="json"))
