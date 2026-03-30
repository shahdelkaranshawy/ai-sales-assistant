#!/usr/bin/env python3
"""Run: python example_build_customer_pgql.py (from this directory)"""

from __future__ import annotations

from query_builder import QueryBuilder


def main() -> None:
    qb = QueryBuilder()
    query, params = (
        qb.select("c.CUSTOMER_ID", "c.CUSTOMER_NAME", "a.ACCOUNT_ID", "a.ARPU")
        .match("(c:CUSTOMER)-[:HAS_ACCOUNT]->(a:ACCOUNT)")
        .where("c.CUSTOMER_ID = :customer_id", "customer_id", "CUST-1001")
        .order_by("a.ARPU", descending=True)
        .limit(20)
        .build()
    )
    print("--- PGQL ---")
    print(query)
    print("--- parameters ---")
    print(params)


if __name__ == "__main__":
    main()
