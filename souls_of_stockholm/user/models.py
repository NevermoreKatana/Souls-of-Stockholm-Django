from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    jwt = models.TextField(max_length=800)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=25)
    country = models.CharField(max_length=100, null=True, blank=True)
