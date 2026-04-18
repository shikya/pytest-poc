Feature: Users API

#  Scenario: Get users list
#    When I call GET /users
#    Then the response status should be 200
#    And the response should be a list

  Scenario: Create and retrieve user
    When I create a user with name "Shrikant" and email "shrikant@test.com"
    Then the response status should be 200

    When I call GET /users
    Then the response should contain email "shrikant@test.com"