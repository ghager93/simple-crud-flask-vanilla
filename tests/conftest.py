import pytest
import flask.testing

from pytest_mock import MockerFixture

from instance import config


@pytest.fixture
def app():
    """Flask application from test project instance"""
    import app
    
    app = app.create_app(config.TestConfig)

    return app


@pytest.fixture()
def mocked_db_app(mocker: MockerFixture):
    """Flask application from test project instance"""
    import app
    from app import db

    app = app.create_app(config.TestConfig)

    mocker.patch("app.db")

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


@pytest.fixture()
def mocked_db_client(mocked_db_app: flask.Flask):
    """A Flask test client. An instance of :class:`flask.testing.TestClient` by default."""
    with mocked_db_app.test_client() as client:
        yield client


@pytest.fixture()
def client(app):
    return app.test_client()
