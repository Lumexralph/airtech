"""Module containing the account user serializers"""

from django.forms import model_to_dict
from rest_framework import  serializers
from account.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    """Class to handle the serializing and deserializing of user signup"""

    class Meta:
        """Class to add additional information to the serializer"""
        model = User
        exclude = ['password']

class UserLoginSerializer(serializers.ModelSerializer):
    """Class to handle the serializing and deserializing of user login"""

    class Meta:
        """Class to add additional information to the serializer"""
        model = User
        exclude = ['password']
        extra_kwargs = {'username': {'required': False}}

    def login(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']
        user = User.objects.filter(email=email).first()
        data = {
            'error': True
        }

        if user:
            result = user.check_password(password)

            if result:
                user_data = model_to_dict(user)
                user_data['error'] = False
                return user_data

        return data


class UserSerializer(serializers.ModelSerializer):
    """Class to handle the serializing and deserializing of user details"""

    class Meta:
        """Class to add additional information to the serializer"""
        model = User
        exclude = ['password']
        extra_kwargs = {'username': {'required': False},
        'email': {'required': False},
        'password': {'required': False}}