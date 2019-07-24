"""Module containing the ticket for flights serializers"""

from rest_framework import  serializers
from ticket.models import Ticket
from flight.serializers import FlightDetailSerializer


class TicketSerializer(serializers.ModelSerializer):
    """Class to handle the serializing and deserializing of ticket data"""
    flight = FlightDetailSerializer(many=True, read_only=True)

    class Meta:
        """Class to add additional information to the serializer"""
        model = Ticket
        fields = ['id', 'ticket_class', 'cost', 'booked', 'owners',              'created_at','updated_at','deleted_at', 'flight']
        extra_kwargs = {'flight': {'required': False}}
