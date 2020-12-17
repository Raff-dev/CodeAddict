from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status, generics
from django.core.serializers import serialize
from django.http import JsonResponse
from Profiles.models import Profile
from Movies.models import Movie, Ticket
from Movies.serializers import MovieSerializer
from .Serializers import RegisterSerializer, UserSerializer

from django.contrib.auth.models import User


# Register API
class Register(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(request.data)

        serializer.is_valid(raise_exception=True)
        print('here')

        user = serializer.save()
        print('here')
        result = {
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        }
        return Response(data=result, status=HTTP_201_CREATED)


class Profiles(ViewSet):
    permission_classes = [IsAuthenticated, ]

    @action(methods=['get'], detail=False)
    def get_tickets(self, request, *args, **kwargs):
        profile = request.user.profile
        tickets = profile.tickets.all()

        result = [{
            'Movie title': ticket.movie.title,
            'Buy timestamp': ticket.buy_timestamp,
        } for ticket in tickets]

        return Response(data=result, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=True)
    def buy_ticket(self, request, pk=None, *args, **kwargs):
        try:
            profile = request.user.profile
            movie = Movie.objects.filter(pk=pk).first()
            ticket = Ticket.objects.create(profile=profile, movie=movie)

            result = {
                'Movie title': ticket.movie.title,
                'Buy timestamp': ticket.buy_timestamp,
            }
            return Response(data=result, status=status.HTTP_201_CREATED)

        except Exception as e:
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
