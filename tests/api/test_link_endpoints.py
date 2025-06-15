import pytest
from fastapi import status

def test_create_short_link(client, test_link_data):
    response = client.post("/short", json=test_link_data)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert "url_short" in data
    assert data["url_short"].startswith("http")
    tmp_url = " some url"
    assert data["url_short"] == f"{tmp_url}"

def test_get_original_link(client, test_link_data):
    # First create a short link
    create_response = client.post("/short", json=test_link_data)
    short_url = create_response.json()["url_short"]
    short_code = short_url.split("/")[-1]
    
    # Then try to get the original link
    response = client.get(f"/{short_code}", allow_redirects=False)
    assert response.status_code == status.HTTP_307_TEMPORARY_REDIRECT
    assert response.headers["location"] == test_link_data["url_origin"]

def test_create_user_link(client, test_user_data, test_link_data):
    # First create and login user
    client.post("/user/reg", json=test_user_data)
    login_data = {
        "email": test_user_data["email"],
        "password": test_user_data["password"]
    }
    login_response = client.post("/user/login", json=login_data)
    access_token = login_response.json()["access_token"]
    
    # Then create a link for the user
    response = client.post(
        "/user/create-link",
        json=test_link_data,
        headers={"Authorization": f"Bearer {access_token}"}
    )
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert "url_short" in data
    assert data["url_short"].startswith("http")

def test_get_user_links(client, test_user_data, test_link_data):
    # First create and login user
    client.post("/user/reg", json=test_user_data)
    login_data = {
        "email": test_user_data["email"],
        "password": test_user_data["password"]
    }
    login_response = client.post("/user/login", json=login_data)
    access_token = login_response.json()["access_token"]
    
    # Create a link for the user
    client.post(
        "/user/create-link",
        json=test_link_data,
        headers={"Authorization": f"Bearer {access_token}"}
    )
    
    # Get all user links
    response = client.get(
        "/user/my-links",
        headers={"Authorization": f"Bearer {access_token}"}
    )
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "url_short" in data[0]
    assert "url_origin" in data[0]


def test_delete_user_link(client, test_user_data, test_link_data):
    # First create and login user
    client.post("/user/reg", json=test_user_data)
    login_data = {
        "email": test_user_data["email"],
        "password": test_user_data["password"]
    }
    login_response = client.post("/user/login", json=login_data)
    access_token = login_response.json()["access_token"]
    
    # Create a link for the user
    create_response = client.post(
        "/user/create-link",
        json=test_link_data,
        headers={"Authorization": f"Bearer {access_token}"}
    )
    link_id = create_response.json()["url_short"].split("/")[-1]
    
    # Delete the link
    response = client.delete(
        f"/user/link/{link_id}",
        headers={"Authorization": f"Bearer {access_token}"}
    )
    assert response.status_code == status.HTTP_200_OK 