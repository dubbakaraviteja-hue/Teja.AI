from fastapi import APIRouter
from app.models.schemas import CareerRequest
from app.services.career_service import career_guidance

router = APIRouter(prefix="/career", tags=["Career Guidance"])


@router.post("/")
def career(request: CareerRequest):

    return {
        "response": career_guidance(
            request.message
        )
    }