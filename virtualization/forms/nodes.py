
from .forms import Form
from virtualization.models import Nodes


class NodesForm(models.Model):
    """docstring for Images"""
    class Meta:
        model = Nodes
        fields = __all__