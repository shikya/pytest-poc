from pytest_bdd import scenarios, given, when, then

from pytest_bdd import scenarios, given, when, then, parsers
from main import sum

# Link feature file
scenarios("features/sum.feature")

# Step 1: Given → create fixture
@given(parsers.parse("I have numbers {a:d} and {b:d}"), target_fixture="numbers")
def numbers_fixture(a, b):
    return {"a": a, "b": b}


# Step 2: When → call function
@when("I call sum", target_fixture="result")
def call_sum(numbers):
    return sum(numbers["a"], numbers["b"])


# Step 3: Then → assert
@then(parsers.parse("the result should be {expected:d}"))
def check_result(result, expected):
    assert result == expected