from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TicketTests(APITestCase):
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

        url = '/ticket/flight/13/'
        data = {
            'cost': 67
        }
        
        self.client.post(url, data, HTTP_AUTHORIZATION=token, format='json')

    def test_ticket_is_created_successfully(self):
        """
        Ensure a ticket is successfully created
        """
        url = '/ticket/flight/12/'
        data = {"ticket_class":"BS","cost":0}

        token = 'Bearer ' + self.response['Authorization']
        response = self.client.post(url, data, HTTP_AUTHORIZATION=token, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_all_tickets_created_successfully(self):
        """
        Ensure all tickets are gotten
        """
        url = '/ticket/'
        token = 'Bearer ' + self.response['Authorization']
        response = self.client.get(url, HTTP_AUTHORIZATION=token, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
