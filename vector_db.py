from qdrant_client import QdrantClient

qdrant_client = QdrantClient(
    url="https://14a6c26a-2765-4d0b-bc0e-1f848f2823dc.eu-west-1-0.aws.cloud.qdrant.io:6333", 
    api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.sUNqGBgelEb1je0-IFk-aZFNjvT4GJduiie0aYBgXZI",
)

print(qdrant_client.get_collections())