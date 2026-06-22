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
        "strengths": ["point1","point2","point3","point4"],
        "weaknesses": ["point1","point2","point3","point4"],
        "opportunities": ["point1","point2","point3","point4"],
        "threats": ["point1","point2","point3","point4"],
      }},
      "business_plan": "# Executive Summary\n\nGive a complete business plan.\n\nInclude:\n- Startup cost\n- Revenue model\n- Marketing strategy\n- Operations plan\n- Growth strategy",

"pitch_deck": "Slide 1: Problem\nExplain problem\n\nSlide 2: Solution\nExplain solution\n\nSlide 3: Market\nExplain market size\n\nSlide 4: Revenue Model\nExplain revenue\n\nSlide 5: Competition\nExplain competitors\n\nSlide 6: Funding\nExplain funding",

"viability_report": "# Viability Report\n\nGive detailed viability report with:\n\n- Market opportunity\n- Risks\n- Strengths\n- Weaknesses\n- Final recommendation"
    }}

    IMPORTANT:
    Do not create any other keys.
    Do not return analysis.
    Do not return recommendations.
    Do not return conclusion.

    Only the exact JSON structure above.
    """

    result = ask_llm(prompt)
    print(result)

    print("GROQ RESPONSE:")
    print(result)

    parsed = safe_json(result)

    print("PARSED JSON:")
    print(parsed)

    return parsed