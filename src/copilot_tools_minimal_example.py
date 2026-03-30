"""
Minimal LangChain @tool pattern used in the copilot layer.
Run: pip install langchain-core && python copilot_tools_minimal_example.py
"""

from __future__ import annotations

from typing import Any, Dict, List, Protocol

from langchain_core.tools import tool

from query_builder import QueryBuilder


class GraphClient(Protocol):
    def execute_query(
        self, query: str, parameters: Dict[str, Any] | None = None
    ) -> List[Dict[str, Any]]:
        ...


class FakeGraphClient:
    def execute_query(
        self, query: str, parameters: Dict[str, Any] | None = None
    ) -> List[Dict[str, Any]]:
        _ = query
        cid = (parameters or {}).get("customer_id", "unknown")
        return [
            {
                "CUSTOMER_ID": cid,
                "CUSTOMER_NAME": "Example Retail Co.",
                "NPS_SCORE": 42,
                "INDUSTRY": "Retail",
            }
        ]


def build_sample_tools(graph: GraphClient):
    @tool
    def lookup_customer_profile(customer_id: str) -> dict:
        """Load core customer attributes from the knowledge graph."""
        qb = QueryBuilder()
        q, params = (
            qb.select("c.CUSTOMER_ID", "c.CUSTOMER_NAME", "c.NPS_SCORE", "c.INDUSTRY")
            .match("(c:CUSTOMER)")
            .where("c.CUSTOMER_ID = :customer_id", "customer_id", customer_id)
            .limit(1)
            .build()
        )
        rows = graph.execute_query(q, params)
        return rows[0] if rows else {"error": "not_found", "customer_id": customer_id}

    @tool
    def summarize_prioritization_context(sales_manager_id: str) -> dict:
        """Placeholder: production loads morning-brief + actions from graph + SQL."""
        return {
            "sales_manager_id": sales_manager_id,
            "hint": "Wire to MorningBriefQueries + ActionsRepository in real app.",
            "open_high_priority_actions": 3,
        }

    return [lookup_customer_profile, summarize_prioritization_context]


if __name__ == "__main__":
    tools = build_sample_tools(FakeGraphClient())
    for t in tools:
        if "customer" in t.name:
            print(t.name, "->", t.invoke({"customer_id": "CUST-1"}))
        else:
            print(t.name, "->", t.invoke({"sales_manager_id": "SM-9"}))
