import requests

BASE_URL = "http://127.0.0.1:8000"


def test_get_users():
    response = requests.get(f"{BASE_URL}/users")

    assert response.status_code == 200

    data = response.json()

    # Black-box checks
    assert isinstance(data, list)