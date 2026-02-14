"""Domain service interfaces defining core business capabilities."""
from __future__ import annotations

from typing import Protocol

from src.app.models.conversation import ConversationTurn
from src.app.models.results import (
    AutoResolutionOutcome,
    ClassificationOutcome,
    ResolutionTimeOutcome,
    SimilarTicket,
)
from src.app.models.ticket import Ticket


class ClassificationService(Protocol):
    async def classify(self, ticket: Ticket) -> ClassificationOutcome:
        """Return the predicted ticket category."""


class ResolutionTimeService(Protocol):
    async def estimate(self, ticket: Ticket) -> ResolutionTimeOutcome:
        """Return predicted time to resolution for a ticket."""


class SimilarityService(Protocol):
    async def find_similar(self, ticket: Ticket, top_k: int = 5) -> list[SimilarTicket]:
        """Return similar tickets based on embeddings and metadata."""


class AutoResolutionService(Protocol):
    async def generate(self, ticket: Ticket) -> AutoResolutionOutcome:
        """Return an auto-generated resolution grounded in historical knowledge."""


class ConversationService(Protocol):
    async def append_turn(self, turn: ConversationTurn) -> None:
        """Persist a conversation turn for future context."""

    async def get_history(self, ticket_id: str, limit: int = 10) -> list[ConversationTurn]:
        """Return prior conversation turns for the given ticket."""
