
from .forms import Form
from virtualization.models import Nodes


class NodesForm(Form):
    class Meta:
        model = Nodes
        fields = '__all__'