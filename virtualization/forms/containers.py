from .forms import Form
from virtualization.models import Containers


class ContainersFrom(models.Model):
    """docstring for Images"""
    class Meta:
        model = Containers
        fields = __all__