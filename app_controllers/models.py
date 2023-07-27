from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class LinksData(models.Model):
    """Return all links data"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="123456789", verbose_name="criado pelo usuário:")
    link_id = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    access_mode = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    refresh_rate = models.CharField(max_length=100)
    created_by = models.CharField(max_length=100)
    last_accessed_at = models.CharField(max_length=100)
    external_id = models.CharField(max_length=100)
    created_at = models.CharField(max_length=100)
    institution_user_id = models.CharField(max_length=255)
    credentials_storage = models.CharField(max_length=100)
    fetch_historical = models.BooleanField()
    
