"""Shared AI utility functions with ultra-robust JSON extraction and repair."""

import json
import re
from typing import Optional, Any, Dict


def _clean_reasoning_and_comments(text: str) -> str:
    """Strip reasoning/thought blocks and comments produced by models like GLM-Z1, DeepSeek-R1, QwQ."""
    # 1. Remove <think>...</think> or <thought>...</thought>
    text = re.sub(r"<(think|thought)>[\s\S]*?</\1>", "", text, flags=re.IGNORECASE)
    # 2. If think/thought tag is unclosed, keep the suffix containing the JSON
    has_think_unclosed = "<think>" in text.lower() and "</think>" not in text.lower()
    has_thought_unclosed = "<thought>" in text.lower() and "</thought>" not in text.lower()
    if has_think_unclosed or has_thought_unclosed:
        parts = re.split(r"<(?:think|thought)>", text, maxsplit=1, flags=re.IGNORECASE)
        if len(parts) > 1:
            text = parts[1]
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


def _repair_truncated_json_v1(text: str) -> str:
    """Repair by just closing any open strings, brackets, and braces."""
    text = text.strip()
    if not text:
        return text

    in_string = False
    escape = False
    stack = []
    
    for i, char in enumerate(text):
        if escape:
            escape = False
            continue
        if char == '\\':
            escape = True
            continue
        if char == '"':
            in_string = not in_string
            continue
        if not in_string:
            if char == '{':
                stack.append('{')
            elif char == '[':
                stack.append('[')
            elif char == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
            elif char == ']':
                if stack and stack[-1] == '[':
                    stack.pop()

    repaired = text
    if in_string:
        repaired += '"'
    
    while stack:
        top = stack.pop()
        if top == '{':
            repaired += '}'
        elif top == '[':
            repaired += ']'
            
    return repaired


def _strip_incomplete_tail(text: str) -> str:
    text = text.strip()
    # 1. Strip trailing key and colon: e.g. , "key":
    text = re.sub(r',\s*"[^"]*"\s*:\s*$', '', text)
    # 2. Strip trailing unclosed key: e.g. , "key
    text = re.sub(r',\s*"[^"]*$', '', text)
    # 3. Strip trailing comma: e.g. ,
    text = re.sub(r',\s*$', '', text)
    
    # Also handle the case where it's the first key (no leading comma):
    # e.g., {"key" : or {"key
    text = re.sub(r'\{\s*"[^"]*"\s*:\s*$', '{', text)
    text = re.sub(r'\{\s*"[^"]*$', '{', text)
    
    return text.strip()


def _repair_truncated_json_v2(text: str) -> str:
    """Repair by stripping incomplete trailing keys first, then closing open brackets."""
    text = _strip_incomplete_tail(text)
    return _repair_truncated_json_v1(text)


def _repair_json_and_load(text: str) -> Optional[Dict[str, Any]]:
    # Strategy A: Try simple repair first (keep all list items/values)
    rep1 = _repair_truncated_json_v1(text)
    try:
        res = json.loads(rep1)
        if isinstance(res, dict):
            return res
    except Exception:
        pass

    # Strategy B: If simple repair fails, strip trailing incomplete structures
    rep2 = _repair_truncated_json_v2(text)
    try:
        res = json.loads(rep2)
        if isinstance(res, dict):
            return res
    except Exception:
        pass

    return None


def _fix_unescaped_quotes_in_values(text: str) -> str:
    """Escape any unescaped double quotes inside string values of JSON fields."""
    lines = text.splitlines()
    fixed_lines = []
    
    for line in lines:
        # Match lines like "key": "value" or "key": "value",
        # prefix: "key": "
        # value: the string content of the value
        # suffix: ", or "
        match = re.match(r'^(\s*"[A-Za-z0-9_]+"\s*:\s*")([\s\S]*?)("\s*,?\s*)$', line)
        if match:
            prefix, value, suffix = match.groups()
            # Escape any unescaped double quotes (quotes not preceded by a backslash)
            fixed_value = re.sub(r'(?<!\\)"', r'\"', value)
            line = prefix + fixed_value + suffix
        fixed_lines.append(line)
        
    return '\n'.join(fixed_lines)


def fix_json_structure(text: str) -> str:
    """Repair missing commas and stray brackets in model-generated JSON text."""
    # 1. First, fix any unescaped double quotes in string values
    text = _fix_unescaped_quotes_in_values(text)
    
    lines = text.splitlines()
    cleaned_lines = []
    
    bracket_depth = 0
    in_string = False
    escape = False
    
    for line in lines:
        stripped = line.strip()
        if not stripped:
            cleaned_lines.append(line)
            continue
            
        # Check if this line is a stray closing bracket (e.g., only ']' or '],')
        if re.match(r'^\]\s*,?\s*$', stripped) and bracket_depth == 0:
            continue
            
        # Update bracket depth by scanning the line character by character
        for char in stripped:
            if escape:
                escape = False
                continue
            if char == '\\':
                escape = True
                continue
            if char == '"':
                in_string = not in_string
                continue
            if not in_string:
                if char == '[':
                    bracket_depth += 1
                elif char == ']':
                    bracket_depth = max(0, bracket_depth - 1)
                    
        cleaned_lines.append(line)
        
    # Fix missing commas between fields
    final_lines = []
    for i, line in enumerate(cleaned_lines):
        stripped = line.strip()
        if not stripped:
            final_lines.append(line)
            continue
            
        # Check if the NEXT non-empty line starts a new key-value pair
        has_next_key = False
        for next_line in cleaned_lines[i+1:]:
            next_stripped = next_line.strip()
            if next_stripped:
                if re.match(r'^"[A-Za-z0-9_]+"\s*:', next_stripped):
                    has_next_key = True
                break
                
        if has_next_key:
            # If the current line doesn't end with a comma, or opening bracket/brace, add a comma
            last_char = stripped[-1]
            if last_char not in (',', '[', '{'):
                line = line.rstrip() + ','
                    
        final_lines.append(line)
        
    return '\n'.join(final_lines)


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
    text = fix_json_structure(text)

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

    # Strategy 5: Truncated JSON Repair
    first_brace = text.find("{")
    if first_brace != -1:
        candidate = text[first_brace:]
        res = _repair_json_and_load(candidate)
        if res is not None:
            return res

    return None
