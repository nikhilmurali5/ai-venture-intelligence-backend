from app.services.llm_service import ask_llm
from app.services.json_parser import safe_json


def analyze_swot(idea: str):

    prompt = f"""
    Analyze this business idea:

    {idea}

    Return ONLY JSON:

    {{
        "strengths": [],
        "weaknesses": [],
        "opportunities": [],
        "threats": []
    }}
    """

    result = ask_llm(prompt)

    return safe_json(result)