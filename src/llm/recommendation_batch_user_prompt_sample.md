# Batch user prompt pattern (sample)

*Production builds this dynamically: one prompt per **batch** of customers, each block = summarized context + enumerated opportunity signals. The model returns **one JSON array** for all customers.*

---

## Header (template)

```
Generate sales recommendations for the following {N} customers managed by sales manager {SALES_MANAGER_ID}.

For EACH customer, generate up to 3 recommendations IF there are genuine opportunities or risks.
If a customer is in good standing with no urgent issues, generate fewer (even 0).

When multiple opportunities exist, prefer the top 3 by impact category (revenue > churn > nps) and expected_impact_aed.

EVERY recommendation MUST include "customer_id" matching the ID in the section below.

=== CUSTOMER 1 (ID: {CUSTOMER_ID}) ===
Customer Summary:
{SUMMARIZED_CONTEXT_FROM_QUERY_ENGINE}

Detected Opportunity Signals:
  - {signal_type}: {details}
  - ...

=== CUSTOMER 2 (ID: ...) ===
...
```

## Footer (output contract)

```
IMPORTANT OUTPUT REQUIREMENTS:
1. Return EXACTLY ONE JSON array with ALL recommendations for ALL customers.
2. Each object MUST include "customer_id".
3. Raw JSON only — no markdown fences; response must start with [ and end with ].

Each recommendation MUST include (names illustrative):
- recommendation_id, customer_id, type, priority, priority_score
- description, reason
- expected_impact_aed, win_probability (or null), expected_churn_reduction (or null), nps_impact_estimate (or null)
- confidence_score, due_date_time (ISO)
- detailed_reasoning (narrative only — no impact math)
- impact_calculation_text (impact math / metrics only)
- action_reference (e.g. signal or rule id)
- key_data_drivers: [{ "driver", "source" }, ...]
- recommended_next_steps: string[]

detailed_reasoning and impact_calculation_text must NOT duplicate each other.
```

---

This pattern is what feeds `RecommendationGenerator._build_batch_prompt` in the full codebase, before optional JSON-prefix retries for stubborn models.
