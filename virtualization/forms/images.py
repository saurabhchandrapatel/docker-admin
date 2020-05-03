from .forms import Form
from virtualization.models import Images


class ImagesFrom(models.Model):
    """docstring for Images"""
    class Meta:
        model = Images
        fields = __all__