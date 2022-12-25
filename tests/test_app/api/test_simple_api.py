import flask

# from pytest_mock import MockerFixture

from app.api import simple_api


def test_hello_world(app: flask.Flask):
    """Test hello world endpoint returns correctly."""
    with app.test_request_context(method="GET"):
        result = simple_api.hello_world()
        assert result == "hello world!"


def test_post_no_assert(mocked_db_app: flask.Flask):
    """Test endpoint handles post request. No assert."""
    with mocked_db_app.test_request_context(method="POST", json={}):
        result = simple_api.SimpleAPI().post()


def test_post_valid_payload(mocked_db_app: flask.Flask):
    """Test POST 200 response"""
    with mocked_db_app.test_request_context(method="POST", json={}):
        ...
