Feature: User login functionality

  Scenario: Successful login
    Given the user is on the login page
    When the user enters valid credentials
    Then the user should be logged in successfully

  Scenario: Invalid login attempt
    Given the user is on the login page
    When the user enters invalid credentials
    Then an error message should be displayed

  # Add more scenarios as needed
