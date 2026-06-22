from fastapi import APIRouter
from app.models.schemas import QARequest
from app.services.qa_service import answer_question

router = APIRouter(prefix="/qa", tags=["Question Answering"])


@router.post("/")
def qa(request: QARequest):

    return {
        "response": answer_question(
            request.message
        )
    }