from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_openapi_contains_paths():
    response = client.get("/openapi.json")
    assert response.status_code == 200
    body = response.json()
    assert "paths" in body


def test_openapi_contains_health_path():
    response = client.get("/openapi.json")
    assert response.status_code == 200
    body = response.json()
    assert "/health" in body["paths"]