from django.db import models
from django.contrib.auth.models import User

#Movie model
class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.IntegerField(help_text="Duration in minutes")

    def __str__(self):
        return self.title

#Seat model 
class Seat(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.movie.title} - {self.seat_number}"

#Booking model to connect user, movie, and seat
class Booking(models.Model):
    # Relationship to movie
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    booking_date = models.DateTimeField(auto_now_add=True)

    #String 
    def __str__(self):
        return f"{self.user.username} - {self.movie.title} - {self.seat.seat_number}"