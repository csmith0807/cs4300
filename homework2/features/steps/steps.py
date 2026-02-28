from behave import given, when, then
from bookings.models import Movie, Seat, User, Booking
from django.test.client import Client
from datetime import date
from django.urls import reverse


####Booking feature test####
@given('a movie exists')
def step_movie_exists(context):
    context.movie = Movie.objects.create(
        title="BDD Movie",
        description="BDD Description",
        release_date=date.today(),
        duration="1"
    )

@given('a seat for the movie exists')
def step_seat_exists(context):
    context.seat = Seat.objects.create(
        movie=context.movie,
        seat_number="C1"
    )

@when('the user books the seat')
def step_book_seat(context):
    context.seat.is_booked = True
    context.seat.save()

@then('the seat should be marked as booked')
def step_verify_booking(context):
    assert context.seat.is_booked is True

####Login feature test####
@given('a user exists')
def step_user_exists(context):
    context.username = "bdduser"
    context.password = "testpass123"

    context.user, created = User.objects.get_or_create(
        username=context.username
    )

    if created:
        context.user.set_password(context.password)
        context.user.save()

@when('the user logs in')
def step_user_logs_in(context):
    context.client = Client()
    context.logged_in = context.client.login(
        username=context.username,
        password=context.password
    )

@then('the user should be authenticated')
def step_user_authenticated(context):
    assert context.logged_in is True

####History Feature Test####
@given('a logged in user with a booking')
def step_logged_in_user_with_booking(context):
    context.client = Client()

    context.username = "historyuser"
    context.password = "testpass123"

    context.user, created = User.objects.get_or_create(
        username=context.username
    )

    if created:
        context.user.set_password(context.password)
        context.user.save()

    context.client.login(
        username="historyuser",
        password="testpass123"
    )

    context.movie = Movie.objects.create(
        title="History Movie",
        description="Test",
        release_date=date.today(),
        duration="1"
    )

    context.seat = Seat.objects.create(
        movie=context.movie,
        seat_number="D1",
        is_booked=True
    )

    context.booking = Booking.objects.create(
        movie=context.movie,
        seat=context.seat,
        user=context.user
    )

@when('the user visits the booking history page')
def step_visit_history(context):
    context.response = context.client.get(reverse('booking_history'))

@then('the booking should be displayed')
def step_booking_displayed(context):
    assert context.response.status_code == 200
    assert bytes(context.movie.title, 'utf-8') in context.response.content
