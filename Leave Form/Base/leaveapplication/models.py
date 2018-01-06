from django.db import models
from datetime import datetime
from django.utils.timezone import *
class user(models.Model):
    rollno=models.CharField(max_length=8,unique=True)
    password=models.CharField(max_length=8)
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
class Students(models.Model):
    firstname= models.CharField(max_length=100)
    lastname= models.CharField(max_length=100)
    email= models.EmailField()
    rollno=models.CharField(max_length=8,default=0)
    date= models.DateTimeField(default=datetime.now())
    reason=models.CharField(max_length=100,blank=False)
# Create your models here.
