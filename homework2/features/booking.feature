Feature: Booking a seat
    Scenario: User books a seat 
        Given a movie exists
        And a seat for the movie exists
        When the user books the seat
        Then the seat should be marked as booked
