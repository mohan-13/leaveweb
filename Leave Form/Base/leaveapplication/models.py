from django.db import models
from datetime import datetime
from django.utils.timezone import *
from django.contrib.auth.models import User


REASON_CHOICES=(
    ('personal','PERSONAL'),
    ('sick','SICK'),
    ('od','OD'),
    ('studyleave','STUDY LEAVE')
)
STATUS_CHOICES=(
    (1,'SUBMITTED'),
    (2,'APPROVED'),
    (3,'DENIED')
     )
class user(models.Model):
    rollno = models.CharField(max_length=8, unique=True, primary_key=True)
    foreign_user = models.ForeignKey(User, null=True, blank=True)
class Students(models.Model):
    apply_user=models.ForeignKey(User,null=True,blank=True)
    from_date= models.DateTimeField(default=datetime.now())
    to_date=models.DateTimeField(blank=True,default=datetime.now())
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default=STATUS_CHOICES[0][1])

    reason=models.CharField(max_length=100,blank=False,choices=REASON_CHOICES)
# Create your models here.
