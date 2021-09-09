from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    password2 = models.CharField(max_length=50,null=False)
