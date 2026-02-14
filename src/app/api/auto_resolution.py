"""Auto-resolution endpoint powered by RAG and Bedrock."""
from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status

from domain.services.interfaces import AutoResolutionService

from src.app.core.dependencies import get_auto_resolution_service
from src.app.schemas.ticket import AutoResolutionResponse, ClassificationRequest
from src.app.services.mappers import ticket_from_request

router = APIRouter(prefix="/v1/auto-resolution", tags=["auto-resolution"])


@router.post("", response_model=AutoResolutionResponse, status_code=status.HTTP_200_OK)
async def generate_auto_resolution(
    payload: ClassificationRequest,
    service: AutoResolutionService = Depends(get_auto_resolution_service),
) -> AutoResolutionResponse:
    """Generate an automated resolution leveraging RAG pipelines."""
    try:
        ticket = ticket_from_request(payload)
        outcome = await service.generate(ticket)
        return AutoResolutionResponse(
            auto_resolution=outcome.response,
            grounding_ticket_ids=outcome.grounding_ticket_ids,
        )
    except NotImplementedError as exc:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=str(exc)) from exc
