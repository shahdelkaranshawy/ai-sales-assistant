# Sample code

Small, **self-contained** excerpts that mirror patterns in the full sales assistant: **PGQL**, **Pydantic** deal APIs, **LangChain tools**, and **LLM prompts / parsing**. No secrets, no database drivers.

## Python modules (repo root of `src/`)

| File | What it shows |
|------|----------------|
| [`query_builder.py`](query_builder.py) | Fluent **PGQL** string builder used before sending queries to the property graph. |
| [`example_build_customer_pgql.py`](example_build_customer_pgql.py) | Runnable demo: prints a customer→account query + parameters. |
| [`deal_simulator_models_sample.py`](deal_simulator_models_sample.py) | **Pydantic** request/response models for simulate + AI suggestion items. |
| [`copilot_tools_minimal_example.py`](copilot_tools_minimal_example.py) | **LangChain `@tool`** functions with injected graph client (fake implementation). |

## LLM & prompts

See **[`llm/README.md`](llm/README.md)** — copilot + deal simulator + **recommendation engine** prompt patterns (system + batch user prompt, field split for explainability, JSON extraction).

## Run locally

```bash
cd src
pip install -r requirements.txt
python example_build_customer_pgql.py
python deal_simulator_models_sample.py
python copilot_tools_minimal_example.py
python llm/prompt_builder_sample.py
python llm/format_deal_context_sample.py
python llm/json_response_parser_sample.py
python llm/recommendation_prompt_builder_sample.py
```

The production app adds FastAPI routers, real `GraphDBInterface`, SQLAlchemy repos, fifteen+ tools, and full-length domain prompts; see `docs/knowledge-graph.md` and architecture PDFs for the full design.

