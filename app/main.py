from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.database import init_db

# Routers
from app.api.chat import router as chat_router
from app.api.analytics import router as analytics_router
from app.api.files import router as files_router

from app.api.qa import router as qa_router
from app.api.career import router as career_router
from app.api.summary import router as summary_router
from app.api.creative import router as creative_router
from app.api.business import router as business_router
from app.api.export import router as export_router


# ==================================
# CREATE FASTAPI APP FIRST
# ==================================

app = FastAPI(
    title="Teja.AI",
    version="1.0.0",
    description="AI Assistant Backend"
)

# ==================================
# CORS
# ==================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==================================
# DATABASE
# ==================================

init_db()

# ==================================
# ROUTERS
# ==================================

app.include_router(chat_router)

app.include_router(analytics_router)

app.include_router(files_router)

app.include_router(qa_router)

app.include_router(career_router)

app.include_router(summary_router)

app.include_router(creative_router)

app.include_router(business_router)

app.include_router(export_router)

# ==================================
# ROOT
# ==================================

@app.get("/")
def home():
    return {
        "name": "Teja.AI",
        "version": "1.0.0",
        "status": "running"
    }

# ==================================
# HEALTH
# ==================================

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }