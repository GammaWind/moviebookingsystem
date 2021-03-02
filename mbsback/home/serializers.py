from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model

from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    class Meta:
        model = User = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'phone_number','password')

    
    def create(self, validated_data):
        password = make_password(validated_data.pop('password'))
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user