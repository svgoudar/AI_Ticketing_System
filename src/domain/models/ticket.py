"""Domain entity definitions for support tickets."""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

from src.app.value_objects.ticket_priority import TicketPriority
from src.app.value_objects.ticket_category import TicketCategory


@dataclass(slots=True)
class Ticket:
    """Represents a customer support ticket within the domain."""

    ticket_id: str
    text: str
    customer_id: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    priority: TicketPriority = TicketPriority.MEDIUM
    category: Optional[TicketCategory] = None
