from app import APP_NAME, APP_VERSION


def test_app_name():
    assert APP_NAME == "DevOps Git Demo"


def test_app_version():
    assert APP_VERSION == "2.0.0"