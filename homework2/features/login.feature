Feature: User Login

  Scenario: User logs in successfully
    Given a user exists
    When the user logs in
    Then the user should be authenticated