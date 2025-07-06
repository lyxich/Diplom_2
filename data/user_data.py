import uuid


def generate_unique_user():
    return {
        "email": f"testuser_{str(uuid.uuid4())[:8]}@example.com",
        "password": "password",
        "name": "Test User"
    }


INGREDIENTS = ["60d3b41abdacab0026a733c6", "609646e4dc916e00276b2870"]