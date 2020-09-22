from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets, status, filters
from . import serializers, models, permissions
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated


class HelloAPIView(APIView):
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        an_apiview = [
            'an apiview uses the http method such as (Get, Post, Put, Patch, Delete)',
            'It is used when want more control over the logic',
        ]
        return Response({'message': 'Apiview', 'an_apiview': an_apiview})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        return ({'message': 'patch method'})

    def delete(self, request, pk=None):
        return ({'message': 'delete method'})

    def put(request, pk=None):
        """It updates the existing object"""
        return ({'message': 'put method executed'})


class HelloApiViewSet(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializer
    def list(self, request, format=None):
        an_apiviewset = [
            'it uses the actions as methods (list, create, retrieve, update, partial_update, destroy)',
            'it is used to develop quick apis'
        ]

        return Response({'message':'ApiViewSet', 'an_apiviewset': an_apiviewset})


    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message })

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle to retrieve a single object"""
        return Response({'message': 'retrieve method'})

    def update(self, request, pk=None):
        """Handle the update operation"""


class UserProfileViewset(viewsets.ModelViewSet):
    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UserProfilePermissions,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['name', 'email']


class UserProfileLogin(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ProfileFeedItemViewSet(viewsets.ModelViewSet):
    queryset = models.ProfileFeedItem.objects.all()
    serializer_class = serializers.ProfileFeedItemSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.ProfileFeedItemPermissions, IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user_profile = self.request.user)







