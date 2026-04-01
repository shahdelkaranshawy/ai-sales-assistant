# AI Sales Assistant (LLM + Knowledge Graph System)

## Overview

AI-powered **B2B sales assistant** concept: prioritize engagement, surface risk, and support decisions using a **property graph** for enterprise CRM-style data, **LLM reasoning** for recommendations and explanations, **proposal generation**, and **deal simulation** for what-if analysis—with **governance** for policy, audit, and human-in-the-loop review.

> This public repository is **documentation-first** (knowledge-graph architecture diagram, graph schema, PGQL examples, user guide) plus **`src/`** — small **runnable Python samples** (query builder, Pydantic deal models, LangChain `@tool` pattern, **LLM prompts & JSON parsing** under `src/llm/`). The full application lives in a private monorepo; no credentials or customer data are included here.

## Problem

Sales managers face **high volumes** of accounts and signals. It is hard to **prioritize** outreach, see **churn or risk** early, and run **credible what-if** scenarios.

## Solution

- **Knowledge graph** (Oracle Autonomous Graph / PGQL) models customers, accounts, opportunities, and related entities.
- **LangChain + LangGraph workflows** (in the full system) drive **explainable** recommendations, **proposal drafting**, and natural-language summaries.
- **Deal simulation** explores revenue, churn, and win-probability style scenarios with **human-in-the-loop** feedback to improve relevance.

## Key Features

- AI-assisted **daily actions** and prioritization (see architecture diagram and `docs/knowledge-graph.md`).
- **Explainable** rationale tied to graph-backed context where possible.
- **Proposal generator** support for structured customer-facing documents.
- **Deal simulation** for scenario exploration.
- **Governance** hooks (policy, audit, human review) alongside **feedback loops** to refine recommendations over time.

## Architecture

High-level view: the **FastAPI** backend serves the **React** app, runs the **PGQL / property-graph query engine**, and orchestrates **LangChain** tools plus **LangGraph** workflows for **recommendations**, **proposal generation**, and **deal simulation**. **Governance** (policy, audit, guardrails, human-in-the-loop) applies across API and agent layers.

```mermaid
flowchart TB
  subgraph ux [Client]
    react[React dashboard]
  end
  subgraph apiLayer [Application layer]
    fastapi[FastAPI REST API]
  end
  subgraph queryEngine [Graph and query engine]
    graphDb[Oracle Property Graph / PGQL]
  end
  subgraph aiStack [AI orchestration]
    lc[LangChain tools connectors RAG]
    lg[LangGraph workflows agents]
  end
  subgraph capabilities [Sales capabilities]
    rec[Recommendations and prioritization]
    proposal[Proposal generator]
    sim[Deal simulator]
  end
  gov[Governance policy audit guardrails human review]
  react --> fastapi
  fastapi --> graphDb
  fastapi --> lc
  lc --> lg
  lg --> graphDb
  lg --> rec
  lg --> proposal
  lg --> sim
  gov -.-> fastapi
  gov -.-> lg
  gov -.-> react
```

### Knowledge graph schema (diagram)

![Knowledge graph schema](architecture/knowledge-graph-schema.svg)

## Demo

Anonymized **UI samples** from the full application (additional tabs and modules are described in `docs/user-manual.md`).

![Morning Brief dashboard — stats, daily focus, and AI-recommended actions](docs/screenshots/morning-brief-dashboard.png)

![Deal simulator — scenario inputs and predicted outcomes](docs/screenshots/deal-simulator.png)

## Tech Stack

Python, LangGraph, LangChain, RAG patterns, Oracle Graph DB, FastAPI, React.

## Repository layout

| Path | Description |
|------|-------------|
| `architecture/knowledge-graph-schema.svg` | Property graph schema diagram (nodes and relationships). |
| `docs/screenshots/` | Sample UI: Morning Brief, Deal simulator (PNG). |
| `docs/app-walkthrough.pdf` | Application walkthrough. |
| `docs/knowledge-graph.md` | Node types, attributes, relationships (schema reference). |
| `docs/user-manual.md` | User guide (Markdown). |
| `sample_queries/sample-pgql-queries.txt` | Sample PGQL-style query patterns. |
| `src/` | Runnable samples: PGQL `QueryBuilder`, deal **Pydantic** models, **LangChain** tools, **`src/llm/`** prompts & parsers (copilot, deal sim, **recommendation engine**) — [`src/README.md`](src/README.md). |

## License

MIT License.
