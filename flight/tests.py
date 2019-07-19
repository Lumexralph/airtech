"""Module containing tests for the account apps"""
import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Flight


class FlightModelTests(TestCase):
    """Class for the testcases of a flight"""

    def test_flight_was_successfully_created_with_valid_data(self):
        """flight instance should be successfully created"""
        time = timezone.now()
        return_time = timezone.now() + datetime.timedelta(days=30)
        data = {
            'flight_type': 'one way',
            'to_location': 'abuja',
            'from_location': 'lagos',
            'departure_date': time,
            'return_date': return_time,
            'total_seats': 200,
            'available_seats': 100,
        }

        flight = Flight(**data)

        self.assertIs(flight.flight_type, 'one way')
        self.assertEqual(flight.to_location, 'abuja')
        self.assertEqual(flight.from_location, 'lagos')
        self.assertEqual(flight.departure_date, time)
        self.assertEqual(flight.return_date, return_time)
        self.assertEqual(flight.total_seats, 200)
        self.assertEqual(flight.available_seats, 100)
