from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    body = response.json()
    assert "message" in body


def test_info_endpoint():
    response = client.get("/info")
    assert response.status_code == 200
    body = response.json()
    assert body["service"] == "financial_insight_api"
    assert "environment" in body