from fastapi import APIRouter, HTTPException

from app.models.schemas import ChatRequest

from app.services.chat_service import process_chat

from app.db.database import (
    create_chat,
    get_chats,
    get_messages,
    rename_chat,
    pin_chat,
    archive_chat,
    delete_chat,
    search_chats
)

router = APIRouter(
    tags=["Chat"]
)

# =========================
# NEW CHAT
# =========================

@router.post("/new-chat")
def new_chat():

    chat_id = create_chat()

    return {
        "success": True,
        "chat_id": chat_id
    }


# =========================
# ALL CHATS
# =========================

@router.get("/chats")
def chats():

    rows = get_chats()

    return {
        "success": True,
        "total": len(rows),
        "chats": [
            {
                "id": row[0],
                "title": row[1],
                "pinned": row[2],
                "archived": row[3],
                "shared": row[4],
                "created_at": row[5],
                "updated_at": row[6]
            }
            for row in rows
        ]
    }


# =========================
# CHAT HISTORY
# =========================

@router.get("/history/{chat_id}")
def history(chat_id: int):

    messages = get_messages(chat_id)

    return {
        "success": True,
        "chat_id": chat_id,
        "total_messages": len(messages),
        "messages": [
            {
                "role": role,
                "content": content,
                "created_at": created_at
            }
            for role, content, created_at in messages
        ]
    }


# =========================
# CHAT
# =========================

@router.post("/chat/{chat_id}")
def chat(
    chat_id: int,
    request: ChatRequest
):

    try:

        ai_response = process_chat(
            chat_id=chat_id,
            user_message=request.message
        )

        return {
            "success": True,
            "chat_id": chat_id,
            "response": ai_response
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# =========================
# RENAME CHAT
# =========================

@router.post("/rename-chat/{chat_id}")
def rename(
    chat_id: int,
    title: str
):

    rename_chat(
        chat_id,
        title
    )

    return {
        "success": True,
        "message": "Chat renamed successfully"
    }


# =========================
# PIN CHAT
# =========================

@router.post("/pin-chat/{chat_id}")
def pin(chat_id: int):

    pin_chat(chat_id)

    return {
        "success": True,
        "message": "Chat pinned successfully"
    }


# =========================
# ARCHIVE CHAT
# =========================

@router.post("/archive-chat/{chat_id}")
def archive(chat_id: int):

    archive_chat(chat_id)

    return {
        "success": True,
        "message": "Chat archived successfully"
    }


# =========================
# DELETE CHAT
# =========================

@router.delete("/delete-chat/{chat_id}")
def delete(chat_id: int):

    delete_chat(chat_id)

    return {
        "success": True,
        "message": "Chat deleted successfully"
    }


# =========================
# SEARCH CHAT
# =========================

@router.get("/search-chat")
def search(keyword: str):

    rows = search_chats(keyword)

    return {
        "success": True,
        "total": len(rows),
        "results": [
            {
                "id": row[0],
                "title": row[1]
            }
            for row in rows
        ]
    }