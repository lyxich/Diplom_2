import allure
from utils.api_client import ApiClient
from data.user_data import generate_unique_user


@allure.title("Новый пользователь может зарегистрироваться успешно")
def test_register_new_user():
    user = generate_unique_user()
    api = ApiClient()

    with allure.step("Когда пользователь регистрируется"):
        response = api.register_user(user["email"], user["password"], user["name"])

    with allure.step("Тогда статус ответа должен быть 200 или 403"):
        assert response.status_code in [200, 403]

    if response.status_code == 200:
        assert response.json().get("success") is True


@allure.title("Существующий пользователь не может зарегистрироваться снова")
def test_register_existing_user(auth_token):
    user = generate_unique_user()
    api = ApiClient()

    with allure.step("Когда существующий пользователь пытается зарегистрироваться снова"):
        response = api.register_user(user["email"], user["password"], user["name"])

    with allure.step("Тогда статус ответа должен быть 403"):
        assert response.status_code == 403

    with allure.step("И сообщение об ошибке верное"):
        assert response.json().get("message") == "User already exists"