from .forms import Form

from virtualization.models import Plugins


class PluginsForm(models.Model):
    """docstring for Images"""
    class Meta:
        model = Plugins
        fields = __all__