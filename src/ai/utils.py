"""Shared AI utility functions with ultra-robust JSON extraction and repair."""

import json
import re
from typing import Optional, Any, Dict


def _clean_reasoning_and_comments(text: str) -> str:
    """Strip reasoning/thought blocks and comments produced by models like GLM-Z1, DeepSeek-R1, QwQ."""
    # 1. Remove <think>...</think> or <thought>...</thought>
    text = re.sub(r"<(think|thought)>[\s\S]*?</\1>", "", text, flags=re.IGNORECASE)
    # 2. If think tag is unclosed at the start
    if "<think>" in text.lower() and "</think>" not in text.lower():
        text = text.split("<think>", 1)[0]
    # 3. Remove markdown comments // ...
    text = re.sub(r"^[ \t]*//.*$", "", text, flags=re.MULTILINE)
    return text.strip()


def _repair_json_string(text: str) -> str:
    """Apply common JSON repair heuristics."""
    # Fix trailing commas before } or ]
    text = re.sub(r",\s*([\]}])", r"\1", text)
    # Replace Chinese quotes with standard quotes
    text = text.replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
    return text


def parse_json_response(response: Any) -> Optional[Dict[str, Any]]:
    """Try multiple robust strategies to extract a JSON object from an AI response.

    Returns the parsed dict, or None if all strategies fail.
    """
    if response is None:
        return None
    if isinstance(response, dict):
        return response

    text = str(response).strip()
    text = _clean_reasoning_and_comments(text)

    # Strategy 1: Direct JSON parsing
    try:
        res = json.loads(text)
        if isinstance(res, dict):
            return res
    except (json.JSONDecodeError, ValueError):
        pass

    # Strategy 2: Code blocks ```json ... ``` or ``` ... ``` (search from right to left to get final output)
    code_blocks = re.findall(r"```(?:json)?\s*([\s\S]*?)\s*```", text, flags=re.IGNORECASE)
    for block in reversed(code_blocks):
        block = block.strip()
        try:
            res = json.loads(block)
            if isinstance(res, dict):
                return res
        except (json.JSONDecodeError, ValueError):
            pass
        # Try repaired block
        try:
            res = json.loads(_repair_json_string(block))
            if isinstance(res, dict):
                return res
        except (json.JSONDecodeError, ValueError):
            pass

    # Strategy 3: Find outermost JSON object with brace matching (search from the end)
    # Search backwards for the last '}' and find its matching '{'
    last_brace = text.rfind("}")
    if last_brace != -1:
        depth = 0
        for i in range(last_brace, -1, -1):
            if text[i] == "}":
                depth += 1
            elif text[i] == "{":
                depth -= 1
                if depth == 0:
                    candidate = text[i : last_brace + 1]
                    try:
                        res = json.loads(candidate)
                        if isinstance(res, dict):
                            return res
                    except (json.JSONDecodeError, ValueError):
                        try:
                            res = json.loads(_repair_json_string(candidate))
                            if isinstance(res, dict):
                                return res
                        except (json.JSONDecodeError, ValueError):
                            pass

    # Strategy 4: Regex greedy match for { ... }
    match = re.search(r"(\{[\s\S]*\})", text)
    if match:
        candidate = match.group(1)
        try:
            res = json.loads(candidate)
            if isinstance(res, dict):
                return res
        except (json.JSONDecodeError, ValueError):
            try:
                res = json.loads(_repair_json_string(candidate))
                if isinstance(res, dict):
                    return res
            except (json.JSONDecodeError, ValueError):
                pass

    return None
