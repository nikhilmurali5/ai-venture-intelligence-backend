from app.services.json_parser import safe_json
from app.services.llm_service import (
    ask_llm,
    parse_json_response
)

def forecast_trends(idea: str):

    prompt = f"""
    Forecast future trends for:

    {idea}

    Return ONLY valid JSON.

    {{
        "trend_score": 90,
        "future_outlook": "Positive",
        "key_trends": [
            "Sustainability",
            "Automation",
            "Digital Sales"
        ]
    }}
    """

    result = ask_llm(prompt)

    return safe_json(result)