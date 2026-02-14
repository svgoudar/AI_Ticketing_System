"""Resolution time regression endpoint."""
from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status

from domain.services.interfaces import ResolutionTimeService

from src.app.core.dependencies import get_resolution_time_service
from src.app.schemas.ticket import ClassificationRequest, ResolutionTimeResponse
from src.app.services.mappers import ticket_from_request

router = APIRouter(prefix="/v1/resolution-time", tags=["resolution-time"])


@router.post("", response_model=ResolutionTimeResponse, status_code=status.HTTP_200_OK)
async def estimate_resolution_time(
    payload: ClassificationRequest,
    service: ResolutionTimeService = Depends(get_resolution_time_service),
) -> ResolutionTimeResponse:
    """Estimate time to resolve a ticket using regression model."""
    try:
        ticket = ticket_from_request(payload)
        result = await service.estimate(ticket)
        return ResolutionTimeResponse(estimated_resolution_hours=result.estimated_hours)
    except NotImplementedError as exc:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=str(exc)) from exc
