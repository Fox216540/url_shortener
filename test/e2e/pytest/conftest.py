import pytest
from fastapi.testclient import TestClient
from start import app  # Замените на ваш файл с FastAPI приложением

@pytest.fixture
def client():
	return TestClient(app)

@pytest.fixture
def user_data():
	return {
		"email": "test@example.com",
		"password": "TestPass123!",
		"name": "Test User",
		"username": "testusername"
	}

@pytest.fixture
def user_link_data_with_room():
	return {
		"alias": "testalias1",
		"original_url": "https://translate.google.com/",
		"has_room": True
	}

@pytest.fixture
def user_link_data_without_room():
	return {
		"alias": "testalias2",
		"original_url": "https://translate.google.com/",
	}

@pytest.fixture
def user_link_data_without_alias_and_room():
	return {
		"original_url": "https://translate.google.com/",
	}
@pytest.fixture
def user_link_data_without_alias_and_with_room():
	return {
		"original_url": "https://translate.google.com/",
		"has_room": True
	}

@pytest.fixture
def link_data():
	return {
		"url_origin": "https://example.com",
	}