"""Module containing the similar fields and operations of the models"""
from django.db import models


class BaseModel(models.Model):
    """
    Base model to implement common fields

    Attributes:
        created_at: Holds date/time for when an object was created.
        updated_at: Holds date/time for last update on an object.
        deleted_at: Holds date/time for soft-deleted objects.
        deleted_at: Holds user who soft-deleted an objects.
    """
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        """Additional for the base"""
        abstract = True
