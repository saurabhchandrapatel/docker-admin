from django.db import models


class Plugins(models.Model):
    """docstring for Images"""
    
    plugin_id = models.CharField(max_length=200)
    short_id = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    enabled = models.BooleanField()
    settings = models.TextField()
    attrs = models.TextField()


