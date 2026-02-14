"""Application configuration leveraging Pydantic settings."""
from __future__ import annotations

from functools import lru_cache
from typing import List, Literal

from pydantic import Field
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    """Environment-driven application settings."""

    environment: Literal["dev", "stage", "prod"] = Field(
        default="dev", description="Active deployment environment."
    )
    project_name: str = Field(default="AI Ticketing System", description="Service name exposed via FastAPI.")
    version: str = Field(default="0.1.0", description="Semantic version of the API.")
    cors_allow_origins: List[str] = Field(
        default_factory=lambda: ["*"],
        description="List of allowed origins for CORS configuration.",
    )
    cors_allow_methods: List[str] = Field(
        default_factory=lambda: ["GET", "POST", "OPTIONS"],
        description="HTTP methods permitted via CORS.",
    )
    cors_allow_headers: List[str] = Field(
        default_factory=lambda: ["*"],
        description="HTTP headers permitted via CORS.",
    )
    log_level: str = Field(default="INFO", description="Root logging level.")
    aws_region: str = Field(default="us-east-1", description="AWS region for downstream service calls.")
    sagemaker_classifier_endpoint: str = Field(
        default="", description="SageMaker endpoint name for ticket classification."
    )
    sagemaker_regressor_endpoint: str = Field(
        default="", description="SageMaker endpoint name for resolution time regression."
    )
    feature_store_ticket_group: str = Field(
        default="", description="SageMaker Feature Store ticket feature group name."
    )
    feature_store_customer_group: str = Field(
        default="", description="SageMaker Feature Store customer feature group name."
    )
    opensearch_host: str = Field(default="", description="Endpoint for the OpenSearch domain.")
    opensearch_index: str = Field(default="tickets", description="OpenSearch index storing ticket embeddings.")
    bedrock_model_id: str = Field(default="", description="Amazon Bedrock model identifier for RAG responses.")
    dynamodb_conversation_table: str = Field(
        default="", description="DynamoDB table storing conversation memory."
    )
    kinesis_stream_name: str = Field(
        default="", description="Kinesis/MSK stream name carrying CDC events."
    )

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "case_sensitive": False,
    }


@lru_cache(maxsize=1)
def get_settings() -> AppSettings:
    """Return cached application settings instance."""
    return AppSettings()


settings = get_settings()
