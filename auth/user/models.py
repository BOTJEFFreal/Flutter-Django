from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    school_id = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=20)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=150, unique=True)