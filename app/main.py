from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from loguru import logger
from prometheus_fastapi_instrumentator import Instrumentator

from app.api.tasks import router as tasks_router
from app.core import settings
from app.views import index_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan context manager for the FastAPI app.
    """
    logger.info(f"App started. {settings.PROJECT_NAME}")
    yield
    logger.info(f"App shutting down. {settings.PROJECT_NAME}")


app = FastAPI(title=settings.PROJECT_NAME, lifespan=lifespan)

# Prometheus metrics instrumentation - must be set up before app starts
Instrumentator().instrument(app).expose(app)

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.BACKEND_CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
app.mount("/static", StaticFiles(directory=settings.STATIC_DIR), name="static")
templates = Jinja2Templates(directory=settings.TEMPLATES_DIR)

# API ENDPOINTS
app.include_router(tasks_router, prefix="/api", tags=["Tasks"])

# FRONTEND VIEWS
app.include_router(index_router)


@app.get("/")
def read_root():
    return {"message": f"Welcome to {settings.PROJECT_NAME}"}
