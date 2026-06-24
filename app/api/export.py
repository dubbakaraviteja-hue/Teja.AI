from fastapi import APIRouter
from fastapi.responses import FileResponse

from app.db.database import get_messages

from app.services.export_service import (
    export_txt,
    export_docx,
    export_pdf
)

router = APIRouter(
    prefix="/export",
    tags=["Export"]
)


@router.get("/txt/{chat_id}")
def export_chat_txt(chat_id: int):

    messages = get_messages(chat_id)

    filepath = f"exports/chat_{chat_id}.txt"

    export_txt(
        filepath,
        messages
    )

    return FileResponse(
        filepath,
        filename=f"chat_{chat_id}.txt"
    )


@router.get("/docx/{chat_id}")
def export_chat_docx(chat_id: int):

    messages = get_messages(chat_id)

    filepath = f"exports/chat_{chat_id}.docx"

    export_docx(
        filepath,
        messages
    )

    return FileResponse(
        filepath,
        filename=f"chat_{chat_id}.docx"
    )


@router.get("/pdf/{chat_id}")
def export_chat_pdf(chat_id: int):

    messages = get_messages(chat_id)

    filepath = f"exports/chat_{chat_id}.pdf"

    export_pdf(
        filepath,
        messages
    )

    return FileResponse(
        filepath,
        filename=f"chat_{chat_id}.pdf"
    )