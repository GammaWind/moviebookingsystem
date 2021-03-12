
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

from home.models import User
from cinema.models import Show,Seats
import datetime


# Create your models here.

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    amount  = models.DecimalField(max_digits=8,decimal_places=2,null=False)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,null=False) 
    def __str__(self):
        return str(self.payment_id)


class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,default=0) 
    show_id = models.ForeignKey(Show,on_delete=models.CASCADE,default=0)
    payment_id = models.ForeignKey(Payment,on_delete=CASCADE,default=0)

    def __str__(self):
        return str(self.booking_id)





class BookedSeat(models.Model):
    def __str__(self):
        return str(self.seats_ids)
    booking_id = models.ForeignKey(Booking,on_delete=models.CASCADE,default=0)
    seats_ids    = models.ForeignKey(Seats,on_delete=models.CASCADE,default=0)
    show_id = models.ForeignKey(Show,on_delete=models.CASCADE,default=1)

    class Meta:
        unique_together = (('booking_id','show_id', 'seats_ids'),)



class PreBooking(models.Model):

    prebooking_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,default=0) 
    show_id = models.ForeignKey(Show,on_delete=models.CASCADE,default=0)
    created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return str(self.prebooking_id)


    @property
    def seats_ids(self):
        return "Perform calculations, combine with related models, etc. etc."
    

class PreBookingSelectedSeats(models.Model):
    def __str__(self):
        return str(self.seat_id)

    prebooking_id = models.ForeignKey(PreBooking,on_delete=models.CASCADE,default=0)
    seat_id   = models.ForeignKey(Seats,on_delete=models.CASCADE,default=0)
    show_id = models.ForeignKey(Show,on_delete=models.CASCADE,default=1)
    created = models.DateTimeField(auto_now_add=True)
    


   
   
