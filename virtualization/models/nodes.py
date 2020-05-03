
from django.db import models


class Nodes(models.Model):
    
    node_id = models.CharField(max_length=200)
    short_id = models.CharField(max_length=10)
    attrs = models.TextField()
    version = models.CharField(max_length=100)

    
