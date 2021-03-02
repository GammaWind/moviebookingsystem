
from django.db import models
from django.db.models.deletion import CASCADE
from home.models import User
from cinema.models import Show,Seats


# Create your models here.

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)


class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,default=0) 
    show_id = models.ForeignKey(Show,on_delete=models.CASCADE,default=0)
    payment_id = models.ForeignKey(Payment,on_delete=CASCADE,default=0)





class BookedSeat(models.Model):
    booking_id = models.ForeignKey(Booking,on_delete=models.CASCADE,default=0)
    seat_id    = models.ForeignKey(Seats,on_delete=models.CASCADE,default=0)



   
   
