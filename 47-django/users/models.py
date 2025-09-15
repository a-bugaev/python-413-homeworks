"""
users/models.py
"""

from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    """
    add email field to default model
    """

    birth_date: models.CharField = models.CharField(
        max_length=100, null=False, default="email@example.com"
    )
