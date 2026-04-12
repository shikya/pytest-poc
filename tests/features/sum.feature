Feature: Sum function

  Scenario: Add two numbers
    Given I have numbers 2 and 3
    When I call sum
    Then the result should be 5