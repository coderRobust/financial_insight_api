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