from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer

#ViewSet for seat API
class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

#ViewSet for booking API
class BookingViewSet(viewsets.ModelViewSet):
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

