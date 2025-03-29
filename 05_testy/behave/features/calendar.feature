Feature: Calendar functionality
Scenario Outline: Rok przestępny
Given The year <year>
Then it should return <expected>

Examples:
  | year    | expected   |
  | 2001    | False      |
  | 2002    | False      |
  | 2003    | False      |
  | 2004    | True       |
  | 2008    | True       |
  | 2012    | True       |
  | 1900    | False      |
  | 2100    | False      |
  | 2000    | True       |
  | 2400    | True       |
