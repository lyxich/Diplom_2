import allure
import requests


@allure.step("Отправка запроса на вход с email: {email}")
def send_login_request(email, password):
    url = "https://stellarburgers.nomoreparties.site/api/auth/login"
    payload = {"email": email, "password": password}
    return requests.post(url, json=payload, timeout=10)


@allure.title("Пользователь может войти с корректными данными")
def test_login_valid_user(auth_token):
    with allure.step("Дано: пользователь зарегистрирован"):
        pass  # Подготовлен фикстурой

    with allure.step("Когда пользователь отправляет запрос на вход"):
        response = send_login_request("testuser@example.com", "password")

    with allure.step("Тогда статус ответа должен быть 200"):
        assert response.status_code == 200

    with allure.step("И ответ содержит accessToken"):
        assert "accessToken" in response.json()