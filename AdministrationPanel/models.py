# from codecs import getencoder
from unittest.util import _MAX_LENGTH
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
    # is_approved = models.BooleanField(default=False)


# class Studentdetails(models.Model):
#     Firstname = models.TextField(max_length=100)
#     Lastname = models.TextField(max_length=100)
#     Class = models.IntegerField(max_length=50)
#     Contact = models.IntegerField(max_length=50)
#     StudentId = models.IntegerField(max_length=50)
#     Division = models.TextField(max_length=50)
#     RollNumber = models.IntegerField(max_length=50)
#     Gender = models.TextField(max_length=50)
#     Religion = models.TextField(max_length=50)
#     Blood = models.TextField(max_length=50)
#     adminuser = models.ForeignKey(AdminUser, on_delete = models.CASCADE)

# class StudentFee(models.Model):
#     TotalFee = models.IntegerField(max_length=50)
#     PendingFee = models.IntegerField(max_length=50)
#     PaidFee = models.IntegerField(max_length=50)
#     adminuser = models.ForeignKey(AdminUser, on_delete = models.CASCADE)
