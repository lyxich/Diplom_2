import allure
from utils.api_client import ApiClient


@allure.title("Пользователь может обновить имя с токеном")
def test_update_user_with_auth(auth_token):
    new_name = "Обновлённое Имя"

    with allure.step("Когда пользователь обновляет имя"):
        api = ApiClient()
        response = api.update_user_name(auth_token, new_name)

    with allure.step("Тогда статус ответа должен быть 200"):
        assert response.status_code == 200

    with allure.step("И имя пользователя обновилось"):
        json_response = response.json()
        assert json_response.get("user", {}).get("name") == new_name


@allure.title("Неавторизованный пользователь не может обновить данные")
def test_update_user_without_auth():
    with allure.step("Когда неавторизованный пользователь пытается обновить имя"):
        api = ApiClient()
        response = api.update_user_name(None, "Новое Имя")

    with allure.step("Тогда статус ответа должен быть 401"):
        assert response.status_code == 401