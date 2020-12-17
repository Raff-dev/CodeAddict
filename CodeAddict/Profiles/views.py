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
