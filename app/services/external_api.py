import httpx


def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"

    response = httpx.get(url, timeout=5.0)
    response.raise_for_status()

    return response.json()