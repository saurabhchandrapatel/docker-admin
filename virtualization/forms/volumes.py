from .forms import Form
from virtualization.models import Volumes


class VolumesForm(models.Model):
    """docstring for Images"""
    class Meta:
        model = Volumes
        fields = __all__