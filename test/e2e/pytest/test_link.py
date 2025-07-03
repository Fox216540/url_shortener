def create_link(client, link_data):
	response = client.post(
		"/short",
		json=link_data
	)
	assert response.status_code == 200
	return response
	
def get_link(client, short_code):
	response = client.get(f"/{short_code}")
	assert response.status_code == 200

def get_link_with_chat(client, short_code):
	response = client.get(f"/{short_code}/c")
	assert response.status_code == 200
	
def test_functional_link(
		client,
		link_data
	):
	# Создание короткой ссылки
	link = create_link(client, link_data)
	# Получение оригинальной ссылки
	get_link(client, link.json()['url_short'].split('/')[-1])

