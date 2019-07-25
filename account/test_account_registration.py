"""Module containing the account registration test"""

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from account.models import User

class AccountTests(APITestCase):
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

    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'Adenike')

    def test_account_login(self):
        """
        Ensure the user can login to the account
        """
        url = reverse('user-login')
        data = {
            "email": "adenike@gmagil.com",
            "password": "dayo"
            }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'Adenike')

    def test_retrieve_user_successfully(self):
        """
        Ensure a user is successfully retrieved
        """
        url = '/auth/users/3/'
        token = 'Bearer ' + self.response['Authorization']
        response = self.client.put(url, HTTP_AUTHORIZATION=token)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], 3)
        self.assertEqual(response.data['username'], 'Adenike')
        self.assertEqual(response.data['email'], 'adenike@gmagil.com')

    def test_user_updated_successfully(self):
        """
        Ensure a user is successfully retrieved
        """
        url = '/auth/users/4/'
        data = {
            "image_url": "https://images.pexels.com/photos/248797/pexels-photo-248797.jpeg",
            }
        token = 'Bearer ' + self.response['Authorization']
        response = self.client.get(url, data, HTTP_AUTHORIZATION=token, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], 4)
        self.assertEqual(response.data['username'], 'Adenike')
