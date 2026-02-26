from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from rest_framework import viewsets

#view to display all movies
def movie_list(request):
    movies = Movie.objects.all() #get all movies from db
    return render(request, 'bookings/movie_list.html', {
        'movies': movies
    })

#view to book a seat for a movie
def book_seat(request, movie_id):
    #get selected movie
    movie = Movie.objects.get(id=movie_id)

    #return only seats that aren't booked
    seats = Seat.objects.filter(is_booked=False)

    if request.method == "POST":
        seat_id = request.POST.get("seat")
        seat = Seat.objects.get(id=seat_id)
        #label seat booked
        seat.is_booked = True
        seat.save()

        #create booking record
        Booking.objects.create(
            movie=movie,
            seat=seat,
            user=request.user
        )

        #return to booking history page
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

