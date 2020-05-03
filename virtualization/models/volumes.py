from django.db import models
 

class Volumes(models.Model):
    
    volume_id = models.CharField(max_length=200)
    short_id = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    attrs= models.TextField()













