""" from rest_framework import serializers
from .models import LinksData

class LinksDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinksData
        fields = '__all__' """