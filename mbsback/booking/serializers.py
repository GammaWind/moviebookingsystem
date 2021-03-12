
from .models import BookedSeat, Booking, Payment
from django.db import models
from django.db.models import fields
from django.db.models.query import QuerySet
from rest_framework import serializers

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password
from rest_framework.validators import UniqueValidator
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class PaymentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Payment
        fields = [ 'amount']

class BookingSerializer(serializers.ModelSerializer):
    # payment_id = PaymentSerializer(
    # validators = [UniqueValidator(queryset=BookedSeat.objects.all())])
    # seats_id = serializers.IntegerField(required = True,
    #     # validators = [UniqueValidator(queryset=BookedSeat.objects.all())]
    
    # )    
        
    
    class Meta:
        model = Booking
        fields = ('user_id', 'show_id')
        
    extra_kwargs = {
            
            
            'show_id':{'required': True}
        }  

class PreBookingSerializer(serializers.Serializer):
    show_id= serializers.IntegerField()
    seat_ids = serializers.ListField()
    


class ShowSeatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookedSeat
        fields = ('booking_id', 'seat_id')

    