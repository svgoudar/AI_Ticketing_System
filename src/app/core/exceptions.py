"""Custom exception hierarchy providing consistent error responses."""
from __future__ import annotations

from fastapi import HTTPException, status


class AppException(HTTPException):
    """Base application exception with structured metadata."""

    def __init__(self, detail: str, status_code: int = status.HTTP_400_BAD_REQUEST) -> None:
        super().__init__(status_code=status_code, detail=detail)


class UpstreamServiceException(AppException):
    """Raised when an upstream dependency returns an error."""

    def __init__(self, service: str, detail: str) -> None:
        super().__init__(detail=f"{service} failure: {detail}", status_code=status.HTTP_502_BAD_GATEWAY)


class ResourceNotFoundException(AppException):
    """Raised when a requested resource cannot be located."""

    def __init__(self, resource: str, identifier: str) -> None:
        super().__init__(
            detail=f"{resource} with identifier '{identifier}' not found.",
            status_code=status.HTTP_404_NOT_FOUND,
        )


class ValidationException(AppException):
    """Raised when request payloads fail business validation."""

    def __init__(self, detail: str) -> None:
        super().__init__(detail=detail, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
