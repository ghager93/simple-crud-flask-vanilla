import pytest
import flask.testing

from pytest_mock import MockerFixture


@pytest.fixture
def app():
    """Flask application from test project instance"""
    import app
    
    app = app.create_app()
    app.config.update(
        {
            "TESTING": True,
        }
    )
    return app


@pytest.fixture
def mocked_db_app(mocker: MockerFixture):
    """Flask application from test project instance"""
    import app

    app = app.create_app()

    # mocker.patch("app.models.db")

    app.config.update(
        {
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": "sqlite:///test_app.db",
            "SQLALCHEMY_TRACK_MODIFICATIONS": False, 
        }
    )

    with app.app_context():
        yield app


@pytest.fixture()
def mocked_db_client(mocked_db_app: flask.Flask):
    """A Flask test client. An instance of :class:`flask.testing.TestClient` by default."""
    with mocked_db_app.test_client() as client:
        yield client


@pytest.fixture
def client(app):
    return app.test_client()
