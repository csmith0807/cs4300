from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, SeatViewSet, BookingViewSet
from . import views

# DefaultRouter automatically creates RESTful routes
router = DefaultRouter()

# Register API endpoints
router.register(r'movies', MovieViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    # All API routes handled here
    path('', views.movie_list, name='movie_list'),              # Movie list page
    path('book/<int:movie_id>/', views.book_seat, name='book_seat'),  # Seat booking page
    path('history/', views.booking_history, name='booking_history'),  # Booking history page
    path('api/', include(router.urls)),
]