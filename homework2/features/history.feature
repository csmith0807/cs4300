Feature: Booking History

  Scenario: User views booking history
    Given a logged in user with a booking
    When the user visits the booking history page
    Then the booking should be displayed