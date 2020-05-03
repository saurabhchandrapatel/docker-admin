from .forms import Form
from virtualization.models import Services



class ServicesForm(Form):
    class Meta:
        model = Services
        fields = '__all__'