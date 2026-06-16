from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import google.generativeai as genai
import os

from models import ChatRequest

from database import (
    init_db,
    create_chat,
    get_chats,
    get_messages,
    save_message
)

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise Exception(
        "GEMINI_API_KEY not found in .env"
    )

genai.configure(api_key=api_key)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

init_db()

app = FastAPI(
    title="Teja.ai",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def root():
    return {
        "app": "Teja.ai",
        "status": "running",
        "model": "gemini-2.5-flash"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/new-chat")
def new_chat():

    chat_id = create_chat()

    return {
        "chat_id": chat_id
    }


@app.get("/chats")
def chats():
    return {
        "chats": get_chats()
    }


@app.get("/history/{chat_id}")
def history(chat_id: int):

    msgs = get_messages(chat_id)

    return {
        "messages": msgs
    }


@app.post("/chat/{chat_id}")
def chat(chat_id: int, req: ChatRequest):

    save_message(
        chat_id,
        "user",
        req.message
    )

    history = get_messages(chat_id)

    prompt = """
You are Teja AI.

Rules:
- Helpful
- Accurate
- Concise
- Professional

Conversation:
"""

    for role, content in history[-20:]:

        prompt += f"\n{role}: {content}"

    prompt += "\nassistant:"

    try:

        response = model.generate_content(
            prompt
        )

        answer = response.text

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    save_message(
        chat_id,
        "assistant",
        answer
    )

    return {
        "response": answer
    }


if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )