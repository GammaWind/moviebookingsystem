from django.contrib import admin
from django.core.exceptions import ImproperlyConfigured
from .models import Movie
# Register your models here.
admin.site.register(Movie)
