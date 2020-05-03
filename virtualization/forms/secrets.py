
from .forms import Form
from virtualization.models import Secrets



class SecretsForm(Form):
    class Meta:
        model = Secrets
        fields = '__all__'