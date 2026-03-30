"""
PGQL query builder (builder pattern) — excerpt from the production sales-assistant backend.

Oracle Property Graph queries use SELECT … FROM MATCH … WHERE … semantics.
This module has **no** database or FastAPI dependencies; safe to read in isolation.
"""

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, Optional


class QueryType(Enum):
    """Query clause types (reserved for extensions)."""

    SELECT = "SELECT"
    MATCH = "MATCH"
    WHERE = "WHERE"
    ORDER_BY = "ORDER BY"
    LIMIT = "LIMIT"


class QueryBuilder:
    """Fluent builder for PGQL-style graph queries."""

    def __init__(self) -> None:
        self.select_clause: list[str] = []
        self.match_clauses: list[str] = []
        self.where_clauses: list[str] = []
        self.order_by_clauses: list[str] = []
        self.offset_value: Optional[int] = None
        self.limit_value: Optional[int] = None
        self.parameters: Dict[str, Any] = {}

    def select(self, *attributes: str) -> "QueryBuilder":
        self.select_clause.extend(attributes)
        return self

    def match(self, pattern: str) -> "QueryBuilder":
        """Pattern example: (c:CUSTOMER)-[:HAS_ACCOUNT]->(a:ACCOUNT)"""
        self.match_clauses.append(pattern)
        return self

    def where(
        self,
        condition: str,
        param_name: Optional[str] = None,
        param_value: Any = None,
    ) -> "QueryBuilder":
        self.where_clauses.append(condition)
        if param_name is not None and param_value is not None:
            self.parameters[param_name] = param_value
        return self

    def and_where(
        self,
        condition: str,
        param_name: Optional[str] = None,
        param_value: Any = None,
    ) -> "QueryBuilder":
        return self.where(condition, param_name, param_value)

    def order_by(self, expression: str, descending: bool = False) -> "QueryBuilder":
        direction = "DESC" if descending else "ASC"
        self.order_by_clauses.append(f"{expression} {direction}")
        return self

    def offset(self, count: int) -> "QueryBuilder":
        self.offset_value = count
        return self

    def limit(self, count: int) -> "QueryBuilder":
        self.limit_value = count
        return self

    def build(self) -> tuple[str, Dict[str, Any]]:
        parts: list[str] = []
        if self.select_clause:
            parts.append("SELECT " + ", ".join(self.select_clause))
        else:
            parts.append("SELECT *")
        if self.match_clauses:
            match_str = ", ".join(f"MATCH {m}" for m in self.match_clauses)
            parts.append(f"FROM {match_str}")
        if self.where_clauses:
            parts.append("WHERE " + " AND ".join(self.where_clauses))
        if self.order_by_clauses:
            parts.append("ORDER BY " + ", ".join(self.order_by_clauses))
        if self.offset_value is not None and self.offset_value > 0:
            parts.append(f"OFFSET {self.offset_value}")
        if self.limit_value is not None:
            parts.append(f"LIMIT {self.limit_value}")
        return "\n".join(parts), dict(self.parameters)

    def reset(self) -> "QueryBuilder":
        self.select_clause.clear()
        self.match_clauses.clear()
        self.where_clauses.clear()
        self.order_by_clauses.clear()
        self.offset_value = None
        self.limit_value = None
        self.parameters.clear()
        return self
