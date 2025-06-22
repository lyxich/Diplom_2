import allure
import requests


ORDERS_URL = "https://stellarburgers.nomoreparties.site/api/orders"


@allure.step("Получить заказы с токеном")
def get_orders(token):
    headers = {"Authorization": token}
    return requests.get(ORDERS_URL, headers=headers, timeout=10)


@allure.title("Авторизованный пользователь может получить свои заказы")
def test_get_orders_with_auth(auth_token):
    with allure.step("Когда пользователь запрашивает свои заказы"):
        response = get_orders(auth_token)

    with allure.step("Тогда статус ответа должен быть 200"):
        assert response.status_code == 200

    with allure.step("И список заказов присутствует"):
        assert "orders" in response.json()


@allure.title("Неавторизованный пользователь не может получить заказы")
def test_get_orders_without_auth():
    with allure.step("Когда неавторизованный пользователь запрашивает заказы"):
        response = requests.get(ORDERS_URL, timeout=10)

    with allure.step("Тогда статус ответа должен быть 401"):
        assert response.status_code == 401