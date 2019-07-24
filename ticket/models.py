"""Module that holds the ticket entities"""

from django.db import models

from account.models import User
from shared.base_model import BaseModel


class Ticket(BaseModel):
    """Class to handle tickets for users when flight is booked"""

    class Meta:
        """Class to add more information to ticket model"""
        ordering = ('created_at', )

    BUSINESS = 'BS'
    FIRST = 'FR'
    ECONOMY = 'EC'
    TICKET_CLASS = [
        (BUSINESS, 'Business'),
        (FIRST, 'First'),
        (ECONOMY, 'Economy'),
    ]
    ticket_class = models.CharField(
        max_length=2,
        choices=TICKET_CLASS,
        default=BUSINESS,
    )
    cost = models.IntegerField(default=0)
    booked = models.BooleanField(default=False)
    owners = models.ForeignKey(User, null=True, related_name='my_tickets', on_delete=models.CASCADE)
