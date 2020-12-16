from django.db import models
from Profiles.models import Profile
from django.core.validators import MaxValueValidator, MinValueValidator


class Movie(models.Model):
    title = models.CharField(max_length=30, unique=True)

    price = models.DecimalField(max_digits=8, decimal_places=2)

    description = models.CharField(max_length=300, null=True)

    rating = models.IntegerField(null=True, validators=[
        MaxValueValidator(10),
        MinValueValidator(1)
    ])

    class Meta():
        ordering = ['title']

    def __str__(self):
        return self.title


class Ticket(models.Model):
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name='tickets')

    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='tickets')

    class Meta():
        ordering = ['movie__title', 'profile__user__first_name', ]

    def __str__(self):
        return f"{self.profile}'s {self.movie} ticket"
