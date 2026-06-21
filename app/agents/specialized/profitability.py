import json
from app.services.llm_service import ask_llm
from app.services.json_parser import safe_json
def analyze_profitability(idea: str):

    prompt = f"""
    Analyze profitability for:

    {idea}

    Return ONLY valid JSON.

    {{
        "profitability_score": 85,
        "estimated_margin": "35%"
    }}
    """

    result = ask_llm(prompt)

    print("PROFITABILITY RESPONSE:")
    print(result)

    result = result.replace("```json", "")
    result = result.replace("```", "")
    result = result.strip()

    return safe_json(result)