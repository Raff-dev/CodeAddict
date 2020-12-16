from django.contrib import admin

from Movies.models import Movie, Ticket

admin.site.register(Movie)
admin.site.register(Ticket)
