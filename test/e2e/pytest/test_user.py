def register_user(client, user_data):
	response = client.post("/user/reg", json=user_data)
	assert response.status_code == 200
	return response


def logout_user(client, cookies):
	response = client.post("/user/logout", cookies=cookies)
	assert response.status_code == 200


def login_user(client, identifier, password):
	response = client.post("/user/login", json={
		"email_or_username": identifier,
		"password": password
	})
	assert response.status_code == 200
	return response


def change_password(client, token, old_password, new_password):
	response = client.patch("/user/change-password", json={
		"old_password": old_password,
		"new_password": new_password
	}, headers={"Authorization": f"Bearer {token}"})
	assert response.status_code == 200


def change_email(client, token, new_email):
	response = client.patch("/user/change-email", json={
		"email": new_email
	}, headers={"Authorization": f"Bearer {token}"})
	assert response.status_code == 200


def change_name(client, token, new_name):
	response = client.patch("/user/change-name", json={
		"name": new_name
	}, headers={"Authorization": f"Bearer {token}"})
	assert response.status_code == 200


def change_username(client, token, new_username):
	response = client.patch("/user/change-username", json={
		"username": new_username
	}, headers={"Authorization": f"Bearer {token}"})
	assert response.status_code == 200


def refresh_tokens(client, cookies):
	response = client.post("/user/refresh-tokens", cookies=cookies)
	assert response.status_code == 200
	return response


def create_link(client, token, link_data):
	response = client.post("/user/create-link", json=link_data,
						   headers={"Authorization": f"Bearer {token}"})
	assert response.status_code == 200
	return response


def get_links(client, token):
	response = client.post("/user/my-links",
						   headers={"Authorization": f"Bearer {token}"})
	assert response.status_code == 200

def delete_link(client, token, link_id):
	response = client.delete(f"/user/link/{link_id}",
							 headers={"Authorization": f"Bearer {token}"})
	assert response.status_code == 200

def delete_links(client, token):
	response = client.delete("/user/links",
							 headers={"Authorization": f"Bearer {token}"})
	assert response.status_code == 200


def delete_user(client, token):
	response = client.delete("/user/",
							 headers={"Authorization": f"Bearer {token}"})
	assert response.status_code == 200


def test_functional_user(
		client,
		user_data,
		user_link_data_with_room,
		user_link_data_without_room,
		user_link_data_without_alias_and_room,
		user_link_data_without_alias_and_with_room
):
	# Регистрация и выход
	reg_response = register_user(client, user_data)
	logout_user(client, reg_response.cookies)

	# Логин по username и выход
	login_response = login_user(client, user_data['username'], user_data['password'])
	logout_user(client, login_response.cookies)

	# Логин по email
	login_response = login_user(client, user_data['email'], user_data['password'])
	token = login_response.json()['access_token']

	# Изменения профиля
	change_password(client, token, user_data['password'], "newpassword123!")
	change_email(client, token, "newusername@gmail.com")
	change_name(client, token, "New Name")
	change_username(client, token, "newusername")

	# Обновление токенов
	refresh_response = refresh_tokens(client, login_response.cookies)
	new_token = refresh_response.json()['access_token']

	# Работа со ссылками
	link = create_link(client, new_token, user_link_data_with_room)
	create_link(client, new_token, user_link_data_without_room)
	create_link(client, new_token, user_link_data_without_alias_and_with_room)
	create_link(client, new_token, user_link_data_without_alias_and_room)
	
	# Удаление ссылки
	delete_link(client, new_token, link.json()['short_code'])
	
	# Получение всех ссылок
	get_links(client, new_token)
	
	# Удаление всех ссылок
	delete_links(client, new_token)

	# Удаление пользователя
	delete_user(client, new_token)
