from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, SeatViewSet, BookingViewSet

# DefaultRouter automatically creates RESTful routes
router = DefaultRouter()

# Register API endpoints
router.register(r'movies', MovieViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    # All API routes handled here
    path('', include(router.urls)),
]