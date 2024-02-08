Feature: Search information in service page

  Scenario: User searches for a service
    Given the user is on the service page
    When the user search about the team
    Then the user see display relevant team information

  Scenario: User searches information about linkedin page
    Given the user is on the service page
    When the user search the linkedin button
    Then the linkedin button redirect to the linkedin page

  # Add more scenarios as needed
