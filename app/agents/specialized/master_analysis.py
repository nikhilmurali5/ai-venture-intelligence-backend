from app.services.llm_service import ask_llm
from app.services.json_parser import safe_json


def analyze_everything(idea: str):
    prompt = f"""
    Analyze this business idea:

    {idea}

    Return ONLY valid JSON.

    Required format:

    {{
      "market": {{
        "market_score": 85,
        "market_size": "Large",
        "demand": "High"
      }},
      "competition": {{
        "competition_score": 70,
        "competition_level": "Medium"
      }},
      "profitability": {{
        "profitability_score": 80,
        "profit_margin": "25%"
      }},
      "risk": {{
        "risk_score": 35,
        "risk_level": "Low"
      }},
      "trend": {{
        "trend_score": 88,
        "future_growth": "Strong"
      }},
      "swot": {{
        "strengths": ["point1","point2"],
        "weaknesses": ["point1","point2"],
        "opportunities": ["point1","point2"],
        "threats": ["point1","point2"]
      }},
      "business_plan": "Detailed business plan",
      "pitch_deck": "Detailed pitch deck",
      "viability_report": "Detailed viability report"
    }}

    IMPORTANT:
    Do not create any other keys.
    Do not return analysis.
    Do not return recommendations.
    Do not return conclusion.

    Only the exact JSON structure above.
    """

    result = ask_llm(prompt)

    print("GROQ RESPONSE:")
    print(result)

    parsed = safe_json(result)

    print("PARSED JSON:")
    print(parsed)

    return parsed