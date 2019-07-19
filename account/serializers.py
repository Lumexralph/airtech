"""Module containing the account user serializers"""

from rest_framework import  serializers
from account.models import User


class UserSerializer(serializers.ModelSerializer):
    """Class to handle the serializing and deserializing of user data"""

    class Meta:
        """Class to add additional information to the serializer"""
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'image_url']
        