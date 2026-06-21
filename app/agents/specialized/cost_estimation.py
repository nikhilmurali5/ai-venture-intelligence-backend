from app.services.json_parser import safe_json
from app.services.llm_service import (
    ask_llm,
    parse_json_response
)

def estimate_cost(idea: str):

    prompt = f"""
    Estimate startup costs for:

    {idea}

    Return ONLY valid JSON.

    {{
        "estimated_cost": 500000,
        "cost_level": "Medium",
        "major_expenses": [
            "Machinery",
            "Raw Materials",
            "Licenses"
        ]
    }}
    """

    result = ask_llm(prompt)

    return safe_json(result)