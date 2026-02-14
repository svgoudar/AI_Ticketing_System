"""Domain result value objects returned by services."""
from __future__ import annotations

from dataclasses import dataclass
from typing import List

from src.app.value_objects.ticket_category import TicketCategory


@dataclass(slots=True)
class ClassificationOutcome:
    category: TicketCategory
    confidence: float


@dataclass(slots=True)
class ResolutionTimeOutcome:
    estimated_hours: float


@dataclass(slots=True)
class SimilarTicket:
    ticket_id: str
    similarity_score: float
    summary: str


@dataclass(slots=True)
class AutoResolutionOutcome:
    response: str
    grounding_ticket_ids: List[str]
