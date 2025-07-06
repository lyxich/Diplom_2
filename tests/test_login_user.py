import allure
from utils.api_client import ApiClient
from data.user_data import generate_unique_user


@allure.title("Пользователь может войти с корректными данными")
def test_login_valid_user(auth_token):
    with allure.step("Когда пользователь отправляет запрос на вход"):
        api = ApiClient()
        response = api.login_user(generate_unique_user()["email"], "password")

    with allure.step("Тогда статус ответа должен быть 200"):
        assert response.status_code == 200

    with allure.step("И ответ содержит accessToken"):
        assert "accessToken" in response.json()