Feature: Search functionality

  Scenario: User searches for a product
    Given the user is on the search page
    When the user enters a product name
    Then the search results should display relevant products

  Scenario: User searches with an empty query
    Given the user is on the search page
    When the user submits an empty search
    Then a message should indicate no results

  # Add more scenarios as needed
