import flask

# from pytest_mock import MockerFixture

from app import db
from app.api import simple_api


def test_hello_world(app: flask.Flask):
    """Test hello world endpoint returns correctly."""
    with app.test_request_context(method="GET"):
        result = simple_api.hello_world()
        assert result == "hello world!"


def test_post_empty_payload(mocked_db_app: flask.Flask):
    with mocked_db_app.test_request_context(method="POST", json={}):
        result = simple_api.SimpleAPI().post()
