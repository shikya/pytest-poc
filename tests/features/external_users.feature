Feature: External Users API

  Scenario: Fetch users from external API
    When I call GET /external-users
    Then the response status should be 200
    And the response should contain external user "John Doe"