from app.services.gemini_service import generate_response


def answer_question(question: str):

    return generate_response(question)