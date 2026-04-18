from pytest_bdd import scenarios, when, then
import pytest
import respx
import httpx

scenarios("features/external_users.feature")


# ----------------------
# FIXTURE
# ----------------------
@pytest.fixture
def context():
    return {}


# ----------------------
# STEPS
# ----------------------

@when("I call GET /external-users")
def call_external_api(client, context):
    with respx.mock:
        respx.get("https://jsonplaceholder.typicode.com/users").mock(
            return_value=httpx.Response(
                200,
                json=[
                    {"id": 1, "name": "John Doe"},
                    {"id": 2, "name": "Jane Doe"},
                ],
            )
        )

        response = client.get("/external-users")
        context["response"] = response


@then("the response status should be 200")
def check_status(context):
    assert context["response"].status_code == 200


@then('the response should contain external user "John Doe"')
def check_user(context):
    data = context["response"].json()

    names = [user["name"] for user in data]

    assert "John Doe" in names