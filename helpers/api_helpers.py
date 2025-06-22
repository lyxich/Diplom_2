import requests
import random
import string

BASE_URL = "https://stellarburgers.nomoreparties.site/api"

def generate_email():
    letters = string.ascii_lowercase
    return f"{''.join(random.choice(letters) for _ in range(7))}@example.com"

def generate_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

def generate_name():
    return ''.join(random.choices(string.ascii_letters, k=8))