"""Define some fixtures to use in the project."""
import pytest

from apistar import test

from app.app import app

client = test.TestClient(app)


@pytest.fixture(scope='session')
def app_client_connection_root():
    response = client.get('/')
    return response


@pytest.fixture(scope='session')
def app_client_root_connection_all():
    response = client.get('/all')
    return response
