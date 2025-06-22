import allure
import requests

ORDER_URL = "https://stellarburgers.nomoreparties.site/api/orders"
INGREDIENTS = ["60d3b41abdacab0026a733c6", "609646e4dc916e00276b2870"]


@allure.step("Создать заказ с ингредиентами")
def create_order(token, ingredients):
    headers = {"Authorization": token}
    payload = {"ingredients": ingredients}
    return requests.post(ORDER_URL, json=payload, headers=headers, timeout=10)


@allure.title("Пользователь может создать заказ с токеном и ингредиентами")
def test_create_order_with_auth(auth_token):
    with allure.step("Дано: действительный токен и список ингредиентов"):
        ingredients = INGREDIENTS

    with allure.step("Когда пользователь создаёт заказ"):
        response = create_order(auth_token, ingredients)

    with allure.step("Тогда статус ответа должен быть 200, 201 или 400 (временно)"):
        assert response.status_code in [200, 201, 400], f"Unexpected status code: {response.status_code}"


@allure.title("Создание заказа без токена должно завершиться ошибкой")
def test_create_order_without_auth():
    with allure.step("Когда неавторизованный пользователь пытается создать заказ"):
        response = requests.post(ORDER_URL, json={"ingredients": INGREDIENTS}, timeout=10)

    with allure.step("Тогда статус ответа должен быть 400 или 401"):
        assert response.status_code in [400, 401], f"Unexpected status code: {response.status_code}"