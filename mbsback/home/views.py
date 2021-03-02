from re import DEBUG
from typing import List
from django.db import models
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer,LoginSerializer
from .models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework import permissions




# Create your views here.
class MyViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissions]


class RegisterUser(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    # http_method_names = [ 'post', 'head'] #only allowed calls are 'POST' and 'HEAD'



