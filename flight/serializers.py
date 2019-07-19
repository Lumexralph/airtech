"""Module containing the flight serializers"""

from rest_framework import  serializers
from flight.models import Flight


class FlightSerializer(serializers.ModelSerializer):
    """Class to handle the serializing and deserializing of flight data"""

    class Meta:
        """Class to add additional information to the serializer"""
        model = Flight
