"""Module containing tests for the account apps"""
from django.test import TestCase

from .models import User


class UserModelTests(TestCase):
    """Class for the testcases of a user"""

    def test_user_was_successfully_created_with_valid_data(self):
        """user instance should be successfully created"""
        data = {
            'username': 'lumex',
            'email': 'user@gmail.com',
            'password': '12345',
        }
        user = User(**data)
        self.assertIs(user.is_admin, False)
        self.assertEqual(user.username, 'lumex')
        self.assertEqual(user.email, 'user@gmail.com')

    def test_user_was_not_successfully_created_with_invalid_data(self):
        """user instance should not be successfully created"""
        data = {
            'username': 1,
            'email': 'user@gmail.com',
            'password': '12345',
        }
        user = User(**data)
        self.assertIs(user.is_admin, False)
        self.assertNotIsInstance(user.username, str)
        self.assertEqual(user.email, 'user@gmail.com')
