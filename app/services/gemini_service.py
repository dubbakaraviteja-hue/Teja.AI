from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv(dotenv_path=".env")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

print("KEY FOUND:", bool(GEMINI_API_KEY))
print("KEY:", GEMINI_API_KEY[:10] + "..." if GEMINI_API_KEY else "NO KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env")

genai.configure(api_key=GEMINI_API_KEY)


def generate_response(prompt: str):
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Error: {str(e)}"


def ask_gemini(prompt: str):
    return generate_response(prompt)