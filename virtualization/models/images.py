from django.db import models

class Images(models.Model):
    
    name = models.CharField(max_length=100)
    attrs = models.TextField()
    image_id = models.CharField(max_length=100)
    labels = models.CharField(max_length=100)
    short_id = models.CharField(max_length=10)
    tags = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"