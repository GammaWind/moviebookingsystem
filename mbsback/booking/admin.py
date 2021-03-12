from django.contrib import admin
from .models import BookedSeat, Booking, Payment, PreBooking
# Register your models here.
admin.site.register(BookedSeat)
admin.site.register(Payment)
admin.site.register(Booking)
admin.site.register(PreBooking)
