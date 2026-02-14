"""Classification API endpoints."""
from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status

from domain.services.interfaces import ClassificationService

from src.app.core.dependencies import get_classification_service
from src.app.schemas.ticket import ClassificationRequest, ClassificationResponse
from src.app.services.mappers import ticket_from_request

router = APIRouter(prefix="/v1/classification", tags=["classification"])


@router.post("", response_model=ClassificationResponse, status_code=status.HTTP_200_OK)
async def classify_ticket(
    payload: ClassificationRequest,
    service: ClassificationService = Depends(get_classification_service),
) -> ClassificationResponse:
    """Classify incoming support tickets using the configured ML service."""
    try:
        ticket = ticket_from_request(payload)
        result = await service.classify(ticket)
        return ClassificationResponse(category=result.category.value, confidence=result.confidence)
    except NotImplementedError as exc:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=str(exc)) from exc
