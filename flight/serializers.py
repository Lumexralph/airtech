"""Module containing the flight serializers"""

from rest_framework import  serializers
from flight.models import Flight
from account.serializers import UserSerializer


class FlightSerializer(serializers.ModelSerializer):
    """Class to handle the serializing and deserializing of flight data"""

    class Meta:
        """Class to add additional information to the serializer"""
        model = Flight
        fields = '__all__'


class FlightDetailSerializer(serializers.ModelSerializer):
    """Class to handle the serializing and deserializing of flight data"""
    reservations = UserSerializer(many=True, read_only=True)

    class Meta:
        """Class to add additional information to the serializer"""
        model = Flight
        fields = '__all__'
        extra_kwargs = {'to_location': {'required': False},
                        'from_location': {'required': False},
                        'departure_date': {'required': False},
                        'return_date': {'required': False},
                        'available_seats': {'required': False},
                        'flight_type': {'required': False},
                        'total_seats': {'required': False}}
