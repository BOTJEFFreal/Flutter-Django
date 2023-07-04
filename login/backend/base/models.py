from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    school_id = models.TextField()
    # username = models.CharField(max_length=100)
    # password = models.CharField(max_length=100)

    # USERNAME_FIELD = 'username'

    