"""Module containing the flight entity"""
from django.db import models

from ticket.models import Ticket

class Flight(models.Model):
    """Model for flights in the system"""

    class Meta:
        """Class to add more information on flight model"""
        ordering = ('departure_date', )

    flight_type = models.CharField(max_length=50, unique=True)
    to_location = models.CharField(max_length=150)
    from_location = models.CharField(max_length=150)
    departure_date = models.DateTimeField()
    ticket = models.ForeignKey(Ticket, related_name='flight', on_delete=models.CASCADE, null=True)
    return_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    total_seats = models.PositiveIntegerField()
    available_seats = models.PositiveIntegerField()
