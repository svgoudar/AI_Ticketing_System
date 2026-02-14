"""Ticket similarity search endpoint."""
from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query, status

from domain.services.interfaces import SimilarityService

from src.app.core.dependencies import get_similarity_service
from src.app.schemas.ticket import ClassificationRequest, SimilarityResponse, SimilarTicket
from src.app.services.mappers import ticket_from_request

router = APIRouter(prefix="/v1/similarity", tags=["similarity"])


@router.post("", response_model=SimilarityResponse, status_code=status.HTTP_200_OK)
async def find_similar_tickets(
    payload: ClassificationRequest,
    top_k: int = Query(default=5, ge=1, le=20, description="Number of similar tickets to return."),
    service: SimilarityService = Depends(get_similarity_service),
) -> SimilarityResponse:
    """Return similar tickets using vector search backed by OpenSearch."""
    try:
        ticket = ticket_from_request(payload)
        results = await service.find_similar(ticket, top_k=top_k)
        duplicates = [
            SimilarTicket(
                ticket_id=item.ticket_id,
                similarity_score=item.similarity_score,
                summary=item.summary,
            )
            for item in results
        ]
        return SimilarityResponse(duplicates=duplicates)
    except NotImplementedError as exc:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=str(exc)) from exc
