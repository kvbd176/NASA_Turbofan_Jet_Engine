from fastapi import FastAPI

from api.routes.dashboard import router as dashboard_router
from api.routes.analytics import router as analytics_router
from api.routes.reports import router as reports_router
from api.routes.chat import router as chat_router
from api.routes.pipeline import router as pipeline_router
from api.routes.history import router as history_router
from api.routes.upload import router as upload_router

from auth.routes import router as auth_router

from database.database import Base, engine
from database import models

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="NASA Predictive Maintenance API"
)


# Authentication
app.include_router(auth_router)


# Upload
app.include_router(
    upload_router,
    prefix="/upload",
    tags=["Upload"]
)


# Pipeline
app.include_router(
    pipeline_router,
    prefix="/pipeline",
    tags=["Pipeline"]
)


# Dashboard
app.include_router(
    dashboard_router,
    prefix="/dashboard",
    tags=["Dashboard"]
)


# Analytics
app.include_router(
    analytics_router,
    prefix="/analytics",
    tags=["Analytics"]
)


# Reports
app.include_router(
    reports_router,
    prefix="/reports",
    tags=["Reports"]
)


# Chat
app.include_router(
    chat_router,
    prefix="/chat",
    tags=["Chat"]
)


# History
app.include_router(
    history_router,
    prefix="/chat",
    tags=["History"]
)


@app.get("/")
def root():
    return {
        "message": "NASA Predictive Maintenance API Running"
    }