"""Module containing tests for the account apps"""
import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

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


class FlightTests(APITestCase):
    def setUp(self):
        """
        Configurations to be made available before each
        individual test case inheriting from this class.
        """
        url = reverse('account-registration')
        data = {
            "username": "Adenike",
            "email": "adenike@gmagil.com",
            "password": "dayo"
            }

        self.response = self.client.post(url, data, format='json')

        url = reverse('create-flight')
        data = {
            "flight_type": "economy",
            "to_location": "Abuja",
            "from_location": "Lagos",
            "departure_date": "2019-08-22T14:47:05Z",
            "return_date": "2019-08-27T14:47:05Z",
            "total_seats": 50,
            "available_seats": 37,
                    }

        token = 'Bearer ' + self.response['Authorization']
        self.client.post(url, data, HTTP_AUTHORIZATION=token, format='json')

    def test_flight_is_not_updated_when_it_not_exist(self):
        """
        Ensure a flight is successfully retrieved
        """
        url = '/flight/4/'
        data = {}
        token = 'Bearer ' + self.response['Authorization']
        response = self.client.put(url, data, HTTP_AUTHORIZATION=token, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_flight_was_deleted_successfully(self):
        """
        Ensure a flight is successfully deleted
        """
        url = '/flight/5/'
        token = 'Bearer ' + self.response['Authorization']
        response = self.client.delete(url, HTTP_AUTHORIZATION=token, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_flight_was_successfully_created(self):
        """
        Ensure the flight can be created
        """
        url = reverse('create-flight')
        data = {
            "flight_type": "economy",
            "to_location": "Abuja",
            "from_location": "Lagos",
            "departure_date": "2019-08-22T14:47:05Z",
            "return_date": "2019-08-27T14:47:05Z",
            "total_seats": 50,
            "available_seats": 37,
                    }

        token = 'Bearer ' + self.response['Authorization']
        response = self.client.post(url, data, HTTP_AUTHORIZATION=token, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Flight.objects.count(), 2)


    def test_flight_is_retrieved_successfully(self):
        """
        Ensure a flight is successfully retrieved
        """
        url = '/flight/2/'
    
        token = 'Bearer ' + self.response['Authorization']
        response = self.client.get(url, HTTP_AUTHORIZATION=token, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], 2)

    def test_flight_is_updated_successfully(self):
        """
        Ensure a flight is successfully retrieved
        """
        url = '/flight/3/'
        data = {}
        token = 'Bearer ' + self.response['Authorization']
        response = self.client.put(url, data, HTTP_AUTHORIZATION=token, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], 3)


    def test_to_get_all_created_fights(self):
        """
        Ensure flights can be gotten
        """
        url = reverse('create-flight')


        token = 'Bearer ' + self.response['Authorization']
        response = self.client.get(url, HTTP_AUTHORIZATION=token, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_flight_was_unsuccessfully_created(self):
        """
        Ensure the flight can't be created with invalid or incomplete data
        """
        url = reverse('create-flight')
        data = {
            "flight_type": "economy",
            "total_seats": 50,
            "available_seats": 37,
                    }

        token = 'Bearer ' + self.response['Authorization']
        response = self.client.post(url, data, HTTP_AUTHORIZATION=token, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Flight.objects.count(), 1)

    def test_flight_reservation_made_successfully(self):
        """
        Ensure reservation is made for a flight
        """
        url = '/flight/4/reservations'

        token = 'Bearer ' + self.response['Authorization']
        response = self.client.put(url, data={}, HTTP_AUTHORIZATION=token, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['to_location'], 'Abuja')
        self.assertEqual(response.data['from_location'], 'Lagos')

    def test_get_a_flight_reservation_successfully(self):
        """
        Ensure reservation is gotten
        """
        url = '/flight/9/reservations'

        token = 'Bearer ' + self.response['Authorization']
        response = self.client.get(url, HTTP_AUTHORIZATION=token, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], 9)
        self.assertEqual(response.data['to_location'], 'Abuja')
        self.assertEqual(response.data['from_location'], 'Lagos')
