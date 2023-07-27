from django.shortcuts import render
from django.urls import path, include
from .views import *

urlpatterns = [
    path('indexx/', index, name='index'),
    path('integracao/', generate_access_token, name='integracao'),
    path('webhook/', webhook, name='webhook'),

    
]