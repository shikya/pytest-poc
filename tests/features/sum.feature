Feature: Sum function

  Scenario: Add two numbers
    Given I have numbers 2 and 3
    When I call sum
    Then the result should be 5

  Scenario Outline: Add numbers
    Given I have numbers <a> and <b>
    When I call sum
    Then the result should be <result>

  Examples:
    | a | b | result |
    | 1 | 2 | 3      |
    | 5 | 7 | 12     |