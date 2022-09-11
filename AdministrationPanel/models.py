# from codecs import getencoder
from django.db import models

# Create your models here.

class AdminUsers(models.Model):
    Username = models.TextField(max_length=100)
    Email = models.TextField(max_length=100)
    Password = models.TextField(max_length=100)
    