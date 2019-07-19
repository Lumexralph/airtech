"""Module that holds the ticket entities"""

from django.db import models


class Ticket(models.Model):
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
    created_at = models.DateField(auto_now_add=True)
    deleted_at = models.DateTimeField(blank=True, null=True)