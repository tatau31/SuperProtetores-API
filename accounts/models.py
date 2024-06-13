from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    
    cpf = models.CharField(primary_key=True, max_length=11, unique=True)
    pass
