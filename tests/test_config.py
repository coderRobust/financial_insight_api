from app.config import settings


def test_app_env_present():
    assert settings.APP_ENV is not None


def test_host_present():
    assert settings.HOST is not None


def test_port_is_integer():
    assert isinstance(settings.PORT, int)


def test_settings_dict_contains_expected_keys():
    data = settings.as_dict()
    assert "APP_ENV" in data
    assert "HOST" in data
    assert "PORT" in data
    assert "LOG_LEVEL" in data
    
    
def test_config_values_match_endpoint():
    from fastapi.testclient import TestClient
    from main import app

    client = TestClient(app)

    response = client.get("/config-check")
    assert response.status_code == 200

    data = response.json()

    assert data["env"] == settings.APP_ENV
    assert data["port"] == settings.PORT