from pydantic import BaseModel


# =========================
# CHAT
# =========================

class ChatRequest(BaseModel):
    message: str


# =========================
# RENAME CHAT
# =========================

class RenameRequest(BaseModel):
    title: str


# =========================
# QUESTION ANSWERING
# =========================

class QARequest(BaseModel):
    message: str


# =========================
# CAREER GUIDANCE
# =========================

class CareerRequest(BaseModel):
    message: str


# =========================
# TEXT SUMMARIZATION
# =========================

class SummaryRequest(BaseModel):
    text: str


# =========================
# CREATIVE CONTENT
# =========================

class CreativeRequest(BaseModel):
    message: str


# =========================
# BUSINESS IDEA DEVELOPER
# =========================

class BusinessRequest(BaseModel):
    message: str


# =========================
# FILE UPLOAD
# =========================

class FileResponse(BaseModel):
    filename: str
    status: str

