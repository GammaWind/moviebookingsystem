from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import User

# Create your views here.

class UserView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = User.objects.all()


