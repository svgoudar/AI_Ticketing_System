"""Value object representing ticket priority levels."""
from __future__ import annotations

from enum import Enum


class TicketPriority(str, Enum):
    """Enumerates allowed ticket priorities."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"
