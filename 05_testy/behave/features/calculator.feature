Feature: Calculator functionality
  As a user
  I want to perform basic arithmetic operations
  So that I can do quick calculations

  Scenario: Addition of two numbers
    Given I have a calculator
    When I add 5 and 7
    Then the result should be 12

  Scenario: Subtraction of two numbers
    Given I have a calculator
    When I subtract 8 from 15
    Then the result should be 7