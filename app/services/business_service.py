from app.services.gemini_service import generate_response


def business_idea(message: str):

    prompt = f"""
    You are an expert startup and business consultant.

    User Idea:
    {message}

    Give:
    1. Business Overview
    2. Target Customers
    3. Investment Required
    4. Revenue Model
    5. Marketing Strategy
    6. Growth Plan
    7. Risks
    """

    return generate_response(prompt)