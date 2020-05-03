from .forms import Form
from virtualization.models import Swarm


class SwarmForm(models.Model):
    """docstring for Images"""
    class Meta:
        model = Swarm
        fields = __all__