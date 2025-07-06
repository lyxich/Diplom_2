import requests
from data.urls import (
    ORDER_URL,
    REGISTER_URL,
    LOGIN_URL,
    ORDERS_URL,
    UPDATE_URL,
)


class ApiClient:
    def create_order(self, ingredients, token=None):
        headers = {}
        if token:
            headers["Authorization"] = token
        payload = {"ingredients": ingredients}
        return requests.post(ORDER_URL, json=payload, headers=headers, timeout=10)

    def register_user(self, email, password, name):
        payload = {"email": email, "password": password, "name": name}
        return requests.post(REGISTER_URL, json=payload, timeout=10)

    def login_user(self, email, password):
        payload = {"email": email, "password": password}
        return requests.post(LOGIN_URL, json=payload, timeout=10)

    def get_orders(self, token):
        headers = {"Authorization": token}
        return requests.get(ORDERS_URL, headers=headers, timeout=10)

    def update_user_name(self, token, new_name):
        headers = {"Authorization": token}
        payload = {"name": new_name}
        return requests.patch(UPDATE_URL, json=payload, headers=headers, timeout=10)