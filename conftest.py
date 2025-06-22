import pytest
import requests


@pytest.fixture(scope="module")
def auth_token():
    email = "testuser@example.com"
    password = "password"
    name = "Test User"

    # Регистрация пользователя (если ещё не зарегистрирован)
    register_response = requests.post(
        "https://stellarburgers.nomoreparties.site/api/auth/register",
        json={"email": email, "password": password, "name": name},
        timeout=10
    )

    if register_response.status_code == 403:
        pass  # Пользователь уже существует
    else:
        assert register_response.status_code == 200

    # Авторизация
    login_response = requests.post(
        "https://stellarburgers.nomoreparties.site/api/auth/login",
        json={"email": email, "password": password},
        timeout=10
    )
    assert login_response.status_code == 200

    token = login_response.json().get("accessToken")
    assert token is not None

    yield token  # Возвращаем строку токена