"""mbsback URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from cinema.models import Cinema
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from home import views
from django.urls import path, include
from cinema.views import CityAPI,MoviesInCityAPI,MovieInCinemaHallsAPI,SeatsForShowAPI
from home.views import RegisterUser, LoginUser, UserAPI


from knox import views as knox_views
from booking.views import PreBookAPI,ShowBookedSeatsAPI



router = routers.DefaultRouter()
# router.register(r'registeruser', views.RegisterUser, 'RegisterUser')
# router.register(r'loginuser', views.LoginUser, 'LoginUser')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path('api/auth/', include('djoser.urls.authtoken')),
    # path('api/login/', include('djoser.urls.authtoken')),
    path('', include('frontend.urls')),
    path('api/auth', include('knox.urls')),
    path('api/auth/register', views.RegisterUser.as_view()),
    path('api/auth/login', LoginUser.as_view()),
    path('api/auth/user', UserAPI.as_view()),
    path('api/auth/logout', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('api/city',CityAPI.as_view({'get':'cities'}),name="CityAPI"),
    path('api/movies/<int:cityid>',MoviesInCityAPI.as_view({'get':'moviein'}),name="MoviesInCityAPI"),
    path('api/cinemahalls/<int:movieid>',MovieInCinemaHallsAPI.as_view({'get':'movieincinemahalls'}),name="MovieInCinemaHallsAPI"),
    path('api/seats/<int:showid>',SeatsForShowAPI.as_view({'get':'seatsforshow'}),name="SeatsForShowAPI"),
    path('api/prebooking', PreBookAPI.as_view()),
    path('api/showbookedseats/<int:showid>',ShowBookedSeatsAPI.as_view({'get':'get'})),
    
    


]
 