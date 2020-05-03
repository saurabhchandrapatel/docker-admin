from django.db import models
from virtualization.models import Containers


class Networks(models.Model):
    name = models.CharField(max_length=100)
    network_id = models.CharField(max_length=100)
    short_id = models.CharField(max_length=10)
    container = models.ForeignKey(Containers, on_delete=models.CASCADE)
    attrs = models.TextField(max_length=100)

    

