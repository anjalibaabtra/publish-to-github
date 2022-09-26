# from codecs import getencoder
from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth

# Create your models here.

class AdminUser(AbstractUser):
    Username = models.TextField(max_length=100)
    Email = models.TextField(max_length=100)
    Password = models.TextField(max_length=100)
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
