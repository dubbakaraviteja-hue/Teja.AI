from app.db.database import (
    save_message,
    update_chat_title,
    get_messages
)

from app.services.gemini_service import (
    generate_response
)

from app.utils.title_generator import (
    generate_title
)


def process_chat(
    chat_id: int,
    user_message: str
):

    history = get_messages(chat_id)

    if len(history) == 0:

        title = generate_title(
            user_message
        )

        update_chat_title(
            chat_id,
            title
        )

    save_message(
        chat_id,
        "user",
        user_message
    )

    conversation = ""

    for role, content, _ in history:

        conversation += (
            f"{role}: {content}\n"
        )

    conversation += (
        f"user: {user_message}"
    )

    ai_response = generate_response(
        conversation
    )

    save_message(
        chat_id,
        "assistant",
        ai_response
    )

    return ai_response