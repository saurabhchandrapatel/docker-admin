from .forms import Form
from virtualization.models import Networks


class NetworksFrom(models.Model):
    """docstring for Images"""
    class Meta:
        model = Networks
        fields = __all__