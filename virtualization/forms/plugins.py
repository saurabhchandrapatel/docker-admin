from .forms import Form

from virtualization.models import Plugins

class PluginsForm(Form):
    class Meta:
        model = Plugins
        fields = '__all__'