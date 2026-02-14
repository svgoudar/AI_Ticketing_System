"""Conversion helpers between API schemas and domain entities."""
from __future__ import annotations

from datetime import datetime

from domain.models.ticket import Ticket
from domain.value_objects.ticket_priority import TicketPriority

from src.app.schemas.ticket import ClassificationRequest


def ticket_from_request(payload: ClassificationRequest) -> Ticket:
    """Convert a request payload into a domain ticket entity."""
    created_at = payload.created_at or datetime.utcnow()
    priority = TicketPriority.MEDIUM
    if payload.priority:
        try:
            priority = TicketPriority(payload.priority.lower())
        except ValueError:
            priority = TicketPriority.MEDIUM
    return Ticket(
        ticket_id=payload.ticket_id or "",
        text=payload.ticket_text,
        customer_id=payload.customer_id,
        created_at=created_at,
        priority=priority,
        category=None,
    )
