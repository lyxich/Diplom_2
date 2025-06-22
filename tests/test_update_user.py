import allure
import requests


UPDATE_URL = "https://stellarburgers.nomoreparties.site/api/auth/user"


@allure.step("Обновление имени пользователя на {new_name}")
def update_user_name(token, new_name):
    headers = {"Authorization": token}
    payload = {"name": new_name}
    return requests.patch(UPDATE_URL, json=payload, headers=headers, timeout=10)


@allure.title("Пользователь может обновить имя с токеном")
def test_update_user_with_auth(auth_token):
    new_name = "Обновлённое Имя"

    with allure.step("Когда пользователь обновляет имя"):
        response = update_user_name(auth_token, new_name)

    with allure.step("Тогда статус ответа должен быть 200"):
        assert response.status_code == 200

    with allure.step("И имя пользователя обновилось"):
        assert response.json()["user"]["name"] == new_name


@allure.title("Неавторизованный пользователь не может обновить данные")
def test_update_user_without_auth():
    with allure.step("Когда неавторизованный пользователь пытается обновить имя"):
        response = requests.patch(UPDATE_URL, json={"name": "Новое Имя"}, timeout=10)

    with allure.step("Тогда статус ответа должен быть 401"):
        assert response.status_code == 401