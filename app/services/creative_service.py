from app.services.gemini_service import generate_response


def generate_content(prompt: str):

    full_prompt = f"""
    You are a creative AI assistant.

    Create high-quality content for:

    {prompt}
    """

    return generate_response(full_prompt)