"""Module containing the ticket for flights serializers"""

from rest_framework import  serializers
from ticket.models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    """Class to handle the serializing and deserializing of ticket data"""

    class Meta:
        """Class to add additional information to the serializer"""
        model = Ticket
