from django.contrib import admin
from .models import BookedSeat, Booking, Payment
# Register your models here.
admin.site.register(BookedSeat)
admin.site.register(Payment)
admin.site.register(Booking)
