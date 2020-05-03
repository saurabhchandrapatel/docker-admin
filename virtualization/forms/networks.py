from .forms import Form
from virtualization.models import Networks

class NetworksFrom(Form):
    class Meta:
        model = Networks
        fields = '__all__'