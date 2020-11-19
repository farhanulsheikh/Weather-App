from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'weather-home'),
    path('weather_page/', views.weather_page, name = 'weather_page'),

]