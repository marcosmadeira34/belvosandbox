from django.shortcuts import render
# importar a classe User do Django
from django.contrib.auth.models import User
from django.http import HttpResponse
import os

from pprint import pprint
from belvo.client import Client
from belvo.enums import AccessMode
from dotenv import load_dotenv, find_dotenv
from belvo.resources.links import Links

load_dotenv(find_dotenv())

# gerar token de acesso
def generate_access_token(request):
    # Widget branding    
    
    widget = {
    "branding": {
    #"company_icon": "https://mysite.com/icon.svg",
    #"company_logo": "https://mysite.com/logo.svg",
    "company_name": "I-Extrato",
    #"social_proof": bool('true'),
    
    "company_benefit_header": "Rápida aprovação",
    "company_benefit_content": "Integração bancária de alta performance",
    #"opportunity_loss": "",
    #"social_proof": bool('false'),
    #"overlay_background_color": "#F0F2F4"
    
    }
}

    scopes = "read_institutions,write_links,read_links"
    client = Client(os.getenv("SECRET_ID"), os.getenv("SECRET_PASSWORD"), "sandbox")
    token = client.WidgetToken.create(widget=widget, scopes=scopes)
    # incluir futuramente o external_id do usuário na variável de contexto
    # external_id = {'external_id': user_id}
    response = render(request, 'integracao.html', {'access_token': token['access']})
    return response
    
  




def index(request):
    return render(request, 'indexx.html')
    
def all_links():
    """Retrieve all links"""
    client = Client(os.getenv("SECRET_ID"), os.getenv("SECRET_PASSWORD"), "sandbox")
    links = client.Links.list()
    print(links)

