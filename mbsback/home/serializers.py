from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password
from rest_framework.validators import UniqueValidator
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('last_name', 'first_name', 'email')

# Register Serializer
class RegisterUserSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    phone_number = serializers.CharField(required=True)
   
    class Meta:
        model = User = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'phone_number','password')

    
    
    extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'phone_number':{'required': True}
        }

    def validate(self, attrs):
       

        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number = validated_data['phone_number']
        )
        


        
        user.set_password(validated_data['password'])
        user.save()

        return user
    

class LoginSerializer(serializers.Serializer):
    
  username = serializers.CharField()
  password = serializers.CharField()

  def validate(self, data):
    user = authenticate(**data)
    if user and user.is_active:
      return user
    raise serializers.ValidationError("Incorrect Credentials")