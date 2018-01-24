from django.db import models
from datetime import datetime
from django.utils.timezone import *
from django.contrib.auth.models import User
class user(models.Model):
    rollno = models.CharField(max_length=8, unique=True, primary_key=True)
    foreign_user = models.ForeignKey(User, null=True, blank=True)
class Students(models.Model):
    firstname= models.CharField(max_length=100)
    lastname= models.CharField(max_length=100)
    email= models.EmailField()
    rollno=models.CharField(max_length=8)
    date= models.DateTimeField(default=datetime.now())
    reason=models.CharField(max_length=100,blank=False)
# Create your models here.
