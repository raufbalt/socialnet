from django.db import models
from django.contrib.auth.models import AbstractUser

class Account(AbstractUser):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=20, unique=True)

    secret_word = models.CharField(max_length=50)

    def __str__(self):
        return self.username
