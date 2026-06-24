from fastapi import APIRouter
from app.models.schemas import CreativeRequest
from app.services.creative_service import generate_content

router = APIRouter(prefix="/creative", tags=["Creative Content"])


@router.post("/")
def creative(request: CreativeRequest):

    return {
        "response": generate_content(
            request.message
        )
    }