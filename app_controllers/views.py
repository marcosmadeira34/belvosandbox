from django.shortcuts import render
from django.http import JsonResponse
# importar a classe User do Django
from django.contrib.auth.models import User
from django.http import HttpResponse
import os
import json
from django.views.decorators.csrf import csrf_exempt

from pprint import pprint
from belvo.client import Client
from belvo.enums import AccessMode
from dotenv import load_dotenv, find_dotenv
from belvo.resources.links import Links
from .models import LinksData
from django.contrib.auth.decorators import login_required

load_dotenv(find_dotenv())


def index(request):
    return render(request, 'indexx.html')


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
        
# @login_required
def all_links(request):
    """Retrieve all links"""
    user_id = User.objects.get(id = request.user.id)
    client = Client(os.getenv("SECRET_ID"), os.getenv("SECRET_PASSWORD"), "sandbox")
    links = client.Links.list()    
    results = list(links)
    for result in results:
        data = LinksData.objects.update_or_create(
                        link_id = result['id'],
                        institution = result['institution'],
                        access_mode = result['access_mode'],
                        status = result['status'],
                        refresh_rate = result['refresh'],
                        created_by = result['created_by'],
                        last_accessed_at = result['last_accessed_at'],
                        external_id = result['external_id'],
                        created_at = result['created_at'],
                        institution_user_id = result['institution_user_id'],
                        credentials_storage = result['credentials_storage'],
                        fetch_historical = result['fetch_historical'],
                        )
        return data


@csrf_exempt
def webhook(request):
    print(request.body)
    return HttpResponse()