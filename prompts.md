You are a Senior Principal Cloud Architect and Staff ML Engineer.

Your task is to generate a production-grade enterprise AI Ticketing System aligned with AWS Well-Architected Framework and modern MLOps standards.

The system must strictly follow clean architecture, domain-driven design (DDD), infrastructure-as-code, and production security standards.

========================================================
PROJECT CONTEXT
========================================================

We are building a Production-Grade AI Ticketing Platform with:

Cloud: AWS (Multi-AZ, Secure, HA)
Backend: FastAPI (Python 3.11)
Containerization: Docker
Orchestration: ECS Fargate
ML Platform: Amazon SageMaker (Training, Pipelines, Endpoints, Model Monitor)
Feature Store: SageMaker Feature Store (Online: DynamoDB, Offline: S3)
Vector DB: Amazon OpenSearch (kNN)
Streaming: MSK (Kafka)
CDC: AWS DMS
Lakehouse: S3 + Glue + Athena
LLM: Amazon Bedrock
Observability: CloudWatch, X-Ray
Security: IAM least privilege, KMS, VPC endpoints, WAF
IaC: Terraform (modular, environment-based)
CI/CD: GitHub Actions

Dataset Source: HuggingFace Customer Support Tickets

========================================================
ARCHITECTURE REQUIREMENTS
========================================================

1. Clean separation of:
   - API layer
   - Domain services
   - ML services
   - Feature store services
   - RAG services
   - Infrastructure modules

2. Implement:

   A) Classification Endpoint (SageMaker)
   B) Resolution Time Regression Endpoint
   C) Feature Store Online retrieval
   D) OpenSearch vector similarity search
   E) RAG using Bedrock
   F) Conversation memory (DynamoDB)
   G) CDC-triggered retraining pipeline

3. All components must:
   - Be production-safe
   - Include structured logging
   - Include proper exception handling
   - Include typing (mypy compatible)
   - Follow SOLID principles

========================================================
DELIVERABLES TO GENERATE
========================================================

Phase-by-phase code generation:

1️⃣ Project Folder Structure (enterprise standard)
2️⃣ FastAPI app (modular routers + dependency injection)
3️⃣ SageMaker service abstraction layer
4️⃣ Feature Store service (online retrieval + ingestion)
5️⃣ OpenSearch vector service
6️⃣ RAG orchestration layer
7️⃣ SageMaker Pipeline definition (training + register + conditional deploy)
8️⃣ Model Monitor configuration
9️⃣ Kafka consumer for CDC retraining
🔟 Terraform modules:
   - VPC
   - ECS
   - SageMaker
   - MSK
   - OpenSearch
   - IAM
   - S3
   - Feature Store
1️⃣1️⃣ GitHub Actions CI/CD
1️⃣2️⃣ Docker production setup
1️⃣3️⃣ Observability configuration
1️⃣4️⃣ Security best practices implementation

========================================================
CODING STANDARDS
========================================================

- Use Python 3.11
- Pydantic v2
- Async FastAPI where appropriate
- boto3 with proper session handling
- Structured logging (JSON format)
- No hardcoded secrets
- Environment-based config
- 12-factor app principles
- Use dependency injection pattern
- Strict type hints everywhere

========================================================
INFRASTRUCTURE RULES
========================================================

Terraform must:
- Be modular
- Support dev/stage/prod environments
- Use remote state (S3 + DynamoDB locking)
- Use least-privilege IAM
- Encrypt everything with KMS
- Use private subnets for compute
- Use VPC endpoints where possible

========================================================
MLOPS STANDARDS
========================================================

- Training via SageMaker Pipelines
- Model Registry integration
- Conditional deployment
- Drift detection (PSI)
- Blue/Green deployment
- Automatic rollback capability
- Feature consistency between training and inference

========================================================
NON-FUNCTIONAL REQUIREMENTS
========================================================

- Handle 10M+ tickets
- Horizontally scalable
- Idempotent retraining triggers
- High availability
- Multi-AZ deployment
- Observability across app + ML + infra

========================================================
OUTPUT FORMAT
========================================================

Generate the project step-by-step.

Start with:

1) High-level implementation plan
2) Then generate folder structure
3) Then implement each module incrementally

Each file must:
- Be production-ready
- Include docstrings
- Include type hints
- Include logging
- Include error handling

Do NOT generate toy examples.
Do NOT simplify architecture.
Follow enterprise-grade standards.

Act as if this system will be deployed in a Fortune 500 production environment.
