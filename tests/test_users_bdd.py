import pytest
from pytest_bdd import scenarios, when, then, parsers

BASE_URL = "http://127.0.0.1:8000"

scenarios("features/users.feature")


# Shared response container
# class Context:
#     response = None


# context = Context()
# ----------------------
# FIXTURES
# ----------------------
@pytest.fixture
def context():
    return {}   # shared mutable state
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

# ----------------------
# STEPS
# ----------------------

@when(parsers.parse('I create a user with name "{name}" and email "{email}"'))
def create_user(client, context, name, email):
    payload = {
        "name": name,
        "email": email
    }

    res = client.post("/users", json=payload)

    context["create_response"] = res


@then("the response status should be 200")
def check_status(context):
    assert context["create_response"].status_code == 200


@when("I call GET /users")
def get_users(client, context):
    res = client.get("/users")
    context["get_response"] = res


@then(parsers.parse('the response should contain email "{email}"'))
def check_user_present(context, email):
    data = context["get_response"].json()

    emails = [user["email"] for user in data]

    assert email in emails