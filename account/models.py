"""Module containing the user entity"""
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)

from shared.base_model import BaseModel


class UserManager(BaseUserManager):
    def create_user(self, **kwargs):
        """
        Creates and saves a User with the given credentials.
        """
        email = kwargs.get("email")
        password = kwargs.get("password")
        username = kwargs.get("username")

        user = self.model(
            username=username, email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password)
        user.is_superuser = user.is_staff = True
        user.is_active = user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, BaseModel):
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
    is_admin = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __str__(self):
        return self.email
