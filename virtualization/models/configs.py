
from django.db import models


class Configs(models.Model):
    """docstring for Images"""
    name = models.CharField(max_length=100)
    attrs = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Config"
        verbose_name_plural = "Configs"
    
