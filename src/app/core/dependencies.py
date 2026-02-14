"""Dependency providers for FastAPI routes."""
from __future__ import annotations

from functools import lru_cache

from domain.services.interfaces import (
    AutoResolutionService,
    ClassificationService,
    ConversationService,
    ResolutionTimeService,
    SimilarityService,
)


from src.app.services.stubs import (
    NotConfiguredAutoResolutionService,
    NotConfiguredClassificationService,
    NotConfiguredConversationService,
    NotConfiguredResolutionTimeService,
    NotConfiguredSimilarityService,
)


@lru_cache(maxsize=1)
def _classification_service() -> ClassificationService:
    return NotConfiguredClassificationService()


@lru_cache(maxsize=1)
def _resolution_time_service() -> ResolutionTimeService:
    return NotConfiguredResolutionTimeService()


@lru_cache(maxsize=1)
def _similarity_service() -> SimilarityService:
    return NotConfiguredSimilarityService()


@lru_cache(maxsize=1)
def _auto_resolution_service() -> AutoResolutionService:
    return NotConfiguredAutoResolutionService()


@lru_cache(maxsize=1)
def _conversation_service() -> ConversationService:
    return NotConfiguredConversationService()


def get_classification_service() -> ClassificationService:
    """Return the classification service implementation."""
    return _classification_service()


def get_resolution_time_service() -> ResolutionTimeService:
    """Return the resolution time regression service."""
    return _resolution_time_service()


def get_similarity_service() -> SimilarityService:
    """Return the similarity search service."""
    return _similarity_service()


def get_auto_resolution_service() -> AutoResolutionService:
    """Return the auto-resolution service."""
    return _auto_resolution_service()


def get_conversation_service() -> ConversationService:
    """Return the conversation memory service."""
    return _conversation_service()
