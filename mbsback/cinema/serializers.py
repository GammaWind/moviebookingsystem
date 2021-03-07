from django.db import models
from django.db.models import fields
from django.db.models.query import QuerySet
from rest_framework import serializers
from .models import Cinema, CinemaHall, City,MoviesInCities, Show
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password
from rest_framework.validators import UniqueValidator
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class CitySerializer(serializers.ModelSerializer):
  class Meta:
    model = City
    fields = ('city_name','city_id')
    QuerySet = City.objects.all()


class MoviesinCitySerializer(serializers.ModelSerializer):
  
  class Meta:
    model = MoviesInCities
    fields = ['movie_id']
    depth = 1
    
class ShowSerialzer(serializers.ModelSerializer):
  class Meta:
    model = Show
    fields = ['cinemahall_id']
    depth = 1




  
  




  


