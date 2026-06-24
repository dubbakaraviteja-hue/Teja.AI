from fastapi import APIRouter, UploadFile, File
from pathlib import Path
import shutil

from app.db.database import (
    save_file,
    get_library
)

router = APIRouter(
    tags=["Files"]
)

UPLOAD_DIR = "uploads"

Path(UPLOAD_DIR).mkdir(
    exist_ok=True
)


@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...)
):

    file_path = (
        f"{UPLOAD_DIR}/{file.filename}"
    )

    with open(
        file_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    extension = (
        file.filename
        .split(".")[-1]
        .lower()
    )

    save_file(
        file.filename,
        extension,
        file_path
    )

    return {
        "success": True,
        "filename": file.filename,
        "path": file_path
    }


@router.get("/library")
def library():

    rows = get_library()

    return {
        "files": [
            {
                "id": row[0],
                "file_name": row[1],
                "file_type": row[2],
                "file_path": row[3],
                "created_at": row[4]
            }
            for row in rows
        ]
    }