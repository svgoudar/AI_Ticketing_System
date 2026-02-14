"""FastAPI entrypoint wiring API routers and middleware."""
from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api import auto_resolution, classification, conversation, resolution_time, similarity
from .core.config import settings
from .core.logging import configure_logging, get_logger
from .core.middleware import RequestLoggingMiddleware

logger = get_logger(__name__)


@asynccontextmanager
def lifespan(app: FastAPI):  # type: ignore[override]
    configure_logging()
    logger.info(
        "application_startup",
        extra={"extra": {"environment": settings.environment, "version": settings.version}},
    )
    yield
    logger.info("application_shutdown")


def create_app() -> FastAPI:
    """Instantiate the FastAPI application with shared configuration."""
    application = FastAPI(
        title=settings.project_name,
        version=settings.version,
        docs_url="/docs",
        redoc_url="/redoc",
        lifespan=lifespan,
    )

    application.add_middleware(RequestLoggingMiddleware)
    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_allow_origins,
        allow_methods=settings.cors_allow_methods,
        allow_headers=settings.cors_allow_headers,
        allow_credentials=True,
    )

    application.include_router(classification.router)
    application.include_router(resolution_time.router)
    application.include_router(similarity.router)
    application.include_router(auto_resolution.router)
    application.include_router(conversation.router)

    return application


app = create_app()
