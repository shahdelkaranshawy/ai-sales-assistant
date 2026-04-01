# LLM & prompts (samples)

Anonymized excerpts aligned with production: **copilot**, **deal simulator**, and **recommendation engine**. Not verbatim dumps (those include employer branding, full tool lists, long formula tables, and internal signal catalogs).

| File | Purpose |
|------|---------|
| [`copilot_system_prompt_sample.md`](copilot_system_prompt_sample.md) | Copilot **system** prompt structure: role, read-only rule, tool categories, style, metrics, guardrails. |
| [`prompt_builder_sample.py`](prompt_builder_sample.py) | Loads copilot markdown + **session context** (page, account, deal). |
| [`deal_simulator_llm_prompt_sample.md`](deal_simulator_llm_prompt_sample.md) | **JSON-only** deal outcome prediction template + placeholders. |
| [`format_deal_context_sample.py`](format_deal_context_sample.py) | **Context blocks** for the deal prediction prompt. |
| [`json_response_parser_sample.py`](json_response_parser_sample.py) | Parse model output: fences, braces, comma-separated numbers. |
| [`recommendation_engine_system_prompt_sample.md`](recommendation_engine_system_prompt_sample.md) | Recommendation **system** prompt — principles, allowed `type` values, ranking, **detailed_reasoning** vs **impact_calculation_text** split, catalog constraints. |
| [`recommendation_batch_user_prompt_sample.md`](recommendation_batch_user_prompt_sample.md) | **Batch user** prompt: per-customer sections + **single JSON array** output contract. |
| [`recommendation_prompt_builder_sample.py`](recommendation_prompt_builder_sample.py) | Minimal **Python** stitch of header + customer blocks + footer (like `_build_batch_prompt`). |

```bash
cd llm
python3 prompt_builder_sample.py
python3 format_deal_context_sample.py
python3 json_response_parser_sample.py
python3 recommendation_prompt_builder_sample.py
```

Production recommendation code lives in `RecommendationGenerator` (`generator.py`): it adds full **expected_impact_aed / churn / NPS / win-probability** instruction tables, JSON-array retry prefixes, caching, and concurrency. See also `architecture/KG_updated_v9.svg` and `docs/knowledge-graph.md` for domain context.
