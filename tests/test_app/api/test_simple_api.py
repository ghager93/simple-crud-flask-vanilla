import flask

# from pytest_mock import MockerFixture

from app.api import simple_api
from app.models import Simple


def test_hello_world(app: flask.Flask):
    """Test hello world endpoint returns correctly."""
    # with app.test_request_context(method="GET"):
    result = simple_api.hello_world()

    assert result == "hello world!"


def test_post_no_assert(mocked_db_app: flask.Flask):
    """Test endpoint handles post request. No assert."""
    # with mocked_db_app.test_request_context(method="POST", json={}):
    result = simple_api.SimpleAPI(Simple).post()


def test_post_request_no_assert(mocked_db_app: flask.Flask):
    """Test actual request. No assert."""
    with mocked_db_app.test_request_context(method="POST", json={}):
        result = mocked_db_app.post("/simple")


def test_post_valid_payload(mocked_db_app: flask.Flask):
    """Test POST 200 response"""
    sample_payload = {"string": "valid test."}

    with mocked_db_app.test_request_context(method="POST", json=sample_payload):
        result = simple_api.SimpleAPI(Simple).post()

        assert 200 <= result[1] < 300

