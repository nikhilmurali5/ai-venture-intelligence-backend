import json
import re

def safe_json(response):

    try:
        response = response.strip()

        if "```json" in response:
            response = response.split("```json")[1]
            response = response.split("```")[0]

        return json.loads(response)

    except Exception as e:

        print("JSON ERROR:", e)

        try:
            match = re.search(r"\{[\s\S]*\}", response)

            if match:
                return json.loads(match.group(0))

        except Exception as e:
            print("REGEX JSON ERROR:", e)

        return {}