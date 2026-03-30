"""
Extract a JSON object from messy LLM text (markdown fences, prose, commas in numbers).

Adapted from the deal-simulator integration; standalone — no FastAPI imports.
"""

from __future__ import annotations

import json
import re
from typing import Any, Dict, Optional

_THOUSANDS_SEP_RE = re.compile(r"(\d),(\d{3})(?=\D|$)")


def sanitize_llm_json(js: str) -> str:
    prev = None
    while prev != js:
        prev = js
        js = _THOUSANDS_SEP_RE.sub(r"\1\2", js)
    return js


def extract_json_object(text: str) -> Optional[Dict[str, Any]]:
    """Return first dict-like JSON object found in `text`, or None."""
    if not text or not text.strip():
        return None
    text = text.strip()
    m = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", text, re.DOTALL)
    if m:
        raw = m.group(1).strip()
    elif text.startswith("{"):
        brace_count = 0
        end = 0
        for i, ch in enumerate(text):
            if ch == "{":
                brace_count += 1
            elif ch == "}":
                brace_count -= 1
                if brace_count == 0:
                    end = i + 1
                    break
        raw = text[:end]
    else:
        m2 = re.search(r"(\{[\s\S]*\})", text)
        raw = m2.group(1) if m2 else None
    if not raw:
        return None
    raw = sanitize_llm_json(raw)
    try:
        out = json.loads(raw)
        return out if isinstance(out, dict) else None
    except json.JSONDecodeError:
        return None


if __name__ == "__main__":
    samples = [
        '{"win_probability": 0.7, "revenue": 1,234,567}',
        "```json\n{\"a\": 1}\n```",
        "Here you go: {\"win_probability\": 0.5, \"revenue\": 100}",
    ]
    for s in samples:
        print(extract_json_object(s))
