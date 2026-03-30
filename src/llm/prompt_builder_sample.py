"""
Build the copilot system prompt: static markdown + dynamic session block.

Production uses Pydantic `PageContextInput` from the API layer; this sample uses
a small dataclass. Prompt text is loaded from `copilot_system_prompt_sample.md`.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass
class PageContextSample:
    """Subset of fields the real app sends with each chat turn."""

    page: str
    account_id: str | None = None
    account_name: str | None = None
    deal_id: str | None = None
    deal_name: str | None = None
    metrics: str | None = None


def _base_prompt() -> str:
    md = Path(__file__).with_name("copilot_system_prompt_sample.md").read_text(encoding="utf-8")
    # Strip the title line used only for GitHub display
    lines = md.splitlines()
    if lines and lines[0].startswith("# Sample system prompt"):
        lines = lines[1:]
        while lines and not lines[0].strip():
            lines = lines[1:]
    # Skip italic editor note (not part of model prompt)
    while lines and (lines[0].strip().startswith("*Structure mirrors") or not lines[0].strip()):
        lines = lines[1:]
    return "\n".join(lines).strip()


def build_system_prompt_sample(
    sales_manager_id: str,
    page_context: PageContextSample,
) -> str:
    """Mirror of production `build_system_prompt` — inject session context."""
    block = f"""
## Current session context
- Sales manager ID: {sales_manager_id}
- Current page: {page_context.page}"""
    if page_context.account_id:
        block += f"\n- Account ID: {page_context.account_id}"
    if page_context.account_name:
        block += f"\n- Account name: {page_context.account_name}"
    if page_context.deal_id:
        block += f"\n- Deal ID: {page_context.deal_id}"
    if page_context.deal_name:
        block += f"\n- Deal name: {page_context.deal_name}"
    if page_context.metrics:
        block += f"\n- Visible metrics: {page_context.metrics}"
    return _base_prompt() + block


if __name__ == "__main__":
    ctx = PageContextSample(page="account_detail", account_id="A-100", account_name="Acme Retail")
    print(build_system_prompt_sample("SM-42", ctx)[:1200])
    print("\n--- ... truncated ---\n")
