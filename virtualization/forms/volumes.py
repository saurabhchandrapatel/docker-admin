from .forms import Form
from virtualization.models import Volumes


class VolumesForm(Form):
    class Meta:
        model = Volumes
        fields = '__all__'