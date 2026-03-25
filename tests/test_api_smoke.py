from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    body = response.json()

    assert body["status"] == "ok"
    assert body["service"] == "financial_insight_api"

    # 👇 THIS IS KEY
    assert "version" in body


def test_docs_endpoint():
    response = client.get("/docs")
    assert response.status_code == 200


def test_openapi_endpoint():
    response = client.get("/openapi.json")
    assert response.status_code == 200
    assert "paths" in response.json()