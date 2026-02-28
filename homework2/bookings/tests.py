from django.test import TestCase
from datetime import date
from django.contrib.auth.models import User
from .models import Movie, Seat, Booking
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

#### UNIT TESTING ####
class MovieModelTest(TestCase):

    #Create movie for testing
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="Test Description",
            release_date=date(2026, 1, 1),
            duration=1
        )

    #Test if the movie title was saved correctly
    def test_movie_creation(self):
        self.assertEqual(self.movie.title, "Test Movie")


class BookingTest(TestCase):

    def setUp(self):
        #Create user for testing
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )

        #Create movie for testing
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="Test Description",
            release_date=date(2026, 1, 1),
            duration=1
        )

        #Create seat linked to movie for testing
        self.seat = Seat.objects.create(
            movie=self.movie,
            seat_number="A1"
        )

    def test_booking_creation(self):
        #Create booking object
        booking = Booking.objects.create(
            movie=self.movie,
            seat=self.seat,
            user=self.user
        )
        #Test if booking was successfully created
        self.assertEqual(booking.user.username, 'testuser')

#### INTEGRATION TESTING ####
class MovieAPITest(APITestCase):

    def setUp(self):
        #Create movie for testing that will be returned by the API
        self.movie = Movie.objects.create(
            title="API Movie",
            description="API Description",
            release_date=date(2026, 1, 1),
            duration=1
        )

    def test_get_movies(self):
        #Send get request to movie API
        response = self.client.get('/api/movies/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class BookingAPITest(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='apiuser',
            password='testpass'
        )

        # Log in the test client as the created user
        self.client.login(username='apiuser', password='testpass')

        # Create a movie
        self.movie = Movie.objects.create(
            title="Movie",
            description="Desc",
            release_date=date(2026, 1, 1),
            duration=1
        )

        # Create a seat linked to the movie
        self.seat = Seat.objects.create(
            movie=self.movie,
            seat_number="B1"
        )

    def test_create_booking(self):
        # Create booking data for POST request
        data = {
            "movie": self.movie.id,
            "seat": self.seat.id
        }

        # Send POST request to create booking via API
        response = self.client.post('/api/bookings/', data)

        # Check that booking was successfully created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)