Feature: TodoList Management
  As a user
  I want to manage my todo list
  So that I can keep track of my tasks

  Scenario: Adding a task to the todo list
    Given I have an empty todo list
    When I add a task "Buy groceries"
    Then the todo list should contain 1 task
    And the todo list should contain the task "Buy groceries"
    And the task "Buy groceries" should be marked as not completed

  Scenario: Marking a task as completed
    Given I have a todo list with the following tasks:
      | task          | completed |
      | Buy groceries | False     |
    When I mark the task "Buy groceries" as completed
    Then the todo list should contain 1 task
    And the task "Buy groceries" should be marked as completed
    And the todo list should contain 0 pending tasks

  Scenario: Removing a task from the todo list
    Given I have a todo list with the following tasks:
      | task          | completed |
      | Buy groceries | False     |
      | Clean house   | False     |
    When I remove the task "Buy groceries"
    Then the todo list should contain 1 task
    And the todo list should not contain the task "Buy groceries"
    And the todo list should contain the task "Clean house"

  Scenario: Getting pending tasks
    Given I have a todo list with the following tasks:
      | task          | completed |
      | Buy groceries | False     |
      | Clean house   | True      |
      | Do laundry    | False     |
    When I get the pending tasks
    Then I should get a list with 2 tasks
    And the list should contain the task "Buy groceries"
    And the list should contain the task "Do laundry"
    And the list should not contain the task "Clean house"

  Scenario: Getting all tasks
    Given I have a todo list with the following tasks:
      | task          | completed |
      | Buy groceries | False     |
      | Clean house   | True      |
    When I get all tasks
    Then I should get a list with 2 tasks
    And the list should contain the task "Buy groceries" with status False
    And the list should contain the task "Clean house" with status True
