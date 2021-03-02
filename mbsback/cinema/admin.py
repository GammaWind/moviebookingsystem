from django.contrib import admin
from .models import Cinema, CinemaHall, CinemasInCity, City, Seats, Show

# Register your models here.
admin.site.register(City)
admin.site.register(Cinema)
admin.site.register(CinemasInCity)
admin.site.register(CinemaHall)
admin.site.register(Show)
admin.site.register(Seats)


