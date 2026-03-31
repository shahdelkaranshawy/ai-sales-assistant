# AI Sales Assistant (LLM + Knowledge Graph System)

## Overview

AI-powered **B2B sales assistant** concept: prioritize engagement, surface risk, and support decisions using a **property graph** for enterprise CRM-style data, **LLM reasoning** for recommendations and explanations, and **deal simulation** for what-if analysis.

> This public repository is **documentation-first** (architecture PDFs, graph schema, PGQL examples, user guide) plus **`src/`** — small **runnable Python samples** (query builder, Pydantic deal models, LangChain `@tool` pattern, **LLM prompts & JSON parsing** under `src/llm/`). The full application lives in a private monorepo; no credentials or customer data are included here.

## Problem

Sales managers face **high volumes** of accounts and signals. It is hard to **prioritize** outreach, see **churn or risk** early, and run **credible what-if** scenarios.

## Solution

- **Knowledge graph** (Oracle Autonomous Graph / PGQL) models customers, accounts, opportunities, and related entities.
- **LLM + LangGraph-style workflows** (in the full system) generate **explainable** recommendations and natural-language summaries.
- **Deal simulation** explores revenue, churn, and win-probability style scenarios with **human-in-the-loop** feedback to improve relevance.

## Key Features

- AI-assisted **daily actions** and prioritization (see architecture PDFs).
- **Explainable** rationale tied to graph-backed context where possible.
- **Deal simulation** for scenario exploration.
- **Feedback loops** to refine recommendations over time.

## Architecture

```mermaid
flowchart LR
  react[React dashboard]
  api[FastAPI backend]
  graphDb[Oracle Property Graph PGQL]
  llm[LLM LangGraph workflows]
  sim[Deal simulator]
  react --> api
  api --> graphDb
  api --> llm
  api --> sim
```

## Tech Stack

Python, LangGraph, LangChain, RAG patterns, Oracle Graph DB, FastAPI, React.

## Repository layout

| Path | Description |
|------|-------------|
| `architecture/graph-design.pdf` | Graph database design (e&). |
| `architecture/ai-action-recommender.pdf` | AI / action recommender overview. |
| `docs/app-walkthrough.pdf` | Application walkthrough. |
| `docs/knowledge-graph.md` | Node types, attributes, relationships (schema reference). |
| `docs/user-manual.md` | User guide (Markdown). |
| `sample_queries/sample-pgql-queries.txt` | Sample PGQL-style query patterns. |
| `src/` | Runnable samples: PGQL `QueryBuilder`, deal **Pydantic** models, **LangChain** tools, **`src/llm/`** prompts & parsers (copilot, deal sim, **recommendation engine**) — [`src/README.md`](src/README.md). |

## Results

- **Design-level** artifact set suitable for MSc admissions: shows you can specify **real AI + graph** systems without leaking production implementation or data.

## License

MIT License.
