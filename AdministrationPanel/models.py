# from codecs import getencoder
from dataclasses import dataclass
# from datetime import date, datetime
from email.policy import default
from statistics import mode
from unittest.util import _MAX_LENGTH
import django
from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth

# Create your models here.

class StudentFee(models.Model):
    Name = models.TextField(max_length=100,default='')
    Email = models.TextField(max_length=100,default='')
    AdmissionNum = models.IntegerField(default=0)
    Contact = models.BigIntegerField(default=000)
    Std = models.IntegerField(default=0)
    Division = models.TextField(max_length=50, default='')
    TotalFee = models.IntegerField(default=0)
    PendingFee = models.IntegerField(default=0)
    PaidFee = models.IntegerField(default=0)
   

class AdminUser(AbstractUser):
    Name = models.TextField(max_length=100,default='')
    Firstname = models.TextField(max_length=100,default='')
    Lastname = models.TextField(max_length=100,default='')
    Std = models.IntegerField(default=0)
    Contact = models.BigIntegerField(default=000)
    AdmissionNum = models.IntegerField(default=0)
    Division = models.TextField(max_length=50, default='')
    RollNumber = models.IntegerField(default=0)
    DOB = models.TextField(max_length=100, default='')
    Gender = models.TextField(max_length=50,default='')
    Religion = models.TextField(max_length=50,default='')
    Blood = models.TextField(max_length=50, default='')
    Subject = models.TextField(max_length=50, default='')
    JoinDate = models.TextField(max_length=50, default='')
    WorkExperience = models.IntegerField(default=0)
    Salary = models.IntegerField(default=0)
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)

class TeachersSalary(models.Model):
    Name = models.TextField(max_length=100,default='')
    Salary = models.BigIntegerField(default=0)

  