"""Placeholder service implementations until infrastructure wiring is provided."""
from __future__ import annotations

from domain.models.conversation import ConversationTurn
from domain.models.results import (
    AutoResolutionOutcome,
    ClassificationOutcome,
    ResolutionTimeOutcome,
    SimilarTicket,
)
from domain.models.ticket import Ticket
from domain.services.interfaces import (
    AutoResolutionService,
    ClassificationService,
    ConversationService,
    ResolutionTimeService,
    SimilarityService,
)
class NotConfiguredClassificationService(ClassificationService):
    async def classify(self, ticket: Ticket) -> ClassificationOutcome:
        raise NotImplementedError("Classification service is not yet configured.")


class NotConfiguredResolutionTimeService(ResolutionTimeService):
    async def estimate(self, ticket: Ticket) -> ResolutionTimeOutcome:
        raise NotImplementedError("Resolution time service is not yet configured.")


class NotConfiguredSimilarityService(SimilarityService):
    async def find_similar(self, ticket: Ticket, top_k: int = 5) -> list[SimilarTicket]:
        raise NotImplementedError("Similarity service is not yet configured.")


class NotConfiguredAutoResolutionService(AutoResolutionService):
    async def generate(self, ticket: Ticket) -> AutoResolutionOutcome:
        raise NotImplementedError("Auto-resolution service is not yet configured.")


class NotConfiguredConversationService(ConversationService):
    async def append_turn(self, turn: ConversationTurn) -> None:
        raise NotImplementedError("Conversation service is not yet configured.")

    async def get_history(self, ticket_id: str, limit: int = 10) -> list[ConversationTurn]:
        raise NotImplementedError("Conversation service is not yet configured.")
