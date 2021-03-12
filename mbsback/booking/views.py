         
from .models import BookedSeat, PreBooking, PreBookingSelectedSeats
from .serializers import BookingSerializer, PreBookingSerializer, ShowSeatsSerializer
from django.shortcuts import render
from rest_framework import generics, permissions, response,viewsets
from django.db import connection
from django.core.cache import cache
from cinema.models import Show,Seats
import datetime






# Create your views here.

class BookingAPI(generics.GenericAPIView):
    # permission_classes = [
    # permissions.IsAuthenticated,
    # ]
    serializer_class = BookingSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        booking = serializer.save()
        return response.Response({"booking" : BookingSerializer(booking, context=self.get_serializer_context()).data})





class PreBookAPI(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
        ]
    serializer_class = PreBookingSerializer    
    def post(self, request, *args, **kwargs):
        print(request.user)
        
        serializer = self.get_serializer(data=request.data)
        print(serializer.initial_data['seats_ids'])

        
        
        
        
        tuple1 = tuple(serializer.initial_data['seats_ids'])    
       
        
        sqlStatement = '''SELECT count(*) FROM booking_bookedseat WHERE seats_ids_id in('''
        for i in range(len(tuple1)):
            sqlStatement += ' %s,'
        sqlStatement = sqlStatement[:-1]    
        sqlStatement += ')'    
        cursor = connection.cursor()
        cursor.execute(sqlStatement,tuple1)


        
        row = cursor.fetchone()
        if row[0] > 0:
            
            return response.Response('seats already booked')
        elif row[0] == 0:
            
            
            for t in tuple1:
                timed = (datetime.datetime.now() - datetime.timedelta(minutes=5))
                validPreBook = PreBookingSelectedSeats.objects.filter(seat_id= t,created__gte = timed )
                if len(validPreBook) == 0:
                    pass
                    
                else:
                    return response.Response('Please Try again') 
            serializer.is_valid(raise_exception=True)
            serializer.save()           
            for t in tuple1:
                prebookseats =PreBookingSelectedSeats.objects.create(
                        prebooking_id = PreBooking.objects.get(prebooking_id = serializer.data['prebooking_id']),
                        show_id = Show.objects.get(show_id =serializer.data['show_id']),
                        seat_id = Seats.objects.get(seat_id = t)
                        )
                       
                
                prebookseats.save()
            


            
        return response.Response({"prebooking" : PreBookingSerializer(context=self.get_serializer_context()).data})


class ShowBookedSeatsAPI(viewsets.ViewSet):
    serializer_class = ShowSeatsSerializer

    def get(self,request,showid):
        queryset = BookedSeat.objects.all().filter(show_id=showid)
        serializer = ShowSeatsSerializer(queryset,many = True)

        return response.Response(serializer.data)


        



