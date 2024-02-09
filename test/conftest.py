import pytest
from src.app import server  # Adjust the import according to your project structure

@pytest.fixture
def app():
    yield server


@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client