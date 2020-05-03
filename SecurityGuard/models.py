from django.db import models
from django.contrib.auth.models import User
import datetime

class Time(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    time=models.DateTimeField(null=True,blank=True)
    Lon=models.FloatField(max_length=50,null=False) #خط طول
    Lat=models.FloatField(max_length=50,null=False) #خط عرض
    out=models.BooleanField(default=False)
    def __unicode__(self):
        return self.time

class locations(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    Lon=models.FloatField(max_length=50,null=False) #خط طول
    Lat=models.FloatField(max_length=50,null=False) #خط عرض
    active=models.BooleanField(default=True)
    Present=models.BooleanField(default=False)
