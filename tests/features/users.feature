Feature: Users API

  Scenario: Get users list
    When I call GET /users
    Then the response status should be 200
    And the response should be a list