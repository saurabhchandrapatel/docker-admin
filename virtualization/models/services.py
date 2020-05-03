from django.db import models

class Services(models.Model):
    
    service_id = models.CharField(max_length=200)
    short_id = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    version= models.CharField(max_length=100)
    attrs= models.TextField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"