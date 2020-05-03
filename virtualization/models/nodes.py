
from django.db import models


class Nodes(models.Model):
    
    node_id = models.CharField(max_length=200)
    short_id = models.CharField(max_length=10)
    attrs = models.TextField()
    version = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Node"
        verbose_name_plural = "Nodes"
