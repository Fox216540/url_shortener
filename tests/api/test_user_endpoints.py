import pytest
from fastapi import status

def test_create_user(client, test_user_data):
    response = client.post("/user/reg", json=test_user_data)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["username"] == test_user_data["username"]
    assert "access_token" in data
    assert "refresh_token" in response.cookies

def test_check_username_exists(client, test_user_data):
    # First create a user
    client.post("/user/reg", json=test_user_data)
    
    # Then check if username exists
    response = client.get(f"/user/check-username?username={test_user_data['username']}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["exist"] is True


def test_check_empty_username_exists(client, test_user_data):
    # First create a user
    client.post("/user/reg", json="")

    # Then check if username exists
    response = client.get(f"/user/check-username?username={test_user_data['username']}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["exist"] is True

def test_check_email_exists(client, test_user_data):
    # First create a user
    client.post("/user/reg", json=test_user_data)
    
    # Then check if email exists
    response = client.get(f"/user/check-email?email={test_user_data['email']}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["exist"] is True

def test_login_user(client, test_user_data):
    # First create a user
    client.post("/user/reg", json=test_user_data)
    
    # Then try to login
    login_data = {
        "email": test_user_data["email"],
        "password": test_user_data["password"]
    }
    response = client.post("/user/login", json=login_data)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["username"] == test_user_data["username"]
    assert "access_token" in data
    assert "refresh_token" in response.cookies

def test_logout_user(client, test_user_data):
    # First create and login user
    client.post("/user/reg", json=test_user_data)
    login_data = {
        "email": test_user_data["email"],
        "password": test_user_data["password"]
    }
    login_response = client.post("/user/login", json=login_data)
    refresh_token = login_response.cookies.get("refresh_token")
    
    # Then try to logout
    response = client.post("/user/logout")
    assert response.status_code == status.HTTP_200_OK
    assert "refresh_token" not in response.cookies

def test_change_password(client, test_user_data):
    # First create and login user
    client.post("/user/reg", json=test_user_data)
    login_data = {
        "email": test_user_data["email"],
        "password": test_user_data["password"]
    }
    login_response = client.post("/user/login", json=login_data)
    access_token = login_response.json()["access_token"]
    
    # Then try to change password
    change_password_data = {
        "old_password": test_user_data["password"],
        "new_password": "newpassword123"
    }
    response = client.post(
        "/user/change-password",
        json=change_password_data,
        headers={"Authorization": f"Bearer {access_token}"}
    )
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["username"] == test_user_data["username"] 