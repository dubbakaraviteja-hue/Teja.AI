from fastapi import APIRouter
from app.models.schemas import BusinessRequest
from app.services.business_service import business_idea

router = APIRouter(prefix="/business", tags=["Business Ideas"])


@router.post("/")
def business(request: BusinessRequest):

    return {
        "response": business_idea(
            request.message
        )
    }