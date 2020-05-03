from .forms import Form
from virtualization.models import Containers


class ContainersFrom(Form):
    class Meta:
        model = Containers
        fields = '__all__'