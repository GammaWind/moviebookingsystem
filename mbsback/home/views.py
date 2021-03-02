from re import DEBUG
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password

# Create your views here.

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # DEBUG
    # @action(detail=True, methods=['post'])
    # def create_auth(request):
    #     serialized = UserSerializer(data=request.DATA)
    #     if serialized.is_valid():
    #         User.objects.create_user(
    #             serialized.init_data['email'],
    #             serialized.init_data['fist_name'],
    #             serialized.init_data['last_name'],
    #             serialized.init_data['phonr_number'],
    #             make_password(serialized.init_data['password'])
    #         )
    #         return Response(serialized.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)