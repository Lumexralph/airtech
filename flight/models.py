"""Module containing the flight entity"""
from django.db import models

from ticket.models import Ticket
from account.models import User
from shared.base_model import BaseModel

class Flight(BaseModel):
    """Model for flights in the system"""

    class Meta:
        """Class to add more information on flight model"""
        ordering = ('departure_date', )

    flight_type = models.CharField(max_length=50)
    to_location = models.CharField(max_length=150)
    from_location = models.CharField(max_length=150)
    departure_date = models.DateTimeField()
    ticket = models.ForeignKey(Ticket, related_name='flight',
                               on_delete=models.CASCADE, null=True)
    return_date = models.DateTimeField()
    total_seats = models.PositiveIntegerField()
    available_seats = models.PositiveIntegerField()
    reservations = models.ForeignKey(User, related_name='reserved_flights',
                                     on_delete=models.DO_NOTHING, null=True)
