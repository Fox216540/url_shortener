def test_health_check(client):
	response = client.get("/live")
	assert response.status_code == 200
	assert response.json() == {"status": "ok"}

def test_health_db_check(client):
	response = client.get("/health/db")
	assert response.status_code == 200

def test_register_and_login(client):
	# 1. Регистрация пользователя
	response = client.post(
		"/user/reg",
		json={
			"email": "test@example.com",
			"password": "TestPass123!",
			"name": "Test User",
			"username": "testusername"
		}
	)
	assert response.status_code == 200

	# user_id = response.json()["id"]
	#
	#
	# # 3. Логин
	# login_response = client.post(
	# 	"/api/auth/login",
	# 	data={
	# 		"username": "testuser",
	# 		"password": "TestPass123!"
	# 	}
	# )
	# assert login_response.status_code == 200
	# token = login_response.json()["access_token"]
	#
	# # 4. Доступ к защищенному эндпоинту
	# protected_response = client.get(
	# 	"/api/users/me",
	# 	headers={"Authorization": f"Bearer {token}"}
	# )
	# assert protected_response.status_code == 200
	# assert protected_response.json()["username"] == "testuser"