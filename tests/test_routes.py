from fastapi.testclient import TestClient
from main import app  # from root


client = TestClient(app)


def test_get_assets():
    response = client.get("/assets")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
