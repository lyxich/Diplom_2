import allure
from utils.api_client import ApiClient


@allure.title("Авторизованный пользователь может получить свои заказы")
def test_get_orders_with_auth(auth_token):
    with allure.step("Когда пользователь запрашивает свои заказы"):
        api = ApiClient()
        response = api.get_orders(auth_token)

    with allure.step("Тогда статус ответа должен быть 200"):
        assert response.status_code == 200

    with allure.step("И список заказов присутствует"):
        json_response = response.json()
        assert "orders" in json_response


@allure.title("Неавторизованный пользователь не может получить заказы")
def test_get_orders_without_auth():
    with allure.step("Когда неавторизованный пользователь запрашивает заказы"):
        api = ApiClient()
        response = api.get_orders(None)

    with allure.step("Тогда статус ответа должен быть 401"):
        assert response.status_code == 401