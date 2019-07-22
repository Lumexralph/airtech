"""Module containing the account user serializers"""

from django.forms import model_to_dict
from rest_framework import  serializers
from account.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    """Class to handle the serializing and deserializing of user signup"""

    class Meta:
        """Class to add additional information to the serializer"""
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'image_url', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserLoginSerializer(serializers.ModelSerializer):
    """Class to handle the serializing and deserializing of user login"""

    class Meta:
        """Class to add additional information to the serializer"""
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'image_url', 'email']
        extra_kwargs = {'username': {'required': False}}

    def login(self, validated_data):
        email = validated_data['email']
        user = User.objects.filter(email=email).first()

        user_data = model_to_dict(user)
        return user_data
