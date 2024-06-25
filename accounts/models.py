from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    cpf = models.CharField(max_length=11, unique=True, primary_key=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=11)
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name