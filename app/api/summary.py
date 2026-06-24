from fastapi import APIRouter
from app.models.schemas import SummaryRequest
from app.services.summary_service import summarize

router = APIRouter(prefix="/summary", tags=["Summary"])


@router.post("/")
def summary(request: SummaryRequest):

    return {
        "response": summarize(
            request.text
        )
    }