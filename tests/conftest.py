import pytest

from fastapi.testclient import TestClient
from sqlmodel import Session

from app.main import app
from app.db import test_engine


@pytest.fixture(scope="session")
def test_db():
    with Session(test_engine) as session:
        yield session
    

@pytest.fixture(scope="module")
def test_client():
    with TestClient(app) as client:
        yield client
