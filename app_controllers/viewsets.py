""" from rest_framework import viewsets
from .serializers import LinksDataSerializer
from .models import LinksData

class LinksDataViewSet(viewsets.ModelViewSet):
    serializer_class = LinksDataSerializer
    queryset = LinksData.objects.all() """