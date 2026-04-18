Feature: Users API

  Scenario: Create and retrieve user
    When I create a user with name "Shrikant" and email "shrikant@test.com"
    Then the response status should be 200

    When I call GET /users
    Then the response should contain email "shrikant@test.com"