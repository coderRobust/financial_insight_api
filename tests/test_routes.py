from fastapi.testclient import TestClient
from main import app  # from root


client = TestClient(app)


def test_get_assets():
    response = client.get("/assets")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    
def test_config_check_endpoint():
    response = client.get("/config-check")
    assert response.status_code == 200

    data = response.json()

    assert "env" in data
    assert "log_level" in data
    assert "port" in data
