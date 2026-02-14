"""Value object representing ticket categories."""
from __future__ import annotations

from enum import Enum


class TicketCategory(str, Enum):
    """Enumerates supported ticket categories."""

    AUTHENTICATION = "authentication"
    BILLING = "billing"
    PERFORMANCE = "performance"
    USABILITY = "usability"
    OTHER = "other"
