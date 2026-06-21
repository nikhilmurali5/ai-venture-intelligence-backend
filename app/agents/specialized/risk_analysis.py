from app.services.json_parser import safe_json
from app.services.llm_service import (
    ask_llm,
    parse_json_response
)

def analyze_risk(idea: str):

    prompt = f"""
    Analyze risks for:

    {idea}

    Return ONLY valid JSON.

    {{
        "risk_score": 40,
        "risk_level": "Medium",
        "key_risks": [
            "Example risk"
        ]
    }}
    """

    result = ask_llm(prompt)

    return safe_json(result)