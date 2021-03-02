from django.db import models
from django.db.models.aggregates import Max
from django.db.models.base import Model, ModelState
from django.db.models.fields import DateTimeField
from movie.models import Movie

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
    cinama_id = models.ForeignKey(Cinema,on_delete=models.CASCADE,default=0)   

class CinemasInCity(models.Model):
    city_id = models.ForeignKey(City,on_delete=models.CASCADE,default=0) 
    cinema_id = models.ForeignKey(Cinema,on_delete=models.CASCADE,default=0)  

class Seats(models.Model):
    seat_id = models.AutoField(primary_key=True)
    seat_number = models.IntegerField()
    seat_row = models.CharField(max_length=1)
    cinemahall_id = models.ForeignKey(CinemaHall,on_delete=models.CASCADE,default=0)


class Show(models.Model):
    show_id = models.AutoField(primary_key=True)
    show_name = models.CharField(max_length=50)
    show_starttime = models.DateTimeField()
    show_endtime = models.DateTimeField()
    movie_id = models.ForeignKey(Movie,on_delete=models.CASCADE,default=0)
    cinemahall_id = models.ForeignKey(CinemaHall,on_delete=models.CASCADE,default=0)


    