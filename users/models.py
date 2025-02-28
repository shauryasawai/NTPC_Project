from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('grid_operator', 'Grid Operator'),
        ('plant_manager', 'Plant Manager'),
        ('sustainability_team', 'Sustainability Team'),
    ]
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='plant_manager')

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_set",  # Fix reverse accessor issue
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_set",  # Fix reverse accessor issue
        blank=True
    )
