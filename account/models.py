"""Module containing the user entity"""
from django.db import models


class User(models.Model):
    """Model for a user in the system"""

    class Meta:
        """Class to add more information on user model"""
        ordering = ('username', )

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=150, unique=True)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    image_url = models.URLField(
        default='https://res.cloudinary.com/health-id/image/upload/'
        'v1554552278/Profile_Picture_Placeholder.png'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)
