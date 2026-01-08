from django.contrib import admin
from django.urls import path
from authapp import views


urlpatterns = [
    path('',views.home_view,name='home'),
    path('portol/',views.portol_view,name='portol'),
  
]
