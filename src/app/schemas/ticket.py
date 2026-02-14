"""Pydantic schemas representing ticket-based payloads."""
from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class TicketBase(BaseModel):
    ticket_id: Optional[str] = Field(default=None, description="Unique identifier for the ticket.")
    customer_id: Optional[str] = Field(default=None, description="Customer identifier associated with the ticket.")
    ticket_text: str = Field(..., description="Full text of the customer support request.")
    created_at: Optional[datetime] = Field(
        default=None,
        description="ISO timestamp representing when the ticket was created.",
    )
    priority: str = Field(default="medium", description="Priority of the ticket (low/medium/high/critical).")

    model_config = {
        "populate_by_name": True,
        "extra": "forbid",
    }


class ClassificationRequest(TicketBase):
    pass


class ClassificationResponse(BaseModel):
    category: str = Field(..., description="Predicted category label.")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Classifier confidence score.")


class ResolutionTimeResponse(BaseModel):
    estimated_resolution_hours: float = Field(
        ..., ge=0.0, description="Estimated hours required to resolve the ticket."
    )


class SimilarTicket(BaseModel):
    ticket_id: str = Field(..., description="Identifier of the similar ticket.")
    similarity_score: float = Field(..., ge=0.0, le=1.0, description="Similarity score between 0 and 1.")
    summary: str = Field(..., description="Short summary of the similar ticket.")


class SimilarityResponse(BaseModel):
    duplicates: List[SimilarTicket] = Field(default_factory=list, description="Similar tickets in descending order.")


class AutoResolutionResponse(BaseModel):
    auto_resolution: str = Field(..., description="Generated resolution text for the ticket.")
    grounding_ticket_ids: List[str] = Field(
        default_factory=list, description="Identifiers for tickets used to ground the response."
    )


class ConversationTurn(BaseModel):
    ticket_id: str = Field(..., description="Identifier for the conversation thread.")
    user_message: str = Field(..., description="Latest message provided by the user.")
    assistant_message: Optional[str] = Field(
        default=None,
        description="System response when available; omitted when storing user messages only.",
    )
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Timestamp of the conversation turn.")


class ConversationHistoryResponse(BaseModel):
    history: List[ConversationTurn] = Field(
        default_factory=list,
        description="Chronological list of conversation turns for the ticket.",
    )
