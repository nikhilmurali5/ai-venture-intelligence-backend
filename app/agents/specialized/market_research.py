import json
from app.services.json_parser import safe_json
from app.services.llm_service import ask_llm


def analyze_market(idea: str):

    prompt = f"""
    Analyze the market potential for:

    {idea}

    Return ONLY valid JSON.

    Example:

    {{
        "market_score": 85,
        "market_size": "Large",
        "demand": "High"
    }}

    Do not return explanations.
    Do not return markdown.
    Only JSON.
    """

    result = ask_llm(prompt)

    try:
        return safe_json(result)

    except Exception:
        return {
            "market_score": 50,
            "market_size": "Unknown",
            "demand": "Unknown"
        }