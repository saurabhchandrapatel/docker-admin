from .forms import Form
from virtualization.models import Swarm


class SwarmForm(Form):
    class Meta:
        model = Swarm
        fields = '__all__'