from time import time
from django.db import models
from django.contrib.auth.models import AbstractUser
from tomlkit import datetime
from .utils import CustomUserManager
from django.utils import timezone

class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255)
    updated_at = models.DateTimeField(default=timezone.now())
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["full_name"]
    objects = CustomUserManager()