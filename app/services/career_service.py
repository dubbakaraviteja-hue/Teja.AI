from app.services.gemini_service import generate_response


def career_guidance(question: str):

    prompt = f"""
    You are an expert career counselor.

    Answer:

    {question}
    """

    return generate_response(prompt)