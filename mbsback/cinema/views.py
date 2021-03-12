from django.db.models import query
from django.db.models.query import QuerySet
from django.http import request
from rest_framework import response, serializers
from .models import CinemaHall, City,CinemasInCity, MoviesInCities, Seats, Show
from django.shortcuts import render
from .serializers import CitySerializer,MoviesinCitySerializer, ShowSerialzer,SeatsSerilizer
from rest_framework import generics, permissions,viewsets
from rest_framework.response import Response
# Create your views here.


class CityAPI(viewsets.ViewSet):
    # permission_classes = [
    # permissions.IsAuthenticated,
    # ]
    def cities(self, request):
        queryset = City.objects.all()
        serializer = CitySerializer(queryset, many=True)
        return Response(serializer.data)


class MoviesInCityAPI(viewsets.ViewSet):
    def moviein(self, request,cityid):
        queryset = MoviesInCities.objects.all().filter(city_id = cityid)
        serializer = MoviesinCitySerializer(queryset, many=True)
        
        return Response(serializer.data)




class MovieInCinemaHallsAPI(viewsets.ViewSet):
    def movieincinemahalls(self, request,movieid):
        queryset = Show.objects.all().filter(movie_id = movieid)
        serializer = ShowSerialzer(queryset, many=True)
        
        return Response(serializer.data)


class SeatsForShowAPI(viewsets.ViewSet):
    def seatsforshow(self,request,showid):
        queryset = Seats.objects.all().filter(cinemahall_id = showid)
        serializer = SeatsSerilizer(queryset,many = True)

        return Response(serializer.data)



  
        
        
        

        

    

    
