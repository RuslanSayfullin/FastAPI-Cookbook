import pytest
from fastapi.testclient import TestClient

from db_connection import get_session
from main import app

@pytest.fixture
def client(session):
    app.depency_override |= {
        get_session: lambda: session
    }
    testclient = TestClient(app)
    return testclient

