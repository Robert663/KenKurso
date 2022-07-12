from django.db import models
from django.contrib.auth.models import AbstractUser
from .utils import CustomUserManager
from datetime import timezone

class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255)
    updated_at = models.DateTimeField()

    username = None

    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = ["full_name"]
    objects = CustomUserManager()