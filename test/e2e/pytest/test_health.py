def test_health_check(client):
	response = client.get("/live")
	assert response.status_code == 200
	assert response.json() == {
		"status": "ok"
	}

def test_health_all(client):
	response = client.get("/health")
	assert response.status_code == 200
	assert response.json() == {
		"status": "ok",
		"db_status": "ok",
		"token_status": "ok"
	}

def test_health_db_check(client):
	response = client.get("/health/db")
	assert response.status_code == 200
	assert response.json() == {
		"status": "ok",
		"db_status": "ok"
	}

def test_health_token_storage_check(client):
	response = client.get("/health/token")
	assert response.status_code == 200
	assert response.json() == {
		"status": "ok",
		"token_status": "ok"
	}