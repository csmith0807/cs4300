from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

#view to display all movies
def movie_list(request):
    movies = Movie.objects.all() #get all movies from db
    return render(request, 'bookings/movie_list.html', {
        'movies': movies
    })

#view to book a seat for a movie
@login_required
def book_seat(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    seats = Seat.objects.filter(movie=movie)

    if request.method == "POST":
        seat_id = request.POST.get("seat")
        seat = get_object_or_404(Seat, id=seat_id, movie=movie)

        seat.is_booked = True
        seat.save()

        Booking.objects.create(
            movie=movie,
            seat=seat,
            user=request.user
        )

        return redirect('booking_history')

    return render(request, 'bookings/seat_booking.html', {
        'movie': movie,
        'seats': seats
    })

#view to see current bookings
def booking_history(request):
    #get bookings
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_history.html', {
        'bookings': bookings
    })

#ViewSet for seat API
class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

#ViewSet for booking API
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    # Automatically assign logged-in user
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    # Only return bookings belonging to the current user
    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

    #Assign logged-in user when creating booking
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

#Movie view set
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()      #Get all movies
    serializer_class = MovieSerializer  

