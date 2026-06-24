from fastapi import APIRouter

from app.db.database import (
    get_chats,
    get_library
)

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


@router.get("/dashboard")
def dashboard():

    chats = get_chats()
    files = get_library()

    return {
        "total_chats": len(chats),
        "total_files": len(files),
        "status": "active"
    }