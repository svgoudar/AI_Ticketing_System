"""Conversation memory management endpoints."""
from __future__ import annotations

from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Query, status

from domain.models.conversation import ConversationTurn as DomainConversationTurn
from domain.services.interfaces import ConversationService

from src.app.core.dependencies import get_conversation_service
from src.app.schemas.ticket import ConversationHistoryResponse, ConversationTurn

router = APIRouter(prefix="/v1/conversation", tags=["conversation"])


@router.post("", status_code=status.HTTP_202_ACCEPTED)
async def append_conversation_turn(
    payload: ConversationTurn,
    service: ConversationService = Depends(get_conversation_service),
) -> None:
    """Persist a new conversation turn for downstream RAG enrichment."""
    try:
        turn = DomainConversationTurn(
            ticket_id=payload.ticket_id,
            user_message=payload.user_message,
            assistant_message=payload.assistant_message,
            created_at=payload.created_at or datetime.utcnow(),
        )
        await service.append_turn(turn)
    except NotImplementedError as exc:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=str(exc)) from exc


@router.get("/{ticket_id}", response_model=ConversationHistoryResponse, status_code=status.HTTP_200_OK)
async def get_conversation_history(
    ticket_id: str,
    limit: int = Query(default=10, ge=1, le=100, description="Maximum number of history entries to return."),
    service: ConversationService = Depends(get_conversation_service),
) -> ConversationHistoryResponse:
    """Retrieve prior conversation history for the given ticket."""
    try:
        history = await service.get_history(ticket_id=ticket_id, limit=limit)
        payload = [
            ConversationTurn(
                ticket_id=item.ticket_id,
                user_message=item.user_message,
                assistant_message=item.assistant_message,
                created_at=item.created_at,
            )
            for item in history
        ]
        return ConversationHistoryResponse(history=payload)
    except NotImplementedError as exc:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=str(exc)) from exc
