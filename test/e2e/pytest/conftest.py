import pytest
from fastapi.testclient import TestClient
from start import app  # Замените на ваш файл с FastAPI приложением

@pytest.fixture
def client():
    return TestClient(app)