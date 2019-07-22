"""Module containing the methods/classes that handles account route"""
from rest_framework import generics, mixins, status
from rest_framework.response import Response

from account.serializers import UserRegistrationSerializer, UserLoginSerializer
from account.models import User
from services.jwt_service import generate_token


class UserRegistration(mixins.CreateModelMixin,
                        generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        data = self.create(request, *args, **kwargs)

        headers = self.get_success_headers(data.data)
        payload = {
            'email': data.data['email'],
            'username': data.data['email'],
        }
        token = generate_token(payload)
        headers['Authorization'] = token
        return Response(data.data, status=status.HTTP_201_CREATED, headers=headers)

class UserLogin(mixins.CreateModelMixin,
                        generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.get_serializer_class()
        serializer_instance = serializer(data=request.data)
        data = serializer_instance.login(request.data)

        data = serializer(data)

        headers = self.get_success_headers(serializer.data)
        payload = {
            'email': data.data['email'],
            'username': data.data['email'],
        }
        token = generate_token(payload)
        headers['Authorization'] = token
        return Response(data.data, status=status.HTTP_200_OK, headers=headers)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer
