from app.services.gemini_service import generate_response


def generate_title(user_message: str) -> str:
    """
    Generate a short chat title
    from the user's first message.
    """

    prompt = f"""
Generate a short chat title
for the following message.

Rules:
- Maximum 5 words
- No quotes
- No punctuation
- Return title only

Message:
{user_message}
"""

    try:
        title = generate_response(prompt)

        title = (
            title
            .replace('"', '')
            .replace("'", "")
            .strip()
        )

        return title[:50]

    except Exception:
        return (
            user_message[:40]
            .replace("\n", " ")
            .strip()
        )