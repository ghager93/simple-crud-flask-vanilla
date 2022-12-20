import flask

# from pytest_mock import MockerFixture

from app import db
from app.api import simple_api

def test_hello_world(app: flask.Flask):
    """Test handler works."""
    with app.test_request_context(method="GET"):
        result = simple_api.hello_world()
        assert result == "hello world!"
