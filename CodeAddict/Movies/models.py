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
