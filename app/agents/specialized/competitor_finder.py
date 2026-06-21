from app.services.llm_service import ask_llm

from app.services.json_parser import safe_json





def find_competitors(idea: str, location: str):
    prompt = f"""
    Business Idea:
    {idea}

    Location:
    {location}

    Find the TOP 10 competitors.

    Return ONLY JSON:

    {{
      "competitors":[
        {{
          "name":"",
          "description":"",
          "strength":"",
          "weakness":"",
          "estimated_market_position":""
        }}
      ]
    }}
    """



    result = ask_llm(prompt)



    return safe_json(result)