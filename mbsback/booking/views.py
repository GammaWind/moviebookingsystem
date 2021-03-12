         
from .models import BookedSeat
from .serializers import BookingSerializer, PreBookingSerializer, ShowSeatsSerializer
from django.shortcuts import render
from rest_framework import generics, permissions, response,viewsets
from django.db import connection
from django.core.cache import cache






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
        serializer.is_valid(raise_exception=True)
        
        
        tuple1 = tuple(serializer.data['seat_ids'])
        serializer.data['seat_ids'] = set(serializer.data['seat_ids'])
        
        cache_key = request.user.email # needs to be unique
        cache_time = 600 # time in seconds for cache to be valid
         # returns None if no key-value pair
        
        
    
       
        
        sqlStatement = '''SELECT count(*) FROM booking_bookedseat WHERE seat_id_id in('''
        for i in range(len(tuple1)):
            sqlStatement += ' %s,'
        sqlStatement = sqlStatement[:-1]    
        sqlStatement += ')'    
        cursor = connection.cursor()
        cursor.execute(sqlStatement,tuple1)

        row = cursor.fetchone()
        if row[0] > 0:
            #return excption
            return response.Response('seats already booked')
        elif row[0] == 0:
            cache.set(cache_key,serializer.data, cache_time)
            

            if cache.get(serializer.data['show_id']) is not None:
                addSeatsToCache = cache.get(serializer.data['show_id'])
                for i in serializer.data['seat_ids']:
                    if cache.get(serializer.data['show_id']).add(i) is False:
                        return response.Response('Already')
                    else:
                        for i in serializer.data['seat_ids']:
                            cache.get(serializer.data['show_id']).add(i)    

                # cache.set(serializer.data['show_id'],addSeatsToCache, cache_time)

            else:    
                cache.set(serializer.data['show_id'],set(serializer.data['seat_ids']), cache_time)
            data = cache.get(serializer.data['show_id'])
            # print(cache.get(serializer.data['show_id']))
            print(data)
            
           


        # print(row)
        return response.Response({"booking" : BookingSerializer(context=self.get_serializer_context()).data})


class ShowBookedSeatsAPI(viewsets.ViewSet):
    serializer_class = ShowSeatsSerializer

    def get(self,request,showid):
        queryset = BookedSeat.objects.all().filter(show_id=showid)
        serializer = ShowSeatsSerializer(queryset,many = True)

        return response.Response(serializer.data)


        



