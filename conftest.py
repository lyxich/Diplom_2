import pytest
from data.user_data import generate_unique_user
from utils.api_client import ApiClient


@pytest.fixture(scope="function")
def auth_token():
    user = generate_unique_user()
    api = ApiClient()

    # Регистрация
    register_response = api.register_user(user["email"], user["password"], user["name"])
    if register_response.status_code not in [200, 201]:
        raise RuntimeError(f"User registration failed: {register_response.text}")

    # Авторизация
    login_response = api.login_user(user["email"], user["password"])
    if login_response.status_code != 200:
        raise RuntimeError(f"Login failed: {login_response.text}")
    token = login_response.json()["accessToken"]

    yield token

    # Удаление после теста
    delete_response = api.delete_user(token)
    if delete_response.status_code not in [200, 202]:
        raise RuntimeError(f"User deletion failed: {delete_response.text}")