import json
import re

def safe_json(response):

    try:
        response = response.replace("```json", "")
        response = response.replace("```", "")
        response = response.strip()

        return json.loads(response)

    except Exception:

        try:
            match = re.search(
                r"\{.*\}",
                response,
                re.DOTALL
            )

            if match:
                return json.loads(match.group())

        except Exception:
            pass

        print("JSON PARSE FAILED")
        print(response)

        return {}