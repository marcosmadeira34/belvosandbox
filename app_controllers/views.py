from django.shortcuts import render
from django.http import HttpResponse
import os

from pprint import pprint
from belvo.client import Client
from belvo.enums import AccessMode
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# gerar token de acesso
def generate_access_token(request):
    """Manually create a link token"""
    client = Client(os.getenv("SECRET_ID"), os.getenv("SECRET_PASSWORD"), "sandbox")
    token = client.WidgetToken.create()
    context = {'access_token': token['access']}
    response = render(request, 'connect.html', context)
    return response


def index(request):
    return render(request, 'indexx.html')
    
def integracao(request):
    return render(request, 'integracao.html')