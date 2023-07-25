from django.shortcuts import render
from django.urls import path
from .views import *

urlpatterns = [
    path('indexx/', index, name='index'),
    path('connect/', generate_access_token, name='get_link_token'),
    path('integracao/', generate_access_token, name='integracao'),
    
]