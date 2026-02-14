"""Domain representation of conversation history."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class ConversationTurn:
    ticket_id: str
    user_message: str
    assistant_message: str | None
    created_at: datetime
