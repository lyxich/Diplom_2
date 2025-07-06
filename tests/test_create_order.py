import allure
from utils.api_client import ApiClient
from data.user_data import INGREDIENTS


@allure.title("Пользователь может создать заказ с токеном и ингредиентами")
def test_create_order_with_auth(auth_token):
    with allure.step("Когда пользователь создаёт заказ"):
        api = ApiClient()
        response = api.create_order(INGREDIENTS, token=auth_token)

    with allure.step("Тогда статус ответа должен быть 200 или 201"):
        assert response.status_code in [200, 201], f"Unexpected status code: {response.status_code}"

    with allure.step("И ответ содержит 'success' == True"):
        json_response = response.json()
        assert json_response.get("success") is True, "Order creation failed or response invalid"


@allure.title("Создание заказа без токена должно завершиться ошибкой")
def test_create_order_without_auth():
    with allure.step("Когда неавторизованный пользователь пытается создать заказ"):
        api = ApiClient()
        response = api.create_order(INGREDIENTS)

    with allure.step("Тогда статус ответа должен быть 401"):
        assert response.status_code == 401, f"Unexpected status code: {response.status_code}"