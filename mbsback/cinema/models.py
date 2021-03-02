from django.db import models
from django.db.models.aggregates import Max

# Create your models here.

class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=50)


class Cinema(models.Model):
    cinema_id = models.AutoField(primary_key=True)
    cinem_name = models.CharField(max_length=50)

class CinemaHall(models.Model):
    cinemahall_id = models.AutoField(primary_key=True)
    cinemahall_name = models.CharField(max_length=50) 
    cinama_id = models.ForeignKey(Cinema,on_delete=models.CASCADE)   

class CinemasInCity(models.Model):
    city_id = models.ForeignKey(City,on_delete=models.CASCADE) 
    cinema_id = models.ForeignKey(Cinema,on_delete=models.CASCADE)    