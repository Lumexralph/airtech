"""Module containing tests for the ticket app"""
from django.test import TestCase

from .models import Ticket


class TicketModelTests(TestCase):
    """Class for the testcases of a ticket"""

    def test_ticket_was_successfully_created_with_valid_data(self):
        """ticket instance should be successfully created"""
        data = {
            'ticket_class': 'FR',
            'cost': 100,
        }
        ticket = Ticket(**data)
        self.assertIs(ticket.cost, 100)
        self.assertEqual(ticket.ticket_class, 'FR')
        self.assertEqual(ticket.booked, False)

    def test_ticket_was_not_successfully_created_with_invalid_data(self):
        """ticket instance should not be successfully created"""
        data = {
            'username': 1,
            'email': 'user@gmail.com',
            'password': '12345',
        }

        with self.assertRaises(TypeError):
            Ticket(**data)
