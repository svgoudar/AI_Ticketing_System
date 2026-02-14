"""Logging configuration utilities for structured JSON logs."""
from __future__ import annotations

import json
import logging
from logging.config import dictConfig
from typing import Any, Dict

from .config import settings


class JsonLogFormatter(logging.Formatter):
    """Serialize log records into structured JSON."""

    def format(self, record: logging.LogRecord) -> str:  # noqa: D401
        payload = {
            "timestamp": self.formatTime(record, datefmt="%Y-%m-%dT%H:%M:%S.%fZ"),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }
        if record.exc_info:
            payload["exception"] = self.formatException(record.exc_info)
        if record.stack_info:
            payload["stack"] = self.formatStack(record.stack_info)
        if hasattr(record, "extra") and isinstance(record.extra, dict):
            payload.update(record.extra)
        return json.dumps(payload, ensure_ascii=False)


def configure_logging() -> None:
    """Configure root logging handlers using JSON formatting."""
    log_level = settings.log_level.upper()
    dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "json": {
                    "()": JsonLogFormatter,
                }
            },
            "handlers": {
                "stdout": {
                    "class": "logging.StreamHandler",
                    "formatter": "json",
                    "stream": "ext://sys.stdout",
                }
            },
            "root": {
                "handlers": ["stdout"],
                "level": log_level,
            },
        }
    )


def get_logger(name: str) -> logging.Logger:
    """Return a logger configured for structured output."""
    return logging.getLogger(name)
