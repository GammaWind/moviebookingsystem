
from django.db.models.fields import files
from .models import BookedSeat, Booking, Payment, PreBooking
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

class PreBookingSerializer(serializers.ModelSerializer):
    seats_ids = serializers.ListField(source='custom_property', read_only=True,validators=[UniqueValidator(queryset=BookedSeat.objects.all())])
    
            
    class Meta:
        model = PreBooking
        fields = ('prebooking_id','show_id','user_id','seats_ids')
    
    


class ShowSeatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookedSeat
        fields = ('booking_id', 'seats_ids')

    