
from django.db import models

class Secrets(models.Model):
    
    secret_id = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    attrs = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Secret"
        verbose_name_plural = "Secrets"
    