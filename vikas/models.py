from django.db import models
from timezone_field import TimeZoneField
# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=100,primary_key=True)
    real_name = models.CharField(max_length=100)
    time_zone = TimeZoneField()

    
class Activity_period(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    start_time1 = models.CharField(max_length=50)
    end_time1 = models.CharField(max_length=50)
    start_time2 = models.CharField(max_length=50)
    end_time2 = models.CharField(max_length=50)
    start_time3 = models.CharField(max_length=50)
    end_time3 = models.CharField(max_length=50)
