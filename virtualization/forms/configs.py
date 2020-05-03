from .forms import Form
from virtualization.models import Configs

class ConfigsFrom(Form):
    
    class Meta:
        model = Configs
        fields = '__all__'
