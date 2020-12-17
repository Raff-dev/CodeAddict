from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from django.core.serializers import serialize
from django.http import JsonResponse
from Profiles.models import Profile
from Movies.models import Movie, Ticket


class Movies(ViewSet):

    @action(methods=['get'], detail=True)
    def get_movie(self, request, *args, **kwargs):
        movie = Movie.objects.filter(pk=kwargs['pk']).first()
        result = {
            'Title': movie.title,
            'Price': movie.price,
            'Rating': movie.rating,
            'Description': movie.description
        }
        return Response(data=result, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False)
    def get_movies(self, request, *args, **kwargs):
        movies = Movie.objects.all()
        result = [{
            'Title': movie.title,
            'Price': movie.price
        } for movie in movies]

        return Response(data=result, status=status.HTTP_200_OK)
