from app.services.gemini_service import generate_response


def summarize(text: str):

    prompt = f"""
    Summarize the following text clearly:

    {text}
    """

    return generate_response(prompt)