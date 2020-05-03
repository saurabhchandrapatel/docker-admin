
from django.db import models


class Configs(models.Model):
    """docstring for Images"""
    name = models.CharField(max_length=100)
    attrs = models.TextField()
    
