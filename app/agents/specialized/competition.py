import json
from app.services.llm_service import ask_llm
from app.services.json_parser import safe_json
def analyze_competition(idea: str):

    prompt = f"""
    Analyze competition for:

    {idea}

    Return ONLY valid JSON.

    {{
        "competition_score": 70,
        "competition_level": "Medium"
    }}
    """

    result = ask_llm(prompt)

    print("GROQ RESPONSE:")
    print(result)

    result = result.replace("```json", "")
    result = result.replace("```", "")
    result = result.strip()

    return safe_json(result)