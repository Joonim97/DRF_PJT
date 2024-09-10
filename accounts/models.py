from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=50, unique=True)
    birth = models.DateField()
    gender = models.CharField(max_length=10, blank=True, null=True)