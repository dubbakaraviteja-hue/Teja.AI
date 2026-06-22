from google import genai
import os

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_response(prompt: str):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Error: {str(e)}"