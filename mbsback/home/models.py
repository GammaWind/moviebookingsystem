from django.db import models
from django.db.models.query import ModelIterable
from django.core.validators import RegexValidator

# Create your models here.
class User(models.Model):
    email       =   models.EmailField(max_length=255,unique=True,primary_key=True)
    phone_regex =   RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number=  models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    active      =   models.BooleanField(default=True)
    staff       =   models.BooleanField(default=False)
    admin       =   models.BooleanField(default=False)
    timestamp   =   models.DateTimeField(auto_now_add=True)
    password    =   models.CharField(max_length=50)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= []


# class UserCred(models.Manager):

#     email      =  models.OneToOneField(User,on_delete=models.CASCADE,unique=True)
#     password   = models.CharField()
