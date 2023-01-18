import flask

# from pytest_mock import MockerFixture

from app.api import simple_api
from app.models import Simple


def test_hello_world(app: flask.Flask):
    """Test hello world endpoint returns correctly."""
    result = simple_api.hello_world()

    assert result == "hello world!"


def test_post_no_assert(mocked_db_app: flask.Flask):
    """Test endpoint handles post request. No assert."""

    with mocked_db_app.test_request_context("api/simple", method="POST", json={}):
        result = simple_api.SimpleAPI(Simple).post()


def test_post_request_no_assert(mocked_db_app: flask.Flask):
    """Test actual request. No assert."""
    result = mocked_db_app.post("/simple")


def test_post_valid_payload_2xx_status(mocked_db_app: flask.Flask):
    """Test POST 2xx response"""
    sample_payload = {"string": "valid test."}

    with mocked_db_app.test_request_context("api/simple", method="POST", json=sample_payload):
        result = simple_api.SimpleAPI(Simple).post()

    assert 200 <= result[1] < 300


def test_post_valid_payload_2xx_status(mocked_db_client: flask.Flask):
    sample_payload = {"string": "valid test10."}

    result = mocked_db_client.post("/simple/", json=sample_payload)

    assert 200 <= result.status_code < 300



def test_post_save_to_database(mocked_db_app: flask.Flask):
    """Test a valid payload is saved to the database."""
    sample_payload = {"string": "valid test1."}

    client = mocked_db_app.test_client()
    client.post("/simple/", json=sample_payload)

    result = client.get("/simple/")
        
    assert result.json[0] == sample_payload
    

