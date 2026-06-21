import json

from groq import Groq
from groq import RateLimitError

from app.core.config import GROQ_API_KEY


client = Groq(
    api_key=GROQ_API_KEY
)


def ask_llm(prompt: str):

    try:

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    except RateLimitError:

        print("GROQ RATE LIMIT REACHED")

        return """
        {
            "error": "Groq rate limit reached. Please try again later."
        }
        """

    except Exception as e:

        print("LLM ERROR:", str(e))

        return f"""
        {{
            "error": "{str(e)}"
        }}
        """


def parse_json_response(text: str):

    try:

        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

        return json.loads(text)

    except Exception as e:

        print("JSON PARSE ERROR:", str(e))

        return {
            "error": "Invalid JSON response",
            "raw_response": text
        }