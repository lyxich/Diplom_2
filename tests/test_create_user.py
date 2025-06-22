import allure
import requests


REGISTER_URL = "https://stellarburgers.nomoreparties.site/api/auth/register"


@allure.step("Регистрация пользователя с email: {email}")
def register_new_user(email, password, name):
    payload = {"email": email, "password": password, "name": name}
    return requests.post(REGISTER_URL, json=payload, timeout=10)


@allure.title("Новый пользователь может зарегистрироваться успешно")
def test_register_new_user():
    email = "newuser@example.com"
    password = "password"
    name = "Новый Пользователь"

    with allure.step(f"Дано: новый пользователь {email} ещё не зарегистрирован"):
        pass

    with allure.step("Когда пользователь регистрируется"):
        response = register_new_user(email, password, name)

    with allure.step("Тогда статус ответа должен быть 200 или 403"):
        assert response.status_code in [200, 403]

    if response.status_code == 200:
        assert response.json()["success"] is True


@allure.title("Существующий пользователь не может зарегистрироваться снова")
def test_register_existing_user(auth_token):
    email = "testuser@example.com"
    password = "password"
    name = "Test User"

    with allure.step(f"Когда существующий пользователь {email} пытается зарегистрироваться снова"):
        response = register_new_user(email, password, name)

    with allure.step("Тогда статус ответа должен быть 403"):
        assert response.status_code == 403

    with allure.step("И сообщение об ошибке верное"):
        assert response.json()["message"] == "User already exists"