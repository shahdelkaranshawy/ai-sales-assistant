"""
Illustrates how batch recommendation prompts are stitched (header + sections + footer).

Production loads real summaries from ContextProcessor and opportunity rows from the
query engine; this uses placeholder strings.
"""

from __future__ import annotations


def build_batch_user_prompt_sample(
    sales_manager_id: str,
    customers: list[tuple[str, str, list[tuple[str, str]]]],
) -> str:
    """
    Parameters
    ----------
    customers : list of (customer_id, summary_text, [(signal_type, details), ...])
    """
    n = len(customers)
    header = (
        f"Generate sales recommendations for the following {n} customers "
        f"managed by sales manager {sales_manager_id}.\n"
        "For EACH customer, generate up to 3 recommendations IF there are genuine opportunities or risks.\n"
        'EVERY recommendation object MUST include a "customer_id" field.\n\n'
    )
    sections: list[str] = []
    for idx, (cid, summary, signals) in enumerate(customers, 1):
        opp_lines = "".join(f"  - {st}: {det}\n" for st, det in signals)
        sections.append(
            f"=== CUSTOMER {idx} (ID: {cid}) ===\n"
            f"Customer Summary:\n{summary}\n\n"
            f"Detected Opportunity Signals:\n{opp_lines}\n"
        )
    footer = """
IMPORTANT OUTPUT REQUIREMENTS:
Return ONE JSON array only; each item must include customer_id, type, priority,
expected_impact_aed, detailed_reasoning, impact_calculation_text, and other required fields.
Start with [ and end with ].
""".strip()
    return header + "\n".join(sections) + "\n" + footer


if __name__ == "__main__":
    demo = build_batch_user_prompt_sample(
        "SM-100",
        [
            (
                "C-1",
                "Segment: Enterprise. MRC sum: 45,000 AED. Churn score: 0.42. Gap to target: 120,000 AED.",
                [
                    ("contract_ending", "Contract ends in 45 days"),
                    ("high_churn_score", "Churn score above portfolio median"),
                ],
            ),
        ],
    )
    print(demo[:900])
    print("\n--- ... ---\n")
