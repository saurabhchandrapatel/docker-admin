from django.db import models
from virtualization.models import Images

class Containers(models.Model):
    """docstring for Images"""
    
    container_id = models.CharField(max_length=200)
    image = models.ForeignKey(Images, on_delete=models.CASCADE,)
    labels = models.CharField(max_length=100)
    name = models.UUIDField(max_length=100)
    short_id = models.CharField(max_length=15)
    status = models.SmallIntegerField(max_length=100)
    attrs = models.TextField(max_length=100)
   
