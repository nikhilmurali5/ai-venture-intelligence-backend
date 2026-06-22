from app.services.llm_service import ask_llm
from app.services.json_parser import safe_json


def analyze_everything(idea: str):

    prompt = f"""
    Analyze this business idea:

    {idea}

    Return ONLY valid JSON.

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
        "strengths": [],
        "weaknesses": [],
        "opportunities": [],
        "threats": []
      }},

      "business_plan": "Detailed business plan",

      "pitch_deck": "Pitch deck content",

      "viability_report": "Complete viability report"
    }}

    Return ONLY JSON.
    """

    result = ask_llm(prompt)

    return safe_json(result)