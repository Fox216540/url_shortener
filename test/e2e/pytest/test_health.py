def test_health_check(client):
	response = client.get("/live")
	assert response.status_code == 200
	assert response.json() == {"status": "ok"}

def test_health_db_check(client):
	response = client.get("/health/db")
	print(response)
	assert response.status_code == 200

def test_health_token_storage_check(client):
	response = client.get("/health/token")
	print(response)
	assert response.status_code == 200