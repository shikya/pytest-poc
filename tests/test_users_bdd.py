import pytest
from pytest_bdd import scenarios, when, then

BASE_URL = "http://127.0.0.1:8000"

scenarios("features/users.feature")


# Shared response container
class Context:
    response = None


context = Context()

@pytest.fixture
def response():
    # ----------------------
    # FIXTURE (shared state)
    # ----------------------
    return {}   # mutable container

# ----------------------
# STEPS
# ----------------------
@when("I call GET /users")
def call_get_users(client, response):
    response["res"] = client.get(f"{BASE_URL}/users")

@then("the response status should be 200")
def check_status(response):
    assert response["res"].status_code == 200

@then("the response should be a list")
def check_response_type(response):
    data = response["res"].json()
    assert isinstance(data, list)
