from django.db import models

class Students(models.Model):
    firstname= models.CharField(max_length=100)
    lastname= models.CharField(max_length=100)
    email= models.EmailField()
    date= models.DateTimeField()
# Create your models here.
